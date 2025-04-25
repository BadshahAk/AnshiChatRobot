from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
from config import CHATBOT_STATUS  # Assuming you have a variable to manage the chatbot state

# Function to toggle the chatbot on and off
def chatbot_toggle(update: Update, context: CallbackContext):
    """Toggles the chatbot state between 'on' and 'off'."""
    if len(context.args) < 1:
        update.message.reply_text("Usage: /chatbot <on/off>")
        return

    action = context.args[0].lower()
    
    if action == "on":
        # Update chatbot status to 'on' in config or a file
        global CHATBOT_STATUS
        CHATBOT_STATUS = True
        update.message.reply_text("Chatbot is now ON! I'll respond to non-reply messages.")
    elif action == "off":
        # Update chatbot status to 'off' in config or a file
        CHATBOT_STATUS = False
        update.message.reply_text("Chatbot is now OFF! I won't respond to messages.")
    else:
        update.message.reply_text("Invalid option. Use '/chatbot on' or '/chatbot off'.")

# Function to handle non-reply messages when chatbot is 'on'
def handle_chat_message(update: Update, context: CallbackContext):
    """Handles non-reply messages when the chatbot is ON."""
    if CHATBOT_STATUS:
        if update.message.reply_to_message:
            # If the message is a reply, do nothing
            return
        
        # Here you can add AI responses or a predefined message
        update.message.reply_text("Hi! I'm your friendly chatbot. How can I help you today?")

# Registering the /chatbot toggle command
chatbot_toggle_handler = CommandHandler("chatbot", chatbot_toggle)

# Registering the message handler for non-reply messages when chatbot is ON
chat_message_handler = MessageHandler(Filters.text & ~Filters.reply, handle_chat_message)

# Add these handlers to the dispatcher in your main bot setup
