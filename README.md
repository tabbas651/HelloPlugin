# HelloPlugin for Thunder R5.2
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) 

A simple "Hello Plugin" JSON-RPC plugin for the WPEFramework (Thunder) platform.

This plugin exposes a single JSON-RPC method SayHello that returns a greeting message.

## Issue reported 

In Thunder 5.2 , Response giving Unknown method. but same  plugin program working fine for Thunder R4.4.3


curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:9998/jsonrpc' -d '{"jsonrpc":"2.0","id":1,"method":"HelloPlugin.SayHello","params":{"name":"Thamim"}}' ; echo

{"jsonrpc":"2.0","id":1,"error":{"code":-32601,"message":"Unknown method."}}

Thunder R4.4.3 Testing Results:

curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:9998/jsonrpc' -d '{"jsonrpc":"2.0","id":1,"method":"HelloPlugin.1.SayHello","params":{"name":"Thamim"}}' ; echo

{"jsonrpc":"2.0","id":1,"result":{"message":"Hello Thamim from TestPlugin"}}
