# Generated by Django 4.0.4 on 2022-05-08 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rma', '0006_productreturn_created_at_productreturn_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickupLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rma.address')),
            ],
        ),
    ]
