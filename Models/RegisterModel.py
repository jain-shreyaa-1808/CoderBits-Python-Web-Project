import pymongo
import bcrypt
from pymongo import MongoClient

class RegisterModel:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.coderbit
        self.Users=self.db.Users

    def insert_user(self,data):
       hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

       id = self.Users.insert({"username":data.username,"first_name":data.first_name,"last_name":data.last_name,"password":hashed,"email":data.email})
       print("Succesfully added user:",id)
       myuser=self.Users.find_one({"username":data.username})
       if bcrypt.checkpw("happy".encode(),myuser["password"]):
           print("correct password")

