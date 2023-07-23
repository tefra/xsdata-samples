from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_date_spec import TypeDateSpec

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AirReservationCriteria:
    """
    Criteria for searching the Air reservations.

    Parameters
    ----------
    departure_date
        Flight Departure Date or Date Range
    arrival_date
        Flight Arrival Date or Date Range
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    flight_number
    carrier
    passive_only
        Search for Passives Only
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    departure_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
        }
    )
    arrival_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Element",
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    passive_only: bool = field(
        default=False,
        metadata={
            "name": "PassiveOnly",
            "type": "Attribute",
        }
    )
