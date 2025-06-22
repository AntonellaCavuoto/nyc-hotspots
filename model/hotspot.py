from dataclasses import dataclass
@dataclass
class Location:
    n1Loc: str
    n1Lat: float
    n1Lang: float


    def __hash__(self):
        return self.n1Loc

    def __eq__(self, other):
        return self.n1Loc == other.n1Loc

    def __str__(self):
        return f"{self.n1Loc}"