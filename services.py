from dal import UserDAO, DatabaseDAO
import os

class UserService:
    @staticmethod
    def authenticate(username, password):
        password = hash(password)
        return UserDAO.authenticate(username, password)
    
    @staticmethod
    def addUser(username, password) -> bool:
        # hashe le password
        password = hash(password)
        if UserService.userExists(username):
            return False
        else:
            UserDAO.addUser(username, password)
            return True
        
    @staticmethod
    def userExists(username) -> bool:
        return UserDAO.userExists(username)