from django.contrib import admin
from django.urls import path

from .views import ( ArticleListView, ArticleDetailView,
                    ArticleCreateView, ArticleUpdateView
)

app_name = "blog"

urlpatterns = [
    
    path('', ArticleListView.as_view(), name="article_list"), 
    path('<int:id>/', ArticleDetailView.as_view(), name="article_detail"), 
    path('create/', ArticleCreateView.as_view(), name="article_create"), 
    #path('<int:id>/update/', ArticleUpdateView.as_view(), name="article_update"), 
            #HTTP error 405   IDK WHY
    path('update/<int:id>/', ArticleUpdateView.as_view(), name="article_update"), 

]

 
