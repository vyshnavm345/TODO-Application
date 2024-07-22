from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, related_name="user_tasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    