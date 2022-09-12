#!/bin/bash
# What's my status? #0
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f2

