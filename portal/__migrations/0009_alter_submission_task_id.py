# Generated by Django 2.2.4 on 2019-08-24 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_remove_task_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='task_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Task')
        ),
    ]