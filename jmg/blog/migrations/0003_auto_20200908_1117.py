# Generated by Django 3.1.1 on 2020-09-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=300),
        ),
    ]