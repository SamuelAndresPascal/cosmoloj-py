from unit_simple import UnitConverter, Unit


class DimensionTransformer:

    def __init__(self, source: Unit, converter: UnitConverter, target: Unit):
        self._source = source
        self._converter = converter
        self._target = target

    def get_converter(self, source: Unit, target: Unit) -> UnitConverter:
        return (source.get_converter_to(self._source)
                .concatenate(self._converter)
                .concatenate(self._target.get_converter_to(target)))
