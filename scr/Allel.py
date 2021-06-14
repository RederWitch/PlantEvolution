# Klasa reprezentuje Allel, wariację genu

class Allel:
    _id: str = None
    _name: str = None
    _gen_type: str = None
    # Elementy do funkcji
    _water: int = None
    _foto: int = None
    _co2: int = None

    def __init__(self, id: str, name: str, gen_type: str, water: int = 0, foto: int = 0, co2: int = 0):
        self._id = id
        self._name = name
        self._gen_type = gen_type
        self._water = water
        self._foto = foto
        self._co2 = co2

    def __repr__(self) -> str:  # "Allel(name, id, gene_type)"
        return "Allel({}, {}, {})".format(self._name, self._id, self._gen_type)

    def __eq__(self, other):
        return self._id == other.get_id() and self._gen_type == other.get_gen_type()

    def __ne__(self, other):
        return not self == other

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_gen_type(self) -> str:
        return self._gen_type

    def get_water(self) -> int:
        return self._water

    def get_foto(self) -> int:
        return self._foto

    def get_co2(self) -> int:
        return self._co2
