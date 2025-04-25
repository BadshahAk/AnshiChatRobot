from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Function to handle the /ping command
def ping_command(update: Update, context: CallbackContext):
    """Responds to the /ping command to check if the bot is alive."""
    update.message.reply_text("Pong! The bot is alive and running!")

# Registering the /ping command with the CommandHandler
ping_handler = CommandHandler("ping", ping_command)

# Add this handler to the dispatcher in your main bot setup
