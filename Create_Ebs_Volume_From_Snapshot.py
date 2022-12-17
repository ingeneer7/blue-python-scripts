#Create EBS volume from snapshot
import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1c',
      Encrypted=True,
      Size=12,
      SnapshotId='snap-0b319b52ef6f925ec',
      VolumeType='gp2')
