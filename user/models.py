from django.db import models
from django.contrib.auth.models import User

class FriendshipManager(models.Manager):

    def add(self, a, b):
        if a.id > b.id:
            a, b = b, a
        return self.get_or_create(user1=a, user2=b)

    def all_friends(self, user):
        return User.objects.filter(
            models.Q(friendship_low__user2=user) |
            models.Q(friendship_high__user1=user)
        )


class Friends(models.Model):
        user1 = models.ForeignKey(User, on_delete=models.CASCADE,related_name="friendship_low")
        user2= models.ForeignKey(User,on_delete=models.CASCADE,related_name="friendship_high")
        timestamp = models.DateTimeField(auto_now_add=True)
        objects = FriendshipManager()

        class Meta:                                                                                             constraints = [                                           models.UniqueConstraint(fields=['user1','user2'],name="friendship_constrian"),                      models.CheckConstraint(condition=~models.Q(user1_id=models.F('user2')), name='prevent_self_friendship')]

        def __str__(self):
 
            return self.user1.username


