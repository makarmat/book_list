# Generated by Django 3.1.2 on 2020-10-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20201020_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.IntegerField(verbose_name='Data publikacji'),
        ),
    ]
