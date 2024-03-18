from django.db import models
from project.models import Project
from django.contrib.auth.models import User

from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = {
        'Urgent': 'Urgent',
        'High': 'High',
        'Low': 'Low',
        'Normal': 'Normal',
    }
    STATUS_CHOICES = {
        'Pending': 'Pending',
        'In Progress': 'In Progress',
        'Complete': 'Complete',
    }
    task_name = models.CharField(max_length=300)
    task_description = models.TextField()
    task_due_date = models.DateField()
    task_start_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='tasks',on_delete=models.CASCADE)
    attachments = models.FileField(upload_to='attachments')
    priority = models.CharField(default='Urgent', max_length=300, choices=PRIORITY_CHOICES)
    status = models.CharField(default='Pending', max_length=300, choices=STATUS_CHOICES)
    task_assignee = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    related_project_id = models.IntegerField()
    # customize = models.CustomField()
    
    def __str__(self) -> str:
        return self.task_name




