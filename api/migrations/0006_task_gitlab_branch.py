# Generated by Django 4.1.1 on 2022-11-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_task_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="gitlab_branch",
            field=models.CharField(default="main", max_length=256),
        ),
    ]
