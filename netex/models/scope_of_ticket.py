from __future__ import annotations

from dataclasses import dataclass, field

from .scope_of_ticket_enumeration import ScopeOfTicketEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScopeOfTicket:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ScopeOfTicketEnumeration = field(
        default=ScopeOfTicketEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
