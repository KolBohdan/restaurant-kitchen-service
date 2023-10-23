from django.urls import path

from .views import (
    index,
    DishTypeListView,
    DishListView,
    DishDetailView,
    IngredientListView,
    CookListView,
    CookDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("ingredients/", IngredientListView.as_view(), name="ingredient-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
]

app_name = "kitchen"
