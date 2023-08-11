from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label="Title idk",
        widget=forms.TextInput(attrs={"smthhere":"Title"})
        )
    description = forms.CharField(required=False, 
        widget=forms.Textarea( attrs={"class": "new_class_name" } )
                                )
    price = forms.DecimalField(initial=-1)
    
    class Meta:
        model = Product
        fields = [
            "title" ,#gets overwriten by title above
            "description"  ,
            "price" ,  
        ]
        
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
#        if "AAA" not in title:
#            return title
#        else:
#            raise forms.ValidationError("Non-valid title")
        if "AAA" in title:
            raise forms.ValidationError("Non-valid title") 
        return title

class RawProductForm(forms.Form):
    title = forms.CharField(required=True,label="New Title",
                            widget = forms.TextInput(
                                attrs={"smthhere": "Title"}
                                )
                            )
    description = forms.CharField(required=False, 
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "new_class_name"
                                          
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=-1
                               )
    
    
    









