def deco1(fun):

    def inner():
        print('je décore')
        fun()
        print('j\'ai fini de décorer')

    return inner


def titi1():
    print('to_print')


@deco1
def toto1():
    print('moi aussi')


def deco2(fun):

    def inner(to_print: str):
        print('je décore')
        fun(to_print)
        print('j\'ai décoré')

    return inner


@deco2
def toto2(to_print: str):
    print(to_print)


def deco3(c: type):

    def inner():
        print('nouvelle instance !')

    return inner


@deco3
class MyClass:
    pass


def deco4(argument):
    def deco4_instance(fun):
        def inner():
            print(argument)
            fun()
            print('et voilà !')

        return inner
    return deco4_instance


@deco4('bonjour')
def toto4():
    print('toto4')


@deco4('au revoir !')
def tutu4():
    print('tutu4')


if __name__ == "__main__":
    decorated = deco1(titi1)
    decorated()
    toto1()
    toto2('bof')

    titi = MyClass()
    tata = MyClass()
    toto4()
    tutu4()


