from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.ticket_pricing_type import TicketPricingType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TicketsPricingType:
    ticket: list[TicketPricingType] = field(
        default_factory=list,
        metadata={
            "name": "Ticket",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
