from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import MyModel
from .forms import MyModelForm

class MyMixin(object):
    model = MyModel
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

class MyDelete(MyMixin, View):
    template_name = "idk_delete.html" 
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/two/')
        return render(request, self.template_name, context)

class MyUpdate(MyMixin, View):
    template_name = "idk_update.html" # DetailView

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = MyModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = MyModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class MyCreate(View):
    template_name = "idk_create.html"
    def get(self, request, *args, **kwargs):
        form = MyModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = MyModelForm()
        context = {"form": form}
        return render(request, self.template_name, context)

class MyList(View):
    template_name = "idk_list.html"
    queryset = MyModel.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    
    def get(self, request, *args, **kwargs):
        context = { "object_list": self.get_queryset() }
        return render(request, self.template_name , context)


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







