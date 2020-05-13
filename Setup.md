// Setup
python3 -m venv virtual
source virtual/bin/activate
pip install -r requirements.txt

//Create Main Django Project
django-admin startproject Timeo_Project .
python manage.py runserver

// Creating App
python manage.py startapp profiles_api

// Activate
source virtual/bin/activate
python manage.py runserver

//Migration
python manage.py makemigrations
python manage.py migrate

//Heroku
heroku login

heroku logs --tail
