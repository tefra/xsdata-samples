from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.ticket_endorsement import TicketEndorsement

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class InvoluntaryChange:
    """
    Specify the Ticket Endorsement value.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_endorsement: None | TicketEndorsement = field(
        default=None,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "required": True,
        },
    )
