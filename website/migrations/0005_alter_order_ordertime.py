# Generated by Django 3.2 on 2021-05-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_order_ordertime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
