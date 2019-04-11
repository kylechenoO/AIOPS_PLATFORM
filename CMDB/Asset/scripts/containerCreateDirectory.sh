#!/usr/bin/env bash

## check /AIOPS directory and create it
if [ ! -d /AIOPS ];
then
    mkdir /AIOPS;

fi

if [ ! -d /AIOPS/CMDB ];
then
    mkdir /AIOPS/CMDB;

fi
