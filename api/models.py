from enum import Enum

from django.contrib.auth.models import Group, User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .middleware.current_user import get_current_user


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def add_to_default_group(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='default')
        instance.groups.add(group)


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
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                default=get_current_user)

    def __str__(self):
        return '{}@({}, {})'.format(
            self.get_pin_type_display(), self.latitude, self.longitude)


class Comment(models.Model):
    pin = models.ForeignKey(Pin, on_delete=models.CASCADE)
    text = models.TextField()
    by_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                default=get_current_user)
