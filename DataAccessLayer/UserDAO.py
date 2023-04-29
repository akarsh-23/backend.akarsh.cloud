from Model import User 
from boto3.dynamodb.conditions import Attr
import boto3


class UserDAO:
    global dynamodb, table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('users.akarsh.cloud')
    
    def __init__(self, user:User):
        self.__user = user

    def CreateUser(self):
        try:
            table.put_item(
                Item={
                    "userid":self.__user.getId(),
                    "firstname":self.__user.getFirstname(),
                    "lastname":self.__user.getLastname(),
                    "email":self.__user.getEmail(),
                    "gender":self.__user.getGender(),
                    "password":self.__user.getPassword()
                },
                ConditionExpression=Attr("email").not_exists()
            )
            return True;
        except Exception as e:
            raise e