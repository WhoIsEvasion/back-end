from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    name = models>charField(max_length=255)

    def __str__(self):
        return self.
        
class Post(models.Model):
    title = models.CharField(max_length=255)    
    picture = models.FileField(upload_to='media/')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.
   