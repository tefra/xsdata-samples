from collections.abc import Iterable
from dataclasses import dataclass, field

from .booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BookingProcessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
