import os

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic import DeleteView, UpdateView
from .forms import UserPostForm, ChangeUserPostForm, FirstEditInfoForm
from .models import User_Post, Image
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage

class HomePageView(FormMixin, ListView):
    model = User_Post
    form_class = UserPostForm
    template_name = "home/home.html"
    context_object_name = "posts" 
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.username:
            context["edit_form"] = FirstEditInfoForm()
        else:
            context["my_posts_length"] = User_Post.objects.filter(author=self.request.user).count()

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Profile.objects.get(id=self.request.user.id)

        post.save()
        form.save_m2m()
        return redirect("/")

class MyPostsView(FormMixin, ListView):
    queryset = User_Post
    form_class = ChangeUserPostForm
    template_name = "my_posts/my_posts.html"
    context_object_name = "posts" 
    success_url = "/"

    def get_queryset(self):
        return User_Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_posts_length"] = User_Post.objects.filter(author=self.request.user).count()

        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Profile.objects.get(id=self.request.user.id)

        post.save()
        form.save_m2m()
        return redirect("/my_posts")

class DeletePostView(DeleteView):
    model = User_Post
    success_url = reverse_lazy("my_posts")

class UpdatePostView(UpdateView):
    model = User_Post
    fields = ['title', 'theme', 'content', 'tags', 'link']
    success_url = reverse_lazy("my_posts")

class UpdatePrifileView(UpdateView):
    model = Profile
    fields = ["first_name", "last_name", "username"]
    success_url = reverse_lazy("home")

def render_load_image(request: HttpRequest):
    image = request.FILES.get("image")
    print("image =", image)
    # dir_path = os.path.abspath(os.path.join(__file__, "..", "..", "media", "temp_images"))
    # if not os.path.exists(dir_path):
    #     os.makedirs(dir_path)
    # file_path = os.path.abspath(os.path.join(dir_path, image.name))
    # with open(file_path, 'wb+') as destination:
    #     for chunk in image.chunks():
    #         destination.write(chunk)

    Image(image = image).save()
    
    return HttpResponse("Saved")