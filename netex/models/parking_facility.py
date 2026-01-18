from dataclasses import dataclass, field
from typing import Optional

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ParkingFacilityEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
