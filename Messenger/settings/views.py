from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from .forms import EditInfoForm
from home.models import Image
from registration.models import Profile
from .forms import AlbumForm

# Create your views here.

class PersonalInfoView(UpdateView):
    template_name = "info/info.html"
    form_class = EditInfoForm
    model = Profile
    # fields = ['first_name', 'last_name', 'birthday', 'email', 'password']
    def get_success_url(self):
        return reverse('info', kwargs={'pk': self.object.pk})

class AlbumsView(FormMixin, ListView):
    template_name = "albums/albums.html"
    model = Image
    form_class = AlbumForm
    
    def get_success_url(self):
        return reverse('albums', kwargs={'pk': self.object.pk})