from dataclasses import dataclass, field

@dataclass(order = True)
class PersonIngestionModel:
    personCpf: str
    dia: str
    info: dict
   