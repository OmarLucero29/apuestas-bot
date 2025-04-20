from telegram import Update  
from telegram.ext import Updater, CommandHandler, CallbackContext  

def start(update: Update, context: CallbackContext):  
    update.message.reply_text("¡Hola! Soy tu bot de apuestas. Usa /tips.")  

def main():  
    updater = Updater("TU_TOKEN_AQUÍ", use_context=True)  
    updater.dispatcher.add_handler(CommandHandler('start', start))  
    updater.start_polling()  
    updater.idle()  

if __name__ == "__main__":  
    main()  
