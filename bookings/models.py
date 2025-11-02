from django.db import models

class Bus(models.Model):
    BUS_TYPE_CHOICES = [
        ('AC', 'Air Conditioned'),
        ('NON_AC', 'Non-AC'),
        ('SLEEPER', 'Sleeper'),
        ('SEATER', 'Seater'),
    ]
    name=models.CharField(max_length=50)
    bus_number=models.CharField(max_length=100)
    seats=models.IntegerField()
    bus_type = models.CharField(max_length=10, choices=BUS_TYPE_CHOICES)
    price=models.DecimalField(max_digits=10,decimal_places=2)


