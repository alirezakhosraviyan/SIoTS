# Generated by Django 2.1.5 on 2019-01-20 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=1000)),
                ('model', models.CharField(max_length=1000)),
                ('lat', models.CharField(max_length=1000)),
                ('long', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('lat', models.CharField(max_length=1000)),
                ('long', models.CharField(max_length=1000)),
                ('radius', models.IntegerField(default=0)),
                ('devices', models.ManyToManyField(to='profiling.Device')),
            ],
        ),
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel_files')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha', models.FloatField(default=0)),
                ('beta', models.FloatField(default=0)),
                ('gama', models.FloatField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='services',
            field=models.ManyToManyField(to='profiling.Service'),
        ),
        migrations.AddField(
            model_name='device',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='devices', to='profiling.DeviceType'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to='profiling.User'),
        ),
    ]
