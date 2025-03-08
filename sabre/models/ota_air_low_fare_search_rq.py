from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.air_search_prefs_type import AirSearchPrefsType
from sabre.models.alliance_type import AllianceType
from sabre.models.award_shopping_type import AwardShoppingType
from sabre.models.billing_information_type import BillingInformationType
from sabre.models.cabin_pref_type import CabinPrefType
from sabre.models.cabin_type import CabinType
from sabre.models.cache_partition_group_type import CachePartitionGroupType
from sabre.models.cache_partition_type import CachePartitionType
from sabre.models.connection_type import ConnectionType
from sabre.models.departure_days_type import DepartureDaysType
from sabre.models.diversity_control_type import DiversityControlType
from sabre.models.exchange_settings_type import ExchangeSettingsType
from sabre.models.exchange_type import ExchangeType
from sabre.models.global_date_time_type import GlobalDateTimeType
from sabre.models.include_vendor_pref_type import IncludeVendorPrefType
from sabre.models.multi_ticket_display_policy import MultiTicketDisplayPolicy
from sabre.models.origin_destination_flight_type import (
    OriginDestinationFlightType,
)
from sabre.models.origin_destination_information_type import (
    OriginDestinationInformationType,
)
from sabre.models.ota_air_low_fare_search_rq_target import (
    OtaAirLowFareSearchRqTarget,
)
from sabre.models.ota_air_low_fare_search_rq_transaction_status_code import (
    OtaAirLowFareSearchRqTransactionStatusCode,
)
from sabre.models.pos_type import PosType
from sabre.models.prefer_level_type import PreferLevelType
from sabre.models.request_location_type import RequestLocationType
from sabre.models.routing_definition_type import RoutingDefinitionType
from sabre.models.segment_type_code import SegmentTypeCode
from sabre.models.transaction_type import TransactionType
from sabre.models.traveler_info_summary_type import TravelerInfoSummaryType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class OtaAirLowFareSearchRq:
    """The Low Fare Search Request message requests priced itinerary options for
    flights between specific city pairs on specific dates for specific numbers and
    types of passengers.

    Optional request information can include: - Time / Time Window - Connecting cities. - Client Preferences (airlines, cabin, flight types etc.) The Low Fare Search request contains similar information to a Low Fare Search entry on an airline CRS or GDS.

    Attributes:
        pos: Point of sale object.
        origin_destination_information: Origin and Destination location,
            and time information for the Air Low Fare Search request.
        leg: Single leg specification
        travel_preferences: Air Low Fare Search Request preference
            information.
        traveler_info_summary: Specifies the number of passengers and
            types for Air Low Fare Search.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        echo_token: A sequence number for additional message
            identification, assigned by the requesting host system. When
            a request message includes an echo token the corresponding
            response message MUST include an echo token with an
            identical value.
        time_stamp: Indicates the creation date and time of the message
            in UTC using the following format specified by ISO 8601;
            YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour
            clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes
            2003-11-20T13:59:38Z).
        target: Used to indicate whether the request is for the Test or
            Production system.
        version: For all OTA versioned messages, the version of the
            message is indicated by a decimal value.
        transaction_identifier: A unique identifier to relate all
            messages within a transaction (e.g. this would be sent in
            all request and response messages that are part of an on-
            going transaction).
        sequence_nmbr: Used to identify the sequence number of the
            transaction as assigned by the sending system; allows for an
            application to process messages in a certain order or to
            request a resynchronization of messages in the event that a
            system has been off-line and needs to retrieve messages that
            were missed.
        transaction_status_code: This indicates where this message falls
            within a sequence of messages.
        primary_lang_id: Identifes the primary language preference for
            the form of travel represented in a collection. The human
            language is identified by ISO 639 codes.
        alt_lang_id:
        max_responses: A positive integer value that indicates the
            maximum number of responses desired in the return.
        direct_flights_only: Request direct flights between given
            locations. This defaults to false.
        available_flights_only: Include only flights with available
            booking codes (when True or when attribute not present).
        response_type:
        response_version:
        separate_messages: Whether all messages should be printed in
            separate MTP element or not. Works only with PSS response
            serializers.
        truncate_messages: Whether each MTP content should be truncated
            to specified length or not. Works only with PSS response
            serializers.
    """

    class Meta:
        name = "OTA_AirLowFareSearchRQ"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    pos: None | PosType = field(
        default=None,
        metadata={
            "name": "POS",
            "type": "Element",
            "required": True,
        },
    )
    origin_destination_information: list[
        OtaAirLowFareSearchRq.OriginDestinationInformation
    ] = field(
        default_factory=list,
        metadata={
            "name": "OriginDestinationInformation",
            "type": "Element",
            "max_occurs": 10,
        },
    )
    leg: list[OtaAirLowFareSearchRq.Leg] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
        },
    )
    travel_preferences: None | AirSearchPrefsType = field(
        default=None,
        metadata={
            "name": "TravelPreferences",
            "type": "Element",
        },
    )
    traveler_info_summary: None | TravelerInfoSummaryType = field(
        default=None,
        metadata={
            "name": "TravelerInfoSummary",
            "type": "Element",
            "required": True,
        },
    )
    tpa_extensions: None | OtaAirLowFareSearchRq.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
        },
    )
    echo_token: None | str = field(
        default=None,
        metadata={
            "name": "EchoToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    time_stamp: None | str = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
        },
    )
    target: OtaAirLowFareSearchRqTarget = field(
        default=OtaAirLowFareSearchRqTarget.PRODUCTION,
        metadata={
            "name": "Target",
            "type": "Attribute",
        },
    )
    version: None | str = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        },
    )
    transaction_identifier: None | str = field(
        default=None,
        metadata={
            "name": "TransactionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        },
    )
    sequence_nmbr: None | int | bool = field(
        default=None,
        metadata={
            "name": "SequenceNmbr",
            "type": "Attribute",
        },
    )
    transaction_status_code: (
        None | OtaAirLowFareSearchRqTransactionStatusCode
    ) = field(
        default=None,
        metadata={
            "name": "TransactionStatusCode",
            "type": "Attribute",
        },
    )
    primary_lang_id: None | str = field(
        default=None,
        metadata={
            "name": "PrimaryLangID",
            "type": "Attribute",
        },
    )
    alt_lang_id: None | str = field(
        default=None,
        metadata={
            "name": "AltLangID",
            "type": "Attribute",
        },
    )
    max_responses: None | int = field(
        default=None,
        metadata={
            "name": "MaxResponses",
            "type": "Attribute",
        },
    )
    direct_flights_only: bool = field(
        default=False,
        metadata={
            "name": "DirectFlightsOnly",
            "type": "Attribute",
        },
    )
    available_flights_only: bool = field(
        default=True,
        metadata={
            "name": "AvailableFlightsOnly",
            "type": "Attribute",
        },
    )
    response_type: None | str = field(
        default=None,
        metadata={
            "name": "ResponseType",
            "type": "Attribute",
        },
    )
    response_version: None | str = field(
        default=None,
        metadata={
            "name": "ResponseVersion",
            "type": "Attribute",
        },
    )
    separate_messages: bool = field(
        default=False,
        metadata={
            "name": "SeparateMessages",
            "type": "Attribute",
        },
    )
    truncate_messages: bool = field(
        default=True,
        metadata={
            "name": "TruncateMessages",
            "type": "Attribute",
        },
    )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            intelli_sell_transaction:
            diversity_control:
            messaging_details:
            alternate_airport_cities: For each specified location
                provide an alternate location.
            alternate_airport_mileage: Specify maximum allowed distance
                from specified airport.
            award_shopping:
            billing:
            exchange_settings:
            exchange:
            split_taxes:
            alternate_dates_processing:
            itinerary_cache:
            multi_ticket:
            partitions:
            reservation_data:
            alternate_pcc:
        """

        intelli_sell_transaction: None | TransactionType = field(
            default=None,
            metadata={
                "name": "IntelliSellTransaction",
                "type": "Element",
            },
        )
        diversity_control: None | DiversityControlType = field(
            default=None,
            metadata={
                "name": "DiversityControl",
                "type": "Element",
            },
        )
        messaging_details: (
            None | OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails
        ) = field(
            default=None,
            metadata={
                "name": "MessagingDetails",
                "type": "Element",
            },
        )
        alternate_airport_cities: list[
            OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities
        ] = field(
            default_factory=list,
            metadata={
                "name": "AlternateAirportCities",
                "type": "Element",
            },
        )
        alternate_airport_mileage: (
            None | OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportMileage
        ) = field(
            default=None,
            metadata={
                "name": "AlternateAirportMileage",
                "type": "Element",
            },
        )
        award_shopping: None | AwardShoppingType = field(
            default=None,
            metadata={
                "name": "AwardShopping",
                "type": "Element",
            },
        )
        billing: None | BillingInformationType = field(
            default=None,
            metadata={
                "name": "Billing",
                "type": "Element",
            },
        )
        exchange_settings: None | ExchangeSettingsType = field(
            default=None,
            metadata={
                "name": "ExchangeSettings",
                "type": "Element",
            },
        )
        exchange: list[ExchangeType] = field(
            default_factory=list,
            metadata={
                "name": "Exchange",
                "type": "Element",
            },
        )
        split_taxes: None | OtaAirLowFareSearchRq.TpaExtensions.SplitTaxes = (
            field(
                default=None,
                metadata={
                    "name": "SplitTaxes",
                    "type": "Element",
                },
            )
        )
        alternate_dates_processing: (
            None | OtaAirLowFareSearchRq.TpaExtensions.AlternateDatesProcessing
        ) = field(
            default=None,
            metadata={
                "name": "AlternateDatesProcessing",
                "type": "Element",
            },
        )
        itinerary_cache: (
            None | OtaAirLowFareSearchRq.TpaExtensions.ItineraryCache
        ) = field(
            default=None,
            metadata={
                "name": "ItineraryCache",
                "type": "Element",
            },
        )
        multi_ticket: (
            None | OtaAirLowFareSearchRq.TpaExtensions.MultiTicket
        ) = field(
            default=None,
            metadata={
                "name": "MultiTicket",
                "type": "Element",
            },
        )
        partitions: None | OtaAirLowFareSearchRq.TpaExtensions.Partitions = (
            field(
                default=None,
                metadata={
                    "name": "Partitions",
                    "type": "Element",
                },
            )
        )
        reservation_data: (
            None | OtaAirLowFareSearchRq.TpaExtensions.ReservationData
        ) = field(
            default=None,
            metadata={
                "name": "ReservationData",
                "type": "Element",
            },
        )
        alternate_pcc: list[
            OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc
        ] = field(
            default_factory=list,
            metadata={
                "name": "AlternatePCC",
                "type": "Element",
            },
        )

        @dataclass
        class MessagingDetails:
            mdrsubset: (
                None
                | OtaAirLowFareSearchRq.TpaExtensions.MessagingDetails.Mdrsubset
            ) = field(
                default=None,
                metadata={
                    "name": "MDRSubset",
                    "type": "Element",
                },
            )

            @dataclass
            class Mdrsubset:
                code: None | str = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    },
                )

        @dataclass
        class SplitTaxes:
            by_leg: None | bool = field(
                default=None,
                metadata={
                    "name": "ByLeg",
                    "type": "Attribute",
                },
            )
            by_fare_component: None | bool = field(
                default=None,
                metadata={
                    "name": "ByFareComponent",
                    "type": "Attribute",
                },
            )

        @dataclass
        class AlternateDatesProcessing:
            calendar_mode: None | bool = field(
                default=None,
                metadata={
                    "name": "CalendarMode",
                    "type": "Attribute",
                },
            )
            num_options_per_alternate_date: int = field(
                default=9,
                metadata={
                    "name": "NumOptionsPerAlternateDate",
                    "type": "Attribute",
                },
            )

        @dataclass
        class ItineraryCache:
            public_time_to_live: None | int = field(
                default=None,
                metadata={
                    "name": "PublicTimeToLive",
                    "type": "Attribute",
                },
            )
            remove_previous_on_update: None | bool = field(
                default=None,
                metadata={
                    "name": "RemovePreviousOnUpdate",
                    "type": "Attribute",
                },
            )

        @dataclass
        class MultiTicket:
            """
            Attributes:
                display_policy: Display Option Policy, takes values: -
                    SOW - Show OneWays separately - GOW2RT - Group
                    OneWays and match to RoundTrip - SCHS - Group
                    OneWays, match to RoundTrip and show cheaper
                    solution
            """

            display_policy: None | MultiTicketDisplayPolicy = field(
                default=None,
                metadata={
                    "name": "DisplayPolicy",
                    "type": "Attribute",
                },
            )

        @dataclass
        class Partitions:
            partition: list[CachePartitionType] = field(
                default_factory=list,
                metadata={
                    "name": "Partition",
                    "type": "Element",
                },
            )
            group: list[CachePartitionGroupType] = field(
                default_factory=list,
                metadata={
                    "name": "Group",
                    "type": "Element",
                },
            )

        @dataclass
        class ReservationData:
            """
            Attributes:
                dknumber: DK number
            """

            dknumber: None | str = field(
                default=None,
                metadata={
                    "name": "DKNumber",
                    "type": "Attribute",
                },
            )

        @dataclass
        class AlternatePcc:
            """
            Attributes:
                travel_preferences:
                pseudo_city_code: An identification code assigned to an
                    office/agency by a reservation system.
            """

            travel_preferences: (
                None
                | OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences
            ) = field(
                default=None,
                metadata={
                    "name": "TravelPreferences",
                    "type": "Element",
                },
            )
            pseudo_city_code: None | str = field(
                default=None,
                metadata={
                    "name": "PseudoCityCode",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 16,
                },
            )

            @dataclass
            class TravelPreferences:
                vendor_pref: list[
                    OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.VendorPref
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "VendorPref",
                        "type": "Element",
                    },
                )
                tpa_extensions: (
                    None
                    | OtaAirLowFareSearchRq.TpaExtensions.AlternatePcc.TravelPreferences.TpaExtensions
                ) = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    },
                )

                @dataclass
                class VendorPref:
                    """
                    Attributes:
                        code: Identifies a company by the company code.
                        prefer_level:
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
                    prefer_level: PreferLevelType = field(
                        default=PreferLevelType.PREFERRED,
                        metadata={
                            "name": "PreferLevel",
                            "type": "Attribute",
                        },
                    )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes:
                        include_alliance_pref: Consider only these
                            alliances.
                        exclude_alliance_pref: Do not consider these
                            alliances.
                    """

                    include_alliance_pref: list[AllianceType] = field(
                        default_factory=list,
                        metadata={
                            "name": "IncludeAlliancePref",
                            "type": "Element",
                        },
                    )
                    exclude_alliance_pref: list[AllianceType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ExcludeAlliancePref",
                            "type": "Element",
                        },
                    )

        @dataclass
        class AlternateAirportCities:
            """
            Attributes:
                specified_location: A desired location (airport city).
                alternate_location: An alternate location (airport
                    city).
            """

            specified_location: (
                None
                | OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.SpecifiedLocation
            ) = field(
                default=None,
                metadata={
                    "name": "SpecifiedLocation",
                    "type": "Element",
                    "required": True,
                },
            )
            alternate_location: list[
                OtaAirLowFareSearchRq.TpaExtensions.AlternateAirportCities.AlternateLocation
            ] = field(
                default_factory=list,
                metadata={
                    "name": "AlternateLocation",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 5,
                },
            )

            @dataclass
            class SpecifiedLocation:
                location_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "LocationCode",
                        "type": "Attribute",
                        "pattern": r"[A-Z]*",
                    },
                )

            @dataclass
            class AlternateLocation:
                location_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "LocationCode",
                        "type": "Attribute",
                        "pattern": r"[A-Z]*",
                    },
                )

        @dataclass
        class AlternateAirportMileage:
            """
            Attributes:
                number: Maximum allowed number of miles from desired
                    airport.
            """

            number: None | str = field(
                default=None,
                metadata={
                    "name": "Number",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class OriginDestinationInformation(OriginDestinationInformationType):
        """
        Attributes:
            tpa_extensions: Additional elements and attributes to be
                included if required, per Trading Partner Agreement
                (TPA).
            rph: A placeholder for OriginDestinationInformation to be
                referenced wihin the OTA_AirLowFareSearchRS message.
                PricedItineraryType carries the reference to this RPH.
            fixed: OriginDestination node with flight and fare
                information fixed. Used in context shopping
            full_diversity: Request for full diversity of flights for
                the particular OriginDestination node. Used in Exchange
                Context Shopping
        """

        tpa_extensions: (
            None
            | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions
        ) = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
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
        fixed: bool = field(
            default=False,
            metadata={
                "name": "Fixed",
                "type": "Attribute",
            },
        )
        full_diversity: bool = field(
            default=False,
            metadata={
                "name": "FullDiversity",
                "type": "Attribute",
            },
        )

        @dataclass
        class TpaExtensions:
            """
            Attributes:
                flight:
                routing:
                date_flexibility: The number of alternate days around
                    the travel date to search.
                sister_destination_location: List of alternate
                    destination cities to search
                sister_destination_mileage:
                sister_origin_location: List of alternate origin cities
                    to search
                sister_origin_mileage:
                segment_type:
                alternate_time: Maximum time difference/deviation
                    allowed.
                max_one_way_options: Maximum number of options to
                    return.
                num_one_way_options: Number of options for requested
                    date.
                cabin_pref: Defines preferred cabin to be used in a
                    search for this leg level (if SegmentType is "O") or
                    segment (if SegmentType is "X"). The cabin type
                    specified in this element will override the cabin
                    type specified at the request level for this
                    leg/segment. If a cabin type is not specified for
                    this element the cabin type at request level will be
                    used as default for this leg or segment. If the
                    cabin type is not specified at both the leg/segment
                    level and request level a default cabin of "Economy"
                    will be used?
                connection_time: Connection time between segments.
                total_travel_time: Total travel time settings
                include_vendor_pref:
                include_alliance_pref: Consider only these alliances.
                departure_days:
            """

            flight: list[OriginDestinationFlightType] = field(
                default_factory=list,
                metadata={
                    "name": "Flight",
                    "type": "Element",
                },
            )
            routing: list[RoutingDefinitionType] = field(
                default_factory=list,
                metadata={
                    "name": "Routing",
                    "type": "Element",
                },
            )
            date_flexibility: list[
                OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.DateFlexibility
            ] = field(
                default_factory=list,
                metadata={
                    "name": "DateFlexibility",
                    "type": "Element",
                    "max_occurs": 2,
                },
            )
            sister_destination_location: list[RequestLocationType] = field(
                default_factory=list,
                metadata={
                    "name": "SisterDestinationLocation",
                    "type": "Element",
                },
            )
            sister_destination_mileage: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterDestinationMileage
            ) = field(
                default=None,
                metadata={
                    "name": "SisterDestinationMileage",
                    "type": "Element",
                },
            )
            sister_origin_location: list[RequestLocationType] = field(
                default_factory=list,
                metadata={
                    "name": "SisterOriginLocation",
                    "type": "Element",
                },
            )
            sister_origin_mileage: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SisterOriginMileage
            ) = field(
                default=None,
                metadata={
                    "name": "SisterOriginMileage",
                    "type": "Element",
                },
            )
            segment_type: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.SegmentType
            ) = field(
                default=None,
                metadata={
                    "name": "SegmentType",
                    "type": "Element",
                },
            )
            alternate_time: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.AlternateTime
            ) = field(
                default=None,
                metadata={
                    "name": "AlternateTime",
                    "type": "Element",
                },
            )
            max_one_way_options: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.MaxOneWayOptions
            ) = field(
                default=None,
                metadata={
                    "name": "MaxOneWayOptions",
                    "type": "Element",
                },
            )
            num_one_way_options: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.NumOneWayOptions
            ) = field(
                default=None,
                metadata={
                    "name": "NumOneWayOptions",
                    "type": "Element",
                },
            )
            cabin_pref: None | CabinPrefType = field(
                default=None,
                metadata={
                    "name": "CabinPref",
                    "type": "Element",
                },
            )
            connection_time: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.ConnectionTime
            ) = field(
                default=None,
                metadata={
                    "name": "ConnectionTime",
                    "type": "Element",
                },
            )
            total_travel_time: (
                None
                | OtaAirLowFareSearchRq.OriginDestinationInformation.TpaExtensions.TotalTravelTime
            ) = field(
                default=None,
                metadata={
                    "name": "TotalTravelTime",
                    "type": "Element",
                },
            )
            include_vendor_pref: list[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeVendorPref",
                    "type": "Element",
                },
            )
            include_alliance_pref: list[AllianceType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeAlliancePref",
                    "type": "Element",
                },
            )
            departure_days: None | DepartureDaysType = field(
                default=None,
                metadata={
                    "name": "DepartureDays",
                    "type": "Element",
                },
            )

            @dataclass
            class DateFlexibility:
                """
                Attributes:
                    nbr_of_days: Number of alternate dates before and
                        after requested travel date.
                    plus: Number of alternate dates before requested
                        travel date.
                    minus: Number of alternate dates after requested
                        travel date.
                    validate_value: Flag telling if dates within the
                        specified range should be processed in the
                        validate path.
                """

                nbr_of_days: None | int = field(
                    default=None,
                    metadata={
                        "name": "NbrOfDays",
                        "type": "Attribute",
                    },
                )
                plus: None | int = field(
                    default=None,
                    metadata={
                        "name": "Plus",
                        "type": "Attribute",
                    },
                )
                minus: None | int = field(
                    default=None,
                    metadata={
                        "name": "Minus",
                        "type": "Attribute",
                    },
                )
                validate_value: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Validate",
                        "type": "Attribute",
                    },
                )

            @dataclass
            class SisterDestinationMileage:
                number: None | int = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class SisterOriginMileage:
                number: None | int = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class SegmentType:
                """
                Attributes:
                    code: "Code" can be "ARUNK", "O" for normal, or "X"
                        for connection.
                """

                code: None | SegmentTypeCode = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                    },
                )

            @dataclass
            class AlternateTime:
                """
                Attributes:
                    plus_minus: Maximum time difference between actual
                        and desired time.
                    plus: Maximum number of hours after desired time.
                    minus: Maximum number of hours before desired time.
                """

                plus_minus: None | int = field(
                    default=None,
                    metadata={
                        "name": "PlusMinus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 9,
                    },
                )
                plus: None | int = field(
                    default=None,
                    metadata={
                        "name": "Plus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 9,
                    },
                )
                minus: None | int = field(
                    default=None,
                    metadata={
                        "name": "Minus",
                        "type": "Attribute",
                        "min_inclusive": 0,
                        "max_inclusive": 72,
                    },
                )

            @dataclass
            class MaxOneWayOptions:
                value: None | int = field(
                    default=None,
                    metadata={
                        "name": "Value",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class NumOneWayOptions:
                number: None | int = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class ConnectionTime:
                """
                Attributes:
                    min:
                    max:
                    excluded_connection_begin: Excluded connection time
                        begin in format HHMM
                    excluded_connection_end: Excluded connection time
                        end in format HHMM
                    enable_excluded_connection: Enable excluded
                        connection time (default: true)
                """

                min: None | int = field(
                    default=None,
                    metadata={
                        "name": "Min",
                        "type": "Attribute",
                    },
                )
                max: None | int = field(
                    default=None,
                    metadata={
                        "name": "Max",
                        "type": "Attribute",
                    },
                )
                excluded_connection_begin: None | str = field(
                    default=None,
                    metadata={
                        "name": "ExcludedConnectionBegin",
                        "type": "Attribute",
                        "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                    },
                )
                excluded_connection_end: None | str = field(
                    default=None,
                    metadata={
                        "name": "ExcludedConnectionEnd",
                        "type": "Attribute",
                        "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                    },
                )
                enable_excluded_connection: None | bool = field(
                    default=None,
                    metadata={
                        "name": "EnableExcludedConnection",
                        "type": "Attribute",
                    },
                )

            @dataclass
            class TotalTravelTime:
                min: None | int = field(
                    default=None,
                    metadata={
                        "name": "Min",
                        "type": "Attribute",
                    },
                )
                max: None | int = field(
                    default=None,
                    metadata={
                        "name": "Max",
                        "type": "Attribute",
                    },
                )

    @dataclass
    class Leg:
        """
        Attributes:
            departure_date_time:
            arrival_date_time:
            origins:
            destinations:
            connection_locations: Travel Connection Location - for
                example, air uses the IATA 3 letter code.
            carriers: Carrier preferrence information
            cabin: Defines preferred cabin to be used in a search for
                this leg level.
            rph: A placeholder for OriginDestinationInformation to be
                referenced wihin the OTA_AirLowFareSearchRS message.
                PricedItineraryType carries the reference to this RPH.
            max_options: Maximum number of options to return.
        """

        departure_date_time: (
            None | OtaAirLowFareSearchRq.Leg.DepartureDateTime
        ) = field(
            default=None,
            metadata={
                "name": "DepartureDateTime",
                "type": "Element",
            },
        )
        arrival_date_time: None | GlobalDateTimeType = field(
            default=None,
            metadata={
                "name": "ArrivalDateTime",
                "type": "Element",
            },
        )
        origins: None | OtaAirLowFareSearchRq.Leg.Origins = field(
            default=None,
            metadata={
                "name": "Origins",
                "type": "Element",
                "required": True,
            },
        )
        destinations: None | OtaAirLowFareSearchRq.Leg.Destinations = field(
            default=None,
            metadata={
                "name": "Destinations",
                "type": "Element",
                "required": True,
            },
        )
        connection_locations: None | ConnectionType = field(
            default=None,
            metadata={
                "name": "ConnectionLocations",
                "type": "Element",
            },
        )
        carriers: None | OtaAirLowFareSearchRq.Leg.Carriers = field(
            default=None,
            metadata={
                "name": "Carriers",
                "type": "Element",
            },
        )
        cabin: None | OtaAirLowFareSearchRq.Leg.Cabin = field(
            default=None,
            metadata={
                "name": "Cabin",
                "type": "Element",
            },
        )
        rph: None | str = field(
            default=None,
            metadata={
                "name": "RPH",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{1,8}",
            },
        )
        max_options: None | int = field(
            default=None,
            metadata={
                "name": "MaxOptions",
                "type": "Attribute",
            },
        )

        @dataclass
        class Origins:
            origin: list[OtaAirLowFareSearchRq.Leg.Origins.Origin] = field(
                default_factory=list,
                metadata={
                    "name": "Origin",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Origin:
                """
                Attributes:
                    airport_code: Required unless AirportsGroup is
                        specified. Cannot appear with AirportsGroup.
                    airports_group: Name of the airports group
                """

                airport_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "AirportCode",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 8,
                    },
                )
                airports_group: None | str = field(
                    default=None,
                    metadata={
                        "name": "AirportsGroup",
                        "type": "Attribute",
                    },
                )

        @dataclass
        class Destinations:
            destination: list[
                OtaAirLowFareSearchRq.Leg.Destinations.Destination
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Destination",
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

            @dataclass
            class Destination:
                """
                Attributes:
                    airport_code: Required unless AirportsGroup is
                        specified. Cannot appear with AirportsGroup.
                    airports_group: Name of the airports group
                """

                airport_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "AirportCode",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 8,
                    },
                )
                airports_group: None | str = field(
                    default=None,
                    metadata={
                        "name": "AirportsGroup",
                        "type": "Attribute",
                    },
                )

        @dataclass
        class Carriers:
            """
            Attributes:
                include_vendor_pref:
                exclude_vendor_pref: Do not consider these carriers for
                    this leg.
            """

            include_vendor_pref: list[IncludeVendorPrefType] = field(
                default_factory=list,
                metadata={
                    "name": "IncludeVendorPref",
                    "type": "Element",
                },
            )
            exclude_vendor_pref: list[
                OtaAirLowFareSearchRq.Leg.Carriers.ExcludeVendorPref
            ] = field(
                default_factory=list,
                metadata={
                    "name": "ExcludeVendorPref",
                    "type": "Element",
                },
            )

            @dataclass
            class ExcludeVendorPref:
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

        @dataclass
        class Cabin:
            """
            Attributes:
                preference_level:
                type_value: Specifies cabin type.
            """

            preference_level: PreferLevelType = field(
                default=PreferLevelType.PREFERRED,
                metadata={
                    "name": "PreferenceLevel",
                    "type": "Attribute",
                },
            )
            type_value: None | CabinType = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                },
            )

        @dataclass
        class DepartureDateTime(GlobalDateTimeType):
            """
            Attributes:
                week_days: Specify which days of week  to consider for
                    departure. Value format: First letter of the name of
                    the day or '_', eg. 'SMT___S' means we are
                    interested in departing at Saturday, Sunday, Monday
                    or Tuesday. Even if there are schedules for
                    Wednesday, Thursday or Friday, they won't be
                    returned in ISell response.
            """

            week_days: None | str = field(
                default=None,
                metadata={
                    "name": "WeekDays",
                    "type": "Attribute",
                    "length": 7,
                },
            )
