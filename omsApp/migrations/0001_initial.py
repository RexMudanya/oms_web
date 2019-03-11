# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^(?:254|\\+254|0)?(7(?:(?:[129][0-9])|(?:0[0-8])|(4[0-1]))[0-9]{6})$', message=b'Phone number accept number starting with 254/07/+254')])),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['firstname'],
            },
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('longtitude', models.DecimalField(max_digits=22, decimal_places=16, blank=True)),
                ('latitude', models.DecimalField(max_digits=22, decimal_places=16, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100, blank=True)),
                ('price', models.FloatField()),
            ],
            options={
                'ordering': ['productId'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeOfPick', models.TimeField()),
                ('deliverytype', models.ForeignKey(to='omsApp.DeliveryType', on_delete=django.db.models.deletion.PROTECT)),
                ('locationId', models.ForeignKey(to='omsApp.Location', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['timeOfPick'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50, choices=[(b'Be', b'Beverages'), (b'De', b'Desserts')])),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateOfTransaction', models.DateTimeField()),
                ('customerId', models.ForeignKey(to='omsApp.Customer')),
                ('productId', models.ForeignKey(to='omsApp.Product', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'ordering': ['-dateOfTransaction'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.ForeignKey(to='omsApp.ProductType', on_delete=django.db.models.deletion.PROTECT),
        ),
        migrations.AddField(
            model_name='order',
            name='transactionId',
            field=models.ForeignKey(to='omsApp.Transaction'),
        ),
        migrations.AddField(
            model_name='offer',
            name='productId',
            field=models.ForeignKey(to='omsApp.Product', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
