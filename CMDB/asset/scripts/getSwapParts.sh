#!/usr/bin/env bash

## get all swap partitions
swapon -s | awk -F' ' '/partition/{ printf("%s,%s\n", $1, $4 / $3); }'
