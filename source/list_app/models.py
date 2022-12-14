from datetime import datetime
from email.policy import default
from time import timezone
from django.db import models
from django.db.models import TextChoices

class Choices(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROPGRESS = 'IN_PROGRESS', 'В процессе'
    DONE = 'DONE', 'Выполнена'



class Task(models.Model):
    task = models.CharField(verbose_name='Задача', max_length=300, null=False, blank=False, default='Новая задача')
    description = models.TextField(verbose_name='Описание', max_length=3000, null = False, blank=False)
    status = models.CharField(verbose_name='Статус', max_length=12, choices = Choices.choices)
    deadline_date = models.DateField(verbose_name='Deadline', auto_now_add=False, auto_now=False, blank = True, null = True)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_deleted = models.BooleanField(verbose_name="Удалено", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    def __str__(self) -> str:
        return f'Task: {self.task} Description: {self.description}, Status: {self.status}, deadline: {self.deadline_date}'
    

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = datetime.now()
        self.is_deleted = True
        self.save()
