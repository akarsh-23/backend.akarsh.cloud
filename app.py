import boto3
import json

def handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }