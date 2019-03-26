from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.c4e

new_post = {
    "title": "C4E28",
    "author": "Bang",
    "content": "Hello World",
}
db.posts.insert_one(new_post)