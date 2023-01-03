from django.db import models


class Device(models.Model):
    """Sensor in system."""
    serial_number = models.CharField(primary_key=True,
                                     unique=True,
                                     max_length=14)

    def __str__(self):
        return self.serial_number
