# Generated by Django 5.0.7 on 2024-08-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.SmallIntegerField(default=0),
        ),
    ]
