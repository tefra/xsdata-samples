from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PropulsionTypeEnumeration(StrEnum):
    COMBUSTION = "combustion"
    ELECTRIC = "electric"
    ELECTRIC_ASSIST = "electricAssist"
    HYBRID = "hybrid"
    HUMAN = "human"
    OTHER = "other"
