from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class AdditionalDriverTypeEnumeration(StrEnum):
    NONE = "none"
    NAMED = "named"
    ANY = "any"
    OTHER = "other"
