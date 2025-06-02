from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .forms import EditInfoForm
from home.models import Image

# Create your views here.

class PersonalInfoView(FormView):
    template_name = "info/info.html"
    form_class = EditInfoForm

class AlbumsView(ListView):
    template_name = "albums/albums.html"
    model = Image