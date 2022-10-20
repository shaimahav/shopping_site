# Generated by Django 3.1.5 on 2022-02-28 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buyer', '0006_order_tb'),
        ('seller', '0004_product_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracking_tb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(default='Order being prepared', max_length=30)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('orderid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buyer.order_tb')),
            ],
        ),
    ]
