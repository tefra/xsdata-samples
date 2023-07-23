from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.connection import Connection
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_meal_service import TypeMealService

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightDetails:
    """
    Specific details within a flight segment.

    Parameters
    ----------
    connection
    meals
    in_flight_services
    key
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. Date and time are
        represented as Airport Local Time at the place of departure. The
        correct time zone offset is also included.
    arrival_time
        The date and time at which this entity arrives at the destination.
        Date and time are represented as Airport Local Time at the place of
        arrival. The correct time zone offset is also included.
    flight_time
        Time spent (minutes) traveling in flight, including airport taxi
        time.
    travel_time
        Total time spent (minutes) traveling including flight time and
        ground time.
    distance
        The distance traveled. Units are specified in the parent response
        element.
    equipment
    on_time_performance
        Represents flight on time performance as a percentage from 0 to 100
    origin_terminal
    destination_terminal
    ground_time
    automated_checkin
        “True” indicates that the flight allows automated check-in. The
        default is “False”.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    connection: None | Connection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
        }
    )
    meals: list[TypeMealService] = field(
        default_factory=list,
        metadata={
            "name": "Meals",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    in_flight_services: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InFlightServices",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    flight_time: None | int = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    travel_time: None | int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    distance: None | int = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Attribute",
        }
    )
    equipment: None | str = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    on_time_performance: None | int = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Attribute",
        }
    )
    origin_terminal: None | str = field(
        default=None,
        metadata={
            "name": "OriginTerminal",
            "type": "Attribute",
        }
    )
    destination_terminal: None | str = field(
        default=None,
        metadata={
            "name": "DestinationTerminal",
            "type": "Attribute",
        }
    )
    ground_time: None | int = field(
        default=None,
        metadata={
            "name": "GroundTime",
            "type": "Attribute",
        }
    )
    automated_checkin: bool = field(
        default=False,
        metadata={
            "name": "AutomatedCheckin",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
