from enum import Enum

from django.db import models


class Pin(models.Model):
    PICKPOCKET = 1
    DRUNK = 2
    ROBBERY = 3
    SCAM = 4
    HARASSMENT = 5
    OTHERS = 6

    TYPE_CHOICES = (
        (PICKPOCKET, "Pickpocket"),
        (DRUNK, "Drunk"),
        (ROBBERY, "Robbery"),
        (SCAM, "Scam"),
        (HARASSMENT, "Harassment"),
        (OTHERS, "Others"),
    )

    pin_type = models.IntegerField(choices=TYPE_CHOICES)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return '{}@({}, {})'.format(
            self.get_pin_type_display(), self.latitude, self.longitude)


class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    text = models.TextField()
