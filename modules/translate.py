from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from googletrans import Translator

# Function to handle the /translate command
def translate_command(update: Update, context: CallbackContext):
    """Translates a given text into the specified language."""
    # Check if user has provided text to translate
    if len(context.args) < 2:
        update.message.reply_text("Usage: /translate <target_language_code> <text_to_translate>")
        return
    
    target_language = context.args[0]
    text_to_translate = ' '.join(context.args[1:])

    # Initialize the translator
    translator = Translator()

    try:
        # Translate the text
        translated_text = translator.translate(text_to_translate, dest=target_language).text
        update.message.reply_text(f"Translated Text: {translated_text}")
    except Exception as e:
        update.message.reply_text(f"Error: Could not translate. {str(e)}")

# Registering the /translate command with the CommandHandler
translate_handler = CommandHandler("translate", translate_command)

# Add this handler to the dispatcher in your main bot setup
