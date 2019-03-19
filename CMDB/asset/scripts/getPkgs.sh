#!/usr/bin/env bash

## check OSVersion and get all installed pkgs
if [ -f /etc/redhat-release ];
then
    rpm -qa;

else
    dpkg -l | awk -F' ' '
        BEGIN{
            flag = 0;
        }
        /^\\+\\+\\+/{
            flag = 1;
            next;
        }
        {
            if(flag){
                printf("%s-%s\n", $2, $3);
            }else{
                next;
            }
        }'

fi
