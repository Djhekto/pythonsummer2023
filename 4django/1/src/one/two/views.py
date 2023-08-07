from django.shortcuts import render
from django.http import HttpResponse

def home(*args, **kwargs):
    return HttpResponse("<h1>Home</h1>")#peak web design





