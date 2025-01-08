# Django
```bash
django-admin startproject name

python3 manager.py startapp name
```
## 1. Django Process
### 1.1 Introduction
Django, is an open source web development framework written in the python language and following an MVC design.

 - Provide automated scripting tools for project engineering management

 - Database ORM support (Object Relational Mapping)

 - Templates

 - Forms

 - Admin management site

 - Document Management

 - Authentication rights

 - Session Mechanism

 - Caching

MVT for Django
 - M is Model, which has the same function as M in MVC and is responsible for interacting with the database and processing data.
 - V is View, which has the same function as C in MVC, it receives requests, performs business processing and returns answers.
 - T is Template, which has the same function as V in MVC and is responsible for encapsulating and constructing the html to be returned.

### 1.2 Virtual environment
 - Installation of virtual environment
```bash
sudo pip install virtualenv
sudo pip install virtualenvwrapper
```
 - Configure Environment Variables
```bash
# 1、Create a directory to store the virtual environment
mkdir 
$HOME/.virtualenvs

# 2、Open the ~/.bashrc file and add the following:
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# 3、Run
source ~/.bashrc
```
 - Create virtual environment
```bash
mkvirtualenv -p python3 py3_django
```
 - View virtual environment
```bash
workon
```
 - Use virtual environment
```bash
workon py3_django
```
 - Exit virtual environment
```bash
deactivate
```
 - Delete virtual environment
```bash
deactivate
rmvirtualenv py3_django
```
 - Install the toolkit in a virtual environment
```bash
pip install django
```
 - View packages installed in a virtual environment
```bash
pip list
```
### 1.3 Create django project
 - Create project
```bash
cd ~/Desktop/Code
django-admin startproject bookmanager
python manage.py runserver
```
 - Create Sub-Applications
```bash
cd ~/Desktop/Code/bookmanager
python manage.py startapp book
```
 - Register/install the sub-application
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add sub app
    'book.apps.BookConfig'
]
```