# "Writing your first Django app" Tutorial Code & Other Django/Python Tips

This repository contains a simple django application for creating polls and leaving suggestions. It is based on the [Django documentation's tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/), and is a small project for experimenting with new things and breaking stuff. This README is a collection of parts of the tutorial that I am saving for future reference, mistakes I made while following the tutorial, and other useful tips.

## Django Project Structure 

### Project vs Application

What’s the difference between a project and an app? An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
* The outer mysite/ root directory is just a container for the project. It can be renamed to whatever you want, Django doesn't care. 
* The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you'll need to use to import anything inside it (e.g. mysite.urls).

Create apps from the same directory as manage.py, and type the command: 

```
python3 manage.py startapp <appname>
```

```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

This resulting directory structure will house the poll application.

## Makemigrations vs Migrate

The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.

### makemigrations

```
python3 manage.py makemigrations
```
Creates migrations for changes to models

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py.


### migrate

```
python3 manage.py migrate
```

Applies changes to the database

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app. You’ll see a message for each migration it applies. 



## Django & Python Naming Conventions

## Virtual Environments

## What should I put in the .gitignore?

## Resources 
* [Django docs tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
* [Django database API](https://docs.djangoproject.com/en/3.0/topics/db/queries/)

