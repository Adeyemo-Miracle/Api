from django.db import models

# Create your models here.

class App(models.Model):
    title = models.CharField(max_length=255)
    body=models.TextField(max_length=255)
    completed = models.BooleanField(default=True)


    def __str__(self):
        return self.title
