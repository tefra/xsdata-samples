from collections.abc import Iterable
from dataclasses import dataclass, field

from .reservation_enumeration import ReservationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ServiceReservationFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[ReservationEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
