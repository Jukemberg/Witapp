# Witapp test project

## Requirements

I have used only base Django for this project, so the only requirement is to install it, for example i have used a venv but you can do it globally too.

global
```bash
pip install django==5.0.4
```
with venv
```bash
python -m venv venv
. venv/bin/activate
pip install django==5.0.4
```
with venv (from Windows)
```bash
python -m venv venv
. venv/Scripts/activate
pip install django==5.0.4
```

## Introduction

The project contains already in itself a small db with some data so you can access it more easily for review, it has:

- an Admin superuser (witapp/admin)
- some Polls
- my test User

If instead you prefer to start clean:
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

I have left the project with DEBUG=True in the settings for ease of use while developing and especially for the EMAIL_BACKEND i didn't wanted to setup an SMTP so i just left the console one.

To run the project:
```bash
python manage.py runserver
```

## Polls tutorial 1-7

I have implemented the Django tutorial inside the project, after creating a User and logging in there will be an option to view the Polls and interact with them.
If you want to create some new Polls is possible from the [Admin](http://127.0.0.1:8000/admin).
Polls are accessible even without loggin in at their [url](http://127.0.0.1:8000/polls) they don't require an User to be used.

## Requested features

In the app Account there is the Django auth urls and a simple integration of a Profile that allows for simple functions:

- Login
- Register
- Edit your Profile
- Change your password
- Logout
- Forgot password

Inside the edit Profile there is:

- Date of birth
- Place of birth
- Address
- Personal number
- Work number