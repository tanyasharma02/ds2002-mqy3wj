#!/usr/local/bin/python3

import boto3
import sys
import requests
import mimetypes

file_url = sys.argv[1]
bucket_name = sys.argv[2]
expires_in = int(sys.argv[3])

object_name = file_url.split("/")[-1]

response = requests.get(file_url)
with open(object_name, 'wb') as file:
    file.write(response.content)

content_type, _ = mimetypes.guess_type(object_name)
if content_type is None:
    content_type = "application/octet-stream"

s3 = boto3.client('s3', region_name='us-east-1')
with open(object_name, 'rb') as file:
    s3.put_object(
	Body=file,
        Bucket=bucket_name,
        Key=object_name,
        ContentType=content_type
    )

presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)

print(presigned_url)

