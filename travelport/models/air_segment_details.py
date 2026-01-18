from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.brand_id import BrandId
from travelport.models.passenger_details_ref import PassengerDetailsRef

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSegmentDetails:
    """
    An Air marketable travel segment.

    Parameters
    ----------
    passenger_details_ref
    brand_id
    booking_code_list
        Lists classes of service and their counts separated by delimiter |.
    key
    provider_code
    carrier
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
    equipment
    class_of_service
    cabin_class
    operating_carrier
        The actual carrier that is operating the flight.
    flight_number
        Flight Number for the Search Leg Detail.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    passenger_details_ref: list[PassengerDetailsRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerDetailsRef",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    brand_id: list[BrandId] = field(
        default_factory=list,
        metadata={
            "name": "BrandID",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    booking_code_list: None | str = field(
        default=None,
        metadata={
            "name": "BookingCodeList",
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
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    departure_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
            "required": True,
        },
    )
    arrival_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
            "required": True,
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
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        },
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        },
    )
    operating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "OperatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 5,
        },
    )
