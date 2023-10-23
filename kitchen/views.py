from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient
)


def index(request: HttpRequest) -> HttpResponse:
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": Cook.objects.count(),
        "num_dishes": Dish.objects.count(),
        "num_dish_types": DishType.objects.count(),
        "num_ingredients": Ingredient.objects.count(),
        "num_visits": num_visits,
    }
    return render(request, "kitchen/index.html", context=context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
    paginate_by = 5


class DishListView(generic.ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 5


class DishDetailView(generic.DetailView):
    model = Dish


class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 5


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(generic.DetailView):
    model = Cook
