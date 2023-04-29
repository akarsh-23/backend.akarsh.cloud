import boto3
import json
import logging

def handler(event, context):
    print("event: " + str(event))
    print("context: " + str(context))
    return event.get("resource",{"value":"Not Available"})
    