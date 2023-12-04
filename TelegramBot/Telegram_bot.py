from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import dummy_store

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am your bot.')

def products(update, context):
    """Send a list of products when the command /products is issued."""
    product_data = dummy_store.get_products()
    if isinstance(product_data, dict):
        # Format and send the product data
        message = "Products:\n" + "\n".join([f"{product['title']} - ${product['price']}" for product in product_data["products"][:10]])  # Displaying first 10 products
        update.message.reply_text(message)
    else:
        update.message.reply_text(product_data)  # Error message from the API


def main():
    """Start the bot."""
    TOKEN = '6924670285:AAEyuEf-1_nnIT7E13Mh345nqW3-9ZHRx54'

    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(CommandHandler("products", products))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()






if __name__ == '__main__':
    main()
