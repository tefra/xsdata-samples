from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.operating_company import OperatingCompany
from travelport.models.rail_avail_info import RailAvailInfo
from travelport.models.rail_segment_info import RailSegmentInfo
from travelport.models.segment_1 import Segment1
from travelport.models.type_transport_mode import TypeTransportMode

__NAMESPACE__ = "http://www.travelport.com/schema/rail_v52_0"


@dataclass
class RailSegment(Segment1):
    """
    Rail Segment.

    Parameters
    ----------
    rail_segment_info
    operating_company
    rail_avail_info
    ful_fillment_type
    train_number
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. This does not
        include time zone information since it can be derived from the
        origin location.
    arrival_time
        The date and time at which this entity arrives at the destination.
        This does not include time zone information since it can be derived
        from the origin location.
    origin_station_name
        The origin station name for the Journey.
    destination_station_name
        The destination station name for the Journey.
    rail_loc_origin
        RCH specific origin code (a.k.a UCodes) which uniquely identifies a
        train station.
    rail_loc_destination
        RCH specific destination code (a.k.a UCodes) which uniquely
        identifies a train station.
    train_type
        Type of train used. Same as TrainServiceType.
    train_type_code
        Code for type of train used. Same as TrainServiceType.
    transport_mode
        Type of Transport Mode used.
    seat_assignable
        Set to true if there exists seats to be booked
    transport_code
        Supplier specific train code
    reservation_required
        Set to true if a reservation is required for booking.
    travel_time
        Total time spent (minutes) traveling
    host_token_ref
        The reference key for the host token. From the HostTokenList
        Providers RCH.
    cabin_class
        Rail Cabin class specification. The valid values are Economy,
        Business, First and Other
    class_code
        A booking code or fare basis code or fare class.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/rail_v52_0"

    rail_segment_info: list[RailSegmentInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailSegmentInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    operating_company: None | OperatingCompany = field(
        default=None,
        metadata={
            "name": "OperatingCompany",
            "type": "Element",
        },
    )
    rail_avail_info: list[RailAvailInfo] = field(
        default_factory=list,
        metadata={
            "name": "RailAvailInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ful_fillment_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "FulFillmentType",
            "type": "Element",
            "max_occurs": 999,
            "min_length": 0,
            "max_length": 255,
        },
    )
    train_number: None | str = field(
        default=None,
        metadata={
            "name": "TrainNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
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
            "required": True,
        },
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        },
    )
    origin_station_name: None | str = field(
        default=None,
        metadata={
            "name": "OriginStationName",
            "type": "Attribute",
        },
    )
    destination_station_name: None | str = field(
        default=None,
        metadata={
            "name": "DestinationStationName",
            "type": "Attribute",
        },
    )
    rail_loc_origin: None | str = field(
        default=None,
        metadata={
            "name": "RailLocOrigin",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    rail_loc_destination: None | str = field(
        default=None,
        metadata={
            "name": "RailLocDestination",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 8,
            "white_space": "collapse",
        },
    )
    train_type: None | str = field(
        default=None,
        metadata={
            "name": "TrainType",
            "type": "Attribute",
        },
    )
    train_type_code: None | str = field(
        default=None,
        metadata={
            "name": "TrainTypeCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    transport_mode: None | TypeTransportMode = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Attribute",
        },
    )
    seat_assignable: None | bool = field(
        default=None,
        metadata={
            "name": "SeatAssignable",
            "type": "Attribute",
        },
    )
    transport_code: None | str = field(
        default=None,
        metadata={
            "name": "TransportCode",
            "type": "Attribute",
        },
    )
    reservation_required: None | bool = field(
        default=None,
        metadata={
            "name": "ReservationRequired",
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
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    class_code: None | str = field(
        default=None,
        metadata={
            "name": "ClassCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
