from django.urls import path
from .views import PersonalInfoView, AlbumsView

urlpatterns = [
    path("<int:pk>", view = PersonalInfoView.as_view(), name = "info"),
    path("<int:pk>/albums", view = AlbumsView.as_view(), name = "albums")
]