# Generated by Django 4.0.4 on 2022-05-08 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0007_pickuplocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreturn',
            name='address',
        ),
        migrations.AddField(
            model_name='productreturn',
            name='pickup_location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rma.pickuplocation'),
            preserve_default=False,
        ),
    ]
