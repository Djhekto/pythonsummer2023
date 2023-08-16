from django.contrib import admin
from django.urls import path

from .views import ( ArticleListView, ArticleDetailView,
                    ArticleCreateView,
)

app_name = "blog"

urlpatterns = [
    
    path('', ArticleListView.as_view(), name="article_list"), 
    path('<int:id>', ArticleDetailView.as_view(), name="article_detail"), 
    path('create/', ArticleCreateView.as_view(), name="article_create"), 
    
    #path('create/', product_create_view, name='product-list'),
    #path('<int:get_id>/', product_detail_view, name="product-detail"),
    #path('<int:upd_id>/update/', product_update_view, name="product-update"),
    #path('<int:del_id>/delete/', product_delete_view, name="product-delete"),
    # 
]

 
