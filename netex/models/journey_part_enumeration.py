from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class JourneyPartEnumeration(Enum):
    JOINING_TO = "joiningTo"
    SPLITTING_FROM = "splittingFrom"
    SPLITTING_TO = "splittingTo"
    JOIN_FROM = "joinFrom"
    CONNECT_TO = "connectTo"
    IDENTIFICATION_NUMBER_CHANGE = "identificationNumberChange"
