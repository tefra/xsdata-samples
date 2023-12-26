from dataclasses import dataclass, field
from typing import List
from .ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
