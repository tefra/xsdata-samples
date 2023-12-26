from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class OptionJourneyDetails:
    """
    Contains PickUp Return Details for that Cruise Feature/Option Service.

    Parameters
    ----------
    pick_up_location
        IATA/Non-IATA Location Code for Pickup. Examples:YVR
    pick_up_time
        PickUp Time
    pick_up_description
        PickUp Location Description
    pick_up_carrier
        The carrier that is marketing this segment.
    pick_up_flight_number
        The flight number under which the marketing carrier is marketing
        carrier is marketing this flight
    return_location
        IATA/Non-IATA Location Code for Drop Off. Examples:YVR
    return_time
        Return time
    return_description
        Return Location Description
    return_carrier
        The carrier that is marketing this segment.
    return_flight_number
        The flight number under which the marketing carrier is marketing
        carrier is marketing this flight
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    pick_up_location: None | str = field(
        default=None,
        metadata={
            "name": "PickUpLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    pick_up_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "PickUpTime",
            "type": "Attribute",
        },
    )
    pick_up_description: None | str = field(
        default=None,
        metadata={
            "name": "PickUpDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
    pick_up_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PickUpCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    pick_up_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "PickUpFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    return_location: None | str = field(
        default=None,
        metadata={
            "name": "ReturnLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    return_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "ReturnTime",
            "type": "Attribute",
        },
    )
    return_description: None | str = field(
        default=None,
        metadata={
            "name": "ReturnDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
    return_carrier: None | str = field(
        default=None,
        metadata={
            "name": "ReturnCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    return_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "ReturnFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
