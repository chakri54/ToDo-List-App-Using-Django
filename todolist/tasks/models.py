from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)  # Task title
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)  # Completion status

    def __str__(self):
        return self.title