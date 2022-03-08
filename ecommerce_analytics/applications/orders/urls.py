from django.contrib import admin    
from django.urls import path

def from_app(self):
    print('----From app orders----')

urlpatterns = [
    path('orders/', from_app),
]