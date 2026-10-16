from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CouplingTypeEnumeration(StrEnum):
    UNDEFINED = "undefined"
    PLUG = "plug"
    PANTOGRAPH_ABOVE = "pantographAbove"
    PANTOGRAPH = "pantograph"
    INDUCTION = "induction"
    OTHER = "other"
