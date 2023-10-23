from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

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

    def get_absolute_url(self):
        return reverse("kitchen:cook-detail", args=[str(self.id)])


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.ManyToManyField(
        to=Ingredient,
        related_name="dishes"
    )
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
        return (f"{self.name} (price: {self.price}, "
                f"dish type: {self.dish_type.name}")

    def get_cooks(self):
        return "; ".join([str(cook) for cook in self.cooks.all()])

    def get_ingredients(self):
        return "; ".join([str(ingredient) for ingredient in self.ingredients.all()])

    def get_absolute_url(self):
        return reverse("kitchen:dish-detail", args=[str(self.id)])
