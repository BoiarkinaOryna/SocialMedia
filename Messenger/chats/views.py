from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Friends

# Create your views here.
class ChatsView(ListView):
    model = Friends
    template_name = 'chats/chat.html'