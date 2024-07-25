from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    text_task = models.TextField()
    task_answer = models.CharField(max_length=255)
    sort_index = models.IntegerField(default=0)

    class Meta:
        ordering = ['sort_index']
        verbose_name_plural = 'Задания'
        verbose_name = 'Задание'

    def __str__(self):
        return f'{self.name}'


class Variant(models.Model):
    tasks = models.ManyToManyField(Task, related_name='tasks')

    class Meta:
        verbose_name_plural = 'Варианты'
        verbose_name = 'Вариант'

    def __str__(self):
        return f'Вариант {self.id}'


class UserTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    timestamp = models.DateTimeField(auto_now_add=True)
    answer = models.CharField(max_length=255, default="", null=True, blank=True)
    price = models.IntegerField(default=0)
    pricer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher', default=None, null=True,
                               blank=True)
    # 0 - решил на проверку, 1 - проверено
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Решенные задания'
        verbose_name = 'Решенное задание'
