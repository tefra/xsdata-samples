from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


class TypeVehicleChargeIncludedInRate(StrEnum):
    NOT_INCLUDED = "NotIncluded"
    INCLUDED_IN_BASE = "IncludedInBase"
    INCLUDED_IN_TOTAL = "IncludedInTotal"
