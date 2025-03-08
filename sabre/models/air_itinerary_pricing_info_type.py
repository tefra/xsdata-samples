from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlTime

from sabre.models.air_itinerary_pricing_info_type_reissue_exchange import (
    AirItineraryPricingInfoTypeReissueExchange,
)
from sabre.models.air_itinerary_pricing_info_type_spanish_family_discount_indicator import (
    AirItineraryPricingInfoTypeSpanishFamilyDiscountIndicator,
)
from sabre.models.company_name_type import CompanyNameType
from sabre.models.itin_total_fare_type import ItinTotalFareType
from sabre.models.ocfee_type import OcfeeType
from sabre.models.ptcfare_breakdown_type import PtcfareBreakdownType
from sabre.models.response_location_type import ResponseLocationType
from sabre.models.rule_info_type import RuleInfoType
from sabre.models.unflown_price_type import UnflownPriceType
from sabre.models.validating_carrier_info_type import ValidatingCarrierInfoType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AirItineraryPricingInfoType:
    """
    Pricing Information for an Air Itinerary.

    Attributes:
        itin_total_fare: Total price of the itinerary
        ptc_fare_breakdowns: This is a collection of PTC Fare Breakdowns
        fare_infos: This is a collection of FareInfo
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        pricing_source: Used to indicate whether the pricing is public
            or private
        pricing_sub_source: Pricing sub source.
        pseudo_city_code: (MultiPCC) Information about Pseudo City Code
            for wich the fare was produced.
        brand_id: Used to indicate brand code (e.g. SS for SuperSaver)
            or type of Fare (e.g. Sale Fare or Full Coach and so on...)
        fare_returned: Boolean to indicate if a fare returned for the
            BrandID or not (true if fare is returned and false if no
            fare returned)
        fare_status: Detailed reason why fare could not be returned
            (when FareReturned="false"). "A" means "Class is not
            available", "O" - "Class is not offered", "F" - "No fare
            found or applicable".
        cached_itin: Indicates whether the itin is from Cache. If true,
            it is from Cache.
        cache_partition: Indicates source partition of cached itin
        cache_partition_priority: Indicates source partition priority of
            cached itin
        cache_version: Indicates source version of cached itin
        time_to_live: Time to live in cache (in minutes).
        alternate_city_option: Indicates that this option is alternate
            dates option.
        last_ticket_date: Last day to ticket.
        private_fare_type: Private fare type symbol.
        spanish_family_discount_indicator: Spanish Discount indicator
            with values of "A", "B", "C" where "A" indicates Spanish
            Large Family discount only "B" indicates Spanish Large
            Family discount + Spanish Islander discount "C" indicates
            Spanish Islander discount only
        flexible_fare_id: If the fare is an additional flexible fare,
            this is the fare group ID
        previous_exchange_date: Previous Exchange Date
        reissue_exchange: Indicates whether priced as Reissue or
            Exchange
        advanced_purchase_date:
        purchase_by_date:
    """

    itin_total_fare: None | ItinTotalFareType = field(
        default=None,
        metadata={
            "name": "ItinTotalFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    ptc_fare_breakdowns: (
        None | AirItineraryPricingInfoType.PtcFareBreakdowns
    ) = field(
        default=None,
        metadata={
            "name": "PTC_FareBreakdowns",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_infos: None | AirItineraryPricingInfoType.FareInfos = field(
        default=None,
        metadata={
            "name": "FareInfos",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | AirItineraryPricingInfoType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
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
    pricing_sub_source: None | str = field(
        default=None,
        metadata={
            "name": "PricingSubSource",
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"[A-Z_]{1,}",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
        },
    )
    brand_id: None | str = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
        },
    )
    fare_returned: None | bool = field(
        default=None,
        metadata={
            "name": "FareReturned",
            "type": "Attribute",
        },
    )
    fare_status: None | str = field(
        default=None,
        metadata={
            "name": "FareStatus",
            "type": "Attribute",
        },
    )
    cached_itin: bool = field(
        default=False,
        metadata={
            "name": "CachedItin",
            "type": "Attribute",
        },
    )
    cache_partition: None | str = field(
        default=None,
        metadata={
            "name": "CachePartition",
            "type": "Attribute",
        },
    )
    cache_partition_priority: None | int = field(
        default=None,
        metadata={
            "name": "CachePartitionPriority",
            "type": "Attribute",
        },
    )
    cache_version: None | str = field(
        default=None,
        metadata={
            "name": "CacheVersion",
            "type": "Attribute",
        },
    )
    time_to_live: None | int = field(
        default=None,
        metadata={
            "name": "TimeToLive",
            "type": "Attribute",
        },
    )
    alternate_city_option: bool = field(
        default=False,
        metadata={
            "name": "AlternateCityOption",
            "type": "Attribute",
        },
    )
    last_ticket_date: None | str | XmlTime = field(
        default=None,
        metadata={
            "name": "LastTicketDate",
            "type": "Attribute",
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
    spanish_family_discount_indicator: (
        None | AirItineraryPricingInfoTypeSpanishFamilyDiscountIndicator
    ) = field(
        default=None,
        metadata={
            "name": "SpanishFamilyDiscountIndicator",
            "type": "Attribute",
        },
    )
    flexible_fare_id: None | int = field(
        default=None,
        metadata={
            "name": "FlexibleFareID",
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
    reissue_exchange: None | AirItineraryPricingInfoTypeReissueExchange = (
        field(
            default=None,
            metadata={
                "name": "ReissueExchange",
                "type": "Attribute",
            },
        )
    )
    advanced_purchase_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "AdvancedPurchaseDate",
            "type": "Attribute",
        },
    )
    purchase_by_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PurchaseByDate",
            "type": "Attribute",
        },
    )

    @dataclass
    class PtcFareBreakdowns:
        ptc_fare_breakdown: list[PtcfareBreakdownType] = field(
            default_factory=list,
            metadata={
                "name": "PTC_FareBreakdown",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 20,
            },
        )

    @dataclass
    class FareInfos:
        """
        Attributes:
            fare_info: Detailed information on individual priced fares
        """

        fare_info: list[AirItineraryPricingInfoType.FareInfos.FareInfo] = (
            field(
                default_factory=list,
                metadata={
                    "name": "FareInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 10,
                },
            )
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
                None
                | AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions
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
                    | AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining
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
                    | AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Cabin
                ) = field(
                    default=None,
                    metadata={
                        "name": "Cabin",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                fare_note: list[
                    AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.FareNote
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
                    | AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Meal
                ) = field(
                    default=None,
                    metadata={
                        "name": "Meal",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                rule: list[
                    AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Rule
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

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            divide_in_party: Indicates if different passenger types are
                booked in different inventories.
            promo_offer: Promotional offer
            fare_note:
            promo_redemption: Populated if  "Coupon Redemption" rule has
                been hit. This had been developed for Travelocity but
                never used.
            rule: Describes a rule that was hit.
            multiple_traveler_groups:
            ancillary_fee_groups: Ancillary fee groups returned
            legs: This is a collection of Leg Information
            unflown_price:
            validating_carrier:
        """

        divide_in_party: (
            None | AirItineraryPricingInfoType.TpaExtensions.DivideInParty
        ) = field(
            default=None,
            metadata={
                "name": "DivideInParty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        promo_offer: (
            None | AirItineraryPricingInfoType.TpaExtensions.PromoOffer
        ) = field(
            default=None,
            metadata={
                "name": "PromoOffer",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_note: list[AirItineraryPricingInfoType.TpaExtensions.FareNote] = (
            field(
                default_factory=list,
                metadata={
                    "name": "FareNote",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        promo_redemption: (
            None | AirItineraryPricingInfoType.TpaExtensions.PromoRedemption
        ) = field(
            default=None,
            metadata={
                "name": "PromoRedemption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        rule: list[AirItineraryPricingInfoType.TpaExtensions.Rule] = field(
            default_factory=list,
            metadata={
                "name": "Rule",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        multiple_traveler_groups: (
            None
            | AirItineraryPricingInfoType.TpaExtensions.MultipleTravelerGroups
        ) = field(
            default=None,
            metadata={
                "name": "MultipleTravelerGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        ancillary_fee_groups: (
            None | AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups
        ) = field(
            default=None,
            metadata={
                "name": "AncillaryFeeGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        legs: None | AirItineraryPricingInfoType.TpaExtensions.Legs = field(
            default=None,
            metadata={
                "name": "Legs",
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
        validating_carrier: list[ValidatingCarrierInfoType] = field(
            default_factory=list,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class DivideInParty:
            indicator: None | bool = field(
                default=None,
                metadata={
                    "name": "Indicator",
                    "type": "Attribute",
                },
            )

        @dataclass
        class PromoOffer:
            """
            Attributes:
                promo_id: Promotional offer identifier
                corp_id: Airline identifier.
                content_id: This information comes from Fare Notes Rule
                    fired and is taken by Travelocity to look up
                    detailed data on their database to put on the
                    website.
            """

            promo_id: None | str = field(
                default=None,
                metadata={
                    "name": "PromoID",
                    "type": "Attribute",
                },
            )
            corp_id: None | str = field(
                default=None,
                metadata={
                    "name": "CorpID",
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
        class FareNote:
            """
            Attributes:
                fare_type_name: Corresponds to data in the Fare Note
                    rule (action target: Fare Type). For example:
                    "PROMOTIONAL"
                priority_level: FareNote Itin priority
                content_id: Corresponds to data in the Fare Note rule
                    (action target: Content ID Action). For example:
                    "112"
            """

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
        class PromoRedemption:
            promo_id: None | str = field(
                default=None,
                metadata={
                    "name": "PromoID",
                    "type": "Attribute",
                },
            )
            eligible: None | bool = field(
                default=None,
                metadata={
                    "name": "Eligible",
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
        class Rule:
            """
            Attributes:
                type_value: Rule type. For example: "Fare Note Itin",
                    "DRE"
                id: Rule ID
            """

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

        @dataclass
        class MultipleTravelerGroups:
            group_number: None | int = field(
                default=None,
                metadata={
                    "name": "GroupNumber",
                    "type": "Attribute",
                },
            )
            primary_group: None | bool = field(
                default=None,
                metadata={
                    "name": "PrimaryGroup",
                    "type": "Attribute",
                },
            )

        @dataclass
        class AncillaryFeeGroups:
            """
            Attributes:
                ancillary_fee_group: Ancillary fee group returned
                message: Arbitrary message returned from MIP
            """

            ancillary_fee_group: list[
                AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups.AncillaryFeeGroup
            ] = field(
                default_factory=list,
                metadata={
                    "name": "AncillaryFeeGroup",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            message: None | object = field(
                default=None,
                metadata={
                    "name": "Message",
                    "type": "Attribute",
                },
            )

            @dataclass
            class AncillaryFeeGroup:
                """
                Attributes:
                    ancillary_fee_item: OC Fee returned
                    code: Group code
                    name: Group name
                    message: Arbitrary message returned from MIP
                """

                ancillary_fee_item: list[OcfeeType] = field(
                    default_factory=list,
                    metadata={
                        "name": "AncillaryFeeItem",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                code: None | object = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                    },
                )
                name: None | object = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Attribute",
                        "required": True,
                    },
                )
                message: None | object = field(
                    default=None,
                    metadata={
                        "name": "Message",
                        "type": "Attribute",
                    },
                )

        @dataclass
        class Legs:
            leg: list[AirItineraryPricingInfoType.TpaExtensions.Legs.Leg] = (
                field(
                    default_factory=list,
                    metadata={
                        "name": "Leg",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 1,
                    },
                )
            )

            @dataclass
            class Leg:
                """
                Attributes:
                    segment:
                    number:
                    brand_id:
                    brand_description:
                    program_name:
                    program_id:
                    program_code:
                    program_system_code:
                    fare_status: Detailed reason why fare could not be
                        returned (when FareReturned="false"). "A" means
                        "Class is not available", "O" - "Class is not
                        offered", "F" - "No fare found or applicable",
                        "N" - unknown status.
                """

                segment: list[
                    AirItineraryPricingInfoType.TpaExtensions.Legs.Leg.Segment
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "Segment",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                number: None | object = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                    },
                )
                brand_id: None | str = field(
                    default=None,
                    metadata={
                        "name": "BrandID",
                        "type": "Attribute",
                    },
                )
                brand_description: None | str = field(
                    default=None,
                    metadata={
                        "name": "BrandDescription",
                        "type": "Attribute",
                    },
                )
                program_name: None | str = field(
                    default=None,
                    metadata={
                        "name": "ProgramName",
                        "type": "Attribute",
                    },
                )
                program_id: None | str = field(
                    default=None,
                    metadata={
                        "name": "ProgramID",
                        "type": "Attribute",
                    },
                )
                program_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "ProgramCode",
                        "type": "Attribute",
                    },
                )
                program_system_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "ProgramSystemCode",
                        "type": "Attribute",
                    },
                )
                fare_status: None | str = field(
                    default=None,
                    metadata={
                        "name": "FareStatus",
                        "type": "Attribute",
                    },
                )

                @dataclass
                class Segment:
                    """
                    Attributes:
                        number: Reference to the flight segment
                        program_id:
                        program_description:
                        program_system_code:
                        brand_id:
                        brand_name: Used to indicate brand name
                        fare_status: If possible detailed reason why
                            fare could not be returned. "A" means "Class
                            is not available", "O" - "Class is not
                            offered", "F" - "No fare found or
                            applicable", "N" - unknown status.
                    """

                    number: None | int = field(
                        default=None,
                        metadata={
                            "name": "Number",
                            "type": "Attribute",
                        },
                    )
                    program_id: None | str = field(
                        default=None,
                        metadata={
                            "name": "ProgramID",
                            "type": "Attribute",
                        },
                    )
                    program_description: None | str = field(
                        default=None,
                        metadata={
                            "name": "ProgramDescription",
                            "type": "Attribute",
                        },
                    )
                    program_system_code: None | str = field(
                        default=None,
                        metadata={
                            "name": "ProgramSystemCode",
                            "type": "Attribute",
                        },
                    )
                    brand_id: None | str = field(
                        default=None,
                        metadata={
                            "name": "BrandID",
                            "type": "Attribute",
                        },
                    )
                    brand_name: None | str = field(
                        default=None,
                        metadata={
                            "name": "BrandName",
                            "type": "Attribute",
                        },
                    )
                    fare_status: None | str = field(
                        default=None,
                        metadata={
                            "name": "FareStatus",
                            "type": "Attribute",
                        },
                    )
