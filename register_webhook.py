from telegram.ext import Updater
import sys

if len(sys.argv) != 3:
    print('Wrong number of arguments. Expected Telegram token and URL')
    exit(1)

telegram_token = sys.argv[1]
url = sys.argv[2]

updater = Updater(token=telegram_token)
#print(updater.bot.set_webhook(url))
print(updater.bot.get_webhook_info())
