from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingProcessFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[BookingProcessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
