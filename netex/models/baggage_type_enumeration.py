from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BaggageTypeEnumeration(Enum):
    HANDBAG = "handbag"
    HAND_LUGGAGE = "handLuggage"
    SMALL_SUITCASE = "smallSuitcase"
    SUITCASE = "suitcase"
    TRUNK = "trunk"
    OVERSIZE_ITEM = "oversizeItem"
    BICYCLE = "bicycle"
    MOTORCYCLE = "motorcycle"
    SPORTING_EQUIPMENT = "sportingEquipment"
    SKIS = "skis"
    MUSICALNSTRUMENT = "musicalnstrument"
    PUSH_CHAIR = "pushChair"
    WHEELCHAIR = "wheelchair"
    MOTORIZED_WHEELCHAIR = "motorizedWheelchair"
    LARGE_MOTORIZED_WHEELCHAIR = "largeMotorizedWheelchair"
    SMALL_ANIMAL = "smallAnimal"
    ANIMAL = "animal"
    GAME = "game"
    OTHER = "other"
