from django.contrib import admin
from django.urls import path

from .views import (
    MyView, MyList, MyCreate,
    home  
)

app_name = "two"

urlpatterns = [
    
    path('', MyView.as_view() , name="idk"), 
    path('idk/', MyView.as_view(template_name="articles/article_list.html") , name="idk"), 
            #doesnt access it actualy lol
    path('<int:id>/', MyView.as_view() , name="idk_detail"), 
    path('list/', MyList.as_view() , name="idk_list"), 
    path('create/', MyCreate.as_view() , name="idk_create"), 


]
