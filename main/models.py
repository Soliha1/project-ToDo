from unittest.mock import DEFAULT

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    class Statuschoices(models.TextChoices):
        NOT_STARTED='yangi', 'yangi'
        IN_PROGRESS='jarayonda', 'jarayonda'
        COMPLETED='bajarildi', 'bajarildi'


    title=models.CharField()
    details=models.CharField(blank=True, null=True)
    deadline=models.DateField(blank=True, null=True)
    status=models.CharField( max_length=30, choices=Statuschoices.choices, default=Statuschoices.NOT_STARTED[0])
    created_at=models.DateTimeField(auto_now_add=True)

    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


