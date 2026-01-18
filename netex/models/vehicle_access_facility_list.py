from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleAccessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[VehicleAccessFacilityEnumeration] = field(
        default_factory=lambda: [
            VehicleAccessFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        },
    )
