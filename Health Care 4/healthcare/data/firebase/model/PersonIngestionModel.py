from dataclasses import dataclass


@dataclass(order=True)
class PersonIngestionModel:
    id: str
    day: str
    info: dict
