# Generated by Django 5.1.4 on 2024-12-07 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
