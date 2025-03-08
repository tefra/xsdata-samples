from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.air_itinerary_pricing_info_type import (
    AirItineraryPricingInfoType,
)
from sabre.models.free_text_type import FreeTextType
from sabre.models.response_location_type import ResponseLocationType
from sabre.models.ticketing_info_rs_type import TicketingInfoRsType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class TicketPricingType:
    """
    Pricing Information for Single Ticket.

    Attributes:
        origin_destination_options:
        air_itinerary_pricing_info: Pricing Information for a Ticket.
        notes: Provides for free form descriptive information for the
            priced itinerary.
        ticketing_info: Container for TicketingInfoRS_Type.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        number: Ticket position related to entire itinerary
    """

    origin_destination_options: (
        None | TicketPricingType.OriginDestinationOptions
    ) = field(
        default=None,
        metadata={
            "name": "OriginDestinationOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    air_itinerary_pricing_info: None | AirItineraryPricingInfoType = field(
        default=None,
        metadata={
            "name": "AirItineraryPricingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    notes: list[FreeTextType] = field(
        default_factory=list,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        },
    )
    ticketing_info: None | TicketingInfoRsType = field(
        default=None,
        metadata={
            "name": "TicketingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | TicketPricingType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
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

    @dataclass
    class OriginDestinationOptions:
        """
        Indicates which flights are covered by this ticket.
        """

        origin_destination_option: list[
            TicketPricingType.OriginDestinationOptions.OriginDestinationOption
        ] = field(
            default_factory=list,
            metadata={
                "name": "OriginDestinationOption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )

        @dataclass
        class OriginDestinationOption:
            flight_segment: list[
                TicketPricingType.OriginDestinationOptions.OriginDestinationOption.FlightSegment
            ] = field(
                default_factory=list,
                metadata={
                    "name": "FlightSegment",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 4,
                },
            )

            @dataclass
            class FlightSegment:
                """
                Attributes:
                    departure_airport: Departure point of flight
                        segment.
                    arrival_airport: Arrival point of flight segment.
                    departure_date_time:
                """

                departure_airport: None | ResponseLocationType = field(
                    default=None,
                    metadata={
                        "name": "DepartureAirport",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    },
                )
                arrival_airport: None | ResponseLocationType = field(
                    default=None,
                    metadata={
                        "name": "ArrivalAirport",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    },
                )
                departure_date_time: None | str = field(
                    default=None,
                    metadata={
                        "name": "DepartureDateTime",
                        "type": "Attribute",
                        "required": True,
                    },
                )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            validating_carrier: Issuing airline whose numeric airline
                code is reflected in the electronic transaction for the
                flight/value coupon(s).The Validating Carrier shall be
                the controlling and authorising entity for Electronic
                Ticketing transactions..
        """

        validating_carrier: (
            None | TicketPricingType.TpaExtensions.ValidatingCarrier
        ) = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class ValidatingCarrier:
            """
            Attributes:
                code: Identifies a company by the company code.
            """

            code: None | str = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                },
            )
