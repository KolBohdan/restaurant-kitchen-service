from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient
)


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""

    context = {
        "num_cooks": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_ingredients": Ingredient.objects.count(),
    }
    return render(request, "kitchen/index.html", context=context)
