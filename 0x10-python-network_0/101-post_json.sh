#!/bin/bash
# this script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -d "@$2" -X POST -H "Content-Type: applicaion/json" $1
