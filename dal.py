import mysql.connector as my
# env
import os
from dotenv import load_dotenv as ld # type: ignore

class DatabaseDAO:
    con = None

    @staticmethod
    def getCon():
        if DatabaseDAO.con == None:
            con = my.connect(user=os.getenv('DB_USER'), password=os.getenv('DB_PASSWORD'), host=os.getenv('DB_HOST'), database='db_WebAlpha')
            DatabaseDAO.con = con
        
        return DatabaseDAO.con


class UserDAO:

    @staticmethod
    def authenticate(username, password):
        con = DatabaseDAO.getCon()
        cursor = con.cursor()
        # execute the sql function VerifierUtilisateur(email_param VARCHAR(50), password_param VARCHAR(50))
        cursor.execute("SELECT VerifierUtilisateur(%s, %s)", (username, password))
        # get the result
        result = cursor.fetchone()
        # close the cursor
        cursor.close()
        return result[0] == 1 # type: ignore
    
    @staticmethod
    def addUser(username, password):
        con = DatabaseDAO.getCon()
        cursor = con.cursor()         
        cursor.execute("SELECT AjouterUtilisateur(%s, %s)", (username, password))
        cursor.close()
        
    @staticmethod
    def userExists(username):
        con = DatabaseDAO.getCon()
        cursor = con.cursor()
        cursor.execute("SELECT count(*) FROM T_auth WHERE email = %s", (username,))
        result = cursor.fetchone()
        cursor.close()
        return result[0] == 1 # type: ignore