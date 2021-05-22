# Generated by Django 3.2 on 2021-05-15 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_alter_askindex_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('Description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]