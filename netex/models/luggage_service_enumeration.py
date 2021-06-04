from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageServiceEnumeration(Enum):
    LEFT_LUGGAGE = "leftLuggage"
    PORTERAGE = "porterage"
    FREE_TROLLEYS = "freeTrolleys"
    PAID_TROLLEYS = "paidTrolleys"
    OTHER = "other"
