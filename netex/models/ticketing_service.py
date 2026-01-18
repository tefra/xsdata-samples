from __future__ import annotations

from dataclasses import dataclass

from .ticketing_service_version_structure import (
    TicketingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingService(TicketingServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
