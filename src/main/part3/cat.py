from src.main.part3.pet import Pet


class Cat(Pet):

    def __init__(self, name: str = "Cat name", age: int = 0):
        super(Cat, self).__init__(name, age)

    def speak(self) -> str:
        return "Meow"
