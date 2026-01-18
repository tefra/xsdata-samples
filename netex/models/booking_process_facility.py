from __future__ import annotations

from dataclasses import dataclass, field

from .booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingProcessFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BookingProcessEnumeration = field(
        metadata={
            "required": True,
        }
    )
