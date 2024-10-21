from collections.abc import Iterable
from dataclasses import dataclass, field

from .scope_of_ticket_enumeration import ScopeOfTicketEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ScopeOfTicketList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[ScopeOfTicketEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
