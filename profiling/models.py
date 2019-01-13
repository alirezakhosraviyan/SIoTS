from django.db import models


class ExcelFile(models.Model):
    file = models.FileField(upload_to='excel_files')


class Service(models.Model):
    name = models.CharField(max_length=1000, blank=False)


class DeviceType(models.Model):
    type_name = models.CharField(max_length=1000)


class User(models.Model):
    alpha = models.FloatField(default=0)
    beta = models.FloatField(default=0)
    gama = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    type = models.ForeignKey(DeviceType, on_delete=models.DO_NOTHING, related_name='devices')
    brand = models.CharField(max_length=1000)
    model = models.CharField(max_length=1000)
    services = models.ManyToManyField(Service)
    lat = models.CharField(max_length=1000)
    long = models.CharField(max_length=1000)


class Environment(models.Model):
    name = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    long = models.CharField(max_length=1000)
    radius = models.IntegerField(default=0)
    devices = models.ManyToManyField(Device)

