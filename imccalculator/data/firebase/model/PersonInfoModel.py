from dataclasses import dataclass, field

@dataclass(order = True)
class PersonInfoModel:
    dia: str
    info: dict
   