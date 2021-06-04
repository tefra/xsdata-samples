from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DataRoleTypeEnumeration(Enum):
    ALL = "all"
    CREATES = "creates"
    AUGMENTS = "augments"
    VALIDATES = "validates"
    COLLECTS = "collects"
    AGGREGATES = "aggregates"
    DISTRIBUTES = "distributes"
    SECURES = "secures"
    REDISTRIBUTES = "redistributes"
    OWNS = "owns"
    OTHER = "other"
