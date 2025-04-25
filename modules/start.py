from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config import START_IMAGE_LINK

# Function to handle the /start command
def start_command(update: Update, context: CallbackContext):
    """Send a welcome message and bot information."""
    user = update.effective_user
    message = (
        f"Hello {user.first_name}!\n\n"
        "Welcome to AnshiChatRobot! I'm a cute, sanskari baby girl who loves to chat.\n"
        "I can respond to random messages and answer your questions. "
        "Type /help for a list of commands you can use.\n\n"
        f"Support: {SUPPORT_CHAT_LINK}\n"
        f"Updates: {UPDATE_CHANNEL_LINK}"
    )

    # Sending the start message with an image
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=START_IMAGE_LINK)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Registering the /start command with the CommandHandler
start_handler = CommandHandler("start", start_command)

# Add this handler to the dispatcher in your main bot setup
