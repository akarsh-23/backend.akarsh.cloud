from BusinessLogicLayer.UserBO import UserBO
from Model.User import User
import uuid


def handler(event, context):
    user = User()
    user.setId(str(uuid.uuid1()))
    user.setFirstname(event.get("firstname"))
    user.setLastname(event.get("lastname"))
    user.setEmail(event.get("email"))
    user.setGender(event.get("gender"))
    user.setPassword(event.get("pass"))
    response = "Something went wrong!!!"
    try:
        signedup = UserBO(user).signUp()
        if signedup:
            response = "You Have Been Signed Up!"
    finally:
        return response
    
if __name__ == "__main__":
    handler({
        "firstname":"Akarsh",
        "lastname":"Shrivastava",
        "email":"akarsh@akarsh.cloud",
        "gender":"Male",
        "pass":"akarsh@2301"
    }, {})