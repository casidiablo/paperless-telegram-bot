from bottle import run, post, request
from telegram.ext import Updater
from pprint import pprint
import os
import logging

telegram_token = os.environ['TELEGRAM_TOKEN']
secret = os.environ['SECRET']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

updater = Updater(token=telegram_token)

def choose_bigger_photo(options):
    bigger = None
    bigger_size = 0
    for option in options:
        if option['file_size'] > bigger_size:
            bigger = option
            bigger_size = option['file_size']
    
    return bigger

@post('/token/%s' % secret)
def process():
    message = request.json['message']
    logging.info(message)

    if 'photo' in message:
        bigger = choose_bigger_photo(message['photo'])
        filename = message.get('caption') or bigger['file_id']
        filename = filename + '.png'
        file_id = bigger['file_id']
    elif 'document' in message:
        original_filename = message['document']['file_name']
        _, file_extension = os.path.splitext(original_filename)
        if 'caption' in message:
            filename = message.get('caption') + file_extension
        else:
            filename = original_filename
        file_id = message['document']['file_id']
    else:
        logging.error('Didnt find photo or document')
        return 'Ignoring'
        
    file = updater.bot.get_file(file_id)
    download_result = file.download(custom_path=('/downloads/%s' % filename))

    logging.info(download_result)

    return "File downloaded? %s" % download_result

run(host='0.0.0.0', port=8080, debug=True)
