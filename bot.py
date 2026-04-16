import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ YES, I WANT PROFIT", callback_data="yes")],
        [InlineKeyboardButton("❌ JUST WATCHING", callback_data="no")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 Welcome to Cricket Profit System\n\n"
        "💰 Do you want to earn from today's match?",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "yes":
        keyboard = [
            [InlineKeyboardButton("👉 JOIN CHANNEL", url=CHANNEL_LINK)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.message.reply_text(
            "🔥 Smart Choice!\n\n"
            "📊 Join our channel and get today's winning tip:",
            reply_markup=reply_markup
        )

        # Follow-up after 2 minutes
        await asyncio.sleep(120)

        await query.message.reply_text(
            "💎 VIP ACCESS AVAILABLE\n\n"
            "💰 High accuracy premium tips\n"
            "📩 Message admin to join VIP now!"
        )

    else:
        await query.message.reply_text(
            "👍 No problem!\n\n"
            "You can join later anytime when you're ready."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
