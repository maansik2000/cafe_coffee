# Generated by Django 3.2 on 2021-05-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210528_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='orderTime',
        ),
        migrations.AddField(
            model_name='order',
            name='orderTiming',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
