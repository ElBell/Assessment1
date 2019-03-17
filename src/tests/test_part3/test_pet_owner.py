from unittest import TestCase

from src.main.part3.cat import Cat
from src.main.part3.dog import Dog
from src.main.part3.pet_owner import PetOwner


class TestPetOwner(TestCase):

    def test_constructor(self):
        expected = "George"
        expected_pet = Dog()
        test_owner = PetOwner(expected, [expected_pet])
        actual_pet = test_owner.pets[0]
        self.assertEqual(expected, test_owner.name)
        self.assertEqual(expected_pet, actual_pet)

    def test_add_pet(self):
        expected = Dog()
        owner = PetOwner("")
        owner.add_pet(expected)
        actual = owner.pets[0]
        self.assertEqual(expected, actual)

    def test_add_pet2(self):
        expected = Dog()
        other = Cat()
        owner = PetOwner("")
        owner.add_pet(expected)
        owner.add_pet(other)
        self.assertEqual(expected, owner.pets[0])
        self.assertEqual(other, owner.pets[1])

    def test_owner_of(self):
        test_dog = Dog()
        owner = PetOwner("")
        owner.add_pet(test_dog)
        actual = owner.is_owner_of(test_dog)
        self.assertTrue(actual)

    def test_remove_pet(self):
        expected = Dog()
        other = Cat()
        owner = PetOwner("")
        owner.add_pet(other)
        owner.add_pet(expected)
        owner.remove_pet(other)
        self.assertEqual(expected, owner.pets[0])

    def test_youngest_age(self):
        expected = 1
        dog = Dog(age=expected)
        cat = Cat(age=3)
        owner = PetOwner("test", [dog, cat])
        actual = owner.youngest_age()
        self.assertEqual(expected, actual)

    def test_oldest_age(self):
        expected = 3
        dog = Dog(age=expected)
        cat = Cat(age=3)
        owner = PetOwner("test", [dog, cat])
        actual = owner.oldest_age()
        self.assertEqual(expected, actual)

    def test_average_age(self):
        expected = 2
        dog = Dog(age=1)
        cat = Cat(age=3)
        owner = PetOwner("test", [dog, cat])
        actual = owner.average_age()
        self.assertEqual(expected, actual)
