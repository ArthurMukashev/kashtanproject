# Generated by Django 5.0.3 on 2024-04-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_task_sort_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='answer',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
