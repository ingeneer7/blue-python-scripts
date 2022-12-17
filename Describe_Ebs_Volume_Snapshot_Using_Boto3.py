#Describe EBS Volume Snapshot
import boto3
ec2_boto3=boto3.client("ec2")

ec2_boto3.describe_snapshots(SnapshotIds=[
          'snap-0cc6fcfeb47686472'
      ])
