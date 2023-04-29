from Model import User 
import boto3
import botocore

class UserDAO:
    
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
                }
            )
            return true;
        except Exception as e:
            raise e