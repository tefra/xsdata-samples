from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sabre.models.air_fee_type import AirFeeType
from sabre.models.air_tax_type import AirTaxType
from sabre.models.baggage_information_list_type import (
    BaggageInformationListType,
)
from sabre.models.currency_amount_type import CurrencyAmountType
from sabre.models.currency_conversions_type import CurrencyConversionsType
from sabre.models.fare_component_taxes_type import FareComponentTaxesType
from sabre.models.fare_messages_type import FareMessagesType
from sabre.models.obfee_type import ObfeeType
from sabre.models.penalty_applicability import PenaltyApplicability
from sabre.models.penalty_type import PenaltyType
from sabre.models.rate_of_exchange_type import RateOfExchangeType
from sabre.models.reissue_info_type import ReissueInfoType
from sabre.models.selling_fare_data_type import SellingFareDataType
from sabre.models.surcharges_type import SurchargesType
from sabre.models.vccinformation_type import VccinformationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FareType:
    """
    Holds a base fare, tax, total and currency information on a price.

    Attributes:
        base_fare: Price of the inventory excluding taxes and fees.
        non_refundable_base_fare: Non-refundable base fare amount
        fare_construction: Fare construction total amount.
        equiv_fare: Price of the inventory excluding taxes and fees in
            the payable currency.
        taxes: This is a collection of Taxes
        fees: This is a collection of Fees
        obfees: This is a collection of ob Fees
        rate_of_exchange:
        currency_conversions:
        total_fare: The total price that the passenger would pay
            (includes fare, taxes, fees)
        reissue_info_list: Reissue information
        penalties_info: Penalties information
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        negotiated_fare: Indicator to show if this is a private fare.
        negotiated_fare_code: Code used to identify the private fare.
    """

    base_fare: CurrencyAmountType = field(
        metadata={
            "name": "BaseFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    non_refundable_base_fare: None | CurrencyAmountType = field(
        default=None,
        metadata={
            "name": "NonRefundableBaseFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_construction: None | CurrencyAmountType = field(
        default=None,
        metadata={
            "name": "FareConstruction",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    equiv_fare: None | FareType.EquivFare = field(
        default=None,
        metadata={
            "name": "EquivFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    taxes: None | FareType.Taxes = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fees: None | FareType.Fees = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    obfees: None | FareType.Obfees = field(
        default=None,
        metadata={
            "name": "OBFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    rate_of_exchange: None | RateOfExchangeType = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    currency_conversions: None | CurrencyConversionsType = field(
        default=None,
        metadata={
            "name": "CurrencyConversions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    total_fare: CurrencyAmountType = field(
        metadata={
            "name": "TotalFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    reissue_info_list: None | FareType.ReissueInfoList = field(
        default=None,
        metadata={
            "name": "ReissueInfoList",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    penalties_info: None | FareType.PenaltiesInfo = field(
        default=None,
        metadata={
            "name": "PenaltiesInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    tpa_extensions: None | FareType.TpaExtensions = field(
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

    @dataclass(kw_only=True)
    class EquivFare(CurrencyAmountType):
        """
        Attributes:
            effective_price_deviation: Effective Price Deviation
        """

        effective_price_deviation: None | Decimal = field(
            default=None,
            metadata={
                "name": "EffectivePriceDeviation",
                "type": "Attribute",
                "fraction_digits": 3,
            },
        )

    @dataclass(kw_only=True)
    class Taxes:
        """
        Attributes:
            fare_components_taxes:
            legs_taxes:
            tax: Any individual tax applied to the fare
            total_tax: Total (summary) of taxes applied to the fare
        """

        fare_components_taxes: None | FareType.Taxes.FareComponentsTaxes = (
            field(
                default=None,
                metadata={
                    "name": "FareComponentsTaxes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        legs_taxes: None | FareType.Taxes.LegsTaxes = field(
            default=None,
            metadata={
                "name": "LegsTaxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        tax: list[AirTaxType] = field(
            default_factory=list,
            metadata={
                "name": "Tax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )
        total_tax: None | CurrencyAmountType = field(
            default=None,
            metadata={
                "name": "TotalTax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class FareComponentsTaxes:
            fare_component_taxes: list[FareComponentTaxesType] = field(
                default_factory=list,
                metadata={
                    "name": "FareComponentTaxes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

        @dataclass(kw_only=True)
        class LegsTaxes:
            leg_taxes: list[FareType.Taxes.LegsTaxes.LegTaxes] = field(
                default_factory=list,
                metadata={
                    "name": "LegTaxes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class LegTaxes:
                """
                Attributes:
                    tax: Any individual tax applied to the fare
                    number:
                """

                tax: list[AirTaxType] = field(
                    default_factory=list,
                    metadata={
                        "name": "Tax",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 1,
                        "max_occurs": 99,
                    },
                )
                number: None | int = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                    },
                )

    @dataclass(kw_only=True)
    class Fees:
        """
        Attributes:
            fee: Any additional fee incurred by the passenger but not
                shown on the ticket.
        """

        fee: list[AirFeeType] = field(
            default_factory=list,
            metadata={
                "name": "Fee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 9,
            },
        )

    @dataclass(kw_only=True)
    class Obfees:
        """
        Attributes:
            obfee: OB fees
            ttype_amount: Total T-type OB Fee
        """

        obfee: list[ObfeeType] = field(
            default_factory=list,
            metadata={
                "name": "OBFee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        ttype_amount: None | Decimal = field(
            default=None,
            metadata={
                "name": "TTypeAmount",
                "type": "Attribute",
                "fraction_digits": 3,
            },
        )

    @dataclass(kw_only=True)
    class ReissueInfoList:
        """
        Attributes:
            reissue_info: Reissue Info
        """

        reissue_info: list[ReissueInfoType] = field(
            default_factory=list,
            metadata={
                "name": "ReissueInfo",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class PenaltiesInfo:
        """
        Attributes:
            penalty: Penalty Info
        """

        penalty: list[FareType.PenaltiesInfo.Penalty] = field(
            default_factory=list,
            metadata={
                "name": "Penalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Penalty:
            """
            Attributes:
                cat16_text_only: Missing Data
                type_value:
                applicability:
                refundable:
                changeable:
                conditions_apply:
                amount:
                currency_code: A currency code (e.g. USD, EUR, PLN)
                decimal_places: Indicates the number of decimal places
                    for a particular currency. This is equivalent to the
                    ISO 4217 standard "minor unit".
                cat16_info:
            """

            cat16_text_only: list[
                FareType.PenaltiesInfo.Penalty.Cat16TextOnly
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Cat16TextOnly",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            type_value: None | PenaltyType = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                },
            )
            applicability: None | PenaltyApplicability = field(
                default=None,
                metadata={
                    "name": "Applicability",
                    "type": "Attribute",
                },
            )
            refundable: None | bool = field(
                default=None,
                metadata={
                    "name": "Refundable",
                    "type": "Attribute",
                },
            )
            changeable: None | bool = field(
                default=None,
                metadata={
                    "name": "Changeable",
                    "type": "Attribute",
                },
            )
            conditions_apply: bool = field(
                default=False,
                metadata={
                    "name": "ConditionsApply",
                    "type": "Attribute",
                },
            )
            amount: None | Decimal = field(
                default=None,
                metadata={
                    "name": "Amount",
                    "type": "Attribute",
                    "fraction_digits": 3,
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
            decimal_places: None | int = field(
                default=None,
                metadata={
                    "name": "DecimalPlaces",
                    "type": "Attribute",
                },
            )
            cat16_info: bool = field(
                default=False,
                metadata={
                    "name": "Cat16Info",
                    "type": "Attribute",
                },
            )

            @dataclass(kw_only=True)
            class Cat16TextOnly:
                """
                Attributes:
                    fare_basis_code: Fare basis code
                    fare_component_id: Fare component Id
                """

                fare_basis_code: str = field(
                    metadata={
                        "name": "FareBasisCode",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "pattern": r"[A-Z0-9]+(/[A-Z0-9]+)?",
                    }
                )
                fare_component_id: int = field(
                    metadata={
                        "name": "FareComponentID",
                        "type": "Attribute",
                        "required": True,
                    }
                )

    @dataclass(kw_only=True)
    class TpaExtensions:
        """
        Attributes:
            surcharges: Surcharge information
            legs: This is a collection of Leg Information
            fare_components: A collection of additional information for
                each Fare Component
            messages:
            baggage_information_list:
            selling_fare_data_list:
            commission_data:
        """

        surcharges: list[SurchargesType] = field(
            default_factory=list,
            metadata={
                "name": "Surcharges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        legs: None | FareType.TpaExtensions.Legs = field(
            default=None,
            metadata={
                "name": "Legs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_components: None | FareType.TpaExtensions.FareComponents = field(
            default=None,
            metadata={
                "name": "FareComponents",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        messages: None | FareMessagesType = field(
            default=None,
            metadata={
                "name": "Messages",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        baggage_information_list: None | BaggageInformationListType = field(
            default=None,
            metadata={
                "name": "BaggageInformationList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        selling_fare_data_list: (
            None | FareType.TpaExtensions.SellingFareDataList
        ) = field(
            default=None,
            metadata={
                "name": "SellingFareDataList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        commission_data: None | FareType.TpaExtensions.CommissionData = field(
            default=None,
            metadata={
                "name": "CommissionData",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass(kw_only=True)
        class Legs:
            """
            Attributes:
                leg: Leg Information
            """

            leg: list[FareType.TpaExtensions.Legs.Leg] = field(
                default_factory=list,
                metadata={
                    "name": "Leg",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class Leg:
                """
                Attributes:
                    base_fare: Price of the inventory excluding taxes
                        and fees.
                    equiv_fare: Price of the inventory excluding taxes
                        and fees in the payable currency.
                    taxes: This is a collection of Taxes
                    total_fare: The total price that the passenger would
                        pay (includes fare, taxes, fees)
                    total_mileage:
                    number:
                    fare_status: Detailed reason why fare could not be
                        returned (when FareReturned="false"). "A" means
                        "Class is not available", "O" - "Class is not
                        offered", "F" - "No fare found or applicable",
                        "N" - unknown status.
                """

                base_fare: CurrencyAmountType = field(
                    metadata={
                        "name": "BaseFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                equiv_fare: (
                    None | FareType.TpaExtensions.Legs.Leg.EquivFare
                ) = field(
                    default=None,
                    metadata={
                        "name": "EquivFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                taxes: None | FareType.TpaExtensions.Legs.Leg.Taxes = field(
                    default=None,
                    metadata={
                        "name": "Taxes",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                total_fare: CurrencyAmountType = field(
                    metadata={
                        "name": "TotalFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                total_mileage: (
                    None | FareType.TpaExtensions.Legs.Leg.TotalMileage
                ) = field(
                    default=None,
                    metadata={
                        "name": "TotalMileage",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                number: None | int = field(
                    default=None,
                    metadata={
                        "name": "Number",
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

                @dataclass(kw_only=True)
                class EquivFare(CurrencyAmountType):
                    """
                    Attributes:
                        effective_price_deviation: Effective Price
                            Deviation
                    """

                    effective_price_deviation: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "EffectivePriceDeviation",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class Taxes:
                    """
                    Attributes:
                        tax: Any individual tax applied to the fare
                    """

                    tax: AirTaxType = field(
                        metadata={
                            "name": "Tax",
                            "type": "Element",
                            "namespace": "http://www.opentravel.org/OTA/2003/05",
                            "required": True,
                        }
                    )

                @dataclass(kw_only=True)
                class TotalMileage:
                    amount: object = field(
                        metadata={
                            "name": "Amount",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

        @dataclass(kw_only=True)
        class FareComponents:
            """
            Attributes:
                fare_component: Subtotal pricing summary for Fare
                    Component.
            """

            fare_component: list[
                FareType.TpaExtensions.FareComponents.FareComponent
            ] = field(
                default_factory=list,
                metadata={
                    "name": "FareComponent",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                },
            )

            @dataclass(kw_only=True)
            class FareComponent:
                """
                Attributes:
                    base_fare: Price of the inventory excluding taxes
                        and fees.
                    equiv_fare: Price of the inventory excluding taxes
                        and fees in the payable currency.
                    taxes: This is a collection of Taxes
                    total_fare: The total price that the passenger would
                        pay (includes fare, taxes, fees)
                    segment:
                    handling_markup_detail:
                    fare_retailer_rule: Matched General Retailer Rule
                        Code or Adjusted Selling Level Retailer Rule
                        Code
                    program_id:
                    program_description: Used to indicate program
                        description
                    program_system_code:
                    brand_id: Used to indicate brand code
                    brand_name: Used to indicate brand name
                """

                base_fare: None | CurrencyAmountType = field(
                    default=None,
                    metadata={
                        "name": "BaseFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                equiv_fare: (
                    None
                    | FareType.TpaExtensions.FareComponents.FareComponent.EquivFare
                ) = field(
                    default=None,
                    metadata={
                        "name": "EquivFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                taxes: (
                    None
                    | FareType.TpaExtensions.FareComponents.FareComponent.Taxes
                ) = field(
                    default=None,
                    metadata={
                        "name": "Taxes",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                total_fare: None | CurrencyAmountType = field(
                    default=None,
                    metadata={
                        "name": "TotalFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                segment: list[
                    FareType.TpaExtensions.FareComponents.FareComponent.Segment
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "Segment",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                handling_markup_detail: list[
                    FareType.TpaExtensions.FareComponents.FareComponent.HandlingMarkupDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "HandlingMarkupDetail",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    },
                )
                fare_retailer_rule: list[
                    FareType.TpaExtensions.FareComponents.FareComponent.FareRetailerRule
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareRetailerRule",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
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

                @dataclass(kw_only=True)
                class EquivFare(CurrencyAmountType):
                    """
                    Attributes:
                        effective_price_deviation: Effective Price
                            Deviation
                    """

                    effective_price_deviation: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "EffectivePriceDeviation",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class Taxes:
                    """
                    Attributes:
                        tax: Any individual tax applied to the fare
                    """

                    tax: AirTaxType = field(
                        metadata={
                            "name": "Tax",
                            "type": "Element",
                            "namespace": "http://www.opentravel.org/OTA/2003/05",
                            "required": True,
                        }
                    )

                @dataclass(kw_only=True)
                class Segment:
                    """
                    Attributes:
                        leg_index: Refers to OriginDestinationOption of
                            current itinerary
                        flight_index: Refers to FlightSegment within
                            OriginDestinationOption of current itinerary
                    """

                    leg_index: int = field(
                        metadata={
                            "name": "LegIndex",
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    flight_index: int = field(
                        metadata={
                            "name": "FlightIndex",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

                @dataclass(kw_only=True)
                class HandlingMarkupDetail:
                    """
                    Attributes:
                        markup_handling_fee_app_id: Markup/Handling fee
                            Application ID
                        markup_type_code: Markup type code, reserved for
                            future extension
                        fare_amount_after_markup: Fare Amount after
                            markup
                        markup_amount: Markup Amount
                        amount_currency: Markup currency
                        markup_rule_source_pcc: Markup Rule Source PCC
                        markup_rule_item_number: Markup Rule Item Number
                    """

                    markup_handling_fee_app_id: None | str = field(
                        default=None,
                        metadata={
                            "name": "MarkupHandlingFeeAppID",
                            "type": "Attribute",
                        },
                    )
                    markup_type_code: None | str = field(
                        default=None,
                        metadata={
                            "name": "MarkupTypeCode",
                            "type": "Attribute",
                        },
                    )
                    fare_amount_after_markup: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "FareAmountAfterMarkup",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        },
                    )
                    markup_amount: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "MarkupAmount",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        },
                    )
                    amount_currency: None | str = field(
                        default=None,
                        metadata={
                            "name": "AmountCurrency",
                            "type": "Attribute",
                            "pattern": r"[a-zA-Z]{3}",
                        },
                    )
                    markup_rule_source_pcc: None | str = field(
                        default=None,
                        metadata={
                            "name": "MarkupRuleSourcePCC",
                            "type": "Attribute",
                            "pattern": r"[0-9A-Z]{3,4}",
                        },
                    )
                    markup_rule_item_number: None | int = field(
                        default=None,
                        metadata={
                            "name": "MarkupRuleItemNumber",
                            "type": "Attribute",
                        },
                    )

                @dataclass(kw_only=True)
                class FareRetailerRule:
                    """
                    Attributes:
                        transaction_type: General or
                            AdjustedSellingLevel
                        code:
                    """

                    transaction_type: str = field(
                        metadata={
                            "name": "TransactionType",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Za-z]+",
                        }
                    )
                    code: str = field(
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Za-z]{2,20}",
                        }
                    )

        @dataclass(kw_only=True)
        class SellingFareDataList:
            selling_fare_data: list[SellingFareDataType] = field(
                default_factory=list,
                metadata={
                    "name": "SellingFareData",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class CommissionData:
            """
            Attributes:
                vccinformation:
                cat35_commission_percentage: Cat 35 Commission
                    Percentage
                cat35_commission_amount: Cat 35 Commission Amount
                cat35_markup_amount: Cat 35 Markup Amount in equivalent
                    amount currency
                commission_amount_in_equivalent: Commission Amount in
                    equivalent amount currency
                commission_source: Commission Source [value C for Cat
                    35, A for AMC, M for Manual]
            """

            vccinformation: list[VccinformationType] = field(
                default_factory=list,
                metadata={
                    "name": "VCCInformation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "max_occurs": 23,
                },
            )
            cat35_commission_percentage: None | Decimal = field(
                default=None,
                metadata={
                    "name": "Cat35CommissionPercentage",
                    "type": "Attribute",
                },
            )
            cat35_commission_amount: None | Decimal = field(
                default=None,
                metadata={
                    "name": "Cat35CommissionAmount",
                    "type": "Attribute",
                },
            )
            cat35_markup_amount: None | Decimal = field(
                default=None,
                metadata={
                    "name": "Cat35MarkupAmount",
                    "type": "Attribute",
                },
            )
            commission_amount_in_equivalent: None | Decimal = field(
                default=None,
                metadata={
                    "name": "CommissionAmountInEquivalent",
                    "type": "Attribute",
                },
            )
            commission_source: None | str = field(
                default=None,
                metadata={
                    "name": "CommissionSource",
                    "type": "Attribute",
                    "length": 1,
                },
            )
