from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


# Create your views here.

# class HomePageView(ListView):
#     def get_queryset(self):

#         return queryset

class HomePageView(TemplateView):
    template_name = "home/home.html"