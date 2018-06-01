from django.test import TestCase

from .models import Pin


class PinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pin.objects.create(
            pin_type=Pin.SCAM,
            latitude=51.508531285930100,
            longitude=-0.076132304958301
        )

    def test_pin_str_representation(self):
        pin = Pin.objects.get(id=1)
        self.assertTrue(isinstance(pin, Pin))
        self.assertEqual(str(pin),
                         'Scam@(51.508531285930100, -0.076132304958301)')
