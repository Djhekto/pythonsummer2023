from django.contrib import admin
from django.urls import path

from .views import ( ArticleListView,
)

app_name = "blog"

urlpatterns = [
    
    path('', ArticleListView.as_view(), name="article_list"), 
    #path('create/', product_create_view, name='product-list'),
    #path('<int:get_id>/', product_detail_view, name="product-detail"),
    #path('<int:upd_id>/update/', product_update_view, name="product-update"),
    #path('<int:del_id>/delete/', product_delete_view, name="product-delete"),
    # 
]

 
