from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DistanceToWork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    miles = models.IntegerField()


class DriveToWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    distance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} | {self.distance}"


class GasCardGiven(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_given = models.DateField(default=timezone.now)


def needs_a_gas_card(test_user):
    gas_card = 250
    days_driven = test_user.drivetowork_set.count()
    distance = test_user.distancetowork.miles
    compensated_miles = test_user.gascardgiven_set.count() * gas_card
    total_mileage = (days_driven * distance) - compensated_miles
    return total_mileage >= 250


def calculate_user_mileage_data(user):
    gas_card = 250
    days_driven = user.drivetowork_set.count()
    distance = user.distancetowork.miles
    gas_cards_given = user.gascardgiven_set.count()
    compensated_miles = gas_cards_given * gas_card
    uncompensated_miles = (days_driven * distance) - compensated_miles
    return {
        "days_driven": days_driven,
        "distance": distance,
        "compensated_miles": compensated_miles,
        "uncompensated_miles": uncompensated_miles,
        "gas_cards_given": gas_cards_given,
    }
