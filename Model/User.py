class User:
    def __init__(self):
        self.__id = str()
        self.__firstname = str()
        self.__lastname = str()
        self.__email = str()
        self.__gender = str()
        self.__password = str()

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getFirstname(self):
        return self.__firstname

    def setFirstname(self, firstname):
        self.__firstname = firstname

    def getLastname(self):
        return self.__lastname

    def setLastname(self, lastname):
        self.__lastname = lastname

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password