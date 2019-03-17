from unittest import TestCase

from src.main.part3.cat import Cat
from src.main.part3.pet import Pet
from src.main.part3.pet_owner import PetOwner


class TestCat(TestCase):

    def test_nullary_constructor(self):
        expected_owner: PetOwner = None
        expected_name: str = "Cat name"
        expected_age: int = 0
        pet: Pet = Cat()

        actual_name: str = pet.name
        actual_age: int = pet.age
        actual_owner: PetOwner = pet.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Pet"
        expected_age: int = 0
        pet: Pet = Cat(name=expected_name)

        actual_name: str = pet.name
        actual_age: int = pet.age
        actual_owner: PetOwner = pet.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age(self):
        expected_owner: PetOwner = None
        expected_name: str = "Cat name"
        expected_age: int = 3
        pet: Pet = Cat(age=expected_age)

        actual_name: str = pet.name
        actual_age: int = pet.age
        actual_owner: PetOwner = pet.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Pet"
        expected_age: int = 3
        pet: Pet = Cat(expected_name, expected_age)

        actual_name: str = pet.name
        actual_age: int = pet.age
        actual_owner: PetOwner = pet.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_set_and_get_owner(self):
        pet: Pet = Cat()
        expected: PetOwner = PetOwner("")
        pet.owner = expected
        self.assertEqual(expected, pet.owner)
