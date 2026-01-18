from __future__ import annotations

from dataclasses import dataclass, field

from .vehicle_access_facility_enumeration import (
    VehicleAccessFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleAccessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | VehicleAccessFacilityEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
