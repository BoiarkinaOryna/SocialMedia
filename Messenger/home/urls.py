from django.urls import path
from .views import HomePageView, MyPostsView, DeletePostView, UpdatePostView

urlpatterns = [
    path('', view = HomePageView.as_view(), name = 'home'),
    path("my_posts/", view = MyPostsView.as_view(), name = 'my_posts'),
    path("my_posts/<pk>/delete/", view = DeletePostView.as_view(), name = 'delete_post'),
    path("my_posts/<pk>/change/", view = UpdatePostView.as_view(), name = 'change_post'),
]