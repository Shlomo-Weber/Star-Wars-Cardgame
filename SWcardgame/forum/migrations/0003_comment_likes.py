# Generated by Django 3.0.3 on 2020-03-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200316_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]