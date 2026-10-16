from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DataRoleTypeEnumeration(StrEnum):
    ALL = "all"
    CREATES = "creates"
    AUGMENTS = "augments"
    VALIDATES = "validates"
    COLLECTS = "collects"
    AGGREGATES = "aggregates"
    DISTRIBUTES = "distributes"
    SECURES = "secures"
    REDISTRIBUTES = "redistributes"
    SUPPORTS = "supports"
    OWNS = "owns"
    OTHER = "other"
