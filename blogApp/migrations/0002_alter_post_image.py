# Generated by Django 4.1.4 on 2023-02-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='BlogPictures'),
        ),
    ]
