from src.main.part3.pet import Pet


class Dog(Pet):

    def __init__(self, name: str = "Dog name", age: int = 0):
        super(Dog, self).__init__(name, age)

    def speak(self) -> str:
        return "Bark"
