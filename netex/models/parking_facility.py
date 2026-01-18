from __future__ import annotations

from dataclasses import dataclass, field

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | ParkingFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
