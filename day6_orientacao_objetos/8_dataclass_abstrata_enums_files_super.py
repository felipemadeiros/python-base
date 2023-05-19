from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import List

# enum - Enumerador (ajuda a evitar erros de digitacao)
class InstrumentType(str, Enum):
    string = "string"
    wind = "wind"
    keys = "keys"
    drums = "drums"
    

# Abstracao e herança com dataclass
@dataclass
class Instrument(ABC):
    name: str
    sound: str
    type: InstrumentType # enum
    color: List[str] = field(default_factory=list) # field

    @abstractmethod
    def play(self):
        ...

@dataclass
class Guitar(Instrument):
    sound: str = "Ding Ding Ding"
    type: InstrumentType = InstrumentType.string # enum
    color: List[str] = field(default_factory=lambda: ["red", "black"]) #field

    def play(self):
        return self.sound

# super()
@dataclass
class EletricGuitar(Guitar):
    sound: str = "Wah Wah Wah"

    def play(self, distortion="wave"):
        return_from_base_class = super().play()
        
        if distortion == "wave":
            return "˜˜˜".join(return_from_base_class.split())
        return return_from_base_class

@dataclass
class Flute(Instrument):
    sound: str = "Flu Flu Flu"
    type: InstrumentType = InstrumentType.wind # enum

    def play(self):
        return self.sound

# test = Instrument() # Testing error when try instantiate a abstract class

gianini = Guitar("Gianini m2")
print(gianini.play())
print(gianini.color)

yamaha = Flute("Yamaha Magic Flute")
print(yamaha.play())

lespaul = EletricGuitar("lespaul m1")
print(lespaul.play())



