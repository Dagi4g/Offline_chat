from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friend_user")
    friend = models.ForeignKey(User,on_delete=models.CASCADE,related_name="friend_friend")

    class Meta:

        constraints = [
                models.UniqueConstraint(fields=['user','friend'],name="friendship_constrian"),
                models.CheckConstraint(condition=models.Q(user=models.F('friend')), name='prevent_self_friendship')
                ]

    
