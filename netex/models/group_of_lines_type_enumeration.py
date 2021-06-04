from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupOfLinesTypeEnumeration(Enum):
    MARKETING = "marketing"
    ADMINISTRATIVE = "administrative"
    SCHEDULING = "scheduling"
    CONTROL = "control"
    TARIFF = "tariff"
    OTHER = "other"
