from django.db import models

# Create your models here.

"""
     post = Post.objects.all() == SELECT * FROM posts
"""

class Post(models.Model):
     title = models.CharField(max_length=56)
     description = models.CharField(max_length=256)
     rate= models.IntegerField(null=True, blank=True)
     created_at = models.DateTimeField(auto_now_add=True, null=True)
     updated_at = models.DateTimeField(auto_now=True, null=True)

     def __str__(self):
          return f"{self.title}: {self.description}"