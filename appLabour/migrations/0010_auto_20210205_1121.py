# Generated by Django 3.1.4 on 2021-02-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0009_sample_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='Photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
