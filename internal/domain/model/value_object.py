from enum import Enum

class Verdict(Enum):
    OK = 0
    WA = 1
    TL = 1


class Difficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class Problem:
    problem: str
    difficulty: Difficulty
    answer: str


