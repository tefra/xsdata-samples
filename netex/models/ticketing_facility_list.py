from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[TicketingFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
