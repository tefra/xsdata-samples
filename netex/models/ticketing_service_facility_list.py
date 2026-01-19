from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Sequence[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
