from enum import Enum

from django.db import models


class Pin(models.Model):

    class Type(Enum):
        PICKPOCKET = "Pickpocket"
        DRUNK = "Drunk"
        ROBBERY = "Robbery"
        SCAM = "Scam"
        HARASSMENT = "Harassment"
        OTHERS = "Others"

        @classmethod
        def choices(cls):
            return [(t.name, t.value) for t in cls]

    pin_type = models.CharField(max_length=10, choices=Type.choices())
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    text = models.TextField()
