from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_mct_connection import TypeMctConnection

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class MctSearch:
    """
    Search the MCT data for exceptions.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    arrive_station: str = field(
        metadata={
            "name": "ArriveStation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    depart_station: None | str = field(
        default=None,
        metadata={
            "name": "DepartStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    connection: None | TypeMctConnection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
        },
    )
    arrive_carrier: None | str = field(
        default=None,
        metadata={
            "name": "ArriveCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    depart_carrier: None | str = field(
        default=None,
        metadata={
            "name": "DepartCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    arrive_flight: None | str = field(
        default=None,
        metadata={
            "name": "ArriveFlight",
            "type": "Attribute",
        },
    )
    depart_flight: None | str = field(
        default=None,
        metadata={
            "name": "DepartFlight",
            "type": "Attribute",
        },
    )
    previous_station: None | str = field(
        default=None,
        metadata={
            "name": "PreviousStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    next_station: None | str = field(
        default=None,
        metadata={
            "name": "NextStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    previous_country: None | str = field(
        default=None,
        metadata={
            "name": "PreviousCountry",
            "type": "Attribute",
            "length": 2,
        },
    )
    next_country: None | str = field(
        default=None,
        metadata={
            "name": "NextCountry",
            "type": "Attribute",
            "length": 2,
        },
    )
    previous_state: None | str = field(
        default=None,
        metadata={
            "name": "PreviousState",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    next_state: None | str = field(
        default=None,
        metadata={
            "name": "NextState",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    travel_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Attribute",
        },
    )
