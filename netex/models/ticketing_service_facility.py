from __future__ import annotations

from dataclasses import dataclass, field

from .ticketing_service_facility_enumeration import (
    TicketingServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingServiceFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingServiceFacilityEnumeration | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
