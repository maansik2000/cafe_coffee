# Generated by Django 3.2 on 2021-05-01 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_rename_firstname_askindex_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askindex',
            name='email',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
