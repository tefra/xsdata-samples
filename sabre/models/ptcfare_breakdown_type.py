from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

from sabre.models.company_name_type import CompanyNameType
from sabre.models.fare_calc_line_type import FareCalcLineType
from sabre.models.fare_directionality import FareDirectionality
from sabre.models.fare_type import FareType
from sabre.models.free_text_type import FreeTextType
from sabre.models.passenger_type_quantity_type import PassengerTypeQuantityType
from sabre.models.ptcfare_breakdown_type_reissue_exchange import (
    PtcfareBreakdownTypeReissueExchange,
)
from sabre.models.response_location_type import ResponseLocationType
from sabre.models.rule_info_type import RuleInfoType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class PtcfareBreakdownType:
    """
    Per passenger type code pricing for this itinerary.

    Set if fareBreakdown was requested.

    Attributes:
        passenger_type_quantity: Number of individuals traveling under
            this PTC
        fare_basis_codes: This is a collection of Fare Basis Codes
        passenger_fare: The total passenger fare with cost breakdown.
        endorsements: Container for endorsements.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        fare_infos: This is a collection of FareInfo
        pricing_source: Indicates whether the fare is public or private.
        private_fare_type: Private fare type symbol.
        last_ticket_date: Last day to ticket.
        previous_exchange_date: Previous Exchange Date
        reissue_exchange: Indicates whether priced as Reissue or
            Exchange
    """

    class Meta:
        name = "PTCFareBreakdownType"

    passenger_type_quantity: None | PassengerTypeQuantityType = field(
        default=None,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    fare_basis_codes: None | PtcfareBreakdownType.FareBasisCodes = field(
        default=None,
        metadata={
            "name": "FareBasisCodes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    passenger_fare: None | FareType = field(
        default=None,
        metadata={
            "name": "PassengerFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        },
    )
    endorsements: None | PtcfareBreakdownType.Endorsements = field(
        default=None,
        metadata={
            "name": "Endorsements",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | PtcfareBreakdownType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_infos: None | PtcfareBreakdownType.FareInfos = field(
        default=None,
        metadata={
            "name": "FareInfos",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    pricing_source: None | str = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
            "pattern": r"[0-9A-Z_]{1,13}",
        },
    )
    private_fare_type: None | str = field(
        default=None,
        metadata={
            "name": "PrivateFareType",
            "type": "Attribute",
            "length": 1,
        },
    )
    last_ticket_date: None | str | XmlTime = field(
        default=None,
        metadata={
            "name": "LastTicketDate",
            "type": "Attribute",
        },
    )
    previous_exchange_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PreviousExchangeDate",
            "type": "Attribute",
        },
    )
    reissue_exchange: None | PtcfareBreakdownTypeReissueExchange = field(
        default=None,
        metadata={
            "name": "ReissueExchange",
            "type": "Attribute",
        },
    )

    @dataclass
    class FareBasisCodes:
        """
        Attributes:
            fare_basis_code: Fare basis code for the price for this PTC
        """

        fare_basis_code: list[
            PtcfareBreakdownType.FareBasisCodes.FareBasisCode
        ] = field(
            default_factory=list,
            metadata={
                "name": "FareBasisCode",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 400,
            },
        )

        @dataclass
        class FareBasisCode:
            """
            Attributes:
                value:
                private_fare_type: Private fare type symbol.
                fare_component_reference_id:
                account_code: Matched Account Code
                mileage: Mileage (AWARD Shopping)
                booking_code: Booking code
                availability_break: Availability break after this
                    segment
                departure_airport_code: Departure point of flight
                    segment.
                arrival_airport_code: Arrival point of flight segment.
                fare_component_begin_airport: If this attribute is
                    present, the enclosing FareBasisCode element is the
                    first portion of a new fare component. It represents
                    the origin airport of the fare component.
                fare_component_end_airport: If this attribute is
                    present, the enclosing FareBasisCode element is the
                    first portion of a new fare component. It represents
                    the destination airport of the fare component.
                fare_component_directionality: If this attribute is
                    present, the enclosing FareBasisCode element is the
                    first portion of a new fare component. If its value
                    is "FROM" it means that fare component origin and
                    destination are ordered the same as the departure
                    and arival airports of the leg. Value "TO" means the
                    opposite ordering of fare component origin and
                    destination.
                gov_carrier: Governing carrier
            """

            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "min_length": 1,
                    "max_length": 16,
                },
            )
            private_fare_type: None | str = field(
                default=None,
                metadata={
                    "name": "PrivateFareType",
                    "type": "Attribute",
                    "length": 1,
                },
            )
            fare_component_reference_id: None | int = field(
                default=None,
                metadata={
                    "name": "FareComponentReferenceID",
                    "type": "Attribute",
                },
            )
            account_code: None | str = field(
                default=None,
                metadata={
                    "name": "AccountCode",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 20,
                },
            )
            mileage: None | int = field(
                default=None,
                metadata={
                    "name": "Mileage",
                    "type": "Attribute",
                },
            )
            booking_code: None | str = field(
                default=None,
                metadata={
                    "name": "BookingCode",
                    "type": "Attribute",
                    "length": 1,
                },
            )
            availability_break: None | bool = field(
                default=None,
                metadata={
                    "name": "AvailabilityBreak",
                    "type": "Attribute",
                },
            )
            departure_airport_code: None | object = field(
                default=None,
                metadata={
                    "name": "DepartureAirportCode",
                    "type": "Attribute",
                },
            )
            arrival_airport_code: None | object = field(
                default=None,
                metadata={
                    "name": "ArrivalAirportCode",
                    "type": "Attribute",
                },
            )
            fare_component_begin_airport: None | str = field(
                default=None,
                metadata={
                    "name": "FareComponentBeginAirport",
                    "type": "Attribute",
                    "pattern": r"[A-Z]{3}",
                },
            )
            fare_component_end_airport: None | str = field(
                default=None,
                metadata={
                    "name": "FareComponentEndAirport",
                    "type": "Attribute",
                    "pattern": r"[A-Z]{3}",
                },
            )
            fare_component_directionality: None | FareDirectionality = field(
                default=None,
                metadata={
                    "name": "FareComponentDirectionality",
                    "type": "Attribute",
                },
            )
            gov_carrier: None | str = field(
                default=None,
                metadata={
                    "name": "GovCarrier",
                    "type": "Attribute",
                    "pattern": r"[0-9A-Z]{2,3}",
                },
            )

    @dataclass
    class Endorsements:
        """
        Attributes:
            endorsement: Specifies ticket endorsement information.
            tpa_extensions:
            non_refundable_indicator: Indicates whether the ticket is
                refundable. If true, the ticket is NOT refundable.
            non_endorsable_indicator: Indicates whether the ticket is
                endorsable. If true, the ticket is NOT endorsable.
        """

        endorsement: list[FreeTextType] = field(
            default_factory=list,
            metadata={
                "name": "Endorsement",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "max_occurs": 9,
            },
        )
        tpa_extensions: None | str = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        non_refundable_indicator: None | bool = field(
            default=None,
            metadata={
                "name": "NonRefundableIndicator",
                "type": "Attribute",
            },
        )
        non_endorsable_indicator: None | bool = field(
            default=None,
            metadata={
                "name": "NonEndorsableIndicator",
                "type": "Attribute",
            },
        )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            fare_calc_line: Fare calculation line.
            fare_type:
        """

        fare_calc_line: None | FareCalcLineType = field(
            default=None,
            metadata={
                "name": "FareCalcLine",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_type: None | PtcfareBreakdownType.TpaExtensions.FareType = field(
            default=None,
            metadata={
                "name": "FareType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class FareType:
            value: str = field(
                default="",
                metadata={
                    "required": True,
                },
            )
            name: None | str = field(
                default=None,
                metadata={
                    "name": "Name",
                    "type": "Attribute",
                },
            )

    @dataclass
    class FareInfos:
        """
        Attributes:
            fare_info: Detailed information on individual priced fares
        """

        fare_info: list[PtcfareBreakdownType.FareInfos.FareInfo] = field(
            default_factory=list,
            metadata={
                "name": "FareInfo",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 10,
            },
        )

        @dataclass
        class FareInfo:
            """
            Attributes:
                departure_date: Departure Date for this priced fare.
                fare_reference: FareReference is the booking code.
                rule_info: Information regarding restrictions governing
                    use of the fare.
                marketing_airline: The marketing airline.
                departure_airport: Departure point of flight segment.
                arrival_airport: Arrival point of flight segment.
                tpa_extensions:
                negotiated_fare: Indicator to show if this is a private
                    fare.
                negotiated_fare_code: Code used to identify the private
                    fare.
            """

            departure_date: None | str = field(
                default=None,
                metadata={
                    "name": "DepartureDate",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            fare_reference: None | str = field(
                default=None,
                metadata={
                    "name": "FareReference",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                },
            )
            rule_info: None | RuleInfoType = field(
                default=None,
                metadata={
                    "name": "RuleInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            marketing_airline: list[CompanyNameType] = field(
                default_factory=list,
                metadata={
                    "name": "MarketingAirline",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            departure_airport: None | ResponseLocationType = field(
                default=None,
                metadata={
                    "name": "DepartureAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            arrival_airport: None | ResponseLocationType = field(
                default=None,
                metadata={
                    "name": "ArrivalAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            tpa_extensions: (
                None | PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions
            ) = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            negotiated_fare: bool = field(
                default=False,
                metadata={
                    "name": "NegotiatedFare",
                    "type": "Attribute",
                },
            )
            negotiated_fare_code: None | str = field(
                default=None,
                metadata={
                    "name": "NegotiatedFareCode",
                    "type": "Attribute",
                },
            )

            @dataclass
            class TpaExtensions:
                seats_remaining: (
                    None
                    | PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining
                ) = field(
                    default=None,
                    metadata={
                        "name": "SeatsRemaining",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                cabin: (
                    None
                    | PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Cabin
                ) = field(
                    default=None,
                    metadata={
                        "name": "Cabin",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                fare_note: list[
                    PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.FareNote
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareNote",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                meal: (
                    None
                    | PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Meal
                ) = field(
                    default=None,
                    metadata={
                        "name": "Meal",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                rule: list[
                    PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Rule
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "Rule",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )

                @dataclass
                class SeatsRemaining:
                    number: None | int = field(
                        default=None,
                        metadata={
                            "name": "Number",
                            "type": "Attribute",
                        },
                    )
                    below_min: None | bool = field(
                        default=None,
                        metadata={
                            "name": "BelowMin",
                            "type": "Attribute",
                        },
                    )

                @dataclass
                class Cabin:
                    cabin: str = field(
                        default="Economy",
                        metadata={
                            "name": "Cabin",
                            "type": "Attribute",
                        },
                    )

                @dataclass
                class FareNote:
                    fare_type_name: None | str = field(
                        default=None,
                        metadata={
                            "name": "FareTypeName",
                            "type": "Attribute",
                        },
                    )
                    priority_level: None | int = field(
                        default=None,
                        metadata={
                            "name": "PriorityLevel",
                            "type": "Attribute",
                        },
                    )
                    content_id: None | str = field(
                        default=None,
                        metadata={
                            "name": "ContentID",
                            "type": "Attribute",
                        },
                    )

                @dataclass
                class Meal:
                    code: None | str = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                        },
                    )

                @dataclass
                class Rule:
                    type_value: None | str = field(
                        default=None,
                        metadata={
                            "name": "Type",
                            "type": "Attribute",
                        },
                    )
                    id: None | int = field(
                        default=None,
                        metadata={
                            "name": "ID",
                            "type": "Attribute",
                        },
                    )
