import boto3

dynamodb = boto3.resource('dynamodb')


table = dynamodb.create_table(
    TableName='Cars',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'model',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'model',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print('Table status:', table.table_status)

print('Waiting for', table.name, 'to complete creating...')
table.meta.client.get_waiter('table_exists').wait(TableName='Cars')
print('Table status:', dynamodb.Table('Cars').table_status)
