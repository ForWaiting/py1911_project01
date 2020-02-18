from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    自定义用户类继承django自带用户系统
    """
    telephone = models.CharField(max_length=20,verbose_name='手机号')
    voteinfo = models.ManyToManyField('VoteInfo')


class VoteInfo(models.Model):

    vote_title = models.CharField(max_length=30)

    def __str__(self):
        return self.vote_title
class VoteOption(models.Model):
    content = models.CharField(max_length=50)
    vote_num = models.IntegerField(default=0)
    vote = models.ForeignKey(VoteInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.content
