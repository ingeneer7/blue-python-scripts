import boto3

# create an SNS client
sns = boto3.client('sns')

# Set the name of the topic
topic_name = 'my-topic'

# Create the topic
response = sns.create_topic(Name=topic_name)

# Get the ARN of the topic
topic_arn = response['TopicArn']

# Set the email address to subscribe
email_address = 'cacheout7@gmail.com'

# Subscribe the email address to the topic
response = sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email_address)

# Print the subscription ARN
print(response['SubscriptionArn'])
