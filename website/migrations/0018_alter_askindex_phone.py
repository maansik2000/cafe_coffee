# Generated by Django 3.2 on 2021-05-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_alter_askindex_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askindex',
            name='phone',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
