PostgreSQL setup için  aşağıdaki gibi indir 
pip install psycopg2 

Django Rest Framework (DRF) setup için 
pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.
INSTALLED_APPS = [
# ...
# Third party apps:
'rest_framework',
]

Install Swagger
# https://drf-yasg.readthedocs.io/en/stable/readme.html

backend tarafından frontend kısmına anlaşılır dökümantasyon için swagger ile düzenli bir dökümantasyon sağlanır
swagger GET,PUT,DELETE vb ne kullanıldı ise hepsini tarayıp endpoint(url) ile ilgili API dokumantasyonu sağlıyor


indirmek için :

pip install drf-yasg

Add 'drf_yasg' to your INSTALLED_APPS setting.

INSTALLED_APPS = [
# ...
'django.contrib.staticfiles',
# required for serving swagger ui's css/js files
# Third party apps:
'drf_yasg',
# ...
]


Install Debug Toolbar # https://django-debug-toolbar.readthedocs.io/en/latest/
Django Hata Ayıklama Araç Çubuğu, çeşitli hata ayıklama bilgilerini görüntüleyen bir dizi yapılandırılabilir paneldir:

pip install django-debug-toolbar

Add "debug_toolbar" to your INSTALLED_APPS setting:

INSTALLED_APPS = [
# Third party apps:
# ...
"debug_toolbar",
# ...
]

Add the middleware to the top:
MIDDLEWARE = [
"debug_toolbar.middleware.DebugToolbarMiddleware",
# ...
]

Add configuration of internal IPs to "settings.py":
INTERNAL_IPS = [
"127.0.0.1",
]

Seperate Dev and Prod Settings














