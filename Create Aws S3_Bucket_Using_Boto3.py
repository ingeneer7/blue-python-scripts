#Public S3 Bucket
import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("bluecohort")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)

print(response)

#Private S3 Bucket
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("bluecohort2")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
    
)

print(response)

