from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Friends

@login_required
def profile_view(request):
    username = User.objects.get(username=request.user)
    friends = Friends.objects.all_friends(username)
    return render(request, 'user/profile.html', {'user': request.user,"friends":friends})

