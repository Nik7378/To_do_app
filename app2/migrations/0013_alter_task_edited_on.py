# Generated by Django 4.1.5 on 2023-02-14 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0012_alter_task_edited_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='edited_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 2, 14, 7, 20, 31, 89609, tzinfo=datetime.timezone.utc)),
        ),
    ]
