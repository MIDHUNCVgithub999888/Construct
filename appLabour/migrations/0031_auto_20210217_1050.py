# Generated by Django 3.1.6 on 2021-02-17 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0030_auto_20210217_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='Image1',
            new_name='Image',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Image2',
        ),
        migrations.RemoveField(
            model_name='images',
            name='Image3',
        ),
        migrations.AddField(
            model_name='images',
            name='Model',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='images',
            name='Price',
            field=models.IntegerField(default=0),
        ),
    ]
