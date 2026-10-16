from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PassageTypeEnumeration(StrEnum):
    NONE = "none"
    PATHWAY = "pathway"
    CORRIDOR = "corridor"
    OVERPASS = "overpass"
    UNDERPASS = "underpass"
    TUNNEL = "tunnel"
    OTHER = "other"
