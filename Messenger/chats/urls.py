from django.urls import path
from .views import ChatsView

urlpatterns = [
    path("<int:pk>", view = ChatsView.as_view(), name = "chats")
]