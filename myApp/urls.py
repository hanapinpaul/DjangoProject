from django.contrib import admin
from django.urls import path, include 
from . import views



urlpatterns = [
path ("",views.helloworld, name = "helloworld"),
path ("testpath/",views.testPath, name = "testPath")
]
