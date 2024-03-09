from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CruiseItinerary:
    """
    Contains one day's journey Record.

    Parameters
    ----------
    departure_date
        The date at which this entity departs.
    departure_time
        The  time at which this entity departs.
    arrival_date
        The date at which this entity arrives at the destination.
    arrival_time
        The time at which this entity arrives at the destination.
    boarding_date
        The date at which this passenger boards the entity.
    boarding_time
        The time at which this passenger boards the entity.
    status
        Port of call status .Possible Values (List): SS - New item, LL -
        Waitlisted item, NN - Item is no need/need status, IX - Canceled
        item, HK - Booked item, HL - Booked item, HN - Booked item, UC -
        Unconfirmed item
    port_name
        Port of call name
    port_indicator
        Port of call type. Can be of the following values : P - Port of Cal,
        S - At Sea, E - Embarkation Port, D - Disembarkation Port
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    departure_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        },
    )
    departure_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        },
    )
    arrival_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ArrivalDate",
            "type": "Attribute",
        },
    )
    arrival_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        },
    )
    boarding_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BoardingDate",
            "type": "Attribute",
        },
    )
    boarding_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "BoardingTime",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        },
    )
    port_name: None | str = field(
        default=None,
        metadata={
            "name": "PortName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
    port_indicator: None | str = field(
        default=None,
        metadata={
            "name": "PortIndicator",
            "type": "Attribute",
            "length": 1,
        },
    )
