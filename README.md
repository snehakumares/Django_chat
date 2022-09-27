# Django_chat

### Real time chat application using django

## Requirements
1. Python
2. PIP

## Setup 
1. Navigate to the folder to create virtual environment 
2. Create virtual environment
```sh
   py -m venv <venv-name>
```
3. Activate virtual environment
```sh
  <venv-name>\Scripts\activate.bat
```
4. Install django
```sh
  py -m pip install Django
```
5. Create project
```sh
   django-admin startproject chatapp 
```
   This will create a folder named chatapp which contains a file manage.py and a folder named chatapp
```
   chatapp
   ├── manage.py
   ├── chatapp
       ├── __init__.py
       ├── asgi.py
       ├── settings.py
       ├── urls.py
       ├── wsgi.py
```
6. Download the code. Replace the contents of the main folder chatapp, with the downloaded code

## Run the project
```sh
cd chat
py manage.py runserver
```
