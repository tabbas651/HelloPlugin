#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os
import zipfile

def get_memory_info(pid):
    info = {"RssAnon": 0, "RssFile": 0, "RssShmem": 0, "TotalRSS": 0, "TotalPSS": 0}

    try:
        with open(f"/proc/{pid}/status") as f:
            for line in f:
                if line.startswith("RssAnon:"):
                    info["RssAnon"] = int(line.split()[1])
                elif line.startswith("RssFile:"):
                    info["RssFile"] = int(line.split()[1])
                elif line.startswith("RssShmem:"):
                    info["RssShmem"] = int(line.split()[1])
        info["TotalRSS"] = info["RssAnon"] + info["RssFile"] + info["RssShmem"]
    except FileNotFoundError:
        return None

    result = subprocess.run(
        f"grep -i Pss /proc/{pid}/smaps | awk '{{sum+=$2}} END {{print sum}}'",
        shell=True, capture_output=True, text=True
    )
    try:
        info["TotalPSS"] = int(result.stdout.strip() or 0)
    except ValueError:
        info["TotalPSS"] = 0

    return info

def generate_html_report(process_data):
    now = datetime.now()
    time_str = f"Current date and time: {now}"

    html = f"""<html>
<head>
<title>Thunder Process Memory Summary</title>
<style>
body {{ font-family: Arial, sans-serif; }}
h2 {{ color: #2b3e50; }}
table {{ border-collapse: collapse; width: 100%; margin-top: 10px; }}
th, td {{ border: 1px solid #2b3e50; text-align: center; padding: 8px; }}
th {{ background-color: #2b3e50; color: white; }}
</style>
</head>
<body>
<h2>Thunder Process Memory Summary</h2>
<p>Generated on: {time_str}</p>
<table>
<tr>
<th>Process Name</th><th>PID</th><th>RssAnon (kB)</th><th>RssFile (kB)</th><th>RssShmem (kB)</th><th>Total RSS (kB)</th><th>Total PSS (kB)</th>
</tr>"""
    for pdata in process_data:
        html += f"""
<tr>
<td>{pdata['name']}</td>
<td>{pdata['pid']}</td>
<td>{pdata['RssAnon']}</td>
<td>{pdata['RssFile']}</td>
<td>{pdata['RssShmem']}</td>
<td>{pdata['TotalRSS']}</td>
<td>{pdata['TotalPSS']}</td>
</tr>"""
    html += "</table></body></html>"
    return html

def main():

    processes = []
    # Check if WPEFramework is running first
    print("Searching for WPEFramework processes...")
    result = subprocess.run(["pgrep", "-af", "WPEFramework"], capture_output=True, text=True)
    wpe_found = False
    for line in result.stdout.strip().split("\n"):
        if line:
            parts = line.split(None, 1)
            pid = parts[0]
            pname = "WPEFramework"
            meminfo = get_memory_info(pid)
            if meminfo:
                meminfo["pid"] = pid
                meminfo["name"] = pname
                processes.append(meminfo)
                wpe_found = True
                print(f"Found WPEFramework process: PID {pid}")
    # Only check Thunder if WPEFramework is not running
    if not wpe_found:
        print("No WPEFramework processes found. Searching for Thunder processes...")
        result = subprocess.run(["pgrep", "-af", "Thunder"], capture_output=True, text=True)
        thunder_found = False
        for line in result.stdout.strip().split("\n"):
            if line:
                parts = line.split(None, 1)
                pid = parts[0]
                pname = "Thunder"
                meminfo = get_memory_info(pid)
                if meminfo:
                    meminfo["pid"] = pid
                    meminfo["name"] = pname
                    processes.append(meminfo)
                    thunder_found = True
                    print(f"Found Thunder process: PID {pid}")
        if not thunder_found:
            print("No Thunder processes found either.")
    else:
        print(f"WPEFramework is running. Skipping Thunder process search.")
        print(f"Total WPEFramework processes found: {len(processes)}")

    # Generate HTML report accordingly
    if not processes:
        print("No processes found to analyze. Generating empty report.")

    html = generate_html_report(processes)
    os.makedirs("artifacts", exist_ok=True)
    output_file = "artifacts/thunder_memory_summary.html"

    # Write the HTML file
    with open(output_file, "w") as f:
        f.write(html)


    # ✅ Create versioned zip file
    zip_path = f"artifacts/Thunder-Memory-Report.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(output_file, arcname="thunder_memory_summary.html")

    print(f"✅ Memory report generated and zipped: {zip_path}")
if __name__ == "__main__":
    main()
