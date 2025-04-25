from database import data_collection

# Function to store general data (like settings or configuration)
def store_data(data):
    """Store general data in the database."""
    result = data_collection.insert_one(data)
    return result

# Function to get data by key (e.g., settings or configuration)
def get_data_by_key(key):
    """Retrieve data from the database by its key."""
    data = data_collection.find_one({"key": key})
    return data

# Function to update data by key (if the key already exists)
def update_data_by_key(key, new_data):
    """Update existing data by its key."""
    result = data_collection.update_one(
        {"key": key},
        {"$set": new_data},
        upsert=True  # Creates a new document if the key doesn't exist
    )
    return result

# Function to delete data by key
def delete_data_by_key(key):
    """Delete data from the database by its key."""
    result = data_collection.delete_one({"key": key})
    return result.deleted_count

# Function to get all stored data
def get_all_data():
    """Retrieve all stored data from the database."""
    data = data_collection.find()
    return list(data)
