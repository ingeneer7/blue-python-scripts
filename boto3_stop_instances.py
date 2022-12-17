#Script that lists running EC2 instances
import boto3

client = boto3.client('ec2')

response = client.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print("Running Instance Image ID: {} Running instance Instance Type: {} Public IP Address: {} Private IP Address: {}"
              .format(instance['InstanceId'],instance['InstanceType'],instance['PublicIpAddress'],instance['PrivateIpAddress']))

    
#Script that stops all running EC2 instances
ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    instance.stop()

#Script that stops running EC2 instances witht the dev tag
ec2 = boto3.resource("ec2")

ec2_running = {'Name': 'instance-state-name', 'Values': ['running']}
dev_tag = {'Name': 'tag:environment', 'Values': ['dev']}

for instance in ec2.instances.filter(Filters=[dev_tag]):
    instance.stop()
    print("The following EC2 instances are now stopping:", instance.id)
    
    