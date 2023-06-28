from dataclasses import dataclass


@dataclass
class MutableNotHashable:
    id: int


@dataclass
class MutableHashable:
    id: int

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id


@dataclass(frozen=True)
class ImmutableHashable:
    id: int

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id
