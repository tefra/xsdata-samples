from dataclasses import dataclass, field
from typing import List
from netex.models.booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BookingProcessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
