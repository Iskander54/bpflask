# Boiler plate for python website.
don't forget to change the app name to the client name

## config.py
for all env variable and config variable

## init.py 
to register all your blueprint component

## RUN 
python3 run.py to run the app 

## TRANSLATIONS
routing and translations already implemented

### Translation / language-versionning
#### Fask-babel,babel 
check requirements.txt

#### HOWTO
1- Scan files specified for  text to translate 
`pybabel extract -F babel.cfg -o messages.pot .`

2- Create translation file where we will manually translate text
`pybabel init -i messages.pot -d app/translations -l fr`

translate text in that file

3- Compile all of the translation
`pybabel compile -d app/translations`

messages.mo is created

## Gcloud
`gcloud auth login` : Ouvre une fenetre navigateur pour s'authentifier sur google et sur le projet
`gcloud config set project app` (Pour le site US) 
`gcloud config set project mystical-runway-364716` (Pour le site FR)
`gcloud app deploy` : Déploie l'application dans l'AppEngine
`gcloud app browse` : Ouvre Chrome pour afficher l'application via l'url appengine-mystique


Pour le custom domain DNS sur l'app Engine: https://www.youtube.com/watch?v=iqAku7kveO8&t=8s


## RUN
- go to config.py and :
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    #MAIL_SERVER = os.environ.get('EMAIL_SERVER')
    #MAIL_PORT = os.environ.get('EMAIL_PORT')

- First install packages : $ pip install -r requirements.txt
- Run loccally : python run.py


## Docker
- got to config and :
    #MAIL_SERVER = 'localhost'
    #MAIL_PORT = 1025
    MAIL_SERVER = os.environ.get('EMAIL_SERVER')
    MAIL_PORT = os.environ.get('EMAIL_PORT')
- docker build -t app .
- docker run -d -p 5000:5000  app