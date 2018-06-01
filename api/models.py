from enum import Enum

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


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
    by_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                null=True)

    def __str__(self):
        return '{}@({}, {})'.format(
            self.get_pin_type_display(), self.latitude, self.longitude)


class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    text = models.TextField()
    by_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                null=True)
