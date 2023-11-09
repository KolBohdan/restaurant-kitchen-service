from django.test import TestCase

from kitchen.forms import (
    CookCreationForm,
    DishTypeNameSearchForm,
    DishNameSearchForm,
    IngredientNameSearchForm,
    CookUsernameSearchForm,
)


class FormsTests(TestCase):

    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "test_user",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "test_first_name",
            "last_name": "test_second_name",
            "years_of_experience": 5
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_ingredient_dish_and_dish_type_search_forms(self):
        form_data = {"name": "test"}
        dish_type_form = DishTypeNameSearchForm(data=form_data)
        dish_form = DishNameSearchForm(data=form_data)
        ingredient_form = IngredientNameSearchForm(data=form_data)
        self.assertTrue(dish_form.is_valid())
        self.assertTrue(dish_type_form.is_valid())
        self.assertTrue(ingredient_form.is_valid())

    def test_cook_search_form(self):
        form_data = {"username": "test"}
        form = CookUsernameSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
