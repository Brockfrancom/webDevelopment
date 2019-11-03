from django.db import models

class Blog(models.Model):
    posted_date = models.DateTimeField('date posted')
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    title = models.CharField(max_length=100)

class Comment(models.Model):
    posted_date = models.DateTimeField('date posted')
    author_nickname = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    email = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

