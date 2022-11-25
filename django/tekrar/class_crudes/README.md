 
 DJANGO PROJE AYAĞA KALDIRMA KOMUTLARI 

 1  python -m venv env
 2  .\env\Scripts\activate
 3  pip install django
 4  python -m pip install --upgrade pip
 5  history
 6  clear
 7  pip list
 8  pip freeze
 9  pip freeze > requirements.txt
 10  django-admin startproject main .
 11  python manage.py runserver

 GİTHUB REPODAN PROJE ÇEKİNCE YAPILACAK ADIMLAR

1-python -m venv env
2-env/Scripts/activate
3-pip install -r requirements.txt
4-python.exe -m pip install --upgrade pip
5-pip install python-decouple
6-pip freeze > requirements.txt
7-python manage.py migrate
8-python manage.py createsuperuser
9-python manage.py runserver