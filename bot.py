import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Candle Bot!")

app = ApplicationBuilder().token("8472262475:AAHudipWWRk-cYOKXWkmYEq5lrqH51N8L-4").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
