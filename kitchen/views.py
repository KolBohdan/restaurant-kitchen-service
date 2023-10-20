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
    return render(request, "kitchen/index.html")
