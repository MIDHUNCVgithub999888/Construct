# Generated by Django 3.1.6 on 2021-02-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0017_auto_20210205_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='EducationalQalifications',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='sample',
            name='LanguageKnown',
            field=models.CharField(default='', max_length=100),
        ),
    ]
