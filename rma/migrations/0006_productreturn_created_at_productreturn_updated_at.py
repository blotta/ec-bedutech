# Generated by Django 4.0.4 on 2022-05-07 23:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0005_alter_address_complement_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreturn',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='productreturn',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
