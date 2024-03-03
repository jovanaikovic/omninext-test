import json
import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def createUser(event, context):
    try:
        data = json.loads(event['body'])
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    
    if 'name' not in data or 'email' not in data:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing name or email'})
        }
    

    user = {
        'userId': str(uuid.uuid4()),
        'name': data['name'],
        'email': data['email'],
        'createdAt': str(datetime.utcnow())
    }
    try:
        table.put_item(Item=user)
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not create the user'})
        }

    return {
        'statusCode': 201,
        'body': json.dumps(user)
    }


def getUserById(event, context):
    userId = event['pathParameters']['id']
    result = table.get_item(Key={'userId' : userId})
    user = result.get('Item')

    if not user:
        return {'statusCode': 404, 'body': json.dumps({'error': 'User not found'})}
    
    return {'statusCode': 200, 'body': json.dumps(user)}
