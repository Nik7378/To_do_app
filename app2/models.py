from django.db import models

# Create your models here.

class task(models.Model):
    objects = models.Manager()

    task = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    duedate = models.DateField()
    note = models.TextField()
    progress = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
