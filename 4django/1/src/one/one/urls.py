"""
URL configuration for one project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from two.views import home,aboutsmt
from products.views import product_detail_view, product_create_view, product_c_view,product_cc_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('smt/', home, name='home'),
    path('about/', aboutsmt, name='about'),
    path('product/', product_detail_view, name='product'),
    path('create_product/', product_create_view, name='nproduct'),
    path('c_product/', product_c_view, name='ncproduct'),
    path('cc_product/', product_cc_view, name='nccproduct'),

]
