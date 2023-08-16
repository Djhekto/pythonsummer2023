from typing import Any, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html" 
    form_class = ArticleModelForm
    queryset = Article.objects.all() #blog/Article_list.html
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    #def get_success_url(self):
    #    return "/"


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_update.html"
    form_class = ArticleModelForm
    queryset = Article.objects.all() #blog/Article_list.html
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)



class ArticleListView(ListView):
    template_name = "articles/article_list.html" 
    queryset = Article.objects.all() #blog/Article_list.html
    
class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html" 
    #queryset = Article.objects.all() 
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)
    




