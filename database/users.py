from database import users_collection

# Function to get user by Telegram user ID
def get_user_by_id(user_id):
    user = users_collection.find_one({"user_id": user_id})
    return user

# Function to add or update a user
def upsert_user(user_data):
    result = users_collection.update_one(
        {"user_id": user_data["user_id"]},
        {"$set": user_data},
        upsert=True
    )
    return result

# Function to delete a user
def delete_user(user_id):
    result = users_collection.delete_one({"user_id": user_id})
    return result.deleted_count

# Function to get all users
def get_all_users():
    users = users_collection.find()
    return list(users)

# Function to check if a user exists
def user_exists(user_id):
    user = users_collection.find_one({"user_id": user_id})
    return user is not None
