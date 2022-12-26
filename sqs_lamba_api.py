# Import which service or services you're going to use
import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='boto3-lambda-queue')

# You can now access identifiers
print(queue.url)

###########################################################

#Modifies the Lambda Function to include date and time in json output

import json
import boto3

from datetime import datetime


def lambda_handler(event, context):
 
    date_time = datetime.now()
    current_time = date_time.strftime("%H:%M:%S %p")

    sqs = boto3.client('sqs')
    sqs.send_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/256362179396/boto3-lambda-queue",
        MessageBody=("This message was delivered on: " + str(date_time.strftime('%Y-%m-%d %H:%M:%S')))
    )
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }
