from django.shortcuts import render
from django.views.generic import ListView
from registration.models import Profile

# Create your views here.

class FriendsView(ListView):
    model = Profile
    template_name = "friends/friends.html"

class FriendPageView(ListView):
    model = Profile
    template_name = 'friends/friend_page.html'