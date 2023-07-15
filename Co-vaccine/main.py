import api_key as key
from telegram.ext import *
import response as rs

print("Bot started...")


def start_command(update, context):
    update.message.reply_text("Enter Your area PIN code")


def help_command(update, context):
    update.message.reply_text("Just simply Enter your pin code after giving start command")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = rs.responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(key.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
