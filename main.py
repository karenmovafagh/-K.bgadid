from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! من ربات کارن موفق هستم.")

def main():
    TOKEN = "توکن رباتت اینجا قرار بگیره"
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
