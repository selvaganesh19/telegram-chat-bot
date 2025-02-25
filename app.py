import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random

# Load WhatsApp chat data
with open("WhatsApp Chat with Goks - 🩵🐣✨.txt", "r", encoding="utf-8") as f:
    chat_data = f.readlines()

# Function to get only "Goks - 🩵🐣✨" responses
def get_goks_reply(user_input):
    responses = []
    for i in range(len(chat_data) - 1):
        if user_input.lower() in chat_data[i].lower():
            next_message = chat_data[i + 1].strip()
            if "Goks - 🩵🐣✨:" in next_message:
                responses.append(next_message.split(":", 1)[1].strip())  
    return random.choice(responses) if responses else "Nee enna soldra purila da..?"

# Telegram Bot Setup
TOKEN = "8024901740:AAFc-a9YP5LMAWNch0SJ3OSNE0wf33nmI84"
app_telegram = Application.builder().token(TOKEN).build()

# Command Handler
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Buttu"
    )

# Message Handler
async def handle_message(update: Update, context: CallbackContext):
    try:
        user_message = update.message.text
        response = get_goks_reply(user_message)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text("Sorry, I had an issue processing your request.")

# Adding Handlers
app_telegram.add_handler(CommandHandler("start", start))
app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# Run Telegram Bot (without asyncio.run)
if __name__ == '__main__':
    print("✅ Telegram Bot is running...")
    app_telegram.run_polling()
