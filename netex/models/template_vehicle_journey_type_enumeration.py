from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TemplateVehicleJourneyTypeEnumeration(StrEnum):
    HEADWAY = "headway"
    RHYTHMIC = "rhythmic"
    OTHER = "other"
