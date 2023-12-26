from dataclasses import dataclass
from .ticketing_service_version_structure import (
    TicketingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TicketingService(TicketingServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
