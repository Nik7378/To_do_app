# Generated by Django 4.1.5 on 2023-02-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0006_alter_task_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='note',
            field=models.TextField(max_length=200),
        ),
    ]
