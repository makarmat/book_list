# Generated by Django 3.1.2 on 2020-10-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20201019_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(default=None, max_length=3),
        ),
    ]
