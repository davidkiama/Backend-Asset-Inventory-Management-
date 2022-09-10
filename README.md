# Backend-Asset-Inventory-Management

This is a backend web server for [Werden Desk Asset Application](https://github.com/davidkiama/Client-Asset-Inventory-Management-.git) react frontend application.

This server is developed by Django Framework, PostgreSQL database nad hosted on heroku.


## Table of contents
+ [Features](#features)
+ [How to install ](#how-to-install)
+ [Emvironment variables](#environment-variables)
+ [Technology Used](#technologies-used)
+ [Behaviour Driven Development](#behavior-driven-development)
+ [Authors Info](#author)

## Features

- Django 4.0+
- Profile and Projects API endpoints.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.


## Technologies used
- Back-end Framework: Django (Version 4.0.3)
- Language: Python (Version 3.8.10)

## How to install
Clone this repo, run:
```bash
git clone https://github.com/davidkiama/Backend-Asset-Inventory-Management-.git
```
Install the required pip in virtual environment, Refer to requirements.txt. Run:
```bash
#Install all dependecies
$ pip install -r requirements.txt
```
Remember to connect to a database and create migrations
```bash
# Make databases and make migrations
$ python manage.py makemigrations 
$ python manage.py migrate 
```
Create django superuser then run server in development
```  bash
$ python manage.py createsuperuser 
#4. Running the application
$ python3 manage.py runserver
```
## Environment variables

These are common between environments. The `ENVIRONMENT` variable loads the correct settings, possible values are: `DEVELOPMENT`, `STAGING`, `PRODUCTION`.

```
ENVIRONMENT='DEVELOPMENT'
DJANGO_SECRET_KEY='you-will-never-guess'
DJANGO_DEBUG='True'
DB_NAME=DB_NAME
DB_USER=DB_OWNER
DB_PASSWORD=DB_PASSWORD
DB_HOST=*
CLOUDINARY_CLOUD_NAME=CLOUDINARY_NAME
CLOUDINARY_API_KEY=CLOUDINARY_API
CLOUDINARY_API_SECRET=CLOUDINARY_SECRET
```

## Behavior Driven Development
| Roles | Type | Created by | Functions |
|-------|------|----------|-------------|
|Employee | Regular User| Self registration userRole 1 or by the System Admin | View and Initiate asset mainteance request(s)|
|Manager |Supervisor | Self registration userRole 2 or or by the System Admin | View and Approve or Reject employee(s) asset maintenance requests. Assign Assets to employee(s)
| System Admin | Django | SuperUser | System Administrator |


| Module | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Auth | Name, Email and Password | User authentication features: SignUp, Login and update account information  |
| Employee | Logged In user details | All employee defined view ports and actions. |
| Manager | Logged In user details |  All employee defined view ports and actions.|



****
## Authors

| Module | Author |
| ------ | ------ |
| Authentication   | [Lewis Murgor](https://github.com/lewis-murgor)  |
| Manager App | [John Kimani](https://github.com/John-Kimani) |
| Employee App | [David Kiama](https://github.com/davidkiama) |