from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.airline_type import AirlineType
from sabre.models.fare_details_type import FareDetailsType
from sabre.models.mileage_display_type import MileageDisplayType
from sabre.models.plus_up_type import PlusUpType
from sabre.models.request_location_type import RequestLocationType
from sabre.models.reservation_type import ReservationType
from sabre.models.side_trip_type import SideTripType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class ExchangeOriginDestinationFlightType:
    """
    Attributes:
        origin_location: Flight origin code
        destination_location: Flight destination code
        airline: Airline information
        side_trip: Side trip information
        reservation: Reservation information
        mileage_display: Mileage information
        booking_date_time: Booking date and time
        fare:
        plus_up:
        number: Flight number
        departure_date_time: Departure date and time
        arrival_date_time: Arrival date and time
        marriage_status: Marriage status
        type_value: Flight type (A: Air Segment, K: ARUNK, O: Open
            Segment)
        flown: Specify whether the flight is flown.
        class_of_service: Class of service
    """

    origin_location: None | RequestLocationType = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    destination_location: None | RequestLocationType = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    airline: None | AirlineType = field(
        default=None,
        metadata={
            "name": "Airline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    side_trip: None | SideTripType = field(
        default=None,
        metadata={
            "name": "SideTrip",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    reservation: None | ReservationType = field(
        default=None,
        metadata={
            "name": "Reservation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    mileage_display: list[MileageDisplayType] = field(
        default_factory=list,
        metadata={
            "name": "MileageDisplay",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    booking_date_time: None | str = field(
        default=None,
        metadata={
            "name": "BookingDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        },
    )
    fare: None | ExchangeOriginDestinationFlightType.Fare = field(
        default=None,
        metadata={
            "name": "Fare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    plus_up: list[PlusUpType] = field(
        default_factory=list,
        metadata={
            "name": "PlusUp",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    number: None | int = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        },
    )
    departure_date_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        },
    )
    arrival_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}(:[0-9]{2})?",
        },
    )
    marriage_status: None | str = field(
        default=None,
        metadata={
            "name": "MarriageStatus",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "pattern": r"[AKO]",
        },
    )
    flown: bool = field(
        default=False,
        metadata={
            "name": "Flown",
            "type": "Attribute",
        },
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z]{1,2}",
        },
    )

    @dataclass
    class Fare(FareDetailsType):
        adjustment: (
            None | ExchangeOriginDestinationFlightType.Fare.Adjustment
        ) = field(
            default=None,
            metadata={
                "name": "Adjustment",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class Adjustment:
            """
            Attributes:
                value: Adjustment Value, can be positive or negative,
                    number or percentage
                currency: Currency of Adjustment's Value
                group: Markup/Discount Group
            """

            value: None | str = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(\+|-)?([0-9]+(\.[0-9]*)?|\.[0-9]+)%?",
                },
            )
            currency: None | str = field(
                default=None,
                metadata={
                    "name": "Currency",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                },
            )
            group: None | int = field(
                default=None,
                metadata={
                    "name": "Group",
                    "type": "Attribute",
                },
            )
