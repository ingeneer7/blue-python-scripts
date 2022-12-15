#Describe VPC
import boto3
client=boto3.client("ec2")

#Describe available VPC
x=client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
len(no_of_vpcs)

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    
#Describe one vpc based on vpc id
x=client.describe_vpcs(VpcIds=["vpc-05f97d4a","vpc-0764dcc2284a0bf83"])
x

#Describe vpc based on filter
x=client.describe_vpcs()
x=client.describe_vpcs(Filters=[
          {
              'Name': 'vpc-id',
              'Values': [
                  'vpc-05f97d4a',
                  'vpc-0764dcc2284a0bf83'
                  
              ]
          },
      ])
      
x
