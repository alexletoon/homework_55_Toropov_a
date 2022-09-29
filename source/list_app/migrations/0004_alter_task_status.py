# Generated by Django 4.1.1 on 2022-09-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0003_alter_task_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('NEW', 'Новая'), ('IN_PROGRESS', 'В процессе'), ('DONE', 'Выполнена')], max_length=12, verbose_name='Статус'),
        ),
    ]