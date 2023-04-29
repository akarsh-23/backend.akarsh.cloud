from DataAccessLayer.UserDAO import UserDAO
from Model.User import User

class UserBO:
    def __init__(self, user:User):
        self.userdao = UserDAO(user)

    def signUp(self):
        try:
            created = self.userdao.CreateUser()
            if created:
                return True
        except Exception as e:
            raise e