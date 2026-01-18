from dataclasses import dataclass, field

from .booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class BookingProcessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BookingProcessEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
