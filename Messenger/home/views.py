from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic import DeleteView
from .forms import UserPostForm, ChangeUserPostForm
from .models import User_Post, Tag
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

class HomePageView(FormMixin, ListView):
    queryset = User_Post.objects.all()
    form_class = UserPostForm
    template_name = "home/home.html"
    success_url = "/"

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
        return redirect("/")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = 'create_post'
        return context

class MyPostsView(FormMixin, ListView):
    queryset = User_Post.objects.all()
    form_class = ChangeUserPostForm
    template_name = "my_posts/my_posts.html"
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        
    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Profile.objects.get(id=self.request.user.id).update()
        
        post.save()
        # tags = Tag.objects.all()
        # for tag in tags:
        #     print('tag.id =', int(tag.id))
        #     post.tags.add(int(tag.id))
        # post.save()
        # form.save_m2m()
        return redirect("/my_posts")
    
class DeletePostView(DeleteView):
    model = User_Post
    success_url = reverse_lazy("my_posts")