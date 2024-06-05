from dataclasses import dataclass
from typing import Mapping, Collection

from apischema import deserialize


@dataclass(frozen=True)
class Foo:
    bar: str


foo = Foo("bar")
assert foo.bar == "bar"

assert Foo("toto").bar == "toto"

assert deserialize(Foo, {"bar": "bar"}) == Foo("bar")
assert deserialize(Mapping[str, Collection[Foo]], {"key": [{"bar": "42"}]}) == {
    "key": [Foo("42")]
}
