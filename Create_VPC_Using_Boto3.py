#Creating a VPC with Boto3
import boto3
client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.10.0.0/16')
