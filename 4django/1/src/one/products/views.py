from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def product_detail_view(request,*args, **kwargs):
    obj1 = Product.objects.get(id=1)
    context = { "pr_obj": obj1}

    return render(request,"products/detail.html", context)
    return render(request,"detail.html", {})



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