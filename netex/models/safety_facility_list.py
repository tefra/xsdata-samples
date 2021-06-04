from dataclasses import dataclass, field
from typing import List
from netex.models.safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SafetyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
