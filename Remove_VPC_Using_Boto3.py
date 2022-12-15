#Remove VPC
import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
      VpcId='vpc-05f97d4a'
      
  )

response
