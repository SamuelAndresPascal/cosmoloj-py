from dataclasses import dataclass


def validate(fun=None):
    def validate_instance(c: type):
        def inner(*args, **kwargs):
            instance = c(*args, **kwargs)
            fun(instance)
            return instance

        return inner
    return validate_instance


def autovalidate(c: type):
    def inner(*args, **kwargs):
        instance = c(*args, **kwargs)
        instance.validate()
        return instance
    return inner


def checker(person):
    assert person.name == 'Samuel' or person.name == 'Sam'
    print('rien')


@validate(checker)
@dataclass(frozen=True)
class Person:
    name: str
    age: int


@autovalidate
@dataclass(frozen=True)
class Person2:
    name: str
    age: int

    def validate(self):
        assert self.name == 'Samuel' or self.name == 'Sam'


toto = Person('Samuel', 41)
print(toto)
tata = Person(name='Sam', age=14)
print(tata)
print(type(toto))

tutu = Person2(name='Sam', age=14)
