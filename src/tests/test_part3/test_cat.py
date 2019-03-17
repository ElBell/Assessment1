from unittest import TestCase

from src.main.part3.cat import Cat
from src.main.part3.pet_owner import PetOwner


class TestCat(TestCase):

    def test_nullary_constructor(self):
        expected_owner: PetOwner = None
        expected_name: str = "Cat name"
        expected_age: int = 0
        cat: Cat = Cat()

        actual_name: str = cat.name
        actual_age: int = cat.age
        actual_owner: PetOwner = cat.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Cat"
        expected_age: int = 0
        cat: Cat = Cat(name=expected_name)

        actual_name: str = cat.name
        actual_age: int = cat.age
        actual_owner: PetOwner = cat.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age(self):
        expected_owner: PetOwner = None
        expected_name: str = "Cat name"
        expected_age: int = 3
        cat: Cat = Cat(age=expected_age)

        actual_name: str = cat.name
        actual_age: int = cat.age
        actual_owner: PetOwner = cat.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Cat"
        expected_age: int = 3
        cat: Cat = Cat(expected_name, expected_age)

        actual_name: str = cat.name
        actual_age: int = cat.age
        actual_owner: PetOwner = cat.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_speak(self):
        cat: Cat = Cat()
        expected: str = "Meow"
        actual: str = cat.speak()
        self.assertEqual(expected, actual)
