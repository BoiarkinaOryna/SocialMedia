from django.shortcuts import render
from django.views.generic import ListView
from registration.models import Profile, User
from .models import Friendship
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

class FriendsView(ListView):
    model = Friendship
    template_name = "friends/friends.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'main'

        user = Profile.objects.get(user_id = self.request.user)
        print("user =", user)
        friendships = Friendship.objects.filter(Q(profile1=user) | Q(profile2=user), accepted=False)
        print("friendships =", friendships)

        users = []
        for friendship in friendships:
            if friendship.profile1 == user:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile2_id).user_id))
            else:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile1_id).user_id))
            print("users =", users)
        context["requests"] = users

        context["recommendations"] = User.objects.exclude(id = self.request.user.id)

        user = Profile.objects.get(user_id = self.request.user)
        print("user =", user)
        friendships = Friendship.objects.filter(Q(profile1=user) | Q(profile2=user), accepted=True)
        print("friendships =", friendships)

        users = []
        for friendship in friendships:
            if friendship.profile1 == user:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile2_id).user_id))
            else:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile1_id).user_id))
            print("users =", users)
        context["all_friends"] = users

        return context

class FriendPageView(ListView):
    model = Friendship
    template_name = 'friends/user_prof.html'


class RequestsView(ListView):
    template_name = "friends/friends.html"
    context_object_name = "all_users"

    def get_queryset(self):
        user = Profile.objects.get(user_id = self.request.user)
        print("user =", user)
        friendships = Friendship.objects.filter(Q(profile1=user) | Q(profile2=user), accepted=False)
        print("friendships =", friendships)

        users = []
        for friendship in friendships:
            if friendship.profile1 == user:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile2_id).user_id))
            else:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile1_id).user_id))
            print("users =", users)
        return users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'requests'
        return context
    
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")
        friend_request = Friendship.objects.filter(profile1_id = user_id, profile2_id = request.user.id).first()
        friend_request.accepted = 1
        friend_request.save()

        return self.get_queryset()
    
class RecommendationsView(ListView):
    template_name = "friends/friends.html"
    context_object_name = "all_users"

    def get_queryset(self):
        return User.objects.exclude(id = self.request.user.id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'recommendations'
        return context
    
    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")
        friend_request = Friendship.objects.create(
            profile1_id = request.user.id,
            profile2_id = user_id
        )
        friend_request.save()

        return JsonResponse({"status": "ok"})

class AllFriendsView(ListView):
    template_name = "friends/friends.html"
    context_object_name = "all_users"

    def get_queryset(self):
        user = Profile.objects.get(user_id = self.request.user)
        print("user =", user)
        friendships = Friendship.objects.filter(Q(profile1=user) | Q(profile2=user), accepted=True)
        print("friendships =", friendships)

        users = []
        for friendship in friendships:
            if friendship.profile1 == user:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile2_id).user_id))
            else:
                users.append(User.objects.get(id = Profile.objects.get(id = friendship.profile1_id).user_id))
            print("users =", users)
        return users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'all_friends'
        return context