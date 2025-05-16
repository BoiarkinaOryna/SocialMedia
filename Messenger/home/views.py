from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from .forms import UserPostForm
from .models import User_Post
from registration.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

class HomePageView(FormMixin, ListView):
    # model = User_Post
    queryset = User_Post.objects.all()
    form_class = UserPostForm
    template_name = "home/home.html"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
        # post_id_delete = 
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        # else:
        #     return self.form_invalid(form)
    
    def form_valid(self, form):
        post = form.save(commit=False)
        print("user =", self.request.user)
        print("form =", form)
        # post.user = self.request.user
        post.author = Profile.objects.get(id=self.request.user.id)
        post.save()
        form.instance = post
        form.save_m2m()
        return redirect("/")

class MyPostsView(ListView):
    queryset = User_Post.objects.all()
    form_class = UserPostForm
    template_name = "my_posts/my_posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = 'change_post'
        return context