# Generated by Django 3.2.4 on 2021-06-11 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
