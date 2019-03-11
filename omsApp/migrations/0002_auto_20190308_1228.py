# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['nameOfLocation']},
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='nameOfLocation',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='description',
            new_name='offerDescription',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='price',
            new_name='priceOffer',
        ),
        migrations.RenameField(
            model_name='offer',
            old_name='type',
            new_name='typeOfOffer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='locationId',
            new_name='placeOfDelivery',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', blank=True),
        ),
        migrations.AlterField(
            model_name='producttype',
            name='type',
            field=models.CharField(max_length=50, choices=[('Be', 'Beverages'), ('De', 'Desserts'), ('Dr', 'Drinks')]),
        ),
    ]
