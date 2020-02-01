#!/bin/bash

echo "======================================================"
echo "===                 D I G I L A B                  ==="
echo "===                                                ==="
echo "=== Create an S3 Bucket AWS and publish a Web Came ==="
echo "===               in just 5 seconds !              ==="
echo "======================================================"

read -n 1 -s -r -p "Press any key to start"
SECONDS=0


echo "1. Create S3 Bucket  'www.wgsws-2.diglab.admin.ch' "
aws s3 mb s3://www.wgsws-2.diglab.admin.ch

echo "2. Configure S3 Bucket for web hosting"
aws s3 website s3://www.wgsws-2.diglab.admin.ch/ --index-document index.html

echo "3. Set Policy for S3 Bucket for public access"
aws s3api put-bucket-policy --bucket www.wgsws-2.diglab.admin.ch --policy file://policy_wgsws-2_s3_public_read.json

echo "4. Upload Web Game code."
aws s3 sync ./2048/ s3://www.wgsws-2.diglab.admin.ch/

# do some work
duration=$SECONDS
echo
echo "Done in $((duration)) seconds."
echo
echo "==> Open Linkt in Browser : http://www.wgsws-2.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/"

open http://www.wgsws-2.diglab.admin.ch.s3-website.eu-central-1.amazonaws.com/
