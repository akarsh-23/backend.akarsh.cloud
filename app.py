from Model.User import User
import boto3
import json
import logging
import uuid


def handler(event, context):
    user = User()
    user.setId(uuid.uuid1())
    user.setFirstname(event.get("firstname"))
    user.setLastname(event.get("lastname"))
    user.setEmail(event.get("email"))
    user.setGender(event.get("gender"))
    user.setPassword(event.get("password"))
    response = "Something went wrong!!!"
    try:
        signedup = UserBO(user).signUp()
        response = "You Have Been Signed Up!"
    finally:
        return response