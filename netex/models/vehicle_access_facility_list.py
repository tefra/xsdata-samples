from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleAccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[VehicleAccessFacilityEnumeration] = field(
        default_factory=lambda: [
            VehicleAccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
