#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo " $0 <file> <bucket>"
    exit 1
fi

#parameters
FILE=$1
BUCKET=$2
EXPIRATION=$3

#uploading file
aws s3 cp "$FILE" "s3://$BUCKET/"

#making link
URL=$(aws s3 presign "s3://$BUCKET/$(basename "$FILE")" --expires-in "$EXPIRATION")

echo "URL: $URL"
