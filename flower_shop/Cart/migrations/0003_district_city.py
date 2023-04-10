# Generated by Django 4.1.7 on 2023-04-08 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_cartitem_alter_cart_options_remove_cart_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.district')),
            ],
        ),
    ]
