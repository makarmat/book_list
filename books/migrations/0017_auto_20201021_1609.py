# Generated by Django 3.1.2 on 2020-10-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20201020_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=128, verbose_name='Autor'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
