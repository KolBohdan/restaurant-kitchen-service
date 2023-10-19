from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant_kitchen_service.settings import AUTH_USER_MODEL


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        to=DishType,
        on_delete=models.CASCADE,
        related_name="dishes"
    )
    cooks = models.ManyToManyField(
        to=AUTH_USER_MODEL,
        related_name="dishes"
    )

    class Meta:
        ordering = ("dish_type", )

    def __str__(self):
        return f"{self.name} (price: {self.price}, dish type: {self.dish_type.name}"
