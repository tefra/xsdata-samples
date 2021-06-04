from dataclasses import dataclass, field
from typing import Optional
from netex.models.parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[ParkingFacilityEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
