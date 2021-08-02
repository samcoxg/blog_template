from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    post = models.CharField(max_length=1000)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100)


