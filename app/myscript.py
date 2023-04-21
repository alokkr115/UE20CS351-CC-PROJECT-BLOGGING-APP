from pymongo import MongoClient
from datetime import datetime

user = 'username'           # username as set for the mongodb admin server (the username used in secret.yaml - before base64 conversion)
password = 'password'       # password as set for the mongodb admin server (the password used in secret.yaml - before base64 conversion)
host = 'mongodb-service'    # service name of the mongodb admin server as set in the service for mongodb server
port = 27017              # port number of the mongodb admin server as set in the service for mongodb server
conn_string = f'mongodb://{user}:{password}@{host}:{port}'

db = MongoClient(conn_string).blog
createdAt = datetime.now()

db.posts.insert_one({"title": "script entry", "author": "myscript.py", "createdAt": createdAt})