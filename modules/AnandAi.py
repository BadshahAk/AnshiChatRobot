from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
import openai
from config import OPENAI_API_KEY

# Set up OpenAI API key
openai.api_key = OPENAI_API_KEY

# Function to handle the /ask command
def ask_command(update: Update, context: CallbackContext):
    """Handles user queries and fetches AI responses from OpenAI."""
    # Check if user has provided a question
    if len(context.args) < 1:
        update.message.reply_text("Usage: /ask <your_question>")
        return

    # Get the question from user input
    user_question = ' '.join(context.args)

    try:
        # Call the OpenAI API to get the answer
        response = openai.Completion.create(
            model="text-davinci-003",  # Use the desired OpenAI model
            prompt=user_question,
            max_tokens=150  # Adjust token count based on your needs
        )

        # Get the response text
        answer = response.choices[0].text.strip()

        # Send the answer back to the user
        update.message.reply_text(f"Answer: {answer}")

    except Exception as e:
        update.message.reply_text(f"Sorry, I couldn't process your request. Error: {str(e)}")

# Registering the /ask command with the CommandHandler
ask_handler = CommandHandler("ask", ask_command)

# Add this handler to the dispatcher in your main bot setup
