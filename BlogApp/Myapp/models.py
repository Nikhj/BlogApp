from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=60,null=False,blank=False)
    content = models.CharField(max_length=600,null=False,blank=False)
    published_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=200,null=False,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)