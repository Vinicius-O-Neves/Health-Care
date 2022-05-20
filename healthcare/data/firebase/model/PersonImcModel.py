from dataclasses import dataclass
from typing import Optional

@dataclass(order=True)
class PersonImcModel:
    id: str
    day: str
    info: dict
