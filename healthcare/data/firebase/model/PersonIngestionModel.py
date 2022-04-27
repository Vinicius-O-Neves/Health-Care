from dataclasses import dataclass


@dataclass(order=True)
class PersonIngestionModel:
    personCpf: int
    day: str
    info: dict
