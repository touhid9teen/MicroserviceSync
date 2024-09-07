from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    todo_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()