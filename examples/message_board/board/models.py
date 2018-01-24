from django.db import models
from django import forms
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=144)
    pub_date = models.DateTimeField('date published', default=datetime.now)
