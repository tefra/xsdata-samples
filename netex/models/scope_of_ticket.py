from dataclasses import dataclass, field
from netex.models.ticketing_facility_enumeration import TicketingFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScopeOfTicket:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TicketingFacilityEnumeration = field(
        default=TicketingFacilityEnumeration.UNKNOWN,
    )
