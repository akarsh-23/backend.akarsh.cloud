import boto3
import json
import logger

def handler(event, context):
    logger.info("event: " + str(event))
    print("event: " + str(event))
    print("context: " + str(context))
    logger.info("context: " + str(context))
    return json.dumps(event)
    