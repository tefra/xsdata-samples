from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EncumbranceEnumeration(Enum):
    LUGGAGE_ENCUMBERED = "luggageEncumbered"
    PUSHCHAIR = "pushchair"
    BAGGAGE_TROLLEY = "baggageTrolley"
    OVERSIZE_BAGGAGE = "oversizeBaggage"
    GUIDE_DOG = "guideDog"
    OTHER_ANIMAL = "otherAnimal"
    OTHER_ENCUMBRANCE_NEED = "otherEncumbranceNeed"
