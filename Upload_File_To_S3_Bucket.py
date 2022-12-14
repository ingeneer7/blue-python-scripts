#Upload one file at a time
import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="test.jpg",
    Bucket="bluecohort",
    Key="testpic.jpg")
    
#Upload multiple files
import os
import glob

cwd=os.getcwd()

cwd=cwd+"/upload/"

files=glob.glob(cwd+"*.jpg")

files

['/Users/irogers/Documents/GitHub/ingeneer7/upload/test3.jpg',
 '/Users/irogers/Documents/GitHub/ingeneer7/upload/test1.jpg',
 '/Users/irogers/Documents/GitHub/ingeneer7/upload/test4.jpg',
 '/Users/irogers/Documents/GitHub/irogers7/upload/test2.jpg']
 
for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="bluecohort",
    Key=file.split("/")[-1])
