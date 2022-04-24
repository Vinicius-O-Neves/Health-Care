from dataclasses import dataclass


@dataclass(order=True)
class PersonIngestionModel:
    personCpf: int
    dia: str
    info: dict
