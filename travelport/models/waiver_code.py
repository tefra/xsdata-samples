from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class WaiverCode:
    """
    Waiver code to override fare validations.

    Parameters
    ----------
    tour_code
    ticket_designator
    endorsement
        Endorsement. Size can be up to 100 characters
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
            "max_length": 15,
        }
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        }
    )
    endorsement: None | str = field(
        default=None,
        metadata={
            "name": "Endorsement",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 100,
        }
    )
