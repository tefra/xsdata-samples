from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.air_itinerary_pricing_info_type import (
    AirItineraryPricingInfoType,
)
from sabre.models.air_itinerary_type import AirItineraryType
from sabre.models.free_text_type import FreeTextType
from sabre.models.ticketing_info_rs_type import TicketingInfoRsType
from sabre.models.tickets_pricing_type import TicketsPricingType
from sabre.models.unflown_price_type import UnflownPriceType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class PricedItineraryType:
    """
    Itinerary with pricing information.

    Attributes:
        air_itinerary: Specifies the origin and destination of the
            traveler.
        air_itinerary_pricing_info: Pricing Information for an Air
            Itinerary.
        notes: Provides for free form descriptive information for the
            priced itinerary.
        ticketing_info: Container for TicketingInfoRS_Type.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        is_from_custom_path: Indicates if itin come from custom
            carrier/routing path.
        sequence_number: Assigns a number to priced itineraries.
        origin_destination_rph: When a PricedItinerary element contains
            flights and pricing information for a single
            OriginDestinationPair from the OTA_LowFareSearchRQ message,
            this RPH attribute identifies that OriginDestinationPair
            from the RQ. When the PricedItinerary contains flights and
            pricing information for all OriginDestinationPairs from the
            OTA_LowFareSearchRQ message, this attribute should not be
            included.
        campaign_id: Program/campaign ID, which the downline clients
            need to determine which marketing text to display.
        alternate_airport: Alternate airport itineraries indicator
        multiple_tickets: Indicates that itinerary should be sold on
            multiple separate tickets
    """

    air_itinerary: None | AirItineraryType = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    air_itinerary_pricing_info: list[
        PricedItineraryType.AirItineraryPricingInfo
    ] = field(
        default_factory=list,
        metadata={
            "name": "AirItineraryPricingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
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
    tpa_extensions: None | PricedItineraryType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    is_from_custom_path: None | bool = field(
        default=None,
        metadata={
            "name": "isFromCustomPath",
            "type": "Attribute",
        },
    )
    sequence_number: None | int = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    origin_destination_rph: None | str = field(
        default=None,
        metadata={
            "name": "OriginDestinationRPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        },
    )
    campaign_id: None | str = field(
        default=None,
        metadata={
            "name": "CampaignID",
            "type": "Attribute",
        },
    )
    alternate_airport: None | bool = field(
        default=None,
        metadata={
            "name": "AlternateAirport",
            "type": "Attribute",
        },
    )
    multiple_tickets: None | bool = field(
        default=None,
        metadata={
            "name": "MultipleTickets",
            "type": "Attribute",
        },
    )

    @dataclass
    class AirItineraryPricingInfo(AirItineraryPricingInfoType):
        """
        Attributes:
            tickets: Pricing information for multiple separate tickets
        """

        tickets: None | TicketsPricingType = field(
            default=None,
            metadata={
                "name": "Tickets",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            additional_fares:
            ops: Populated if an Ops rule has been hit.
            itin_source: The source of the itinerary
            value_bucket: Additional information for Value Bucket
                sorting
            validating_carrier: Issuing airline whose numeric airline
                code is reflected in the electronic transaction for the
                flight/value coupon(s).The Validating Carrier shall be
                the controlling and authorising entity for Electronic
                Ticketing transactions..
            unflown_price: Sum of
                AirItineraryPricingInfo/TPA_Extensions/UnflownPrice
            diversity_swapper:
            failed: Information on problems that occurred while
                processing this itinerary.
        """

        additional_fares: list[
            PricedItineraryType.TpaExtensions.AdditionalFares
        ] = field(
            default_factory=list,
            metadata={
                "name": "AdditionalFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        ops: None | PricedItineraryType.TpaExtensions.Ops = field(
            default=None,
            metadata={
                "name": "Ops",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        itin_source: None | PricedItineraryType.TpaExtensions.ItinSource = (
            field(
                default=None,
                metadata={
                    "name": "ItinSource",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        value_bucket: None | PricedItineraryType.TpaExtensions.ValueBucket = (
            field(
                default=None,
                metadata={
                    "name": "ValueBucket",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        validating_carrier: (
            None | PricedItineraryType.TpaExtensions.ValidatingCarrier
        ) = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        unflown_price: None | UnflownPriceType = field(
            default=None,
            metadata={
                "name": "UnflownPrice",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        diversity_swapper: (
            None | PricedItineraryType.TpaExtensions.DiversitySwapper
        ) = field(
            default=None,
            metadata={
                "name": "DiversitySwapper",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        failed: None | PricedItineraryType.TpaExtensions.Failed = field(
            default=None,
            metadata={
                "name": "Failed",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class AdditionalFares:
            """
            Attributes:
                air_itinerary_pricing_info: Pricing Information for an
                    Air Itinerary.
                notes: Provides for free form descriptive information
                    for the priced itinerary.
                ticketing_info: Information about ticketing (including
                    eTicketNumber).
                multiple_tickets: Indicates that itinerary should be
                    sold on multiple separate tickets
            """

            air_itinerary_pricing_info: (
                None
                | PricedItineraryType.TpaExtensions.AdditionalFares.AirItineraryPricingInfo
            ) = field(
                default=None,
                metadata={
                    "name": "AirItineraryPricingInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
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
            multiple_tickets: None | bool = field(
                default=None,
                metadata={
                    "name": "MultipleTickets",
                    "type": "Attribute",
                },
            )

            @dataclass
            class AirItineraryPricingInfo(AirItineraryPricingInfoType):
                """
                Attributes:
                    tickets: Pricing information for multiple separate
                        tickets
                """

                tickets: None | TicketsPricingType = field(
                    default=None,
                    metadata={
                        "name": "Tickets",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )

        @dataclass
        class Ops:
            """
            Attributes:
                fare_types:
                action_code: Corresponds to data in the Ops rule (action
                    target: Ops Action). The numeric id corresponds to
                    an action performed by Travelocity.
            """

            fare_types: (
                None | PricedItineraryType.TpaExtensions.Ops.FareTypes
            ) = field(
                default=None,
                metadata={
                    "name": "FareTypes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            action_code: None | int = field(
                default=None,
                metadata={
                    "name": "ActionCode",
                    "type": "Attribute",
                    "required": True,
                },
            )

            @dataclass
            class FareTypes:
                fare_type: list[
                    PricedItineraryType.TpaExtensions.Ops.FareTypes.FareType
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareType",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 1,
                    },
                )

                @dataclass
                class FareType:
                    code: None | str = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Z]{1,3}",
                        },
                    )

        @dataclass
        class ItinSource:
            """
            Attributes:
                source: The name of the source.
            """

            source: None | str = field(
                default=None,
                metadata={
                    "name": "Source",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class ValueBucket:
            """
            Attributes:
                price_time_value_rank: Price Time Value rank.
                value_bucket_number: Price Time Value Bucket number.
            """

            price_time_value_rank: None | float = field(
                default=None,
                metadata={
                    "name": "PriceTimeValueRank",
                    "type": "Attribute",
                },
            )
            value_bucket_number: None | int = field(
                default=None,
                metadata={
                    "name": "ValueBucketNumber",
                    "type": "Attribute",
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
                    "pattern": r"[A-Z][0-9A-Z]|[0-9A-Z][A-Z][0-9A-Z]?|[A-Za-z]{0}",
                },
            )

        @dataclass
        class DiversitySwapper:
            """
            Attributes:
                weighed_price_amount: (Penalty * price / 10) -- by which
                    itins are sorted in Diversity Swapper
            """

            weighed_price_amount: None | float = field(
                default=None,
                metadata={
                    "name": "WeighedPriceAmount",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class Failed:
            """
            Attributes:
                minimum_connect_time: Indicates that the itinerary does
                    not fullfill the Minimum Connect Time requirement.
                    It cannot be sold.
            """

            minimum_connect_time: None | bool = field(
                default=None,
                metadata={
                    "name": "MinimumConnectTime",
                    "type": "Attribute",
                },
            )
