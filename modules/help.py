from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

# Function to handle the /help command
def help_command(update: Update, context: CallbackContext):
    """Send a list of available commands and bot information."""
    user = update.effective_user
    message = (
        f"Hello {user.first_name}! Here's a list of commands you can use:\n\n"
        "/start - Start the bot and get a welcome message\n"
        "/ping - Check if the bot is alive\n"
        "/alive - Check if the bot is running\n"
        "/clone <bot_token> - Clone a bot with a given token\n"
        "/ask <question> - Ask the bot a question\n"
        "/scan - Scan a picture for AI answers\n"
        "/chatbot on/off - Toggle the chatbot feature\n\n"
        "For more support, contact our team here: [Support Chat](https://t.me/supportchat)\n"
        "For updates, join our channel: [Update Channel](https://t.me/update_channel)"
    )

    # Send the help message
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# Registering the /help command with the CommandHandler
help_handler = CommandHandler("help", help_command)

# Add this handler to the dispatcher in your main bot setup
