# Generated by Django 4.1.7 on 2023-03-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='name',
            field=models.CharField(default=(), max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
