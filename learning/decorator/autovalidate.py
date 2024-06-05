from dataclasses import dataclass


def autovalidate(c: type):
    def inner(*args, **kwargs):
        instance = c(*args, **kwargs)
        instance.validate()
        return instance
    return inner


@autovalidate
@dataclass(frozen=True)
class Person:
    name: str
    age: int

    def validate(self):
        assert self.name == 'Samuel' or self.name == 'Sam'
        print("validate person")


tutu = Person(name='Sam', age=14)
