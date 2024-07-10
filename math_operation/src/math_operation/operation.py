from math_operation.surface import Surface


class Operation:

    def compute(self, i):
        """Compute the operation over the input coordinates.

        Args:
            i: the input coordinates

        Return:

        """
        pass


class InversibleOperation(Operation):

    def inverse(self, i):
        pass

    def inverseOperation(self) -> Operation:
        pass


class Conversion(Operation):

    def get_surface(self) -> Surface:
        """"""
        pass


class AutoInverse(InversibleOperation):

    def inverseOperation(self) -> Operation:
        return _AnonymAutoInverse(self)


class _AnonymAutoInverse(AutoInverse):

    def __init__(self, parent: AutoInverse):
        self._parent = parent

    def inverse(self, i):
        return self._parent.compute(i)

    def compute(self, i):
        return self._parent.inverse(i)

    def inverseOperation(self) -> Operation:
        return self._parent


class Projection(Conversion):
    pass


class InversibleProjection(Projection, AutoInverse):
    pass
