from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FrequencyOfUseTypeEnumeration(Enum):
    NONE_VALUE = "none"
    UNLIMITED = "unlimited"
    LIMITED = "limited"
    TWICE_ADAY = "twiceADay"
    SINGLE = "single"
