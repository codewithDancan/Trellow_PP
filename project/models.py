from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    project_name = models.CharField(max_length=300)
    project_description = models.TextField(max_length=255)
    project_start_date = models.DateTimeField(auto_now_add=True)
    project_due_date = models.DateField(default=timezone.now)
    attachments = models.FileField(upload_to='attachments', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    project_user_id = models.IntegerField(default=1)
    project_asignee = models .ForeignKey(User, related_name='client', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.project_name