# Generated by Django 2.2.7 on 2020-03-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]