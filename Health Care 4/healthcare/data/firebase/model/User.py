from dataclasses import dataclass
from typing import Optional


@dataclass(order=True)
class User:
    email: str
    cpf: int
    password: str
    confirmPassword: Optional[str]
