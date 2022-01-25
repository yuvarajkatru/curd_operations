CRUD API WITH DJANGO REST FRAMEWORK
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Requirements
Python 3.6
Django 3.2
Django REST Framework
Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command

python -m venv env
After this, it is necessary to activate the virtual environment, you can get more information about this here

You can install all the required dependencies by running

pip install -r requirements.txt
Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around collections and elements, both of which are resources.

localhost:8000/ebook/create/

{
    "name":"prem",
    "email":"c@c.com",
    "password":"a"
}




First we need to create a user, so we can log in

After we create an account we can use those credentials to get a token
localhost:8000/api/login
{

    "email":"c@c.com",
    "password":"a"
}

To get a token first we need to

token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6M30.O09y2tVCvQ7wE-CkRe3uFQJchj3KQj1F8alZ1ChGcGg
