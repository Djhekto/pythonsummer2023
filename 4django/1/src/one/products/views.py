from django.shortcuts import render
#from django.http import HttpResponse
from .models import Product
from .forms import ProductForm,RawProductForm

def dynamic_smth(request, d_id, *args, **kwargs):
    object = Product.objects.get(id = d_id)
    context = {
        "object": object,
        "object_id": d_id
    }
    return render(request, "products/dynamic.html", context)
    

def render_initial_data(request,*args, **kwargs): #outside form init ->differnt views
    init_data = {
        "title" : "ma new title"
        }
    obj1 = Product.objects.get(id=25)#25 lol
    form = ProductForm(request.POST or None, initial=init_data, instance=obj1)
#    form = RawProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form" : form
    }
    return render(request, "products/create_product_init.html", context)
    

#nonraw
def product_create_view(request,*args, **kwargs):
    form1 = ProductForm(request.POST or None)#GET|NON-POST -> EAT AND IGNORE
    if form1.is_valid():#dj builtin seq
        form1.save()
        form1 = ProductForm()#kostili so ** lol
            
    context = { "form": form1,} 
    return render(request,"products/create_product.html", context)
#raw OLD
"""
def product_create_view(request,*args, **kwargs):
    form1 = RawProductForm()#GET|NON-POST -> EAT AND IGNORE

    if request.method == "POST":
        form1 = RawProductForm(request.POST)
        if form1.is_valid():#dj builtin seq
            print(form1.cleaned_data)
            Product.objects.create(**form1.cleaned_data)#kostili so ** lol
        else:
            print("err in one/views",form1.errors)
            
    context = { "form": form1,} 
    return render(request,"products/create_product.html", context)
"""

def product_c_view(request,*args, **kwargs):
    context = { }
    return render(request,"products/c_product.html", context)

def product_cc_view(request,*args, **kwargs):
    if request.method == "POST":
        print(request.POST)
        new_title_cc = request.POST.get("q")
        #Product.objects.create(title=new_title_cc) #<-- create model from POST
    context = { }
    return render(request,"products/cc_product.html", context)

def product_detail_view(request,*args, **kwargs):
    obj1 = Product.objects.get(id=1)
    context = { "pr_obj": obj1}

    return render(request,"products/detail.html", context)
    #return render(request,"detail.html", {})


"""

def product_create_view(request,*args, **kwargs):
    form1 = ProductForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = ProductForm() #rerender to clear fields in views
    
    context = { "pr_form": form1}

    return render(request,"products/create_product.html", context)
"""









"""
class Product(models.Model):
    title       = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=10)
    extra       = models.TextField(default="spam")
    smthnew     = models.BooleanField()
    ahah        = models.TextField(blank=True, null=False)
"""
"""
    context = {
        "pr_title": obj1.title,
        "pr_descr": obj1.description,
        "pr_price": obj1.price,
        "pr_extra": obj1.extra,
        "pr_smthn": obj1.smthnew,
        "pr_ahah": obj1.ahah,
        
    }
"""