#!/bin/bash

echo " !!! This will remove the S3 Bucket 'www.sssws-1.diglab.admin.ch' and all its content !!!"

read -n1 -r -p "Press 'y'-Key to remove the bucket..." key

if [ "$key" = 'y' ]; then
    aws s3 rb s3://www.sssws-1.diglab.admin.ch --force
fi