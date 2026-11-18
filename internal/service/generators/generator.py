from abc import ABC, abstractmethod
from internal.domain.model.value_object import Difficulty

class Generator(ABC):
    def __init__(self, start_range: int, end_range: int):
        pass

    def set_operations(self, difficulty: Difficulty, operators: list[str]):
        pass

    @abstractmethod
    def generate(self, difficulty: Difficulty) -> str:
        pass

