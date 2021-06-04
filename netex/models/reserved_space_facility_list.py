from dataclasses import dataclass, field
from typing import List
from netex.models.reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ReservedSpaceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservedSpaceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
