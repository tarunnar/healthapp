# Generated by Django 2.2.7 on 2020-09-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
