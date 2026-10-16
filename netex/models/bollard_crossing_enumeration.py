from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BollardCrossingEnumeration(StrEnum):
    NONE = "none"
    CONTRASTED = "contrasted"
    YES = "yes"
    PARTIAL = "partial"
    LIMITED = "limited"
