import time
from dataclasses import dataclass
from typing import TypedDict


class Typed(TypedDict):
    name: str
    first_name: str


@dataclass(frozen=True)
class Immutable:
    name: str
    first_name: str


@dataclass
class Mutable:
    name: str
    first_name: str


@dataclass(frozen=True, slots=True)
class ImmutableSlotted:
    name: str
    first_name: str


@dataclass(slots=True)
class MutableSlotted:
    name: str
    first_name: str


SIZE = 1000000

# temps en écriture
start = time.time_ns()
typed_dicts = [Typed(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('typed dict w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
immutables = [Immutable(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('immutable w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
mutables = [Mutable(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('mutable w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
slotted_immutables = [ImmutableSlotted(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('slotted immutable w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
slotted_mutables = [MutableSlotted(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('slotted mutable w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
dicts = [{'name': 'Andrés', 'first_name': 'Samuel'} for x in range(SIZE)]
print('literal dict w:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
dicts2 = [dict(name='Andrés', first_name='Samuel') for x in range(SIZE)]
print('constructed dict w:', (time.time_ns() - start) / 10**9)

n = ''
fn = ''

start = time.time_ns()
for d in typed_dicts:
    n = d['name']
    fn = d['first_name']
print('typed dicts r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for i in immutables:
    n = i.name
    fn = i.first_name
print('immutable r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for m in mutables:
    n = m.name
    fn = m.first_name
print('mutable r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for i in slotted_immutables:
    n = i.name
    fn = i.first_name
print('slotted immutable r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for m in slotted_mutables:
    n = m.name
    fn = m.first_name
print('slotted mutable r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for d in dicts:
    n = d['name']
    fn = d['first_name']
print('literal dict r:', (time.time_ns() - start) / 10**9)

start = time.time_ns()
for d in dicts2:
    n = d['name']
    fn = d['first_name']
print('constructed dict r:', (time.time_ns() - start) / 10**9)

