import pymongo,bcrypt
from pymongo import MongoClient

class Posts:
    def __init__(self):
        self.client=MongoClient()
        self.db=self.client.coderbit
        self.Users=self.db.users
        self.Posts=self.db.posts
    def insert_post(self,data):
        inserted=self.Posts.insert({"username":data.username,"content":data.content})
        return True
    def get_all_post(self):
        all_post=self.Posts.find()
        new_posts=[]
        for post in all_post:
            post["user"]=self.Users.find_one({"username":post["username"]})
            new_posts.append(post)
        return new_posts