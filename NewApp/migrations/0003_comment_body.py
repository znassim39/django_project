# Generated by Django 3.0 on 2019-11-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default=''),
        ),
    ]