# Generated by Django 3.2 on 2021-05-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210528_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTime',
            field=models.TimeField(null=True),
        ),
    ]
