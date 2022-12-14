#Deleting objects from the S3 bucket
import boto3
s3_resource=boto3.client("s3")

#delete one object
s3_resource.delete_object(Bucket='bluecohort',
      Key='test2.jpg')
      
#find all the objects from the bucket
objects=s3_resource.list_objects(Bucket="bluecohort")["Contents"]
len(objects)

#iteration
for object in objects:
    response=s3_resource.delete_object(Bucket='bluecohort',
      Key=object["Key"])
    print(response)
    
