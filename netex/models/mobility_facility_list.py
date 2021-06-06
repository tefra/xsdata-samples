from dataclasses import dataclass, field
from typing import List
from .mobility_facility_enumeration import MobilityFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MobilityFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MobilityFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
