import os
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OPENAI_API_KEY, ENABLE_CHATBOT, LOG_GROUP_ID
import logging
from modules.chatbot import chatbot_reply
from modules.start import start_command
from modules.help import help_command
from modules.ping import ping_command
from modules.alive import alive_command
from modules.ask import ask_command
from modules.scan import scan_command

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Telegram bot client
app = Client(
    "AnshiChatBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Start command: Show the start panel with buttons
@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await start_command(client, message)

# Help command: Show list of all commands
@app.on_message(filters.command("help"))
async def help(client, message: Message):
    await help_command(client, message)

# Ping command: Check if the bot is alive
@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    await ping_command(client, message)

# Alive command: Bot's status
@app.on_message(filters.command("alive"))
async def alive(client, message: Message):
    await alive_command(client, message)

# Ask command: Handle AI questions
@app.on_message(filters.command("ask"))
async def ask(client, message: Message):
    question = message.text.split(' ', 1)[1] if len(message.text.split(' ', 1)) > 1 else None
    if question:
        await ask_command(client, message, question)
    else:
        await message.reply_text("Please ask a question after the command.")

# Scan command: Handle image-based questions
@app.on_message(filters.command("scan"))
async def scan(client, message: Message):
    if message.photo:
        await scan_command(client, message)
    else:
        await message.reply_text("Please send a photo with the question.")

# Chatbot automatic replies in groups (only for non-reply messages)
@app.on_message(filters.text & ~filters.reply)
async def chatbot(client, message: Message):
    if ENABLE_CHATBOT:
        response = await chatbot_reply(client, message)
        if response:
            await message.reply_text(response)

# Log every new user starting the bot
@app.on_message(filters.command("start"))
async def log_user(client, message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    username = message.from_user.username
    chat_id = message.chat.id
    user_info = f"User ID: {user_id}, Name: {user_name}, Username: @{username}, Chat ID: {chat_id}"
    logger.info(f"New user started the bot: {user_info}")

    # Log user in a specific group (for monitoring or logging)
    if LOG_GROUP_ID:
        try:
            await app.send_message(LOG_GROUP_ID, user_info)
        except Exception as e:
            logger.error(f"Failed to log user info: {e}")

# Run the bot
if __name__ == "__main__":
    app.run()
