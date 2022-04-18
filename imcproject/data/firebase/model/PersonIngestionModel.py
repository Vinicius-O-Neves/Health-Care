from dataclasses import dataclass, field

@dataclass(order = True)
class PersonIngestionModel:
    dia: str
    info: dict
   