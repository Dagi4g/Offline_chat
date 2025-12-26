from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q


from .models import Message
from .forms import MessageForm

@login_required
def view_message(request,reciver_id):
    sender = User.objects.get(username=request.user)
    friend = User.objects.get(id=reciver_id)
    messages = Message.objects.filter(sender=sender,recever=friend).order_by("sent_at")
    context = {"messages":messages,"friend":friend,"sender":sender}
    return render(request,"message/show_message.html",context)



@login_required
def chat_view(request, friend_id):
    friend = get_object_or_404(User, id=friend_id)

    messages = Message.objects.filter(
        Q(sender=request.user, recever=friend) |
        Q(sender=friend, recever=request.user)
    ).order_by("sent_at")

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recever = friend
            message.save()
            return redirect("message:view_message", friend_id=friend.id)
    else:
        form = MessageForm()

    return render(request, "message/show_message.html", {
        "friend": friend,
        "messages": messages,
        "form": form
    })
