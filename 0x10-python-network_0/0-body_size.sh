#!/bin/bash
# What's my status? #0
curl -so /dev/null "$1" -w '%{size_download} \n'
