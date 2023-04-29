from DataAccessLayer.UserDAO import UserDAO

class UserBO:
    def __init__(self, user:User):
        self.userdao = UserDAO(user)

    def signUp(self):
        try:
            created = self.userdao.CreateUser()
            if created:
                return true
        except Exception as e:
            raise e