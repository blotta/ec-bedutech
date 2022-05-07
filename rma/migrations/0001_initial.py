# Generated by Django 4.0.4 on 2022-05-07 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=1024)),
                ('number', models.IntegerField()),
                ('cep', models.CharField(max_length=10)),
                ('neighborhood', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rma.address')),
            ],
        ),
    ]
