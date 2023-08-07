from django.shortcuts import render
from django.http import HttpResponse

def home(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)    
    
    #return HttpResponse("<h1>Home</h1>")#peak web design


    return render(request, "home.html", {})




