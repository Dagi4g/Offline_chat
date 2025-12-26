from django.db import models
from django.contrib.auth.models import User

"""
class Friend(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friend_user")
    friend = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friend_friend")

    class Meta:

        constraints = [
                models.UniqueConstraint(fields=['user','friend'],name="friendship_constrian"),
                models.CheckConstraint(condition=~models.Q(user_id=models.F('friend')), name='prevent_self_friendship')
                ]
                """

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name="message_sender")
    recever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_reciver")
    content =  models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


    
