# Generated by Django 5.0 on 2024-03-18 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=300)),
                ('task_description', models.TextField()),
                ('task_due_date', models.DateField()),
                ('task_start_date', models.DateTimeField(auto_now_add=True)),
                ('attachments', models.FileField(upload_to='attachments')),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('High', 'High'), ('Low', 'Low'), ('Normal', 'Normal')], default='Urgent', max_length=300)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='Pending', max_length=300)),
                ('related_project_id', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('task_assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='project.project')),
            ],
        ),
    ]
