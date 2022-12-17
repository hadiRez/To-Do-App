from django.db import models

# Create your models here.


class Todo(models.Model):
    STATUS_CHOICES = (
        ('nost', 'NotStarted'),
        ('ongo', 'OnGoing'),
        ('comp', 'Completed')
    )

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    # status: NotStarted, OnGoing, Completed
    status = models.CharField(choices=STATUS_CHOICES, max_length=4)