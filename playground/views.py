
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view function is a function that takes a request and returns a response.
# Request Handler aka action

# What we can do: We can pull data from a database, transform data , send email and so on.

# First view function
def say_hello(request): 
  return  render(request, 'hello.html')