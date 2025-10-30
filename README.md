# Validate the Thunder R5.2 & Thunder R5.3 using this HelloPlugin
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

A simple "Hello Plugin" JSON-RPC plugin for the WPEFramework (Thunder) platform.

This plugin exposes a single JSON-RPC method SayHello that returns a greeting message.

## Issue reported 
Tested the HelloPlugin in different Thunder releases. Please find the testing results below: In Thunder 5.2, the response returns 'Unknown method,' but the same plugin works fine in Thunder R4.4.3 and Thunder R5.3.

**Thunder R4.4.3 Testing Results:**

**Request :** curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:9998/jsonrpc' -d '{"jsonrpc":"2.0","id":1,"method":"HelloPlugin.1.SayHello","params":{"name":"Thamim"}}' ; echo

**Response :** {"jsonrpc":"2.0","id":1,"result":{"message":"Hello Thamim from TestPlugin"}}

**Thunder 5.2 Testing Results:**

**Request :** curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:9998/jsonrpc' -d '{"jsonrpc":"2.0","id":1,"method":"HelloPlugin.SayHello","params":{"name":"Thamim"}}' ; echo
**Response :** {"jsonrpc":"2.0","id":1,"error":{"code":-32601,"message":"Unknown method."}}

**Thunder 5.3 Testing Results:**

**Request :** curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:9998/jsonrpc' -d '{"jsonrpc":"2.0","id":1,"method":"HelloPlugin.SayHello","params":{"name":"Thamim"}}' ; echo
**Response :** {"jsonrpc":"2.0","id":1,"result":{"message":"Hello \"Thamim\" from TestPlugin"}}


