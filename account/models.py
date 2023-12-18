from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_datetime = models.DateTimeField(auto_now_add=True)
    deposit_count = models.IntegerField(default=0)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    probability_to_win = models.FloatField(default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

    LEVEL_CHOICES = [
        ('Standard', 'Standard'),
        ('Silver', 'Silver'),
        ('Gold', 'Gold'),
        ('Premium', 'Premium'),
    ]

    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Standard')

    def __str__(self):
        return self.user.username