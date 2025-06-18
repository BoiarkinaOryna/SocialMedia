from django.shortcuts import render
from django.views.generic.list import ListView
from friends.models import Friendship

# Create your views here.
class ChatsView(ListView):
    model = Friendship
    template_name = 'chats/chat.html'