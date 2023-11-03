from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient,
)

DISH_URL = reverse("kitchen:dish-list")
DISH_TYPE_URL = reverse("kitchen:dish-type-list")
INGREDIENT_URL = reverse("kitchen:ingredient-list")
COOK_URL = reverse("kitchen:cook-list")
HOME_URL = reverse("kitchen:index")


class PublicAccessTest(TestCase):
    def test_dish_login_required(self):
        res = self.client.get(DISH_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_dish_type_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_ingredient_login_required(self):
        res = self.client.get(INGREDIENT_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_cook_login_required(self):
        res = self.client.get(COOK_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_home_page_login_required(self):
        res = self.client.get(HOME_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateAccessTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

        first_dish_type = DishType.objects.create(
            name="test_dish_type_1",
        )

        second_dish_type = DishType.objects.create(
            name="test_dish_type_2",
        )

        Dish.objects.create(
            name="test_dish_1",
            price=15,
            dish_type=first_dish_type,
        )

        Dish.objects.create(
            name="test_dish_2",
            price=20,
            dish_type=second_dish_type,
        )

    def test_retrive_dish_types(self):
        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_retrive_ingredients(self):
        response = self.client.get(INGREDIENT_URL)
        self.assertEqual(response.status_code, 200)
        ingredients = Ingredient.objects.all()
        self.assertEqual(
            list(response.context["ingredient_list"]),
            list(ingredients)
        )
        self.assertTemplateUsed(response, "kitchen/ingredient_list.html")

    def test_retrive_dishes(self):
        response = self.client.get(DISH_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.all()
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes)
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_retrive_cooks(self):
        response = self.client.get(COOK_URL)
        self.assertEqual(response.status_code, 200)
        cooks = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks)
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "test_user",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "test_first_name",
            "last_name": "test_second_name",
            "years_of_experience": 5
        }

        self.client.post(
            reverse("kitchen:cook-create"), data=form_data
        )
        new_user = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(
            new_user.first_name, form_data["first_name"]
        )
        self.assertEqual(
            new_user.last_name, form_data["last_name"]
        )
        self.assertEqual(
            new_user.years_of_experience, form_data["years_of_experience"]
        )
