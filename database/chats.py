from database import chats_collection

# Function to log a chat message
def log_chat(chat_data):
    result = chats_collection.insert_one(chat_data)
    return result

# Function to get all chat messages for a particular user
def get_chats_by_user(user_id):
    chats = chats_collection.find({"user_id": user_id})
    return list(chats)

# Function to get the latest chat message for a particular user
def get_latest_chat(user_id):
    chat = chats_collection.find({"user_id": user_id}).sort("timestamp", -1).limit(1)
    return chat[0] if chat.count() > 0 else None

# Function to get all chats in the database
def get_all_chats():
    chats = chats_collection.find()
    return list(chats)

# Function to count the number of chats in the database
def count_chats():
    count = chats_collection.count_documents({})
    return count
