#Script that lists running EC2 instances
import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Running Instance Image ID: {} Running instance Instance Type: {} Public IP Address: {} Private IP Address: {}"
              .format(instance['InstanceId'],instance['InstanceType'],instance['PublicIpAddress'],instance['PrivateIpAddress']))
    
#Script that stops running EC2 instance
ec2_list=['i-044f26b9df0f5dbaf', 'i-0c5924fd778cb2fa1']
ec2.instances.filter(Filters=ec2_list).stop()