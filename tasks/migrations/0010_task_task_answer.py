# Generated by Django 5.0.3 on 2024-05-10 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_remove_typetask_type_group_remove_task_type_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_answer',
            field=models.CharField(default='0', max_length=255),
            preserve_default=False,
        ),
    ]
