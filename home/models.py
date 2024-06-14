from django.db import models

class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle


    