from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic import DeleteView, UpdateView
from .forms import UserPostForm, ChangeUserPostForm, FirstEditInfoForm
from .models import User_Post, Image
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

class HomePageView(FormMixin, ListView):
    queryset = User_Post.objects.all()
    form_class = UserPostForm
    template_name = "home/home.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        # user = User_Post.objects.get(request.user)
        if not request.user.username:
            print("request.user.id =", request.user.id)
            return render(request, "home/home.html", {"edit_form": FirstEditInfoForm}, *args, **kwargs)
        return super().get(request, *args, **kwargs)

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
    queryset = User_Post.objects.all()
    form_class = ChangeUserPostForm
    template_name = "my_posts/my_posts.html"
    
    def get(self, request, *args, **kwargs):
        self.queryset = User_Post.objects.filter(author = self.request.user.id)
        return super().get(request, *args, **kwargs)

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