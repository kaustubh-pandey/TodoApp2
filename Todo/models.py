from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=20)
    description = models.TextField()
    time =  models.DateTimeField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.task

