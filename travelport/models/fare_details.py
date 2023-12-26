from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_ticket_designator import FareTicketDesignator

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareDetails:
    """
    Information about this fare component.

    Parameters
    ----------
    fare_ticket_designator
    key
        Fare key
    passenger_detail_ref
        PassengerRef key
    fare_basis
        The fare basis code for this fare
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_ticket_designator: None | FareTicketDesignator = field(
        default=None,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    passenger_detail_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassengerDetailRef",
            "type": "Attribute",
            "required": True,
        },
    )
    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
            "max_length": 20,
        },
    )
