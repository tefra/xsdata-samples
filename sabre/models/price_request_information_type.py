from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from sabre.models.apply_resident_discount_type import ApplyResidentDiscountType
from sabre.models.company_name_type import CompanyNameType
from sabre.models.customer_type_value import CustomerTypeValue
from sabre.models.passenger_status_type import PassengerStatusType
from sabre.models.point_of_sale_override_type import PointOfSaleOverrideType
from sabre.models.point_of_ticketing_override_type import (
    PointOfTicketingOverrideType,
)
from sabre.models.request_pricing_source_type import RequestPricingSourceType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class PriceRequestInformationType:
    """
    Identify pricing source, if negotiated fares are requested and if it is
    a reprice request.

    Attributes:
        negotiated_fare_code:
        account_code:
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        fare_qualifier: Fare Type is specific to a specific fare and
            this is a request for a set of fares based on these
            qualifiers.
        negotiated_fares_only: If set to true then returned fares need
            to match requested AcccountCode/CorpID on all fare
            components
        currency_code: Type of funds preferred for reviewing monetary
            values, in ISO 4217 codes.
        pricing_source: It can be used to indicate whether the fare is
            public or private.
        reprice:
        process_thru_fares_only: Activates processing of thru fares
            only.
        purchase_date: Specify purchase date. Fares returned will be
            based on the purchase date.
        purchase_time: Specify purchase time. Fares returned will be
            based on the purchase time.
        net_fares_used: Set to true when exchange ticket uses net fare.
    """

    negotiated_fare_code: list[
        PriceRequestInformationType.NegotiatedFareCode
    ] = field(
        default_factory=list,
        metadata={
            "name": "NegotiatedFareCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    account_code: list[PriceRequestInformationType.AccountCode] = field(
        default_factory=list,
        metadata={
            "name": "AccountCode",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | PriceRequestInformationType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_qualifier: None | str | bool = field(
        default=None,
        metadata={
            "name": "FareQualifier",
            "type": "Attribute",
        },
    )
    negotiated_fares_only: None | bool = field(
        default=None,
        metadata={
            "name": "NegotiatedFaresOnly",
            "type": "Attribute",
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        },
    )
    pricing_source: None | RequestPricingSourceType = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
        },
    )
    reprice: None | bool = field(
        default=None,
        metadata={
            "name": "Reprice",
            "type": "Attribute",
        },
    )
    process_thru_fares_only: None | bool = field(
        default=None,
        metadata={
            "name": "ProcessThruFaresOnly",
            "type": "Attribute",
        },
    )
    purchase_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "PurchaseDate",
            "type": "Attribute",
        },
    )
    purchase_time: None | str = field(
        default=None,
        metadata={
            "name": "PurchaseTime",
            "type": "Attribute",
        },
    )
    net_fares_used: None | bool = field(
        default=None,
        metadata={
            "name": "NetFaresUsed",
            "type": "Attribute",
        },
    )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            public_fare: This element finds only public fares.
            private_fare: This element finds only private fares.
            iatafare: This element finds only IATA fares.
            web_fare:
            priority: This element governs how flights are returned. A
                user can uses a priority of 1-4 to make this
                determination.
            indicators: This element restricts fares which can be
                returned in response. If a customer passes this element,
                all its children should be specified.
            promo_id: Promotional Identifier - a string which identifies
                a promotion, possibly giving a discount prices etc.
            customer_type:
            multiple_traveler_groups: This element governs how flights
                are returned when multiple passenger groups are
                requested.
            branded_fare_indicators:
            passenger_status:
            point_of_sale_override: Will return the fares available for
                specified point of sale and priced in this point of sale
                currency. Currency is overriden by
                PriceRequestInformation@CurrencyCode.
            point_of_ticketing_override:
            apply_resident_discount: Apply resident discount in CLFE
            eticketable_override:
            currency:
            use_reduced_constructions: Use reduced constructions (simple
                fare paths with restrictions on the number of fare
                components).
            obfees:
            fare_breaks_at_legs: Force fare breaks at leg points if
                split taxes by leg requested. By default set to true.
            fare_adjustment: Capability to specify Plus-Up and Discount
                Amount and Percentage.
        """

        public_fare: (
            None | PriceRequestInformationType.TpaExtensions.PublicFare
        ) = field(
            default=None,
            metadata={
                "name": "PublicFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        private_fare: (
            None | PriceRequestInformationType.TpaExtensions.PrivateFare
        ) = field(
            default=None,
            metadata={
                "name": "PrivateFare",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        iatafare: None | PriceRequestInformationType.TpaExtensions.Iatafare = (
            field(
                default=None,
                metadata={
                    "name": "IATAFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        web_fare: None | PriceRequestInformationType.TpaExtensions.WebFare = (
            field(
                default=None,
                metadata={
                    "name": "WebFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        priority: None | PriceRequestInformationType.TpaExtensions.Priority = (
            field(
                default=None,
                metadata={
                    "name": "Priority",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        indicators: (
            None | PriceRequestInformationType.TpaExtensions.Indicators
        ) = field(
            default=None,
            metadata={
                "name": "Indicators",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        promo_id: None | str = field(
            default=None,
            metadata={
                "name": "PromoID",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        customer_type: (
            None | PriceRequestInformationType.TpaExtensions.CustomerType
        ) = field(
            default=None,
            metadata={
                "name": "CustomerType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        multiple_traveler_groups: (
            None
            | PriceRequestInformationType.TpaExtensions.MultipleTravelerGroups
        ) = field(
            default=None,
            metadata={
                "name": "MultipleTravelerGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        branded_fare_indicators: (
            None
            | PriceRequestInformationType.TpaExtensions.BrandedFareIndicators
        ) = field(
            default=None,
            metadata={
                "name": "BrandedFareIndicators",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        passenger_status: (
            None | PriceRequestInformationType.TpaExtensions.PassengerStatus
        ) = field(
            default=None,
            metadata={
                "name": "PassengerStatus",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        point_of_sale_override: None | PointOfSaleOverrideType = field(
            default=None,
            metadata={
                "name": "PointOfSaleOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        point_of_ticketing_override: None | PointOfTicketingOverrideType = (
            field(
                default=None,
                metadata={
                    "name": "PointOfTicketingOverride",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        apply_resident_discount: None | ApplyResidentDiscountType = field(
            default=None,
            metadata={
                "name": "ApplyResidentDiscount",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        eticketable_override: (
            None
            | PriceRequestInformationType.TpaExtensions.EticketableOverride
        ) = field(
            default=None,
            metadata={
                "name": "ETicketableOverride",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        currency: None | PriceRequestInformationType.TpaExtensions.Currency = (
            field(
                default=None,
                metadata={
                    "name": "Currency",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        use_reduced_constructions: (
            None
            | PriceRequestInformationType.TpaExtensions.UseReducedConstructions
        ) = field(
            default=None,
            metadata={
                "name": "UseReducedConstructions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        obfees: None | PriceRequestInformationType.TpaExtensions.Obfees = (
            field(
                default=None,
                metadata={
                    "name": "OBFees",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        fare_breaks_at_legs: (
            None | PriceRequestInformationType.TpaExtensions.FareBreaksAtLegs
        ) = field(
            default=None,
            metadata={
                "name": "FareBreaksAtLegs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_adjustment: (
            None | PriceRequestInformationType.TpaExtensions.FareAdjustment
        ) = field(
            default=None,
            metadata={
                "name": "FareAdjustment",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class PublicFare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class PrivateFare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class Iatafare:
            ind: bool = field(
                default=False,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class WebFare:
            """
            Attributes:
                ind: Web fare
            """

            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class Priority:
            price: (
                None | PriceRequestInformationType.TpaExtensions.Priority.Price
            ) = field(
                default=None,
                metadata={
                    "name": "Price",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )
            direct_flights: (
                None
                | PriceRequestInformationType.TpaExtensions.Priority.DirectFlights
            ) = field(
                default=None,
                metadata={
                    "name": "DirectFlights",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )
            time: (
                None | PriceRequestInformationType.TpaExtensions.Priority.Time
            ) = field(
                default=None,
                metadata={
                    "name": "Time",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )
            vendor: (
                None
                | PriceRequestInformationType.TpaExtensions.Priority.Vendor
            ) = field(
                default=None,
                metadata={
                    "name": "Vendor",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )

            @dataclass
            class Price:
                priority: None | int = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    },
                )

            @dataclass
            class DirectFlights:
                priority: None | int = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    },
                )

            @dataclass
            class Time:
                priority: None | int = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    },
                )

            @dataclass
            class Vendor:
                priority: None | int = field(
                    default=None,
                    metadata={
                        "name": "Priority",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "max_inclusive": 4,
                    },
                )

        @dataclass
        class Indicators:
            """
            Attributes:
                retain_fare: Currently must be set to true.
                min_max_stay: If set to true, fares that have a min/max
                    stay can be included in the responses. If set to
                    false, then no fares that include a min/max stay
                    requirement will be included in the response.
                refund_penalty: If set to true, fares that have a refund
                    penalty can be included in the responses. If set to
                    false, then no fares that include a refund penalty
                    requirement will be included in the response.
                res_ticketing: If set to true, fares that have a
                    reservation/ticketing can be included in the
                    responses. If set to false, then no fares that
                    include reservation/ticketing requirement will be
                    included in the response.
                travel_policy: This element is currently ignored whether
                    it is true or false.
            """

            retain_fare: (
                None
                | PriceRequestInformationType.TpaExtensions.Indicators.RetainFare
            ) = field(
                default=None,
                metadata={
                    "name": "RetainFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            min_max_stay: (
                None
                | PriceRequestInformationType.TpaExtensions.Indicators.MinMaxStay
            ) = field(
                default=None,
                metadata={
                    "name": "MinMaxStay",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            refund_penalty: (
                None
                | PriceRequestInformationType.TpaExtensions.Indicators.RefundPenalty
            ) = field(
                default=None,
                metadata={
                    "name": "RefundPenalty",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            res_ticketing: (
                None
                | PriceRequestInformationType.TpaExtensions.Indicators.ResTicketing
            ) = field(
                default=None,
                metadata={
                    "name": "ResTicketing",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            travel_policy: (
                None
                | PriceRequestInformationType.TpaExtensions.Indicators.TravelPolicy
            ) = field(
                default=None,
                metadata={
                    "name": "TravelPolicy",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )

            @dataclass
            class RetainFare:
                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class MinMaxStay:
                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class RefundPenalty:
                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class ResTicketing:
                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class TravelPolicy:
                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

        @dataclass
        class CustomerType:
            value: None | CustomerTypeValue = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MultipleTravelerGroups:
            """
            Attributes:
                itineraries_per_group: Indicates desired number of
                    itineraries to be returned in each passenger group
                    at beggining of response.
            """

            itineraries_per_group: None | int = field(
                default=None,
                metadata={
                    "name": "ItinerariesPerGroup",
                    "type": "Attribute",
                    "min_inclusive": 1,
                    "max_inclusive": 99,
                },
            )

        @dataclass
        class BrandedFareIndicators:
            """
            Attributes:
                return_cheapest_unbranded_fare:
                single_branded_fare: Return single brand option per itin
                multiple_branded_fares: Return multiple brand options
                    per itin
            """

            return_cheapest_unbranded_fare: (
                None
                | PriceRequestInformationType.TpaExtensions.BrandedFareIndicators.ReturnCheapestUnbrandedFare
            ) = field(
                default=None,
                metadata={
                    "name": "ReturnCheapestUnbrandedFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            single_branded_fare: None | bool = field(
                default=None,
                metadata={
                    "name": "SingleBrandedFare",
                    "type": "Attribute",
                },
            )
            multiple_branded_fares: None | bool = field(
                default=None,
                metadata={
                    "name": "MultipleBrandedFares",
                    "type": "Attribute",
                },
            )

            @dataclass
            class ReturnCheapestUnbrandedFare:
                """
                Attributes:
                    ind: Indicator to turn on or off return of cheapest
                        unbranded fare referred as "catch all" fare for
                        the branded carriers from the branded fares
                        service.
                """

                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

        @dataclass
        class PassengerStatus:
            state_code: None | str = field(
                default=None,
                metadata={
                    "name": "StateCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_length": 2,
                    "max_length": 8,
                },
            )
            country_code: None | str = field(
                default=None,
                metadata={
                    "name": "CountryCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "pattern": r"[a-zA-Z]{2}",
                },
            )
            city_code: None | str = field(
                default=None,
                metadata={
                    "name": "CityCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "pattern": r"[a-zA-Z]{3}",
                },
            )
            type_value: None | PassengerStatusType = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class EticketableOverride:
            """
            Attributes:
                value: ETicketable override
            """

            value: None | bool = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                },
            )

        @dataclass
        class Currency:
            """
            Attributes:
                dual: Dual currency
                moverride: M override
            """

            dual: None | str = field(
                default=None,
                metadata={
                    "name": "Dual",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                },
            )
            moverride: None | bool = field(
                default=None,
                metadata={
                    "name": "MOverride",
                    "type": "Attribute",
                },
            )

        @dataclass
        class UseReducedConstructions:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class Obfees:
            """
            Attributes:
                rtype: Indicator Returning R-Type OB Fees
                ttype: Indicator Returning T-Type OB Fees
            """

            rtype: None | bool = field(
                default=None,
                metadata={
                    "name": "RType",
                    "type": "Attribute",
                },
            )
            ttype: None | bool = field(
                default=None,
                metadata={
                    "name": "TType",
                    "type": "Attribute",
                },
            )

        @dataclass
        class FareBreaksAtLegs:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class FareAdjustment:
            """
            Attributes:
                value: Adjustment Value, can be positive or negative,
                    number or percentage
                currency: Currency of Adjustment's Value
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

    @dataclass
    class NegotiatedFareCode:
        """
        Attributes:
            code: Any code used to specify an item, for example, type of
                traveler, service code, room amenity, etc.
            code_context: Identifies the source authority for the code.
            uri: Identifies the location of the code table
            quantity: Used to define a quantity of an associated element
                or attribute.
            secondary_code: An additional attribute to allow flexibility
                for particular organizations who require an additional
                code.
            supplier_code: An additional attribute to allow flexibility
                for particular organizations who require an additional
                supplier code.
            content:
        """

        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "pattern": r"[A-Za-z]{3}[0-9]{2}",
            },
        )
        code_context: None | str = field(
            default=None,
            metadata={
                "name": "CodeContext",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 32,
            },
        )
        uri: None | str = field(
            default=None,
            metadata={
                "name": "URI",
                "type": "Attribute",
            },
        )
        quantity: None | int = field(
            default=None,
            metadata={
                "name": "Quantity",
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 999,
            },
        )
        secondary_code: None | str = field(
            default=None,
            metadata={
                "name": "SecondaryCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 16,
            },
        )
        supplier_code: None | str = field(
            default=None,
            metadata={
                "name": "SupplierCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 16,
            },
        )
        content: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
                "choices": (
                    {
                        "name": "Supplier",
                        "type": CompanyNameType,
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                    {
                        "name": "TPA_Extensions",
                        "type": str,
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                ),
            },
        )

    @dataclass
    class AccountCode:
        code: None | str = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 20,
            },
        )
