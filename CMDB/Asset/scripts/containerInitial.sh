#!/usr/bin/env bash

cat $1/containerCreateDirectory.sh | docker exec -i $2 bash
