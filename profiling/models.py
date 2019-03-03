from django.db import models
import random

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
    weight = models.IntegerField(default=random.randint(1, 99))
    trust = models.IntegerField(default=random.randint(1, 99))
    security = models.IntegerField(default=random.randint(1, 99))
    accuracy = models.IntegerField(default=random.randint(1, 99))
    charge = models.IntegerField(default=random.randint(1, 99))

    def evaluator(self):
        return int((self.trust + self.security + self.accuracy + self.charge)/4)

    def __str__(self):
        return str(self.pk)


class Environment(models.Model):
    name = models.CharField(max_length=1000)
    lat = models.CharField(max_length=1000)
    long = models.CharField(max_length=1000)
    radius = models.IntegerField(default=0)
    devices = models.ManyToManyField(Device)

