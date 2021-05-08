#@Created by JoddieNgatz
#Github https://github.com/JoddieNgatz/Youtube-downloader-telegram-bot
# import everything
# import everything
from flask import Flask, request
import re
from time import sleep
import telegram
#import youtube_dl
import pafy

from telegramB.credentials import bot_token, bot_user_name,URL

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

# start the flask app
app = Flask(__name__)
#https://flask.palletsprojects.com/en/1.0.x/quickstart/
#Guide
#use the route() decorator to tell Flask what URL should trigger our function.

app = Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
   # retrieve the message in JSON and then transform it to Telegram object
   update = telegram.Update.de_json(request.get_json(force=True), bot)

   chat_id = update.message.chat.id
   msg_id = update.message.message_id

   # Telegram understands UTF-8, so encode text for unicode compatibility
   text = update.message.text.encode('utf-8').decode()
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   if text == "/start":
       # print the welcoming message
       bot_welcome = """
       Welcome to Youtube downloader bot, this bot will provide a downloadable link of any video url you give and a video. 
       Source code can be found here: github link https://github.com/JoddieNgatz/Youtube-downloader-telegram-bot
       """
       # send the welcoming message
       bot.sendChatAction(chat_id=chat_id, action="typing")
       sleep(1.5)
       bot.sendMessage(chat_id=chat_id, text=bot_welcome, reply_to_message_id=msg_id)

   elif text.startswith('https://') or text.startswith('www.') or text.startswith('youtu'):
        reply = "Recieved file. Processing......"
      
        bot.sendMessage(chat_id=chat_id, text=reply, reply_to_message_id=msg_id)

        #pafy lib resource used: https://pypi.org/project/pafy/

        url = text;
        video = pafy.new(url)
        # print author & video length
        print(video.author, video.length)
        best = video.getbest(preftype="mp4")
        downloadLink = best.url
        bot.sendMessage(chat_id=chat_id, text=downloadLink, reply_to_message_id=msg_id)
        bot.sendVideo(chat_id=chat_id, video=best, reply_to_message_id=msg_id)



   else:
      bot.sendMessage(chat_id=chat_id, text="There was a problem in the message you sent, please send a link", reply_to_message_id=msg_id) 
   
   return 'ok'

@app.route('/test')
def hello_world():
    return "Hello, World"

@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
	#Resources used
	#https://core.telegram.org/bots/webhooks
	#https://github.com/python-telegram-bot/python-telegram-bot/issues/2003
   t = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
   if t:
       return "webhook setup ok- running on {}".format(URL)
   else:
       return "webhook setup failed"

@app.route('/')
def index():
   return '.'


if __name__ == '__main__':
   app.run(threaded=True)
   app.debug = True
   app.run()