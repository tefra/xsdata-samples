from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.codeshare_info import CodeshareInfo
from travelport.models.in_flight_services import InFlightServices
from travelport.models.meals import Meals
from travelport.models.type_eticketability import TypeEticketability
from travelport.models.variance import Variance

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class FlightInfoDetail:
    """
    Parameters
    ----------
    codeshare_info
    meals
    in_flight_services
    variance
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    scheduled_departure_time
        The date and time at which this entity is scheduled to depart. This
        does not include time zone information since it can be derived from
        the origin location.
    scheduled_arrival_time
        The date and time at which this entity is scheduled to arrive at the
        destination. This does not include time zone information since it
        can be derived from the origin location.
    travel_time
        Total time spent (minutes) traveling including flight time and
        ground time.
    eticketability
        Identifies if this particular segment is E-Ticketable
    equipment
    origin_terminal
    origin_gate
        To be used to display origin flight gate number
    destination_terminal
    destination_gate
        To be used to display destination flight gate number
    automated_checkin
        “True” indicates that the flight allows automated check-in. The
        default is “False”.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    codeshare_info: None | CodeshareInfo = field(
        default=None,
        metadata={
            "name": "CodeshareInfo",
            "type": "Element",
        },
    )
    meals: list[Meals] = field(
        default_factory=list,
        metadata={
            "name": "Meals",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    in_flight_services: list[InFlightServices] = field(
        default_factory=list,
        metadata={
            "name": "InFlightServices",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    variance: list[Variance] = field(
        default_factory=list,
        metadata={
            "name": "Variance",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    origin: str = field(
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: str = field(
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    scheduled_departure_time: None | str = field(
        default=None,
        metadata={
            "name": "ScheduledDepartureTime",
            "type": "Attribute",
        },
    )
    scheduled_arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ScheduledArrivalTime",
            "type": "Attribute",
        },
    )
    travel_time: None | int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        },
    )
    eticketability: None | TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        },
    )
    equipment: None | str = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        },
    )
    origin_terminal: None | str = field(
        default=None,
        metadata={
            "name": "OriginTerminal",
            "type": "Attribute",
        },
    )
    origin_gate: None | str = field(
        default=None,
        metadata={
            "name": "OriginGate",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    destination_terminal: None | str = field(
        default=None,
        metadata={
            "name": "DestinationTerminal",
            "type": "Attribute",
        },
    )
    destination_gate: None | str = field(
        default=None,
        metadata={
            "name": "DestinationGate",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    automated_checkin: bool = field(
        default=False,
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
        },
    )
