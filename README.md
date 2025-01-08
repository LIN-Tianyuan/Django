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
python3 manage.py runserver
```
 - Create Sub-Applications
```bash
cd ~/Desktop/Code/bookmanager
python3 manage.py startapp book
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
### 1.4 Model
 - Define the model class
```python
# book/models.py
from django.db import models

# Model class for book list information
class BookInfo(models.Model):
    # Create fields, field types...
    name = models.CharField(max_length=10)

# Model class for character list information
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # Foreign key constraint: which book the character belongs to
    book = models.ForeignKey(BookInfo)
```
 - Model migration (table construction)
```bash
# Generate migration files: generate statements to create tables based on model classes
python3 manage.py makemigrations
# Perform migration: create tables in the database based on the statements generated in the first step
python3 manage.py migrate
```

### 1.5 Site Management
 - Create manager
```bash
python3 manage.py createsuperuser
```
 - Register Model Classes
```python
# book/admin.py
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)
```
 - Optimize model class presentation
```python
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        """Output the model class as a string"""
        return self.name
```
### 1.6 Views and URLs
 - Define the view
```python
# book/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('OK!')
```
 - Configure URLconf
```python
# settings.py
ROOT_URLCONF = 'bookmanager.urls'
```
```python
# bookmanager/urls.py
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('book.urls'))
    # new version: path 
]
```
```python
# book/urls.py
from book.views import index
urlpatterns = [
    url(r'^$', index)
]
```
### 1.7 Template
 - Create a template
```html
<!-- templates/index.html-->
...
```
 - Setting the template lookup path
```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'template')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
 - Template receives incoming data from the view
```python
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
```
 - Template processing data
```html
<!-- templates/index.html-->
... <div>{{title}}</div>
```
### 1.8 Configuration and static files
 - settings.py
```python
# The root directory of the current project, which Django will rely on to locate relevant files within the project. We can also use this parameter to construct file paths.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


STATIC_URL = '/static/' # URL prefix for accessing static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static') 
]   # Directory for finding static files 
```
