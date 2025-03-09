from fastapi import FastAPI
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["azuredb"]
print(db)
users_collection = db["users"]


app = FastAPI()

@app.get("/")
def get_users():
    users = list(users_collection.find({},{"_id":0}))
    return {"users": users}

