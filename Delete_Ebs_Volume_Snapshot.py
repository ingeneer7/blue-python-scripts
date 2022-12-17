#Delete EBS Volume Snapshot
import boto3
ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-0b319b52ef6f925ec')
