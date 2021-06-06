from dataclasses import dataclass, field
from typing import List
from .luggage_locker_facility_enumeration import LuggageLockerFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LuggageLockerFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageLockerFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
