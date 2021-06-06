from dataclasses import dataclass, field
from typing import List
from .accommodation_facility_enumeration import AccommodationFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccommodationFacilityEnumeration] = field(
        default_factory=lambda: [
            AccommodationFacilityEnumeration.UNKNOWN,
        ],
        metadata={
            "tokens": True,
        }
    )
