from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import MyModel

class MyView(View):
    template_name = "home.html"
    
    def get(self, request, id= None, *args, **kwargs):
        context = {}
        if id == None:
            return render(request, self.template_name , {})
        else:
            template_name = "idk_detail.html"
            obj1 = get_object_or_404(MyModel, id = id)
            context['object'] = obj1
            return render(request, template_name , context)# //ne self
            

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







