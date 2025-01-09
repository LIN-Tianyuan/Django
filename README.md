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
## 2. Model
### 2.1 Project Preparation Process
 - Create project and application
```bash
django-admin startproject bookmanager
python manager.py startapp book
```
 - Installation of application
   - Create templates folder in the same directory as the application.
```python
# settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add Sub-Apps
    'book.apps.BookConfig'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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
 - Match urls.py in the project
   - New version: path()
```python
# urls.py
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #The regularity is: as long as it's not admin/, it's a successful match.
    url(r'^',include('book.urls'))
]
```
 - Match urls.py in application
   - Create `urls.py` in the application
```python
from django.conf.urls import url
from book.views import bookList

urlpatterns = [

    # Match the URL of the book list information, call the corresponding bookList view.
    url(r'^booklist/$',bookList)
]
```
 - Prepare the view
```python
def bookList(request):
    return HttpResponse('OK!')
```
 - Start Server, Test Program
```bash
# 进入项目文件中, 开启项目对应的服务器
python manage.py runserver
```
 - Enter the URL in browser
   - http://127.0.0.1:8000/booklist/
### 2.2 Configuration MySQL
```bash
pip install PyMySQL
```
```python
# __init__.py
import pymysql

pymysql.install_as_MySQLdb()
```
```python
# settings.py
DATABASES = {
   'default': {
      'ENGINE': 'django.db.backends.mysql',
      'HOST': '127.0.0.1',  
      'PORT': 3306,  
      'USER': 'root',  
      'PASSWORD': 'mysql',  
      'NAME': 'book'  
   }
}
```
### 2.3 Define the model class
```python
# book/models.py
from django.db import models


class BookInfo(models.Model):
   name = models.CharField(max_length=20)
   pub_date = models.DateField(null=True)
   readcount = models.IntegerField(default=0)
   commentcount = models.IntegerField(default=0)
   is_delete = models.BooleanField(default=False)

   class Meta:
      db_table = 'bookinfo'  # Specify the database table name
      verbose_name = 'Book'  # Name displayed in the admin site

   def __str__(self):
      """Define the display information for each data object"""
      return self.name

class PeopleInfo(models.Model):
   GENDER_CHOICES = (
      (0, 'male'),
      (1, 'female')
   )
   name = models.CharField(max_length=20)
   gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
   description = models.CharField(max_length=200, null=True)
   book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
   is_delete = models.BooleanField(default=False)

   class Meta:
      db_table = 'peopleinfo'
      verbose_name = 'People info'

   def __str__(self):
      return self.name
```
 - Migration
   - Synchronize model classes to the database.
```bash
python manage.py makemigrations

python manage.py migrate
```
### 2.4 shell
```bash
python manage.py shell
```
### 2.5 Database operations - add, delete, modify
 - add
```bash
>>> from book.models import BookInfo,PeopleInfo
>>> book = BookInfo(
...         name='python',
...         pub_date='2010-1-1'
...     )
>>> book.save()
>>> book
<BookInfo: python>
```
```bash
>>> PeopleInfo.objects.create(
...         name='alex',
...         book=book
...     )
<PeopleInfo: alex>
```
 - Modify
```bash
>>> person = PeopleInfo.objects.get(name='tom')
>>> person.name = 'luna'
>>> person.save()
>>> person
<PeopleInfo: luna>
```
```bash
>>> PeopleInfo.objects.filter(name='tom').update(name='luna')
1
```
 - Delete
```bash
>>> person = PeopleInfo.objects.get(name='luna')
>>> person.delete()
(1, {'book.PeopleInfo': 1})
```
```bash
>>> BookInfo.objects.filter(name='python').delete()
(1, {'book.BookInfo': 1, 'book.PeopleInfo': 0})
```
### 2.6 Database operations - query
 - Basic query
```bash
BookInfo.objects.get(id=1)

BookInfo.objects.all()

BookInfo.objects.count()
```
```bash
BookInfo.objects.filter(id=1)

BookInfo.objects.filter(name__contains='l')

BookInfo.objects.filter(name__isnull=True)

BookInfo.objects.filter(id__in=[1,3,5])

BookInfo.objects.filter(id__gt=3)

BookInfo.objects.filter(pub_date__gt='1990-1-1')
```
 - F object, Q object
```bash
# Query books with reads greater than or equal to reviews.
>>> from django.db.models import F
>>> BookInfo.objects.filter(readcount__gt=F('commentcount'))
```
```bash
# Search for books with more than 20 reads
>>> BookInfo.objects.filter(Q(readcount__gt=20))

# Queries for books read more than 20, or numbered less than 3, can only be realized using the Q object
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# Query books with number not equal to 3.
>>> BookInfo.objects.filter(~Q(id=3))
```
 - Function
```bash
>>> from django.db.models import Sum
>>> BookInfo.objects.aggregate(Sum('readcount'))
{'readcount__sum': 126}

>>> BookInfo.objects.count()
# Default ascending order
>>> BookInfo.objects.all().order_by('readcount')
# Descending order
>>> BookInfo.objects.all().order_by('-readcount')
```
 - Related queries
   - one to many
```bash
>>> book = BookInfo.objects.get(id=1)
>>> book.peopleinfo_set.all()
```
```bash
>>> people = PeopleInfo.objects.filter(book__name='python')
```
```bash
# Query all characters with book reads greater than 30
>>> people = PeopleInfo.objects.filter(book__readcount__gt=30)
>>> people
```
   - many to one
```bash
person = PeopleInfo.objects.get(id=1)
person.book
```
```bash
>>> person = PeopleInfo.objects.get(id=1)
>>> person.book_id
1
```
```bash
# Search for a book with the character “tom”.
>>> book = BookInfo.objects.filter(peopleinfo__name='tom')
>>> book

# Search for books that require descriptions of characters that include the word “like.”
>>> book = BookInfo.objects.filter(peopleinfo__description__contains='like')
>>> book
```
 - Pagination
```python
# Query Data
books = BookInfo.objects.all()
# Import Pagination Classes
from django.core.paginator import Paginator
# Create a Pagination Example
paginator=Paginator(books,2)
# Get the data of the specified page number
page_skus = paginator.page(1)
# Get Pagination Data
total_page=paginator.num_pages
```