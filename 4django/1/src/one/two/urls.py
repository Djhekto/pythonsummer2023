from django.contrib import admin
from django.urls import path

from .views import (
    MyView, home  
)

app_name = "two"

urlpatterns = [
    
    path('', MyView.as_view() , name="idk"), 
    path('idk/', MyView.as_view(template_name="articles/article_list.html") , name="idk"), 
            #doesnt access it actualy lol

]
