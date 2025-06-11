from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.forms import ImageField

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    image = models.ImageField(upload_to= "images/", blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.user.username} - {self.text[:10]}"




