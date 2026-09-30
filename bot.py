import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "⚽ សូមស្វាគមន៍មកកាន់ SB24 Live Info!\n"
        "ទទួលព័ត៌មានការប្រកួតបាល់ទាត់ផ្ទាល់ ពិន្ទុ និងលទ្ធផលប្រកួតដែលបានអាប់ដេតតាមពេលវេលាជាក់ស្តែងនៅទីនេះ។"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "SB24 Guide\n"
        "សេវាបើកអាខោន និងព័ត៌មានណែនាំអំពីសេវាកម្ម។"
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bot is online and ready.")


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is required")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("status", status))
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
