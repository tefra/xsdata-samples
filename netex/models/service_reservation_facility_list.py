from dataclasses import dataclass, field
from typing import List

from .reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceReservationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
