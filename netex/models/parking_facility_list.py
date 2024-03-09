from dataclasses import dataclass, field
from typing import List

from .parking_facility_enumeration import ParkingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ParkingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
