# Generated by Django 4.1.5 on 2023-02-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0016_rename_edited_on_task_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]