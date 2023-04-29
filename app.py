import boto3
import json
import logging

def handler(event, context):
    logging.info("event: " + str(event))
    print("event: " + str(event))
    print("context: " + str(context))
    logging.info("context: " + str(context))
    return json.dumps(event)
    