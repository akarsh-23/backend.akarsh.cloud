import boto3
import json

def handler(event, context):
    print("event: " + str(event))
    print("context: " + str(context))
    return str(event["queryStringParameters"])
    