# Generated by Django 2.1.4 on 2018-12-25 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='devices', to='profiling.DeviceType'),
        ),
    ]
