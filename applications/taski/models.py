from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=250,
    )
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    datecompleted = models.DateTimeField(
        null=True, 
        blank=True
    )
    important = models.BooleanField(
        default=False
    )


    def __str__(self) -> str:
        return f'{self.name } by {self.owner.username}'