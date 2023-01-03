from django.db import models


class Device(models.Model):
    """Sensor in system."""
    serial_number = models.CharField(primary_key=True,
                                     unique=True,
                                     max_length=14)

    def __str__(self):
        return self.serial_number


class SensorData(models.Model):
    v0 = models.PositiveIntegerField("sensor_id",
                                     primary_key=True,
                                     unique=True)
    v18 = models.FloatField("dwell_time")
    Time = models.DateTimeField()

    def __str__(self):
        return f'{self.v0}'
