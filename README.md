# Youtube downloader telegram bot

 This bot will provide a video and downloadable link when given a youtube link.
 
 This bot can be found on Telegram: t.me/Youtubedownloader_jod_bot
 
 
 Project Stucture:
 
   app.py
   
   telegramB->:
   
               -credentials.py
               
               -__inti__.py
               
   requirements.txt
   
   procfile
   
   Scripts->
   
________________________________________________________________________
I. Librarys Used:

1.Flask

3.Python-telegram-bot

5.Requests

7.pafy
________________________________________________________________________
II. Steps:

1. Create your bot on BotFather in telegram Acquire Token and user name and add them to credentials.py in telegramB file
2. Activate venv {cd to scripts, activate.bat in cmd if windows}
3. Test and run with debug on true
4. use 127.0.0.1:5000/test to test returns simple hello world, use 127.0.0.1:5000/set_webhook to test if webhook setup okay
5. Go to heruko create account if you don't have one. Once logged in on Dashboad, create a new app follow steps, then go to settings tab and copy domain of the app, paste it in credentials.py in url variable.
6. Now follow heruko steps below to deploy. Success you bot now works.
________________________________________________________________________
III. Resources:

1.Webhook resources:
https://github.com/python-telegram-bot/python-telegram-bot/issues/2003

2.Import issue with vs code
https://stackoverflow.com/questions/53939751/pylint-unresolved-import-error-in-visual-studio-code

3. Pafy documentation for downloads
https://pypi.org/project/pafy/

4. Telegram documentation on Bots
https://core.telegram.org/bots

5. Flask Resources used:
https://flask.palletsprojects.com/en/1.0.x/quickstart/

6.Heruko resources used:
https://devcenter.heroku.com/articles/git

_______________________________________________________________________________
IV: Heruko:

#requiremnts.txt list of all packages you will be using
1. pip freeze > requirements.txt - generate requirements.txt --You can skip this as requirements file is set up to pass deployment

2. add to procfile web: gunicorn app:app  --You can skip this as already added

3. heroku login || heroku login -i   --login to heruko
4. git init
5. heroku git:remote -a heroku-project-name
6. git add .
7. git commit -m "first commit"
8. git push heroku master


__________________________________________________________________________

####   Some Notes  ####

#we need  to create a virtual environment if we dont want to intall global
#to create virtual env all it is is a folder
#use pip intall virtualenv
#####windows: python -m venv <folder_name> 
####windows python -m venv <TELEGRAMBOT>
#####windows python -m venv <venv>
####linux virtualenv <folder_name>

#using virtual env
#windows systems
#cmd= <floder_name>\Scripts\Activate.bat
#POWERSHELL= <FOLDER_NAME>\Scripts\Activate.psi
#Bash= ../<folder_name>/Scripts/activate
#linux= <folder_name>/bin/activate

#to install package pip install-r requirements.txt
_______________________________________________________
