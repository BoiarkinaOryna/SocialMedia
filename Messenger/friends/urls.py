from django.urls import path
from .views import FriendsView, FriendPageView

urlpatterns = [
    path("", view = FriendsView.as_view(), name = "friends"),
    path("friend/", view = FriendPageView.as_view(), name='friend_page')
]