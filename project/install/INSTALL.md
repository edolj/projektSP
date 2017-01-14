Lokalno Django

programsko okolje: vseeno

rabimmo python in django
pip install python
pip install django

naredimo strukturo za django
django-admin startproject mysite
python manage.py runserver
python manage.py startapp webPage

pozenemo server
python manage.py runserver
(dobimo http kjer se nahaja aplikacija)

Setup Database:
python manage.py migrate
python manage.py makemigrations (article)
python manage.py sqlmigrate webPage 0001
python manage.py showmigrations
python manage.py migrate

za teste: python manage.py test
