from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import psutil
import os

# Function to handle the /alive command
def alive_command(update: Update, context: CallbackContext):
    """Responds to the /alive command to check if the bot is still running."""
    
    # Getting the bot's process information
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Memory usage in MB
    cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage in percentage

    # Sending the bot's status information
    status_message = (
        f"The bot is alive and running!\n\n"
        f"Memory Usage: {memory_usage:.2f} MB\n"
        f"CPU Usage: {cpu_usage}%"
    )

    update.message.reply_text(status_message)

# Registering the /alive command with the CommandHandler
alive_handler = CommandHandler("alive", alive_command)

# Add this handler to the dispatcher in your main bot setup
