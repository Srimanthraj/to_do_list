from django.db import models

# Create your models here.


class Homework(models.Model):

    taskTitle2 = models.CharField(max_length=30)
    taskDesc2 = models.TextField()
    # time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle2
