#Creates/Launches multiple ec2 instances
import boto3
ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-0b5eea76982371e91',
      InstanceType='t2.micro',
    MaxCount=4,
      MinCount=3)
