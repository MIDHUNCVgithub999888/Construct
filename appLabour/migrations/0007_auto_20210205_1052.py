# Generated by Django 3.1.4 on 2021-02-05 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0006_auto_20210205_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='Photo',
            field=models.ImageField(default=0, upload_to='media/'),
        ),
    ]
