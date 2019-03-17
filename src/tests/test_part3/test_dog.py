from unittest import TestCase

from src.main.part3.dog import Dog
from src.main.part3.pet_owner import PetOwner


class TestDog(TestCase):

    def test_nullary_constructor(self):
        expected_owner: PetOwner = None
        expected_name: str = "Dog name"
        expected_age: int = 0
        dog: Dog = Dog()

        actual_name: str = dog.name
        actual_age: int = dog.age
        actual_owner: PetOwner = dog.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Dog"
        expected_age: int = 0
        dog: Dog = Dog(name=expected_name)

        actual_name: str = dog.name
        actual_age: int = dog.age
        actual_owner: PetOwner = dog.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age(self):
        expected_owner: PetOwner = None
        expected_name: str = "Dog name"
        expected_age: int = 3
        dog: Dog = Dog(age=expected_age)

        actual_name: str = dog.name
        actual_age: int = dog.age
        actual_owner: PetOwner = dog.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_constructor_with_age_name(self):
        expected_owner: PetOwner = None
        expected_name: str = "Name of Dog"
        expected_age: int = 3
        dog: Dog = Dog(expected_name, expected_age)

        actual_name: str = dog.name
        actual_age: int = dog.age
        actual_owner: PetOwner = dog.owner
        self.assertEqual(expected_owner, actual_owner)
        self.assertEqual(expected_age, actual_age)
        self.assertEqual(expected_name, actual_name)

    def test_speak(self):
        dog: Dog = Dog()
        expected: str = "Bark"
        actual: str = dog.speak()
        self.assertEqual(expected, actual)
