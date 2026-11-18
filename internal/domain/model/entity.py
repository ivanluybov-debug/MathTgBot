from dataclasses import dataclass
from internal.domain.model.value_object import Verdict
from datetime import datetime


@dataclass
class User:
    tg_id: int
    name: str
    surname: str

@dataclass
class Attempt:
    attempt_id: int
    user: User
    verdict: Verdict
    timestamp: datetime
    example: str
    answer: str
