from django.db import models

# Create your models here.

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
