import os

# Telegram API credentials
API_ID = os.getenv("API_ID", "your_api_id_here")
API_HASH = os.getenv("API_HASH", "your_api_hash_here")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

# MongoDB URI for storing data
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri_here")

# File Paths
START_IMAGE = os.getenv("START_IMAGE", "your_start_image_url_here")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "your_support_chat_link_here")
UPDATE_CHANNEL = os.getenv("UPDATE_CHANNEL", "your_update_channel_link_here")

# Owner's Telegram ID
OWNER_ID = os.getenv("OWNER_ID", "your_owner_telegram_id_here")

# Log group ID (for logging user details)
LOG_GROUP_ID = os.getenv("LOG_GROUP_ID", "your_log_group_id_here")

# Optional: Bot Settings
ENABLE_CHATBOT = True  # Set to False to disable automatic chatbot replies
