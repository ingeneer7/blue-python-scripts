# Import which service or services you're going to use
import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Create the queue. This returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='boto3-lambda-queue')

# You can now access identifiers
print(queue.url)
