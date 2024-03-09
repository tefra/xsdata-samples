from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.baggage_allowance import BaggageAllowance
from travelport.models.ticket_validity import TicketValidity

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SegmentModifiers:
    """
    To be used to modify the ticket modifiers for air segment.

    Parameters
    ----------
    air_segment_ref
    ticket_validity
        To be used to pass the ticket validity dates
    baggage_allowance
    ticket_designator
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment_ref: None | AirSegmentRef = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "required": True,
        },
    )
    ticket_validity: None | TicketValidity = field(
        default=None,
        metadata={
            "name": "TicketValidity",
            "type": "Element",
        },
    )
    baggage_allowance: None | BaggageAllowance = field(
        default=None,
        metadata={
            "name": "BaggageAllowance",
            "type": "Element",
        },
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Element",
            "min_length": 0,
            "max_length": 20,
        },
    )
