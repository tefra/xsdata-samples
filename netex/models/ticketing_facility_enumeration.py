from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TicketingFacilityEnumeration(StrEnum):
    UNKNOWN = "unknown"
    TICKET_MACHINES = "ticketMachines"
    TICKET_OFFICE = "ticketOffice"
    TICKET_ON_DEMAND_MACHINES = "ticketOnDemandMachines"
    MOBILE_TICKETING = "mobileTicketing"
