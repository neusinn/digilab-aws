#!/bin/bash

echo " !!! This removes the S3 Bucket 'www.sssws-1.diglab.admin.ch' and all its content."

aws s3 rb s3://www.sssws-1.diglab.admin.ch --force
