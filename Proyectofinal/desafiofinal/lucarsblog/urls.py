from django.urls import path

from lucarsblog.views import *

urlpatterns = [
    path('', mostrar_lucarsblog )
]
