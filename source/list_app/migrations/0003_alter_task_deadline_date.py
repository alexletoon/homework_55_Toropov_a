# Generated by Django 4.1.1 on 2022-09-20 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0002_alter_task_deadline_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline_date',
            field=models.DateField(blank=True, null=True, verbose_name='Deadline'),
        ),
    ]
