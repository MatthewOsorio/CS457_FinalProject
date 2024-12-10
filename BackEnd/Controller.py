from UserModel import UserModel
from MangaModel import 
class Controller:
    def __init__(self):
        self.userModel = UserModel()

    def addUser(self, firstname, lastname, email, password):
        self.userModel.insertUserInfo(firstname, lastname, email, password)

    def verifyCredentials(self, email, password):
        return self.userModel.checkCredentials(email, password)