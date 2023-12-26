from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class ShopInformation2:
    """
    Shopping Information required for File Finishing.

    Parameters
    ----------
    search_request
        Search parameters that were used in LFS request
    flights_offered
        Flights with lowest logical airfare returned as response to LFS
        request
    cabin_shopped
    cabin_selected
    lowest_fare_offered
    """

    class Meta:
        name = "ShopInformation"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    search_request: list[ShopInformation2.SearchRequest] = field(
        default_factory=list,
        metadata={
            "name": "SearchRequest",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    flights_offered: list[ShopInformation2.FlightsOffered] = field(
        default_factory=list,
        metadata={
            "name": "FlightsOffered",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    cabin_shopped: None | str = field(
        default=None,
        metadata={
            "name": "CabinShopped",
            "type": "Attribute",
        },
    )
    cabin_selected: None | str = field(
        default=None,
        metadata={
            "name": "CabinSelected",
            "type": "Attribute",
        },
    )
    lowest_fare_offered: None | str = field(
        default=None,
        metadata={
            "name": "LowestFareOffered",
            "type": "Attribute",
        },
    )

    @dataclass
    class SearchRequest:
        """
        Parameters
        ----------
        origin
        destination
        departure_time
            Date and Time at which this entity departs. This does not
            include Time Zone information since it can be derived from
            origin location
        class_of_service
        """

        origin: None | str = field(
            default=None,
            metadata={
                "name": "Origin",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            },
        )
        destination: None | str = field(
            default=None,
            metadata={
                "name": "Destination",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            },
        )
        departure_time: None | str = field(
            default=None,
            metadata={
                "name": "DepartureTime",
                "type": "Attribute",
            },
        )
        class_of_service: None | str = field(
            default=None,
            metadata={
                "name": "ClassOfService",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 2,
            },
        )

    @dataclass
    class FlightsOffered:
        """
        Parameters
        ----------
        origin
        destination
        departure_time
            Date and Time at which this entity departs. This does not
            include Time Zone information since it can be derived from
            origin location
        travel_order
        carrier
        flight_number
        class_of_service
        stop_over
        connection
        """

        origin: None | str = field(
            default=None,
            metadata={
                "name": "Origin",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            },
        )
        destination: None | str = field(
            default=None,
            metadata={
                "name": "Destination",
                "type": "Attribute",
                "length": 3,
                "white_space": "collapse",
            },
        )
        departure_time: None | str = field(
            default=None,
            metadata={
                "name": "DepartureTime",
                "type": "Attribute",
            },
        )
        travel_order: None | int = field(
            default=None,
            metadata={
                "name": "TravelOrder",
                "type": "Attribute",
            },
        )
        carrier: None | str = field(
            default=None,
            metadata={
                "name": "Carrier",
                "type": "Attribute",
                "length": 2,
            },
        )
        flight_number: None | str = field(
            default=None,
            metadata={
                "name": "FlightNumber",
                "type": "Attribute",
                "max_length": 5,
            },
        )
        class_of_service: None | str = field(
            default=None,
            metadata={
                "name": "ClassOfService",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 2,
            },
        )
        stop_over: bool = field(
            default=False,
            metadata={
                "name": "StopOver",
                "type": "Attribute",
            },
        )
        connection: bool = field(
            default=False,
            metadata={
                "name": "Connection",
                "type": "Attribute",
            },
        )
