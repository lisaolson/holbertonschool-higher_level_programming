#!/bin/bash
# Takes in URL, displays all HTTP methods the server will accept
curl -sI -X OPTIONS $1 | grep Allow: | cut -d ":" -f 2 | sed -e 's/^[ \t]*//'
