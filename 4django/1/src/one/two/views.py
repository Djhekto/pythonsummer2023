from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class MyView(View):
    template_name = "home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name , {})



def home(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)    
    
    #return HttpResponse("<h1>Home</h1>")#peak web design


    return render(request, "home.html", {})

def aboutsmt(request, *args, **kwargs):
    smth_info = {"textt": "This is about us",
                 "idk": 012921.19281,
                 "listt": [1,2,3]
                 }
    return render(request, "about.html", smth_info)







