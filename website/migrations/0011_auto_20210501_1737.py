# Generated by Django 3.2 on 2021-05-01 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_askindex_phone_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='askindex',
            name='phone_field',
        ),
        migrations.AddField(
            model_name='askindex',
            name='phone',
            field=models.CharField(max_length=122, null=True),
        ),
    ]