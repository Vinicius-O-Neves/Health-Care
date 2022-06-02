from dataclasses import dataclass


@dataclass(order=True)
class PersonImcModel:
    id: str
    day: str
    info: dict
