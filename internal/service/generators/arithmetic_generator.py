from random import randint, choice

from internal.service.generators.generator import Generator
from internal.domain.model.value_object import Difficulty
from internal.domain.model.errors import DifficultAlreadySetError, DifficultNotSetError


class ArithmeticGenerator(Generator):
    def __init__(self, start_range: int, end_range: int):
        super().__init__(start_range, end_range)

        self.start_range = start_range
        self.end_range = end_range
        self.operations: dict[Difficulty, list[str]] = {}

    def set_operations(self, difficulty: Difficulty, operators: list[str]):
        if difficulty in self.operations:
            raise DifficultAlreadySetError("This difficulty operators already set")

        self.operations[difficulty] = operators


    def generate(self, difficulty: Difficulty) -> str:
        if difficulty not in self.operations:
            raise DifficultNotSetError("This difficulty operators already set")

        left = randint(self.start_range, self.end_range)
        right = randint(self.start_range, self.end_range)

        op = choice(self.operations[difficulty])

        while op == '/' and (difficulty != Difficulty.HARD and left % right != 0 or right == 0):
            right = randint(self.start_range, self.end_range)

        return f"{left} {op} {right}"