# Generated by Django 5.0.8 on 2024-08-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudAPP', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
    ]
