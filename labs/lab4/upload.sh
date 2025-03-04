#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo " $0 <file> <bucket>"
    exit 1
fi

#parameters
FILE=$1
BUCKET=$2

#uploading file
aws s3 cp "$FILE" "s3://$BUCKET/"

#making link
URL=$(aws s3 presign --expires-in 604800 "s3://$BUCKET/$FILE")

echo "URL: $URL"
