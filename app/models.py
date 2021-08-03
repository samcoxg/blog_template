from django.db import models
from mdeditor.fields import MDTextField

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = MDTextField()
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.title
