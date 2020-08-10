Querybook - Books REST API
==============================


https://querybook.herokuapp.com/

What Is This?
-------------

This is a Python/Django/DjangoRestFramework application intended to provide a working example of simple REST API. 
The goal of these endpoints is to provide a base for developers to develop other applications off of. 


How To Use This
---------------

1. Clone app into Your local repository `git clone https://github.com/michal-siedlecki/books`
1. Activate virtual environment `source venv/bin/activate`
1. Run `pip install -U -r requirements.txt` to install dependencies
1. Now create database and database user on Your local PostgreSQL database
1. Run `python manage.py migrate` to populate database with tables
1. Run `python manage.py runserver`
1. Navigate to http://localhost:8000 in your browser


Testing
-------

1. The test folder is outside apps. 
1. Run the command `python manage.py test tests`
1. If you delete the fixtures, or decide to add some of your own run the tests.
