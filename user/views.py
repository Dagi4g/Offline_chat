from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from message.models import Friend

@login_required
def profile_view(request):
    username = User.objects.get(username=request.user)
    friends = Friend.objects.filter(user=username)
    friend_list = [f.friend for f in friends]
    return render(request, 'user/profile.html', {'user': request.user,"friends" : friend_list})

