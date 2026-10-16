from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EncumbranceEnumeration(StrEnum):
    LUGGAGE_ENCUMBERED = "luggageEncumbered"
    PUSHCHAIR = "pushchair"
    BAGGAGE_TROLLEY = "baggageTrolley"
    OVERSIZE_BAGGAGE = "oversizeBaggage"
    GUIDE_DOG = "guideDog"
    OTHER_ANIMAL = "otherAnimal"
    OTHER_ENCUMBRANCE_NEED = "otherEncumbranceNeed"
