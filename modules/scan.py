from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext
import pytesseract
from PIL import Image
import openai
from config import OPENAI_API_KEY
import requests
from io import BytesIO

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to handle the /scan command
def scan_command(update: Update, context: CallbackContext):
    """Handles image messages, performs OCR and answers the extracted question using OpenAI."""
    # Check if the user has sent an image
    if update.message.photo:
        # Get the largest photo
        photo_file = update.message.photo[-1].get_file()
        photo_url = photo_file.file_url

        # Fetch the image from the URL
        response = requests.get(photo_url)
        img = Image.open(BytesIO(response.content))

        try:
            # Perform OCR on the image
            extracted_text = pytesseract.image_to_string(img)

            if extracted_text.strip() == "":
                update.message.reply_text("Sorry, I couldn't read any text from the image.")
                return

            update.message.reply_text(f"Extracted Text: {extracted_text}")

            # Send the extracted text to OpenAI for a response
            response = openai.Completion.create(
                model="text-davinci-003",  # Use the desired OpenAI model
                prompt=extracted_text,
                max_tokens=150  # Adjust token count based on your needs
            )

            # Get the AI response and send it to the user
            ai_answer = response.choices[0].text.strip()
            update.message.reply_text(f"Answer: {ai_answer}")

        except Exception as e:
            update.message.reply_text(f"Error: Could not process the image. {str(e)}")
    else:
        update.message.reply_text("Please send an image with a question for me to scan.")

# Registering the /scan command with the CommandHandler
scan_handler = CommandHandler("scan", scan_command)

# Add this handler to the dispatcher in your main bot setup

# Register the message handler for images
image_handler = MessageHandler(Filters.photo, scan_command)

# Add both handlers to your dispatcher
