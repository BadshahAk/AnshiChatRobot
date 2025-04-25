from pymongo import MongoClient
from config import MONGO_URI

# MongoDB client setup
client = MongoClient(MONGO_URI)
db = client.get_database()

# Collections for users, chats, and data
users_collection = db.users
chats_collection = db.chats
data_collection = db.data

# Function to fetch a user by their Telegram ID
def get_user_by_id(user_id):
    return users_collection.find_one({"user_id": user_id})

# Function to add or update a user
def upsert_user(user_data):
    return users_collection.update_one(
        {"user_id": user_data["user_id"]},
        {"$set": user_data},
        upsert=True
    )

# Function to log chat messages
def log_chat(chat_data):
    return chats_collection.insert_one(chat_data)

# Function to store general data (could be used for settings or configurations)
def store_data(data):
    return data_collection.insert_one(data)

# Function to fetch data by key
def get_data_by_key(key):
    return data_collection.find_one({"key": key})
