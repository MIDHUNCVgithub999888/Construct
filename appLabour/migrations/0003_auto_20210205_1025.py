# Generated by Django 3.1.4 on 2021-02-05 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appLabour', '0002_remove_sample_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='EmailAddress',
            new_name='Email',
        ),
    ]
