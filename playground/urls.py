from django.urls import path
from . import views

# Special Variable: all in lowercase
urlpatterns = [
    path('hello/', views.say_hello)
]