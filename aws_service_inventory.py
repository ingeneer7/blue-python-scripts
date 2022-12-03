#Create a list of services using Python. IE: S3, Lambda, EC2, etc.

#The list should be empty initially
inventory_list = []

#Populate the list using append or insert
inventory_list.append('EC2')
inventory_list.append('S3')
inventory_list.append('Lambda')
inventory_list.append('RDS')
inventory_list.append('CloudFront')
inventory_list.append('Glacier')
inventory_list.append('SNS')
inventory_list.append('EBS')
inventory_list.append('Cloudwatch')
inventory_list.append('VPC')
inventory_list.append('Kinesis')
inventory_list.append('IAM')
inventory_list.append('SQS')
inventory_list.append('Elastic Beanstalk')
inventory_list.append('DynamoDB')
inventory_list.append('ElasticCache')
inventory_list.append('Redshift')
inventory_list.append('EFS')
inventory_list.append('Cognito')
inventory_list.append('Inspector')

#Print the list and the length of the list
#print(inventory_list)
#print(len(inventory_list))

#Remove two specific services from the list by name or by index
del inventory_list[7]
del inventory_list[16]

#Print the new list and the new length of the list
print(inventory_list)
print(len(inventory_list))