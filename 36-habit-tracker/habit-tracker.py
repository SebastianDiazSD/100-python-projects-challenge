"""
Habit Tracker 🇨🇴🏃‍♂️📈
--------------------------------

Project #36 – 100 Python Projects Challenge
Telegram + Pixela + PythonAnywhere Edition

- Sends a daily Telegram reminder to log your running distance.
- Allows entering today’s or previous day’s distance.
- Posts data to Pixela automatically.

Author: Your Name 🇨🇴
"""

import os
import requests
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes,
)
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# --- Telegram conversation states ---
ASK_QUANTITY, ASK_PREVIOUS_DATE, ASK_PREVIOUS_QUANTITY = range(3)

# --- Logging setup ---
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# --- Pixela endpoint ---
PIXELA_URL = f"https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
HEADERS = {"X-USER-TOKEN": PIXELA_TOKEN}

# --- Start command ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey parcero! 🇨🇴 Ready to log your km for today?\n"
        "Send me the number of km you ran 🏃‍♂️\n\n"
        "If you forgot to log another day, type /previous."
    )
    return ASK_QUANTITY

# --- Handle today’s km input ---
async def handle_quantity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quantity = update.message.text.strip()
    date_today = datetime.now().strftime("%Y%m%d")

    try:
        float(quantity)
    except ValueError:
        await update.message.reply_text("Hmm, that doesn’t look like a number, bro 😅. Try again.")
        return ASK_QUANTITY

    data = {"date": date_today, "quantity": quantity}
    res = requests.post(PIXELA_URL, json=data, headers=HEADERS)
    msg = res.json().get("message", "")

    if res.ok:
        await update.message.reply_text(f"✅ Sweet! Logged {quantity} km for today ({date_today}). 🇨🇴🔥")
    else:
        await update.message.reply_text(f"🤔 Could not log: {msg}")

    return ConversationHandler.END

# --- Handle /previous flow ---
async def previous(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Alright, bro 😎. Send me the date you want to log (format YYYYMMDD, e.g., 20251110):"
    )
    return ASK_PREVIOUS_DATE

async def handle_previous_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    date_str = update.message.text.strip()

    try:
        datetime.strptime(date_str, "%Y%m%d")
    except ValueError:
        await update.message.reply_text("Oops, bad format. Use YYYYMMDD (e.g., 20251110).")
        return ASK_PREVIOUS_DATE

    context.user_data["previous_date"] = date_str
    await update.message.reply_text(f"Got it! How many km did you run on {date_str}? 🏃‍♂️")
    return ASK_PREVIOUS_QUANTITY

async def handle_previous_quantity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    quantity = update.message.text.strip()
    date_str = context.user_data["previous_date"]

    try:
        float(quantity)
    except ValueError:
        await update.message.reply_text("That’s not a valid number, man. Try again.")
        return ASK_PREVIOUS_QUANTITY

    data = {"date": date_str, "quantity": quantity}
    res = requests.post(PIXELA_URL, json=data, headers=HEADERS)
    msg = res.json().get("message", "")

    if res.ok:
        await update.message.reply_text(f"✅ Cool! Logged {quantity} km for {date_str}. 🇨🇴")
    else:
        await update.message.reply_text(f"🤔 Could not log: {msg}")

    return ConversationHandler.END

# --- Cancel handler ---
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Alright, cancelled. Catch you later for another run 💪🇨🇴")
    return ConversationHandler.END

# --- Main function ---
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start), CommandHandler("previous", previous)],
        states={
            ASK_QUANTITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_quantity)],
            ASK_PREVIOUS_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_previous_date)],
            ASK_PREVIOUS_QUANTITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_previous_quantity)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)

    print("🤖 Bot is running... ready to log some runs 🇨🇴")
    app.run_polling()

if __name__ == "__main__":
    main()
