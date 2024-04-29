#!/bin/bash
#sends a GET request to the URL, and displays the body of the response
curl -i "$1" | grep -v "^HTTP/"
