from dataclasses import dataclass


def validate(fun=None):
    def validate_instance(c: type):
        def inner(*args, **kwargs):
            instance = c(*args, **kwargs)
            fun(instance)
            return instance

        return inner
    return validate_instance


def checker(person):
    assert person.name == 'Samuel' or person.name == 'Sam'
    print('check person')


@validate(checker)
@dataclass(frozen=True)
class Person:
    name: str
    age: int


toto = Person('Samuel', 41)
print(toto)
tata = Person(name='Sam', age=14)
print(tata)
print(type(toto))
