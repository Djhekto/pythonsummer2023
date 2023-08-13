from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
#from django.http import HttpResponse
from .models import Product
from .forms import ProductForm,RawProductForm

def product_create_view(request,*args, **kwargs):
    form1 = ProductForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        form1 = ProductForm()
    context = { "form": form1,} 
    return render(request,"products/product_create.html", context)

def product_update_view(request, upd_id, *args, **kwargs):
    object = get_object_or_404(Product,id = upd_id)
    form1 = ProductForm(request.POST or None, instance=object)
    if form1.is_valid():
        form1.save()
    context = {
        "object": object,
        "object_id": upd_id
    }
    return render(request, "products/product_create.html", context)  

def product_list_view(request):
    queryset = Product.objects.all()    
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)    

def product_detail_view(request,get_id, *args, **kwargs):
    object = get_object_or_404(Product,id = get_id)
    context = { "object": object,
                "object_id": get_id}

    return render(request,"products/product_detail.html", context)

def product_delete_view(request, del_id, *args, **kwargs):
    object = get_object_or_404(Product,id = del_id)

    if request.method == "POST":
        object.delete()
        return redirect("../../")
    context = {
        "object": object,
        "object_id": del_id
    }
    return render(request, "products/product_delete.html", context) 


















