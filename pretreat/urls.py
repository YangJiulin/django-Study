from . import views
from django.urls import path

urlpatterns = [
    path('upload/',views.upload_apk,name='upload')
]