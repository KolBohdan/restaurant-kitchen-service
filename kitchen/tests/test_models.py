from django.test import TestCase

from kitchen.models import (
    Cook,
    Dish,
    DishType,
    Ingredient,
)


class CookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Cook.objects.create_user(
            username="testcook",
            first_name="test_first",
            last_name="test_last",
            password="test123",
            years_of_experience=5,
        )

    def test_cook_str(self):
        cook = Cook.objects.get(id=1)
        expected_object_name = (
            f"{cook.username} ({cook.first_name} "
            f"{cook.last_name})"
        )
        self.assertEqual(str(cook), expected_object_name)

    def test_get_absolute_url(self):
        cook = Cook.objects.get(id=1)
        self.assertEqual(cook.get_absolute_url(), "/cooks/1/")

    def test_cook_with_years_of_experience(self):
        cook = Cook.objects.get(id=1)
        self.assertEqual(cook.username, "testcook")
        self.assertEqual(cook.years_of_experience, 5)
        self.assertTrue(cook.check_password("test123"))


class DishTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        DishType.objects.create(
            name="testtype",
        )

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(id=1)
        self.assertEqual(str(dish_type), dish_type.name)


class IngredientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        Ingredient.objects.create(
            name="testingredient",
        )

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.get(id=1)
        self.assertEqual(str(ingredient), ingredient.name)


class DishModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        dish_type = DishType.objects.create(
            name="test_name",
        )
        Dish.objects.create(
            name="test_dish",
            price=17,
            dish_type=dish_type,
        )

    def test_dish_str(self):
        dish = Dish.objects.first()
        expected_object_name = (
            f"{dish.name} (price: {dish.price}, "
            f"dish type: {dish.dish_type.name})"
        )
        self.assertEqual(str(dish), expected_object_name)
