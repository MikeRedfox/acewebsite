# Generated by Django 2.2.4 on 2019-08-12 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='submission_url',
            new_name='submission',
        ),
    ]