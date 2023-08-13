from django.db import models
from django.urls import reverse

class Product(models.Model):
    title       = models.CharField(max_length=30)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=10)
    extra       = models.TextField(default="spam")
    smthnew     = models.BooleanField(default=True)
    ahah        = models.TextField(blank=True, null=False)
    
    def get_absolute_url(self):
        #return f"/products/{self.id}"
        return reverse("products:product-detail", kwargs={"get_id": self.id})
    











