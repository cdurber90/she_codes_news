# Generated by Django 4.2.2 on 2023-12-09 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_img',
            field=models.URLField(blank=True),
        ),
    ]
