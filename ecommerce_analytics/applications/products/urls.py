from django.contrib import admin    
from django.urls import path

def from_app(self):
    print('----From app produts----')

urlpatterns = [
    path('products/', from_app),
]