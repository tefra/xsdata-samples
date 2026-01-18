from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.action_code_type import ActionCodeType
from sabre.models.airport_information_type import AirportInformationType
from sabre.models.company_name_type import CompanyNameType
from sabre.models.equipment_type import EquipmentType
from sabre.models.operating_airline_type import OperatingAirlineType
from sabre.models.response_location_type import ResponseLocationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class BookFlightSegmentType:
    """
    Container for the flight segment data plus the MarriageGrp.

    Attributes:
        departure_airport: Departure point of flight segment.
        arrival_airport: Arrival point of flight segment.
        operating_airline: The operating airline of the flight if it is
            a codeshare  flight.
        equipment: The type of equipment  used for the  flight..
        marketing_airline: The marketing airline. This is required for
            use with scheduled airline messages but may be omitted for
            requests by tour operators.
        disclosure_airline: The disclosure airline. This is required by
            the DOT mandate.
        marriage_grp: Many airlines link connection flights together by
            terming them married segments.  When two or more segments
            are married, they must be processed as one unit. The
            segments must be moved, cancelled, and/or priced together.
            The value of the marriage group must be the same for all
            segments.
        stop_airports:
        departure_time_zone:
        arrival_time_zone:
        on_time_performance:
        tpa_extensions:
        departure_date_time:
        arrival_date_time:
        stop_quantity: The number of stops the flight makes
        rph:
        info_source:
        flight_number: The flight number of the flight. This is required
            for use with scheduled airline messages but may be omitted
            for requests by tour operators.
        tour_operator_flight_id: ID of a flight in the Tour Operator's
            inventory. This flight is not necessarily in the inventory
            of an airline. Rather, it is a code created by tour
            operators.
        res_book_desig_code: Specific Booking Class for this segment.
        action_code:
        number_in_party:
        elapsed_time: Elapsed segment trip time.
    """

    departure_airport: AirportInformationType = field(
        metadata={
            "name": "DepartureAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    arrival_airport: AirportInformationType = field(
        metadata={
            "name": "ArrivalAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    operating_airline: None | OperatingAirlineType = field(
        default=None,
        metadata={
            "name": "OperatingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    equipment: list[EquipmentType] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 2,
        },
    )
    marketing_airline: None | CompanyNameType = field(
        default=None,
        metadata={
            "name": "MarketingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    disclosure_airline: None | CompanyNameType = field(
        default=None,
        metadata={
            "name": "DisclosureAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    marriage_grp: None | str = field(
        default=None,
        metadata={
            "name": "MarriageGrp",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        },
    )
    stop_airports: None | BookFlightSegmentType.StopAirports = field(
        default=None,
        metadata={
            "name": "StopAirports",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    departure_time_zone: None | BookFlightSegmentType.DepartureTimeZone = (
        field(
            default=None,
            metadata={
                "name": "DepartureTimeZone",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
    )
    arrival_time_zone: None | BookFlightSegmentType.ArrivalTimeZone = field(
        default=None,
        metadata={
            "name": "ArrivalTimeZone",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    on_time_performance: None | BookFlightSegmentType.OnTimePerformance = (
        field(
            default=None,
            metadata={
                "name": "OnTimePerformance",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
    )
    tpa_extensions: None | BookFlightSegmentType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    departure_date_time: str = field(
        metadata={
            "name": "DepartureDateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_date_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Attribute",
        },
    )
    stop_quantity: None | int = field(
        default=None,
        metadata={
            "name": "StopQuantity",
            "type": "Attribute",
        },
    )
    rph: None | str = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        },
    )
    info_source: None | str = field(
        default=None,
        metadata={
            "name": "InfoSource",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "pattern": r"[0-9]{1,4}[A-Z]?",
        },
    )
    tour_operator_flight_id: None | str = field(
        default=None,
        metadata={
            "name": "TourOperatorFlightID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    res_book_desig_code: None | str = field(
        default=None,
        metadata={
            "name": "ResBookDesigCode",
            "type": "Attribute",
            "pattern": r"[A-Z\s]{1,2}",
        },
    )
    action_code: None | ActionCodeType = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Attribute",
        },
    )
    number_in_party: None | int = field(
        default=None,
        metadata={
            "name": "NumberInParty",
            "type": "Attribute",
        },
    )
    elapsed_time: None | int = field(
        default=None,
        metadata={
            "name": "ElapsedTime",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class StopAirports:
        """
        Attributes:
            stop_airport: Stop point of flight segment.
        """

        stop_airport: list[BookFlightSegmentType.StopAirports.StopAirport] = (
            field(
                default_factory=list,
                metadata={
                    "name": "StopAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                },
            )
        )

        @dataclass(kw_only=True)
        class StopAirport(ResponseLocationType):
            """
            Attributes:
                arrival_date_time: This date should be of the form YYYY-
                    MM-DDTHH:MM:SS
                departure_date_time: This date should be of the form
                    YYYY-MM-DDTHH:MM:SS
                elapsed_time: Elapsed Time in minutes
                duration: Layover time in minutes
                gmtoffset:
                equipment: Equipment type
            """

            arrival_date_time: None | str = field(
                default=None,
                metadata={
                    "name": "ArrivalDateTime",
                    "type": "Attribute",
                },
            )
            departure_date_time: None | str = field(
                default=None,
                metadata={
                    "name": "DepartureDateTime",
                    "type": "Attribute",
                },
            )
            elapsed_time: None | int = field(
                default=None,
                metadata={
                    "name": "ElapsedTime",
                    "type": "Attribute",
                },
            )
            duration: None | int = field(
                default=None,
                metadata={
                    "name": "Duration",
                    "type": "Attribute",
                },
            )
            gmtoffset: None | float = field(
                default=None,
                metadata={
                    "name": "GMTOffset",
                    "type": "Attribute",
                },
            )
            equipment: None | object = field(
                default=None,
                metadata={
                    "name": "Equipment",
                    "type": "Attribute",
                },
            )

    @dataclass(kw_only=True)
    class DepartureTimeZone:
        gmtoffset: None | float = field(
            default=None,
            metadata={
                "name": "GMTOffset",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class ArrivalTimeZone:
        gmtoffset: None | float = field(
            default=None,
            metadata={
                "name": "GMTOffset",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class OnTimePerformance:
        level: None | str = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
            },
        )
        percentage: None | str = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class TpaExtensions:
        e_ticket: None | BookFlightSegmentType.TpaExtensions.ETicket = field(
            default=None,
            metadata={
                "name": "eTicket",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        data_element: (
            None | BookFlightSegmentType.TpaExtensions.DataElement
        ) = field(
            default=None,
            metadata={
                "name": "DataElement",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        message: None | BookFlightSegmentType.TpaExtensions.Message = field(
            default=None,
            metadata={
                "name": "Message",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class ETicket:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass(kw_only=True)
        class DataElement:
            subject_to_government_approval: None | bool = field(
                default=None,
                metadata={
                    "name": "SubjectToGovernmentApproval",
                    "type": "Attribute",
                },
            )

        @dataclass(kw_only=True)
        class Message:
            type_value: None | str = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                },
            )
            text: None | str = field(
                default=None,
                metadata={
                    "name": "Text",
                    "type": "Attribute",
                },
            )
