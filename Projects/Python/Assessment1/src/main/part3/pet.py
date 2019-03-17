import functools
from abc import ABC, abstractmethod


@functools.total_ordering
class Pet(ABC):
    def __init__(self, name: str = "", age: int = 0):
        self.name = name
        self.age = age
        self.owner = None

    def __lt__(self, other):
        return self.age < other.age

    @abstractmethod
    def speak(self) -> str:
        pass
