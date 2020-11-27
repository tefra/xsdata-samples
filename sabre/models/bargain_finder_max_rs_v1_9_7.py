from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional, Union
from sabre.models.bargain_finder_max_common_types_v1_9_7 import (
    AdvResTicketingType,
    AirTripType,
    CompanyNameType,
    EquipmentType,
    FareDirectionality,
    PassengerTypeQuantityType,
    StayRestrictionsType,
)

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


class ActionCodeType(Enum):
    """
    Identifies the action code for a booking - OK, Waitlist etc.
    """
    OK = "OK"
    WAITLIST = "Waitlist"
    OTHER = "Other"


@dataclass
class AirFeeType:
    """Defines the data fields available for the fees.

    Attributes
        value:
        fee_code: Identifies the code for the fee.
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    """
    value: Optional[str] = field(
        default=None,
    )
    fee_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FeeCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )


@dataclass
class AirTaxType:
    """Defines the data fields available for air tax.

    Attributes
        value:
        tax_code: Identifies the code for the tax.
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
        carrier_code: carrier used for this tax
        min_amount: Minumum tax amount
        max_amount: Maximum tax amount
        min_max_currency: Min/Max tax currency code
        rate_used: Tax rate used
        station_code: Airport code at which the tax or surcharge is being applied
        reissue_tax_type: Reissue tax type
        reissue_restriction_applies:
        reissue_tax_refundable:
        apply_to_reissue:
        reissue_max_amount:
        reissue_currency: Reissue tax max amount currency
        published_amount:
        published_currency:
    """
    value: Optional[str] = field(
        default=None,
    )
    tax_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 16,
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )
    carrier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CarrierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    min_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinAmount",
            "type": "Attribute",
        }
    )
    max_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaxAmount",
            "type": "Attribute",
        }
    )
    min_max_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinMaxCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    rate_used: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateUsed",
            "type": "Attribute",
        }
    )
    station_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "StationCode",
            "type": "Attribute",
        }
    )
    reissue_tax_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReissueTaxType",
            "type": "Attribute",
            "length": 1,
        }
    )
    reissue_restriction_applies: bool = field(
        default=False,
        metadata={
            "name": "ReissueRestrictionApplies",
            "type": "Attribute",
        }
    )
    reissue_tax_refundable: bool = field(
        default=False,
        metadata={
            "name": "ReissueTaxRefundable",
            "type": "Attribute",
        }
    )
    apply_to_reissue: bool = field(
        default=False,
        metadata={
            "name": "ApplyToReissue",
            "type": "Attribute",
        }
    )
    reissue_max_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ReissueMaxAmount",
            "type": "Attribute",
        }
    )
    reissue_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReissueCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    published_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "PublishedAmount",
            "type": "Attribute",
        }
    )
    published_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublishedCurrency",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )


@dataclass
class BaggageInformationType:
    """Information about baggage."""
    segment: List["BaggageInformationType.Segment"] = field(
        default_factory=list,
        metadata={
            "name": "Segment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
    allowance: Optional["BaggageInformationType.Allowance"] = field(
        default=None,
        metadata={
            "name": "Allowance",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )

    @dataclass
    class Segment:
        """
        Attributes
            id: Id of segment that current baggage information applies to.
        """
        id: Optional[int] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class Allowance:
        """
        Attributes
            pieces: Number of Pieces
            weight: Weight Limit
            unit: Units of the Weight Limit
        """
        pieces: Optional[int] = field(
            default=None,
            metadata={
                "name": "Pieces",
                "type": "Attribute",
            }
        )
        weight: Optional[int] = field(
            default=None,
            metadata={
                "name": "Weight",
                "type": "Attribute",
            }
        )
        unit: Optional["BaggageInformationType.Allowance.Unit"] = field(
            default=None,
            metadata={
                "name": "Unit",
                "type": "Attribute",
            }
        )

        class Unit(Enum):
            KG = "kg"
            LBS = "lbs"


@dataclass
class CouponOfferType:
    """Not used."""
    promo_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    corp_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    headline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    discount_pctg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CurrencyAmountType:
    """Provides a monetary amount and the code of the currency in which this amount
    is expressed.

    Attributes
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )


@dataclass
class CurrencyConversionsType:
    conversion: List["CurrencyConversionsType.Conversion"] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Conversion:
        """
        Attributes
            from_value:
            to:
            rate_of_exchange: Exchange rate
        """
        from_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "From",
                "type": "Attribute",
                "pattern": r"[a-zA-Z]{3}",
            }
        )
        to: Optional[str] = field(
            default=None,
            metadata={
                "name": "To",
                "type": "Attribute",
                "pattern": r"[a-zA-Z]{3}",
            }
        )
        rate_of_exchange: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "RateOfExchange",
                "type": "Attribute",
            }
        )


@dataclass
class FareCalcLineType:
    """IntelliSell Type."""
    info: Optional[str] = field(
        default=None,
        metadata={
            "name": "Info",
            "type": "Attribute",
        }
    )


@dataclass
class FareComponentBreakdownType:
    """Fare Component Breakdown.

    Attributes
        fare_component_reference_id:
        fare_component_commission: Commission Amount per Fare Component
        rule_id: Commission Rule ID
        program_id: Commission Program ID
        contract_id: Commission Contract ID
    """
    fare_component_reference_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "FareComponentReferenceID",
            "type": "Attribute",
        }
    )
    fare_component_commission: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FareComponentCommission",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    rule_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "RuleID",
            "type": "Attribute",
        }
    )
    program_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ProgramID",
            "type": "Attribute",
        }
    )
    contract_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ContractID",
            "type": "Attribute",
        }
    )


@dataclass
class FareGroupType:
    """IntelliSell Type."""
    fare_type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareTypeName",
            "type": "Attribute",
        }
    )


@dataclass
class FareMessagesType:
    message: List["FareMessagesType.Message"] = field(
        default_factory=list,
        metadata={
            "name": "Message",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Message:
        """
        Attributes
            airline_code:
            type:
            fail_code:
            info: Message text
        """
        airline_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "AirlineCode",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 8,
            }
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "name": "Type",
                "type": "Attribute",
                "length": 1,
            }
        )
        fail_code: Optional[int] = field(
            default=None,
            metadata={
                "name": "FailCode",
                "type": "Attribute",
            }
        )
        info: Optional[str] = field(
            default=None,
            metadata={
                "name": "Info",
                "type": "Attribute",
            }
        )


@dataclass
class FreeTextType:
    """Textual information to provide descriptions and/or additional information.

    Attributes
        value:
        language: Language identification.
    """
    value: Optional[str] = field(
        default=None,
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Attribute",
        }
    )


@dataclass
class HandlingMarkupSummaryType:
    """
    Attributes
        type_code: Value M: Embedded Mark Up, J: Adjusted Selling, H: Handling Fee, G: GST Taxes
        description: Max 10 chars
        monetary_amount_value: Can be negative. This is in equivalent amount currency.
    """
    type_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "required": True,
        }
    )
    monetary_amount_value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MonetaryAmountValue",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )


class MessageClassType(Enum):
    """Definies the available messaage class type.

    Attributes
        E: Error
        W: Warrning
        D: Diagnostic
        I: Info
    """
    E = "E"
    W = "W"
    D = "D"
    I = "I"


@dataclass
class ObfeeType:
    """Defines the data fields available for the ob fees.

    Attributes
        type: OB Fee sub type code
        description: OB Fee description
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    """
    class Meta:
        name = "OBFeeType"

    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )


@dataclass
class OcfeeType:
    """OC Fee details.

    Attributes
        amount: Fee amount
        description: Fee description
        origin_airport: Origin airport
        destination_airport: Destination airport
        carrier: Operating carrier code
        passenger_code: Ancillary fee code
        date: Date for this fee.
        start_segment: Start travel segment
        end_segment: End travel segment
    """
    class Meta:
        name = "OCFeeType"

    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginAirport",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "DestinationAirport",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    passenger_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PassengerCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9]{2,3}",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        }
    )
    start_segment: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartSegment",
            "type": "Attribute",
            "required": True,
        }
    )
    end_segment: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndSegment",
            "type": "Attribute",
            "required": True,
        }
    )


class OtaAirLowFareSearchRsTarget(Enum):
    TEST = "Test"
    PRODUCTION = "Production"


class PollingStatusType(Enum):
    RECEIVED = "received"
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass
class ProcessingMessageType:
    """Message generated per for particular date and leg.

    Attributes
        pricing_source: Pricing source.
        message: Message text
    """
    pricing_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Z_]{1,13}",
        }
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RateOfExchangeType:
    """
    Attributes
        value: Exchange rate
    """
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
        }
    )


@dataclass
class ReissueInfoType:
    """Defines the data fields available for the reissue info type."""
    change_fees: Optional["ReissueInfoType.ChangeFees"] = field(
        default=None,
        metadata={
            "name": "ChangeFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    residual_idicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResidualIdicator",
            "type": "Attribute",
        }
    )
    type_of_service_fee: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceFee",
            "type": "Attribute",
        }
    )
    type_of_reissue_transaction: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOfReissueTransaction",
            "type": "Attribute",
        }
    )
    reissue_result_from_tag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReissueResultFromTag",
            "type": "Attribute",
        }
    )
    form_of_refund: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormOfRefund",
            "type": "Attribute",
        }
    )
    reissue_requires_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReissueRequiresElectronicTicket",
            "type": "Attribute",
        }
    )
    reissue_does_not_allow_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReissueDoesNotAllowElectronicTicket",
            "type": "Attribute",
        }
    )
    tax_refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxRefundable",
            "type": "Attribute",
        }
    )

    @dataclass
    class ChangeFees:
        change_fee: Optional["ReissueInfoType.ChangeFees.ChangeFee"] = field(
            default=None,
            metadata={
                "name": "ChangeFee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "required": True,
            }
        )

        @dataclass
        class ChangeFee:
            """
            Attributes
                highest_change_fee:
                amount:
                currency_code: A currency code (e.g. USD, EUR, PLN)
                decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
                change_fee_waived:
                change_fee_not_applicable:
            """
            highest_change_fee: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "HighestChangeFee",
                    "type": "Attribute",
                }
            )
            amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Amount",
                    "type": "Attribute",
                    "fraction_digits": 3,
                }
            )
            currency_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CurrencyCode",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )
            decimal_places: Optional[int] = field(
                default=None,
                metadata={
                    "name": "DecimalPlaces",
                    "type": "Attribute",
                }
            )
            change_fee_waived: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "ChangeFeeWaived",
                    "type": "Attribute",
                }
            )
            change_fee_not_applicable: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "ChangeFeeNotApplicable",
                    "type": "Attribute",
                }
            )


@dataclass
class ResponseLocationType:
    """Code and optional string to describe a location point.

    Attributes
        value:
        location_code: Location identifying code.
        code_context: Identifies the context of the identifying code, such as IATA, ARC, or internal code, etc.
    """
    value: Optional[str] = field(
        default=None,
    )
    location_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    code_context: str = field(
        default="IATA",
        metadata={
            "name": "CodeContext",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )


@dataclass
class SuccessType:
    """Standard way to indicate successful processing of an OTA message.

    Returning an empty element of this type indicates success.
    """


@dataclass
class SurchargesType:
    value: Optional[str] = field(
        default=None,
    )
    ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ind",
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )


class TicketType(Enum):
    """Paper or e-ticket."""
    E_TICKET = "eTicket"
    PAPER = "Paper"


@dataclass
class UnflownPriceType:
    """Totally Unflown Itinerary Price Information.

    Attributes
        amount:
        currency_code: A currency code (e.g. USD, EUR, PLN)
        decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    """
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z]{3}",
        }
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata={
            "name": "DecimalPlaces",
            "type": "Attribute",
        }
    )


class ValidInterlineType(Enum):
    YES = "Yes"
    NO = "No"
    UNKNOWN = "Unknown"


@dataclass
class ValidatingCarrierInfoType:
    """
    Attributes
        default: Default validating carrier code
        alternate: Alternate validating carrier code
        settlement_method:
        new_vcx_process:
    """
    default: Optional["ValidatingCarrierInfoType.Default"] = field(
        default=None,
        metadata={
            "name": "Default",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    alternate: List["ValidatingCarrierInfoType.Alternate"] = field(
        default_factory=list,
        metadata={
            "name": "Alternate",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 24,
        }
    )
    settlement_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "SettlementMethod",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 3,
        }
    )
    new_vcx_process: Optional[bool] = field(
        default=None,
        metadata={
            "name": "NewVcxProcess",
            "type": "Attribute",
        }
    )

    @dataclass
    class Default:
        country: List["ValidatingCarrierInfoType.Default.Country"] = field(
            default_factory=list,
            metadata={
                "name": "Country",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "pattern": r"[A-Z][0-9A-Z]|[0-9A-Z][A-Z][0-9A-Z]?|[A-Za-z]{0}",
            }
        )

        @dataclass
        class Country:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                }
            )

    @dataclass
    class Alternate:
        country: List["ValidatingCarrierInfoType.Alternate.Country"] = field(
            default_factory=list,
            metadata={
                "name": "Country",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        code: Optional[str] = field(
            default=None,
            metadata={
                "name": "Code",
                "type": "Attribute",
                "pattern": r"[0-9A-Z]{2,3}",
            }
        )

        @dataclass
        class Country:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                }
            )


@dataclass
class AirlineLowestFaresType:
    """IntelliSell Type .

    lowest fare for airline. Currently not used.
    """
    airline: Optional[CompanyNameType] = field(
        default=None,
        metadata={
            "name": "Airline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    no_stops: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoStops",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "LowestFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    itinerary_count: Optional[object] = field(
        default=None,
        metadata={
            "name": "ItineraryCount",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )


@dataclass
class AirportInformationType(ResponseLocationType):
    """Code and optional string to describe a location point.

    Attributes
        terminal_id: Location terminal identifier.
    """
    terminal_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminalID",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{1,}",
        }
    )


@dataclass
class AlternateDateLowestFaresType:
    """IntelliSell Type .

    lowest fare for alternate departure / return date times.
    """
    departure_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    returnl_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnlDateTime",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "LowestFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )


@dataclass
class AlternateLocationLowestFaresType:
    """IntelliSell Type .

    lowest fare for alternate origin / destination pair.
    """
    origin_location: Optional[ResponseLocationType] = field(
        default=None,
        metadata={
            "name": "OriginLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    destination_location: Optional[ResponseLocationType] = field(
        default=None,
        metadata={
            "name": "DestinationLocation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "LowestFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )


@dataclass
class BaggageInformationListType:
    """Baggage information list."""
    baggage_information: List[BaggageInformationType] = field(
        default_factory=list,
        metadata={
            "name": "BaggageInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )


@dataclass
class ComplexProcessingMessageType(ProcessingMessageType):
    """
    Attributes
        leg: Optional list of departure dates for each leg
    """
    leg: List["ComplexProcessingMessageType.Leg"] = field(
        default_factory=list,
        metadata={
            "name": "Leg",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        }
    )

    @dataclass
    class Leg:
        """
        Attributes
            departure_date: Departure date
        """
        departure_date: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureDate",
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class ErrorType(FreeTextType):
    """Standard way to indicate that an error occurred during the processing of an
    OTA message.

    Attributes
        type: The Error element MUST contain the Type attribute that uses a recommended set of values to indicate the error type. The validating XSD can expect to accept values that it has NOT been explicitly coded for and process them by using Type ="Unknown".  Refer to OTA Code List Error Warning Type (EWT).
        short_text:
        code: If present, this refers to a table of coded values exchanged between applications to identify errors or warnings. Refer to OTA Code List Error Codes (ERR).
        doc_url: If present, this URL refers to an online description of the error that occurred.
        status: If present, recommended values are those enumerated in the OTA_ErrorRS, (NotProcessed | Incomplete | Complete | Unknown) however, the data type is designated as string data, recognizing that trading partners may identify additional status conditions not included in the enumeration.
        tag: If present, this attribute may identify an unknown or misspelled tag that caused an error in processing. It is recommended that the Tag attribute use XPath notation to identify the location of a tag in the event that more than one tag of the same name is present in the document. Alternatively, the tag name alone can be used to identify missing data [Type=ReqFieldMissing].
        record_id: If present, this attribute allows for batch processing and the identification of the record that failed amongst a group of records.
        message_class: If present specify the message class.
        node_list: An XPath expression that selects all the nodes whose data caused this error.  Further, this expression should have an   additional contraint which contains the data of the node.  This will provide the offending data back to systems that cannot maintain the original message.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    short_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortText",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    doc_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocURL",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
        }
    )
    record_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    message_class: Optional[MessageClassType] = field(
        default=None,
        metadata={
            "name": "MessageClass",
            "type": "Attribute",
        }
    )
    node_list: Optional[str] = field(
        default=None,
        metadata={
            "name": "NodeList",
            "type": "Attribute",
        }
    )


@dataclass
class FareComponentTaxesType:
    """
    Attributes
        flight_segment: A container for necessary data to describe one or more flight segments.
        tax: Any individual tax applied to the fare
    """
    flight_segment: List["FareComponentTaxesType.FlightSegment"] = field(
        default_factory=list,
        metadata={
            "name": "FlightSegment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
    tax: List[AirTaxType] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 99,
        }
    )

    @dataclass
    class FlightSegment:
        """
        Attributes
            departure_airport_code: Departure point of flight segment.
            arrival_airport_code: Arrival point of flight segment.
        """
        departure_airport_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "DepartureAirportCode",
                "type": "Attribute",
            }
        )
        arrival_airport_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "ArrivalAirportCode",
                "type": "Attribute",
            }
        )


@dataclass
class OneWayProcessingMessageType(ProcessingMessageType):
    """
    Attributes
        departure_date: Departure date
        departure_airport: Location identifying code.
        arrival_airport: Location identifying code.
    """
    departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    departure_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureAirport",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    arrival_airport: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalAirport",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )


@dataclass
class OperatingAirlineType(CompanyNameType):
    """This is an extension of CompanyNameType to include a FlightNumber."""
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "pattern": r"[0-9]{1,4}[A-Z]?",
        }
    )


@dataclass
class RuleInfoType:
    """Contains summary fare rule information as well as detailed Rule Information
    for Fare Basis Codes.  Information may be actual rules data or the results
    returned from a rules-based inquiry.

    Attributes
        res_ticketing_rules: General container for rules regarding fare reservation,  ticketing and sale restrictions
        length_of_stay_rules: Rules providing minimum or maximum stay restrictions.
    """
    res_ticketing_rules: Optional["RuleInfoType.ResTicketingRules"] = field(
        default=None,
        metadata={
            "name": "ResTicketingRules",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    length_of_stay_rules: Optional[StayRestrictionsType] = field(
        default=None,
        metadata={
            "name": "LengthOfStayRules",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )

    @dataclass
    class ResTicketingRules:
        """
        Attributes
            adv_res_ticketing: Container for holding rules regarding advance reservation or ticketing restrictions.
        """
        adv_res_ticketing: Optional[AdvResTicketingType] = field(
            default=None,
            metadata={
                "name": "AdvResTicketing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )


@dataclass
class SellingFareDataType:
    handling_markup_summary: List[HandlingMarkupSummaryType] = field(
        default_factory=list,
        metadata={
            "name": "HandlingMarkupSummary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    layer_type_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LayerTypeName",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TicketingInfoRsType:
    """Extends TicketingInfoType to provide an eTicketNumber.

    Attributes
        ticket_advisory: Open text field available for additional ticket information.
        tpa_extensions: Place holder for additional elements.
        e_ticket_number: If reservation is electronically ticketed at time of booking, this is the field for the eTicket number.
        ticket_time_limit: TicketTimeLimit - Indicates the ticketing arrangement, and allows for the requirement that an itinerary must be ticketed by a certain date and time.
        ticket_type: TicketType - Indicates the type of ticket (Paper, eTicket)
        valid_interline: ValidInterline - Indicates validation of interline ticketing aggrement,
            possible values (Yes, No, Unknown), default=unknown
    """
    class Meta:
        name = "TicketingInfoRS_Type"

    ticket_advisory: List[FreeTextType] = field(
        default_factory=list,
        metadata={
            "name": "TicketAdvisory",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 10,
        }
    )
    tpa_extensions: Optional[str] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    e_ticket_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "eTicketNumber",
            "type": "Attribute",
            "pattern": r"[0-9a-zA-Z]{1,14}",
        }
    )
    ticket_time_limit: Optional[str] = field(
        default=None,
        metadata={
            "name": "TicketTimeLimit",
            "type": "Attribute",
        }
    )
    ticket_type: Optional[TicketType] = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
            "required": True,
        }
    )
    valid_interline: ValidInterlineType = field(
        default=ValidInterlineType.UNKNOWN,
        metadata={
            "name": "ValidInterline",
            "type": "Attribute",
        }
    )


@dataclass
class VccinformationType:
    """Validating Carrier Commission Information.

    Attributes
        fare_component_breakdown:
        validating_carrier:
        commission_amount: Commission Amount (in equivalent amount currency)
        total_amount_including_mark_up: Total Commision amount including Mark-Up
        commission_percent:
    """
    class Meta:
        name = "VCCInformationType"

    fare_component_breakdown: List[FareComponentBreakdownType] = field(
        default_factory=list,
        metadata={
            "name": "FareComponentBreakdown",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 24,
        }
    )
    validating_carrier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ValidatingCarrier",
            "type": "Attribute",
            "pattern": r"[0-9A-Z]{2,3}",
        }
    )
    commission_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CommissionAmount",
            "type": "Attribute",
            "required": True,
            "fraction_digits": 3,
        }
    )
    total_amount_including_mark_up: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "TotalAmountIncludingMarkUp",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )
    commission_percent: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CommissionPercent",
            "type": "Attribute",
            "fraction_digits": 3,
        }
    )


@dataclass
class WarningType(FreeTextType):
    """Standard way to indicate successful processing of an OTA message, but one in
    which warnings are generated.

    Attributes
        type: The Warning element MUST contain the Type attribute that uses a recommended set of values to indicate the warning type. The validating XSD can expect to accept values that it has NOT been explicitly coded for and process them by using Type ="Unknown".  Refer to OTA Code List Error Warning Type (EWT).
        short_text:
        code: If present, this refers to a table of coded values exchanged between applications to identify errors or warnings. Refer to OTA Code List Error Codes (ERR).
        doc_url: If present, this URL refers to an online description of the error that occurred.
        status: If present, recommended values are those enumerated in the OTA_ErrorRS, (NotProcessed | Incomplete | Complete | Unknown) however, the data type is designated as string data, recognizing that trading partners may identify additional status conditions not included in the enumeration.
        tag: If present, this attribute may identify an unknown or misspelled tag that caused an error in processing. It is recommended that the Tag attribute use XPath notation to identify the location of a tag in the event that more than one tag of the same name is present in the document. Alternatively, the tag name alone can be used to identify missing data [Type=ReqFieldMissing].
        record_id: If present, this attribute allows for batch processing and the identification of the record that failed amongst a group of records.
        message_class: If present specify the message class.
    """
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    short_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShortText",
            "type": "Attribute",
        }
    )
    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        }
    )
    doc_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocURL",
            "type": "Attribute",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
        }
    )
    record_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RecordID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    message_class: Optional[MessageClassType] = field(
        default=None,
        metadata={
            "name": "MessageClass",
            "type": "Attribute",
        }
    )


@dataclass
class BookFlightSegmentType:
    """Container for the flight segment data plus the MarriageGrp.

    Attributes
        departure_airport: Departure point of flight segment.
        arrival_airport: Arrival point of flight segment.
        operating_airline: The operating airline of the flight if it is a codeshare  flight.
        equipment: The type of equipment  used for the  flight..
        marketing_airline: The marketing airline. This is required for use with scheduled airline messages but may be omitted for requests by tour operators.
        disclosure_airline: The disclosure airline. This is required by the DOT mandate.
        marriage_grp: Many airlines link connection flights together by terming them married segments.  When two or more segments are married, they must be processed as one unit. The segments must be moved, cancelled, and/or priced together. The value of the marriage group must be the same for all segments.
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
        flight_number: The flight number of the flight. This is required for use with scheduled airline messages but may be omitted for requests by tour operators.
        tour_operator_flight_id: ID of a flight in the Tour Operator's inventory. This flight is not necessarily in the inventory of an airline. Rather, it is a code created by tour operators.
        res_book_desig_code: Specific Booking Class for this segment.
        action_code:
        number_in_party:
        elapsed_time: Elapsed segment trip time.
    """
    departure_airport: Optional[AirportInformationType] = field(
        default=None,
        metadata={
            "name": "DepartureAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    arrival_airport: Optional[AirportInformationType] = field(
        default=None,
        metadata={
            "name": "ArrivalAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    operating_airline: Optional[OperatingAirlineType] = field(
        default=None,
        metadata={
            "name": "OperatingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    equipment: List[EquipmentType] = field(
        default_factory=list,
        metadata={
            "name": "Equipment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 2,
        }
    )
    marketing_airline: Optional[CompanyNameType] = field(
        default=None,
        metadata={
            "name": "MarketingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    disclosure_airline: Optional[CompanyNameType] = field(
        default=None,
        metadata={
            "name": "DisclosureAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    marriage_grp: Optional[str] = field(
        default=None,
        metadata={
            "name": "MarriageGrp",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_length": 1,
            "max_length": 16,
        }
    )
    stop_airports: Optional["BookFlightSegmentType.StopAirports"] = field(
        default=None,
        metadata={
            "name": "StopAirports",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    departure_time_zone: Optional["BookFlightSegmentType.DepartureTimeZone"] = field(
        default=None,
        metadata={
            "name": "DepartureTimeZone",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    arrival_time_zone: Optional["BookFlightSegmentType.ArrivalTimeZone"] = field(
        default=None,
        metadata={
            "name": "ArrivalTimeZone",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    on_time_performance: Optional["BookFlightSegmentType.OnTimePerformance"] = field(
        default=None,
        metadata={
            "name": "OnTimePerformance",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["BookFlightSegmentType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ArrivalDateTime",
            "type": "Attribute",
        }
    )
    stop_quantity: Optional[int] = field(
        default=None,
        metadata={
            "name": "StopQuantity",
            "type": "Attribute",
        }
    )
    rph: Optional[str] = field(
        default=None,
        metadata={
            "name": "RPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        }
    )
    info_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "InfoSource",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "pattern": r"[0-9]{1,4}[A-Z]?",
        }
    )
    tour_operator_flight_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TourOperatorFlightID",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        }
    )
    res_book_desig_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ResBookDesigCode",
            "type": "Attribute",
            "pattern": r"[A-Z\s]{1,2}",
        }
    )
    action_code: Optional[ActionCodeType] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Attribute",
        }
    )
    number_in_party: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberInParty",
            "type": "Attribute",
        }
    )
    elapsed_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "ElapsedTime",
            "type": "Attribute",
        }
    )

    @dataclass
    class StopAirports:
        """
        Attributes
            stop_airport: Stop point of flight segment.
        """
        stop_airport: List["BookFlightSegmentType.StopAirports.StopAirport"] = field(
            default_factory=list,
            metadata={
                "name": "StopAirport",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            }
        )

        @dataclass
        class StopAirport(ResponseLocationType):
            """
            Attributes
                arrival_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
                departure_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
                elapsed_time: Elapsed Time in minutes
                duration: Layover time in minutes
                gmtoffset:
                equipment: Equipment type
            """
            arrival_date_time: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ArrivalDateTime",
                    "type": "Attribute",
                }
            )
            departure_date_time: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DepartureDateTime",
                    "type": "Attribute",
                }
            )
            elapsed_time: Optional[int] = field(
                default=None,
                metadata={
                    "name": "ElapsedTime",
                    "type": "Attribute",
                }
            )
            duration: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Duration",
                    "type": "Attribute",
                }
            )
            gmtoffset: Optional[float] = field(
                default=None,
                metadata={
                    "name": "GMTOffset",
                    "type": "Attribute",
                }
            )
            equipment: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Equipment",
                    "type": "Attribute",
                }
            )

    @dataclass
    class DepartureTimeZone:
        gmtoffset: Optional[float] = field(
            default=None,
            metadata={
                "name": "GMTOffset",
                "type": "Attribute",
            }
        )

    @dataclass
    class ArrivalTimeZone:
        gmtoffset: Optional[float] = field(
            default=None,
            metadata={
                "name": "GMTOffset",
                "type": "Attribute",
            }
        )

    @dataclass
    class OnTimePerformance:
        level: Optional[str] = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
            }
        )
        percentage: Optional[str] = field(
            default=None,
            metadata={
                "name": "Percentage",
                "type": "Attribute",
            }
        )

    @dataclass
    class TpaExtensions:
        e_ticket: Optional["BookFlightSegmentType.TpaExtensions.ETicket"] = field(
            default=None,
            metadata={
                "name": "eTicket",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        data_element: Optional["BookFlightSegmentType.TpaExtensions.DataElement"] = field(
            default=None,
            metadata={
                "name": "DataElement",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        message: Optional["BookFlightSegmentType.TpaExtensions.Message"] = field(
            default=None,
            metadata={
                "name": "Message",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class ETicket:
            ind: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                }
            )

        @dataclass
        class DataElement:
            subject_to_government_approval: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "SubjectToGovernmentApproval",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Message:
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            text: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Text",
                    "type": "Attribute",
                }
            )


@dataclass
class ErrorsType:
    """A collection of errors that occurred during the processing of a message.

    Attributes
        error: Describes an error that occurred during the processing of an OTA message
    """
    error: List[ErrorType] = field(
        default_factory=list,
        metadata={
            "name": "Error",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )


@dataclass
class FareInfoType:
    """Rules for this priced option.

    Attributes
        departure_date: Departure Date for this priced fare.
        fare_reference: FareReferenceCode can be used for either the Fare Basis Code or the Fare Class Code.
        rule_info: Information regarding restrictions governing use of the fare.
        marketing_airline: The marketing airline.
        departure_airport: Departure point of flight segment.
        arrival_airport: Arrival point of flight segment.
        negotiated_fare: Indicator to show if this is a private fare.
        negotiated_fare_code: Code used to identify the private fare.
    """
    departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareReference",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
            "min_length": 1,
            "max_length": 8,
        }
    )
    rule_info: Optional[RuleInfoType] = field(
        default=None,
        metadata={
            "name": "RuleInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    marketing_airline: List[CompanyNameType] = field(
        default_factory=list,
        metadata={
            "name": "MarketingAirline",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    departure_airport: Optional[ResponseLocationType] = field(
        default=None,
        metadata={
            "name": "DepartureAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    arrival_airport: Optional[ResponseLocationType] = field(
        default=None,
        metadata={
            "name": "ArrivalAirport",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    negotiated_fare: bool = field(
        default=False,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        }
    )
    negotiated_fare_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "NegotiatedFareCode",
            "type": "Attribute",
        }
    )


@dataclass
class FareType:
    """Holds a base fare, tax, total and currency information on a price.

    Attributes
        base_fare: Price of the inventory excluding taxes and fees.
        non_refundable_base_fare: Non-refundable base fare amount
        fare_construction: Fare construction total amount.
        equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
        taxes: This is a collection of Taxes
        fees: This is a collection of Fees
        obfees: This is a collection of ob Fees
        rate_of_exchange:
        currency_conversions:
        total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
        reissue_info_list: Reissue information
        penalties_info: Penalties information
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        negotiated_fare: Indicator to show if this is a private fare.
        negotiated_fare_code: Code used to identify the private fare.
    """
    base_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "BaseFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    non_refundable_base_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "NonRefundableBaseFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_construction: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "FareConstruction",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    equiv_fare: Optional["FareType.EquivFare"] = field(
        default=None,
        metadata={
            "name": "EquivFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    taxes: Optional["FareType.Taxes"] = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fees: Optional["FareType.Fees"] = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    obfees: Optional["FareType.Obfees"] = field(
        default=None,
        metadata={
            "name": "OBFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    rate_of_exchange: Optional[RateOfExchangeType] = field(
        default=None,
        metadata={
            "name": "RateOfExchange",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    currency_conversions: Optional[CurrencyConversionsType] = field(
        default=None,
        metadata={
            "name": "CurrencyConversions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    total_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata={
            "name": "TotalFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    reissue_info_list: Optional["FareType.ReissueInfoList"] = field(
        default=None,
        metadata={
            "name": "ReissueInfoList",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    penalties_info: Optional["FareType.PenaltiesInfo"] = field(
        default=None,
        metadata={
            "name": "PenaltiesInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["FareType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    negotiated_fare: bool = field(
        default=False,
        metadata={
            "name": "NegotiatedFare",
            "type": "Attribute",
        }
    )
    negotiated_fare_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "NegotiatedFareCode",
            "type": "Attribute",
        }
    )

    @dataclass
    class EquivFare(CurrencyAmountType):
        """
        Attributes
            effective_price_deviation: Effective Price Deviation
        """
        effective_price_deviation: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "EffectivePriceDeviation",
                "type": "Attribute",
                "fraction_digits": 3,
            }
        )

    @dataclass
    class Taxes:
        """
        Attributes
            fare_components_taxes:
            legs_taxes:
            tax: Any individual tax applied to the fare
            total_tax: Total (summary) of taxes applied to the fare
        """
        fare_components_taxes: Optional["FareType.Taxes.FareComponentsTaxes"] = field(
            default=None,
            metadata={
                "name": "FareComponentsTaxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        legs_taxes: Optional["FareType.Taxes.LegsTaxes"] = field(
            default=None,
            metadata={
                "name": "LegsTaxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        tax: List[AirTaxType] = field(
            default_factory=list,
            metadata={
                "name": "Tax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )
        total_tax: Optional[CurrencyAmountType] = field(
            default=None,
            metadata={
                "name": "TotalTax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class FareComponentsTaxes:
            fare_component_taxes: List[FareComponentTaxesType] = field(
                default_factory=list,
                metadata={
                    "name": "FareComponentTaxes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 99,
                }
            )

        @dataclass
        class LegsTaxes:
            leg_taxes: List["FareType.Taxes.LegsTaxes.LegTaxes"] = field(
                default_factory=list,
                metadata={
                    "name": "LegTaxes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 99,
                }
            )

            @dataclass
            class LegTaxes:
                """
                Attributes
                    tax: Any individual tax applied to the fare
                    number:
                """
                tax: List[AirTaxType] = field(
                    default_factory=list,
                    metadata={
                        "name": "Tax",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 1,
                        "max_occurs": 99,
                    }
                )
                number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                    }
                )

    @dataclass
    class Fees:
        """
        Attributes
            fee: Any additional fee incurred by the passenger but not shown on the ticket.
        """
        fee: List[AirFeeType] = field(
            default_factory=list,
            metadata={
                "name": "Fee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 9,
            }
        )

    @dataclass
    class Obfees:
        """
        Attributes
            obfee: OB fees
            ttype_amount: Total T-type OB Fee
        """
        obfee: List[ObfeeType] = field(
            default_factory=list,
            metadata={
                "name": "OBFee",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        ttype_amount: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "TTypeAmount",
                "type": "Attribute",
                "fraction_digits": 3,
            }
        )

    @dataclass
    class ReissueInfoList:
        """
        Attributes
            reissue_info: Reissue Info
        """
        reissue_info: List[ReissueInfoType] = field(
            default_factory=list,
            metadata={
                "name": "ReissueInfo",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            }
        )

    @dataclass
    class PenaltiesInfo:
        """
        Attributes
            penalty: Penalty Info
        """
        penalty: List["FareType.PenaltiesInfo.Penalty"] = field(
            default_factory=list,
            metadata={
                "name": "Penalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Penalty:
            """
            Attributes
                cat16_text_only: Missing Data
                type:
                applicability:
                refundable:
                changeable:
                conditions_apply:
                amount:
                currency_code: A currency code (e.g. USD, EUR, PLN)
                decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
                cat16_info:
            """
            cat16_text_only: List["FareType.PenaltiesInfo.Penalty.Cat16TextOnly"] = field(
                default_factory=list,
                metadata={
                    "name": "Cat16TextOnly",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            type: Optional["FareType.PenaltiesInfo.Penalty.Type"] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            applicability: Optional["FareType.PenaltiesInfo.Penalty.Applicability"] = field(
                default=None,
                metadata={
                    "name": "Applicability",
                    "type": "Attribute",
                }
            )
            refundable: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Refundable",
                    "type": "Attribute",
                }
            )
            changeable: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Changeable",
                    "type": "Attribute",
                }
            )
            conditions_apply: bool = field(
                default=False,
                metadata={
                    "name": "ConditionsApply",
                    "type": "Attribute",
                }
            )
            amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Amount",
                    "type": "Attribute",
                    "fraction_digits": 3,
                }
            )
            currency_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CurrencyCode",
                    "type": "Attribute",
                    "pattern": r"[a-zA-Z]{3}",
                }
            )
            decimal_places: Optional[int] = field(
                default=None,
                metadata={
                    "name": "DecimalPlaces",
                    "type": "Attribute",
                }
            )
            cat16_info: bool = field(
                default=False,
                metadata={
                    "name": "Cat16Info",
                    "type": "Attribute",
                }
            )

            @dataclass
            class Cat16TextOnly:
                """
                Attributes
                    fare_basis_code: Fare basis code
                    fare_component_id: Fare component Id
                """
                fare_basis_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "FareBasisCode",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "pattern": r"[A-Z0-9]+(/[A-Z0-9]+)?",
                    }
                )
                fare_component_id: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "FareComponentID",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            class Type(Enum):
                REFUND = "Refund"
                EXCHANGE = "Exchange"

            class Applicability(Enum):
                AFTER = "After"
                BEFORE = "Before"

    @dataclass
    class TpaExtensions:
        """
        Attributes
            surcharges: Surcharge information
            legs: This is a collection of Leg Information
            fare_components: A collection of additional information for each Fare Component
            messages:
            baggage_information_list:
            selling_fare_data_list:
            commission_data:
        """
        surcharges: List[SurchargesType] = field(
            default_factory=list,
            metadata={
                "name": "Surcharges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        legs: Optional["FareType.TpaExtensions.Legs"] = field(
            default=None,
            metadata={
                "name": "Legs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_components: Optional["FareType.TpaExtensions.FareComponents"] = field(
            default=None,
            metadata={
                "name": "FareComponents",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        messages: Optional[FareMessagesType] = field(
            default=None,
            metadata={
                "name": "Messages",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        baggage_information_list: Optional[BaggageInformationListType] = field(
            default=None,
            metadata={
                "name": "BaggageInformationList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        selling_fare_data_list: Optional["FareType.TpaExtensions.SellingFareDataList"] = field(
            default=None,
            metadata={
                "name": "SellingFareDataList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        commission_data: Optional["FareType.TpaExtensions.CommissionData"] = field(
            default=None,
            metadata={
                "name": "CommissionData",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class Legs:
            """
            Attributes
                leg: Leg Information
            """
            leg: List["FareType.TpaExtensions.Legs.Leg"] = field(
                default_factory=list,
                metadata={
                    "name": "Leg",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Leg:
                """
                Attributes
                    base_fare: Price of the inventory excluding taxes and fees.
                    equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
                    taxes: This is a collection of Taxes
                    total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
                    total_mileage:
                    number:
                    fare_status: Detailed reason why fare could not be returned (when FareReturned="false"). "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable", "N" - unknown status.
                """
                base_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata={
                        "name": "BaseFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                equiv_fare: Optional["FareType.TpaExtensions.Legs.Leg.EquivFare"] = field(
                    default=None,
                    metadata={
                        "name": "EquivFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                taxes: Optional["FareType.TpaExtensions.Legs.Leg.Taxes"] = field(
                    default=None,
                    metadata={
                        "name": "Taxes",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                total_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata={
                        "name": "TotalFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                total_mileage: Optional["FareType.TpaExtensions.Legs.Leg.TotalMileage"] = field(
                    default=None,
                    metadata={
                        "name": "TotalMileage",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                    }
                )
                fare_status: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "FareStatus",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class EquivFare(CurrencyAmountType):
                    """
                    Attributes
                        effective_price_deviation: Effective Price Deviation
                    """
                    effective_price_deviation: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "EffectivePriceDeviation",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        }
                    )

                @dataclass
                class Taxes:
                    """
                    Attributes
                        tax: Any individual tax applied to the fare
                    """
                    tax: Optional[AirTaxType] = field(
                        default=None,
                        metadata={
                            "name": "Tax",
                            "type": "Element",
                            "namespace": "http://www.opentravel.org/OTA/2003/05",
                            "required": True,
                        }
                    )

                @dataclass
                class TotalMileage:
                    amount: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Amount",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

        @dataclass
        class FareComponents:
            """
            Attributes
                fare_component: Subtotal pricing summary for Fare Component.
            """
            fare_component: List["FareType.TpaExtensions.FareComponents.FareComponent"] = field(
                default_factory=list,
                metadata={
                    "name": "FareComponent",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class FareComponent:
                """
                Attributes
                    base_fare: Price of the inventory excluding taxes and fees.
                    equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
                    taxes: This is a collection of Taxes
                    total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
                    segment:
                    handling_markup_detail:
                    fare_retailer_rule: Matched General Retailer Rule Code or Adjusted Selling Level Retailer Rule Code
                    program_id:
                    program_description: Used to indicate program description
                    program_system_code:
                    brand_id: Used to indicate brand code
                    brand_name: Used to indicate brand name
                """
                base_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata={
                        "name": "BaseFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                equiv_fare: Optional["FareType.TpaExtensions.FareComponents.FareComponent.EquivFare"] = field(
                    default=None,
                    metadata={
                        "name": "EquivFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                taxes: Optional["FareType.TpaExtensions.FareComponents.FareComponent.Taxes"] = field(
                    default=None,
                    metadata={
                        "name": "Taxes",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                total_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata={
                        "name": "TotalFare",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                segment: List["FareType.TpaExtensions.FareComponents.FareComponent.Segment"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Segment",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                handling_markup_detail: List["FareType.TpaExtensions.FareComponents.FareComponent.HandlingMarkupDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "HandlingMarkupDetail",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                fare_retailer_rule: List["FareType.TpaExtensions.FareComponents.FareComponent.FareRetailerRule"] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareRetailerRule",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                program_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramID",
                        "type": "Attribute",
                    }
                )
                program_description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramDescription",
                        "type": "Attribute",
                    }
                )
                program_system_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramSystemCode",
                        "type": "Attribute",
                    }
                )
                brand_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BrandID",
                        "type": "Attribute",
                    }
                )
                brand_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BrandName",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class EquivFare(CurrencyAmountType):
                    """
                    Attributes
                        effective_price_deviation: Effective Price Deviation
                    """
                    effective_price_deviation: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "EffectivePriceDeviation",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        }
                    )

                @dataclass
                class Taxes:
                    """
                    Attributes
                        tax: Any individual tax applied to the fare
                    """
                    tax: Optional[AirTaxType] = field(
                        default=None,
                        metadata={
                            "name": "Tax",
                            "type": "Element",
                            "namespace": "http://www.opentravel.org/OTA/2003/05",
                            "required": True,
                        }
                    )

                @dataclass
                class Segment:
                    """
                    Attributes
                        leg_index: Refers to OriginDestinationOption of current itinerary
                        flight_index: Refers to FlightSegment within OriginDestinationOption of current itinerary
                    """
                    leg_index: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "LegIndex",
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    flight_index: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "FlightIndex",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

                @dataclass
                class HandlingMarkupDetail:
                    """
                    Attributes
                        markup_handling_fee_app_id: Markup/Handling fee Application ID
                        markup_type_code: Markup type code, reserved for future extension
                        fare_amount_after_markup: Fare Amount after markup
                        markup_amount: Markup Amount
                        amount_currency: Markup currency
                        markup_rule_source_pcc: Markup Rule Source PCC
                        markup_rule_item_number: Markup Rule Item Number
                    """
                    markup_handling_fee_app_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "MarkupHandlingFeeAppID",
                            "type": "Attribute",
                        }
                    )
                    markup_type_code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "MarkupTypeCode",
                            "type": "Attribute",
                        }
                    )
                    fare_amount_after_markup: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "FareAmountAfterMarkup",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        }
                    )
                    markup_amount: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "MarkupAmount",
                            "type": "Attribute",
                            "fraction_digits": 3,
                        }
                    )
                    amount_currency: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "AmountCurrency",
                            "type": "Attribute",
                            "pattern": r"[a-zA-Z]{3}",
                        }
                    )
                    markup_rule_source_pcc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "MarkupRuleSourcePCC",
                            "type": "Attribute",
                            "pattern": r"[0-9A-Z]{3,4}",
                        }
                    )
                    markup_rule_item_number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "MarkupRuleItemNumber",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class FareRetailerRule:
                    """
                    Attributes
                        transaction_type: General or AdjustedSellingLevel
                        code:
                    """
                    transaction_type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "TransactionType",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Za-z]+",
                        }
                    )
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Za-z]{2,20}",
                        }
                    )

        @dataclass
        class SellingFareDataList:
            selling_fare_data: List[SellingFareDataType] = field(
                default_factory=list,
                metadata={
                    "name": "SellingFareData",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                }
            )

        @dataclass
        class CommissionData:
            """
            Attributes
                vccinformation:
                cat35_commission_percentage: Cat 35 Commission Percentage
                cat35_commission_amount: Cat 35 Commission Amount
                cat35_markup_amount: Cat 35 Markup Amount in equivalent amount currency
                commission_amount_in_equivalent: Commission Amount in equivalent amount currency
                commission_source: Commission Source [value C for Cat 35, A for AMC, M for Manual]
            """
            vccinformation: List[VccinformationType] = field(
                default_factory=list,
                metadata={
                    "name": "VCCInformation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "max_occurs": 23,
                }
            )
            cat35_commission_percentage: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Cat35CommissionPercentage",
                    "type": "Attribute",
                }
            )
            cat35_commission_amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Cat35CommissionAmount",
                    "type": "Attribute",
                }
            )
            cat35_markup_amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Cat35MarkupAmount",
                    "type": "Attribute",
                }
            )
            commission_amount_in_equivalent: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "CommissionAmountInEquivalent",
                    "type": "Attribute",
                }
            )
            commission_source: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CommissionSource",
                    "type": "Attribute",
                    "length": 1,
                }
            )


@dataclass
class WarningsType:
    warning: List[WarningType] = field(
        default_factory=list,
        metadata={
            "name": "Warning",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )


@dataclass
class ItinTotalFareType(FareType):
    """
    Attributes
        extras: Air Extras total summary amount
        total_with_extras: Total price with Air Extras
        total_mileage:
        service_fee:
    """
    extras: Optional["ItinTotalFareType.Extras"] = field(
        default=None,
        metadata={
            "name": "Extras",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    total_with_extras: Optional["ItinTotalFareType.TotalWithExtras"] = field(
        default=None,
        metadata={
            "name": "TotalWithExtras",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    total_mileage: Optional["ItinTotalFareType.TotalMileage"] = field(
        default=None,
        metadata={
            "name": "TotalMileage",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    service_fee: Optional["ItinTotalFareType.ServiceFee"] = field(
        default=None,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )

    @dataclass
    class Extras:
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TotalWithExtras:
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TotalMileage:
        amount: Optional[str] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ServiceFee:
        """
        Attributes
            amount: Service Fee Amount
            tax_amount: Service Fee Tax
        """
        amount: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Amount",
                "type": "Attribute",
                "required": True,
                "fraction_digits": 3,
            }
        )
        tax_amount: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "TaxAmount",
                "type": "Attribute",
                "required": True,
                "fraction_digits": 3,
            }
        )


@dataclass
class OriginDestinationOptionType:
    """A container for flight segments.

    Attributes
        flight_segment: A container for necessary data to describe one or more legs of a single flight number.
        elapsed_time: Elapsed leg trip time in minutes
    """
    flight_segment: List[BookFlightSegmentType] = field(
        default_factory=list,
        metadata={
            "name": "FlightSegment",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 4,
        }
    )
    elapsed_time: Optional[int] = field(
        default=None,
        metadata={
            "name": "ElapsedTime",
            "type": "Attribute",
        }
    )


@dataclass
class PtcfareBreakdownType:
    """Per passenger type code pricing for this itinerary. Set if fareBreakdown was
    requested.

    Attributes
        passenger_type_quantity: Number of individuals traveling under this PTC
        fare_basis_codes: This is a collection of Fare Basis Codes
        passenger_fare: The total passenger fare with cost breakdown.
        endorsements: Container for endorsements.
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        fare_infos: This is a collection of FareInfo
        pricing_source: Indicates whether the fare is public or private.
        private_fare_type: Private fare type symbol.
        last_ticket_date: Last day to ticket.
        previous_exchange_date: Previous Exchange Date
        reissue_exchange: Indicates whether priced as Reissue or Exchange
    """
    class Meta:
        name = "PTCFareBreakdownType"

    passenger_type_quantity: Optional[PassengerTypeQuantityType] = field(
        default=None,
        metadata={
            "name": "PassengerTypeQuantity",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    fare_basis_codes: Optional["PtcfareBreakdownType.FareBasisCodes"] = field(
        default=None,
        metadata={
            "name": "FareBasisCodes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    passenger_fare: Optional[FareType] = field(
        default=None,
        metadata={
            "name": "PassengerFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    endorsements: Optional["PtcfareBreakdownType.Endorsements"] = field(
        default=None,
        metadata={
            "name": "Endorsements",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["PtcfareBreakdownType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_infos: Optional["PtcfareBreakdownType.FareInfos"] = field(
        default=None,
        metadata={
            "name": "FareInfos",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    pricing_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
            "pattern": r"[0-9A-Z_]{1,13}",
        }
    )
    private_fare_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateFareType",
            "type": "Attribute",
            "length": 1,
        }
    )
    last_ticket_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastTicketDate",
            "type": "Attribute",
        }
    )
    previous_exchange_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousExchangeDate",
            "type": "Attribute",
        }
    )
    reissue_exchange: Optional["PtcfareBreakdownType.ReissueExchange"] = field(
        default=None,
        metadata={
            "name": "ReissueExchange",
            "type": "Attribute",
        }
    )

    @dataclass
    class FareBasisCodes:
        """
        Attributes
            fare_basis_code: Fare basis code for the price for this PTC
        """
        fare_basis_code: List["PtcfareBreakdownType.FareBasisCodes.FareBasisCode"] = field(
            default_factory=list,
            metadata={
                "name": "FareBasisCode",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 400,
            }
        )

        @dataclass
        class FareBasisCode:
            """
            Attributes
                value:
                private_fare_type: Private fare type symbol.
                fare_component_reference_id:
                account_code: Matched Account Code
                mileage: Mileage (AWARD Shopping)
                booking_code: Booking code
                availability_break: Availability break after this segment
                departure_airport_code: Departure point of flight segment.
                arrival_airport_code: Arrival point of flight segment.
                fare_component_begin_airport: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. It represents the origin airport of the fare component.
                fare_component_end_airport: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. It represents the destination airport of the fare component.
                fare_component_directionality: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. If its value is "FROM" it means that fare component origin and destination are ordered the same as the departure and arival airports of the leg. Value "TO" means the opposite ordering of fare component origin and destination.
                gov_carrier: Governing carrier
            """
            value: Optional[str] = field(
                default=None,
                metadata={
                    "min_length": 1,
                    "max_length": 16,
                }
            )
            private_fare_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PrivateFareType",
                    "type": "Attribute",
                    "length": 1,
                }
            )
            fare_component_reference_id: Optional[int] = field(
                default=None,
                metadata={
                    "name": "FareComponentReferenceID",
                    "type": "Attribute",
                }
            )
            account_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "AccountCode",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 20,
                }
            )
            mileage: Optional[int] = field(
                default=None,
                metadata={
                    "name": "Mileage",
                    "type": "Attribute",
                }
            )
            booking_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "BookingCode",
                    "type": "Attribute",
                    "length": 1,
                }
            )
            availability_break: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "AvailabilityBreak",
                    "type": "Attribute",
                }
            )
            departure_airport_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DepartureAirportCode",
                    "type": "Attribute",
                }
            )
            arrival_airport_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ArrivalAirportCode",
                    "type": "Attribute",
                }
            )
            fare_component_begin_airport: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareComponentBeginAirport",
                    "type": "Attribute",
                    "pattern": r"[A-Z]{3}",
                }
            )
            fare_component_end_airport: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareComponentEndAirport",
                    "type": "Attribute",
                    "pattern": r"[A-Z]{3}",
                }
            )
            fare_component_directionality: Optional[FareDirectionality] = field(
                default=None,
                metadata={
                    "name": "FareComponentDirectionality",
                    "type": "Attribute",
                }
            )
            gov_carrier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "GovCarrier",
                    "type": "Attribute",
                    "pattern": r"[0-9A-Z]{2,3}",
                }
            )

    @dataclass
    class Endorsements:
        """
        Attributes
            endorsement: Specifies ticket endorsement information.
            tpa_extensions:
            non_refundable_indicator: Indicates whether the ticket is refundable. If true, the ticket is NOT refundable.
            non_endorsable_indicator: Indicates whether the ticket is endorsable. If true, the ticket is NOT endorsable.
        """
        endorsement: List["PtcfareBreakdownType.Endorsements.Endorsement"] = field(
            default_factory=list,
            metadata={
                "name": "Endorsement",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "max_occurs": 9,
            }
        )
        tpa_extensions: Optional[str] = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        non_refundable_indicator: Optional[bool] = field(
            default=None,
            metadata={
                "name": "NonRefundableIndicator",
                "type": "Attribute",
            }
        )
        non_endorsable_indicator: Optional[bool] = field(
            default=None,
            metadata={
                "name": "NonEndorsableIndicator",
                "type": "Attribute",
            }
        )

        @dataclass
        class Endorsement(FreeTextType):
            pass

    @dataclass
    class TpaExtensions:
        """
        Attributes
            fare_calc_line: Fare calculation line.
            fare_type:
        """
        fare_calc_line: Optional[FareCalcLineType] = field(
            default=None,
            metadata={
                "name": "FareCalcLine",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_type: Optional["PtcfareBreakdownType.TpaExtensions.FareType"] = field(
            default=None,
            metadata={
                "name": "FareType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class FareType:
            value: Optional[str] = field(
                default=None,
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Name",
                    "type": "Attribute",
                }
            )

    @dataclass
    class FareInfos:
        """
        Attributes
            fare_info: Detailed information on individual priced fares
        """
        fare_info: List["PtcfareBreakdownType.FareInfos.FareInfo"] = field(
            default_factory=list,
            metadata={
                "name": "FareInfo",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 10,
            }
        )

        @dataclass
        class FareInfo:
            """
            Attributes
                departure_date: Departure Date for this priced fare.
                fare_reference: FareReference is the booking code.
                rule_info: Information regarding restrictions governing use of the fare.
                marketing_airline: The marketing airline.
                departure_airport: Departure point of flight segment.
                arrival_airport: Arrival point of flight segment.
                tpa_extensions:
                negotiated_fare: Indicator to show if this is a private fare.
                negotiated_fare_code: Code used to identify the private fare.
            """
            departure_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DepartureDate",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            fare_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareReference",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                }
            )
            rule_info: Optional[RuleInfoType] = field(
                default=None,
                metadata={
                    "name": "RuleInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            marketing_airline: List[CompanyNameType] = field(
                default_factory=list,
                metadata={
                    "name": "MarketingAirline",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            departure_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata={
                    "name": "DepartureAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            arrival_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata={
                    "name": "ArrivalAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            tpa_extensions: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            negotiated_fare: bool = field(
                default=False,
                metadata={
                    "name": "NegotiatedFare",
                    "type": "Attribute",
                }
            )
            negotiated_fare_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NegotiatedFareCode",
                    "type": "Attribute",
                }
            )

            @dataclass
            class TpaExtensions:
                seats_remaining: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining"] = field(
                    default=None,
                    metadata={
                        "name": "SeatsRemaining",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                cabin: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Cabin"] = field(
                    default=None,
                    metadata={
                        "name": "Cabin",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                fare_note: List["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.FareNote"] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareNote",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                meal: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Meal"] = field(
                    default=None,
                    metadata={
                        "name": "Meal",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                rule: List["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Rule"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Rule",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )

                @dataclass
                class SeatsRemaining:
                    number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "Number",
                            "type": "Attribute",
                        }
                    )
                    below_min: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "BelowMin",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Cabin:
                    cabin: str = field(
                        default="Economy",
                        metadata={
                            "name": "Cabin",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class FareNote:
                    fare_type_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "FareTypeName",
                            "type": "Attribute",
                        }
                    )
                    priority_level: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "PriorityLevel",
                            "type": "Attribute",
                        }
                    )
                    content_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "ContentID",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Meal:
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Rule:
                    type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Type",
                            "type": "Attribute",
                        }
                    )
                    id: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "ID",
                            "type": "Attribute",
                        }
                    )

    class ReissueExchange(Enum):
        """
        Attributes
            VALUE_1: Priced as Reissue
            VALUE_2: Priced as Exchange
        """
        VALUE_1 = 1
        VALUE_2 = 2


@dataclass
class AirItineraryPricingInfoType:
    """Pricing Information for an Air Itinerary.

    Attributes
        itin_total_fare: Total price of the itinerary
        ptc_fare_breakdowns: This is a collection of PTC Fare Breakdowns
        fare_infos: This is a collection of FareInfo
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        pricing_source: Used to indicate whether the pricing is public or private
        pricing_sub_source: Pricing sub source.
        pseudo_city_code: (MultiPCC) Information about Pseudo City Code for wich the fare was produced.
        brand_id: Used to indicate brand code (e.g. SS for SuperSaver) or type of Fare (e.g. Sale Fare or Full Coach and so on...)
        fare_returned: Boolean to indicate if a fare returned for the BrandID or not (true if fare is returned and false if no fare returned)
        fare_status: Detailed reason why fare could not be returned (when FareReturned="false"). "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable".
        cached_itin: Indicates whether the itin is from Cache. If true, it is from Cache.
        cache_partition: Indicates source partition of cached itin
        cache_partition_priority: Indicates source partition priority of cached itin
        cache_version: Indicates source version of cached itin
        time_to_live: Time to live in cache (in minutes).
        alternate_city_option: Indicates that this option is alternate dates option.
        last_ticket_date: Last day to ticket.
        private_fare_type: Private fare type symbol.
        spanish_family_discount_indicator: Spanish Discount indicator with values of "A", "B", "C" where
                                            "A" indicates Spanish Large Family discount only
                                            "B" indicates Spanish Large Family discount + Spanish Islander discount
                                            "C" indicates Spanish Islander discount only
        flexible_fare_id: If the fare is an additional flexible fare, this is the fare group ID
        previous_exchange_date: Previous Exchange Date
        reissue_exchange: Indicates whether priced as Reissue or Exchange
        advanced_purchase_date:
        purchase_by_date:
    """
    itin_total_fare: Optional[ItinTotalFareType] = field(
        default=None,
        metadata={
            "name": "ItinTotalFare",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    ptc_fare_breakdowns: Optional["AirItineraryPricingInfoType.PtcFareBreakdowns"] = field(
        default=None,
        metadata={
            "name": "PTC_FareBreakdowns",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    fare_infos: Optional["AirItineraryPricingInfoType.FareInfos"] = field(
        default=None,
        metadata={
            "name": "FareInfos",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["AirItineraryPricingInfoType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    pricing_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingSource",
            "type": "Attribute",
            "pattern": r"[0-9A-Z_]{1,13}",
        }
    )
    pricing_sub_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "PricingSubSource",
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"[A-Z_]{1,}",
        }
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
        }
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BrandID",
            "type": "Attribute",
        }
    )
    fare_returned: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FareReturned",
            "type": "Attribute",
        }
    )
    fare_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "FareStatus",
            "type": "Attribute",
        }
    )
    cached_itin: bool = field(
        default=False,
        metadata={
            "name": "CachedItin",
            "type": "Attribute",
        }
    )
    cache_partition: Optional[str] = field(
        default=None,
        metadata={
            "name": "CachePartition",
            "type": "Attribute",
        }
    )
    cache_partition_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "CachePartitionPriority",
            "type": "Attribute",
        }
    )
    cache_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "CacheVersion",
            "type": "Attribute",
        }
    )
    time_to_live: Optional[int] = field(
        default=None,
        metadata={
            "name": "TimeToLive",
            "type": "Attribute",
        }
    )
    alternate_city_option: bool = field(
        default=False,
        metadata={
            "name": "AlternateCityOption",
            "type": "Attribute",
        }
    )
    last_ticket_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastTicketDate",
            "type": "Attribute",
        }
    )
    private_fare_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrivateFareType",
            "type": "Attribute",
            "length": 1,
        }
    )
    spanish_family_discount_indicator: Optional["AirItineraryPricingInfoType.SpanishFamilyDiscountIndicator"] = field(
        default=None,
        metadata={
            "name": "SpanishFamilyDiscountIndicator",
            "type": "Attribute",
        }
    )
    flexible_fare_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "FlexibleFareID",
            "type": "Attribute",
        }
    )
    previous_exchange_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreviousExchangeDate",
            "type": "Attribute",
        }
    )
    reissue_exchange: Optional["AirItineraryPricingInfoType.ReissueExchange"] = field(
        default=None,
        metadata={
            "name": "ReissueExchange",
            "type": "Attribute",
        }
    )
    advanced_purchase_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdvancedPurchaseDate",
            "type": "Attribute",
        }
    )
    purchase_by_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseByDate",
            "type": "Attribute",
        }
    )

    @dataclass
    class PtcFareBreakdowns:
        ptc_fare_breakdown: List[PtcfareBreakdownType] = field(
            default_factory=list,
            metadata={
                "name": "PTC_FareBreakdown",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 20,
            }
        )

    @dataclass
    class FareInfos:
        """
        Attributes
            fare_info: Detailed information on individual priced fares
        """
        fare_info: List["AirItineraryPricingInfoType.FareInfos.FareInfo"] = field(
            default_factory=list,
            metadata={
                "name": "FareInfo",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 10,
            }
        )

        @dataclass
        class FareInfo:
            """
            Attributes
                departure_date: Departure Date for this priced fare.
                fare_reference: FareReference is the booking code.
                rule_info: Information regarding restrictions governing use of the fare.
                marketing_airline: The marketing airline.
                departure_airport: Departure point of flight segment.
                arrival_airport: Arrival point of flight segment.
                tpa_extensions:
                negotiated_fare: Indicator to show if this is a private fare.
                negotiated_fare_code: Code used to identify the private fare.
            """
            departure_date: Optional[str] = field(
                default=None,
                metadata={
                    "name": "DepartureDate",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            fare_reference: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareReference",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                }
            )
            rule_info: Optional[RuleInfoType] = field(
                default=None,
                metadata={
                    "name": "RuleInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            marketing_airline: List[CompanyNameType] = field(
                default_factory=list,
                metadata={
                    "name": "MarketingAirline",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            departure_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata={
                    "name": "DepartureAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            arrival_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata={
                    "name": "ArrivalAirport",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            tpa_extensions: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            negotiated_fare: bool = field(
                default=False,
                metadata={
                    "name": "NegotiatedFare",
                    "type": "Attribute",
                }
            )
            negotiated_fare_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NegotiatedFareCode",
                    "type": "Attribute",
                }
            )

            @dataclass
            class TpaExtensions:
                seats_remaining: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining"] = field(
                    default=None,
                    metadata={
                        "name": "SeatsRemaining",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                cabin: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Cabin"] = field(
                    default=None,
                    metadata={
                        "name": "Cabin",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                fare_note: List["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.FareNote"] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareNote",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                meal: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Meal"] = field(
                    default=None,
                    metadata={
                        "name": "Meal",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                rule: List["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Rule"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Rule",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )

                @dataclass
                class SeatsRemaining:
                    number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "Number",
                            "type": "Attribute",
                        }
                    )
                    below_min: Optional[bool] = field(
                        default=None,
                        metadata={
                            "name": "BelowMin",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Cabin:
                    cabin: str = field(
                        default="Economy",
                        metadata={
                            "name": "Cabin",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class FareNote:
                    fare_type_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "FareTypeName",
                            "type": "Attribute",
                        }
                    )
                    priority_level: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "PriorityLevel",
                            "type": "Attribute",
                        }
                    )
                    content_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "ContentID",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Meal:
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                        }
                    )

                @dataclass
                class Rule:
                    type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Type",
                            "type": "Attribute",
                        }
                    )
                    id: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "ID",
                            "type": "Attribute",
                        }
                    )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            divide_in_party: Indicates if different passenger types are booked in different inventories.
            promo_offer: Promotional offer
            fare_note:
            promo_redemption: Populated if  "Coupon Redemption" rule has been hit. This had been developed for Travelocity but never used.
            rule: Describes a rule that was hit.
            multiple_traveler_groups:
            ancillary_fee_groups: Ancillary fee groups returned
            legs: This is a collection of Leg Information
            unflown_price:
            validating_carrier:
        """
        divide_in_party: Optional["AirItineraryPricingInfoType.TpaExtensions.DivideInParty"] = field(
            default=None,
            metadata={
                "name": "DivideInParty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        promo_offer: Optional["AirItineraryPricingInfoType.TpaExtensions.PromoOffer"] = field(
            default=None,
            metadata={
                "name": "PromoOffer",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        fare_note: List["AirItineraryPricingInfoType.TpaExtensions.FareNote"] = field(
            default_factory=list,
            metadata={
                "name": "FareNote",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        promo_redemption: Optional["AirItineraryPricingInfoType.TpaExtensions.PromoRedemption"] = field(
            default=None,
            metadata={
                "name": "PromoRedemption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        rule: List["AirItineraryPricingInfoType.TpaExtensions.Rule"] = field(
            default_factory=list,
            metadata={
                "name": "Rule",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        multiple_traveler_groups: Optional["AirItineraryPricingInfoType.TpaExtensions.MultipleTravelerGroups"] = field(
            default=None,
            metadata={
                "name": "MultipleTravelerGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        ancillary_fee_groups: Optional["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups"] = field(
            default=None,
            metadata={
                "name": "AncillaryFeeGroups",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        legs: Optional["AirItineraryPricingInfoType.TpaExtensions.Legs"] = field(
            default=None,
            metadata={
                "name": "Legs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        unflown_price: Optional[UnflownPriceType] = field(
            default=None,
            metadata={
                "name": "UnflownPrice",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        validating_carrier: List[ValidatingCarrierInfoType] = field(
            default_factory=list,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class DivideInParty:
            indicator: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Indicator",
                    "type": "Attribute",
                }
            )

        @dataclass
        class PromoOffer:
            """
            Attributes
                promo_id: Promotional offer identifier
                corp_id: Airline identifier.
                content_id: This information comes from Fare Notes Rule fired and is taken by Travelocity to look up detailed data on their database to put on the website.
            """
            promo_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PromoID",
                    "type": "Attribute",
                }
            )
            corp_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CorpID",
                    "type": "Attribute",
                }
            )
            content_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ContentID",
                    "type": "Attribute",
                }
            )

        @dataclass
        class FareNote:
            """
            Attributes
                fare_type_name: Corresponds to data in the Fare Note rule (action target: Fare Type). For example: "PROMOTIONAL"
                priority_level: FareNote Itin priority
                content_id: Corresponds to data in the Fare Note rule (action target: Content ID Action). For example: "112"
            """
            fare_type_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "FareTypeName",
                    "type": "Attribute",
                }
            )
            priority_level: Optional[int] = field(
                default=None,
                metadata={
                    "name": "PriorityLevel",
                    "type": "Attribute",
                }
            )
            content_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ContentID",
                    "type": "Attribute",
                }
            )

        @dataclass
        class PromoRedemption:
            promo_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PromoID",
                    "type": "Attribute",
                }
            )
            eligible: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "Eligible",
                    "type": "Attribute",
                }
            )
            content_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ContentID",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Rule:
            """
            Attributes
                type: Rule type. For example: "Fare Note Itin", "DRE"
                id: Rule ID
            """
            type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                }
            )
            id: Optional[int] = field(
                default=None,
                metadata={
                    "name": "ID",
                    "type": "Attribute",
                }
            )

        @dataclass
        class MultipleTravelerGroups:
            group_number: Optional[int] = field(
                default=None,
                metadata={
                    "name": "GroupNumber",
                    "type": "Attribute",
                }
            )
            primary_group: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "PrimaryGroup",
                    "type": "Attribute",
                }
            )

        @dataclass
        class AncillaryFeeGroups:
            """
            Attributes
                ancillary_fee_group: Ancillary fee group returned
                message: Arbitrary message returned from MIP
            """
            ancillary_fee_group: List["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups.AncillaryFeeGroup"] = field(
                default_factory=list,
                metadata={
                    "name": "AncillaryFeeGroup",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            message: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Message",
                    "type": "Attribute",
                }
            )

            @dataclass
            class AncillaryFeeGroup:
                """
                Attributes
                    ancillary_fee_item: OC Fee returned
                    code: Group code
                    name: Group name
                    message: Arbitrary message returned from MIP
                """
                ancillary_fee_item: List["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups.AncillaryFeeGroup.AncillaryFeeItem"] = field(
                    default_factory=list,
                    metadata={
                        "name": "AncillaryFeeItem",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Name",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                message: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Message",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class AncillaryFeeItem(OcfeeType):
                    pass

        @dataclass
        class Legs:
            leg: List["AirItineraryPricingInfoType.TpaExtensions.Legs.Leg"] = field(
                default_factory=list,
                metadata={
                    "name": "Leg",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Leg:
                """
                Attributes
                    segment:
                    number:
                    brand_id:
                    brand_description:
                    program_name:
                    program_id:
                    program_code:
                    program_system_code:
                    fare_status: Detailed reason why fare could not be returned (when FareReturned="false"). "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable", "N" - unknown status.
                """
                segment: List["AirItineraryPricingInfoType.TpaExtensions.Legs.Leg.Segment"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Segment",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )
                number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Number",
                        "type": "Attribute",
                    }
                )
                brand_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BrandID",
                        "type": "Attribute",
                    }
                )
                brand_description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BrandDescription",
                        "type": "Attribute",
                    }
                )
                program_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramName",
                        "type": "Attribute",
                    }
                )
                program_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramID",
                        "type": "Attribute",
                    }
                )
                program_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramCode",
                        "type": "Attribute",
                    }
                )
                program_system_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ProgramSystemCode",
                        "type": "Attribute",
                    }
                )
                fare_status: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "FareStatus",
                        "type": "Attribute",
                    }
                )

                @dataclass
                class Segment:
                    """
                    Attributes
                        number: Reference to the flight segment
                        program_id:
                        program_description:
                        program_system_code:
                        brand_id:
                        brand_name: Used to indicate brand name
                        fare_status: If possible detailed reason why fare could not be returned. "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable", "N" - unknown status.
                    """
                    number: Optional[int] = field(
                        default=None,
                        metadata={
                            "name": "Number",
                            "type": "Attribute",
                        }
                    )
                    program_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "ProgramID",
                            "type": "Attribute",
                        }
                    )
                    program_description: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "ProgramDescription",
                            "type": "Attribute",
                        }
                    )
                    program_system_code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "ProgramSystemCode",
                            "type": "Attribute",
                        }
                    )
                    brand_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "BrandID",
                            "type": "Attribute",
                        }
                    )
                    brand_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "BrandName",
                            "type": "Attribute",
                        }
                    )
                    fare_status: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "FareStatus",
                            "type": "Attribute",
                        }
                    )

    class SpanishFamilyDiscountIndicator(Enum):
        A = "A"
        B = "B"
        C = "C"

    class ReissueExchange(Enum):
        """
        Attributes
            VALUE_1: Priced as Reissue
            VALUE_2: Priced as Exchange
        """
        VALUE_1 = 1
        VALUE_2 = 2


@dataclass
class AirItineraryType:
    """Specifies the origin and destination of the traveler.

    Attributes
        origin_destination_options: A collection of  OriginDestinationOption
        direction_ind: A directional indicator that identifies a type of air booking (e.g. one-way, round-trip, open-jaw).
        departure_date: Itinerary departure date
    """
    origin_destination_options: Optional["AirItineraryType.OriginDestinationOptions"] = field(
        default=None,
        metadata={
            "name": "OriginDestinationOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    direction_ind: Optional[AirTripType] = field(
        default=None,
        metadata={
            "name": "DirectionInd",
            "type": "Attribute",
        }
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )

    @dataclass
    class OriginDestinationOptions:
        """
        Attributes
            origin_destination_option: A container for flight segments.
        """
        origin_destination_option: List[OriginDestinationOptionType] = field(
            default_factory=list,
            metadata={
                "name": "OriginDestinationOption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )


@dataclass
class TicketPricingType:
    """Pricing Information for Single Ticket.

    Attributes
        origin_destination_options:
        air_itinerary_pricing_info: Pricing Information for a Ticket.
        notes: Provides for free form descriptive information for the priced itinerary.
        ticketing_info: Container for TicketingInfoRS_Type.
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        number: Ticket position related to entire itinerary
    """
    origin_destination_options: Optional["TicketPricingType.OriginDestinationOptions"] = field(
        default=None,
        metadata={
            "name": "OriginDestinationOptions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    air_itinerary_pricing_info: Optional[AirItineraryPricingInfoType] = field(
        default=None,
        metadata={
            "name": "AirItineraryPricingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "required": True,
        }
    )
    notes: List[FreeTextType] = field(
        default_factory=list,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        }
    )
    ticketing_info: Optional[TicketingInfoRsType] = field(
        default=None,
        metadata={
            "name": "TicketingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["TicketPricingType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class OriginDestinationOptions:
        """Indicates which flights are covered by this ticket."""
        origin_destination_option: List["TicketPricingType.OriginDestinationOptions.OriginDestinationOption"] = field(
            default_factory=list,
            metadata={
                "name": "OriginDestinationOption",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )

        @dataclass
        class OriginDestinationOption:
            flight_segment: List["TicketPricingType.OriginDestinationOptions.OriginDestinationOption.FlightSegment"] = field(
                default_factory=list,
                metadata={
                    "name": "FlightSegment",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                    "max_occurs": 4,
                }
            )

            @dataclass
            class FlightSegment:
                """
                Attributes
                    departure_airport: Departure point of flight segment.
                    arrival_airport: Arrival point of flight segment.
                    departure_date_time:
                """
                departure_airport: Optional[ResponseLocationType] = field(
                    default=None,
                    metadata={
                        "name": "DepartureAirport",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                arrival_airport: Optional[ResponseLocationType] = field(
                    default=None,
                    metadata={
                        "name": "ArrivalAirport",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "required": True,
                    }
                )
                departure_date_time: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "DepartureDateTime",
                        "type": "Attribute",
                        "required": True,
                    }
                )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            validating_carrier: Issuing airline whose numeric airline code is reflected in the electronic transaction for the flight/value coupon(s).The Validating Carrier shall be the controlling and authorising entity for Electronic Ticketing transactions..
        """
        validating_carrier: Optional["TicketPricingType.TpaExtensions.ValidatingCarrier"] = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class ValidatingCarrier:
            """
            Attributes
                code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                }
            )


@dataclass
class TicketsPricingType:
    ticket: List[TicketPricingType] = field(
        default_factory=list,
        metadata={
            "name": "Ticket",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )


@dataclass
class PricedItineraryType:
    """Itinerary with pricing information.

    Attributes
        air_itinerary: Specifies the origin and destination of the traveler.
        air_itinerary_pricing_info: Pricing Information for an Air Itinerary.
        notes: Provides for free form descriptive information for the priced itinerary.
        ticketing_info: Container for TicketingInfoRS_Type.
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        is_from_custom_path: Indicates if itin come from custom carrier/routing path.
        sequence_number: Assigns a number to priced itineraries.
        origin_destination_rph: When a PricedItinerary element contains flights and pricing information for a single OriginDestinationPair from the OTA_LowFareSearchRQ message, this RPH attribute identifies that OriginDestinationPair from the RQ. When the PricedItinerary contains flights and pricing information for all OriginDestinationPairs from the OTA_LowFareSearchRQ message, this attribute should not be included.
        campaign_id: Program/campaign ID, which the downline clients need to determine which marketing text to display.
        alternate_airport: Alternate airport itineraries indicator
        multiple_tickets: Indicates that itinerary should be sold on multiple separate tickets
    """
    air_itinerary: Optional[AirItineraryType] = field(
        default=None,
        metadata={
            "name": "AirItinerary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    air_itinerary_pricing_info: List["PricedItineraryType.AirItineraryPricingInfo"] = field(
        default_factory=list,
        metadata={
            "name": "AirItineraryPricingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    notes: List[FreeTextType] = field(
        default_factory=list,
        metadata={
            "name": "Notes",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 5,
        }
    )
    ticketing_info: Optional[TicketingInfoRsType] = field(
        default=None,
        metadata={
            "name": "TicketingInfo",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    tpa_extensions: Optional["PricedItineraryType.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        }
    )
    is_from_custom_path: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isFromCustomPath",
            "type": "Attribute",
        }
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_destination_rph: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginDestinationRPH",
            "type": "Attribute",
            "pattern": r"[0-9]{1,8}",
        }
    )
    campaign_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CampaignID",
            "type": "Attribute",
        }
    )
    alternate_airport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlternateAirport",
            "type": "Attribute",
        }
    )
    multiple_tickets: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MultipleTickets",
            "type": "Attribute",
        }
    )

    @dataclass
    class AirItineraryPricingInfo(AirItineraryPricingInfoType):
        """
        Attributes
            tickets: Pricing information for multiple separate tickets
        """
        tickets: Optional[TicketsPricingType] = field(
            default=None,
            metadata={
                "name": "Tickets",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

    @dataclass
    class TpaExtensions:
        """
        Attributes
            additional_fares:
            ops: Populated if an Ops rule has been hit.
            itin_source: The source of the itinerary
            value_bucket: Additional information for Value Bucket sorting
            validating_carrier: Issuing airline whose numeric airline code is reflected in the electronic transaction for the flight/value coupon(s).The Validating Carrier shall be the controlling and authorising entity for Electronic Ticketing transactions..
            unflown_price: Sum of AirItineraryPricingInfo/TPA_Extensions/UnflownPrice
            diversity_swapper:
            failed: Information on problems that occurred while processing this itinerary.
        """
        additional_fares: List["PricedItineraryType.TpaExtensions.AdditionalFares"] = field(
            default_factory=list,
            metadata={
                "name": "AdditionalFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        ops: Optional["PricedItineraryType.TpaExtensions.Ops"] = field(
            default=None,
            metadata={
                "name": "Ops",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        itin_source: Optional["PricedItineraryType.TpaExtensions.ItinSource"] = field(
            default=None,
            metadata={
                "name": "ItinSource",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        value_bucket: Optional["PricedItineraryType.TpaExtensions.ValueBucket"] = field(
            default=None,
            metadata={
                "name": "ValueBucket",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        validating_carrier: Optional["PricedItineraryType.TpaExtensions.ValidatingCarrier"] = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        unflown_price: Optional[UnflownPriceType] = field(
            default=None,
            metadata={
                "name": "UnflownPrice",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        diversity_swapper: Optional["PricedItineraryType.TpaExtensions.DiversitySwapper"] = field(
            default=None,
            metadata={
                "name": "DiversitySwapper",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )
        failed: Optional["PricedItineraryType.TpaExtensions.Failed"] = field(
            default=None,
            metadata={
                "name": "Failed",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            }
        )

        @dataclass
        class AdditionalFares:
            """
            Attributes
                air_itinerary_pricing_info: Pricing Information for an Air Itinerary.
                notes: Provides for free form descriptive information for the priced itinerary.
                ticketing_info: Information about ticketing (including eTicketNumber).
                multiple_tickets: Indicates that itinerary should be sold on multiple separate tickets
            """
            air_itinerary_pricing_info: Optional["PricedItineraryType.TpaExtensions.AdditionalFares.AirItineraryPricingInfo"] = field(
                default=None,
                metadata={
                    "name": "AirItineraryPricingInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            notes: List[FreeTextType] = field(
                default_factory=list,
                metadata={
                    "name": "Notes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "max_occurs": 5,
                }
            )
            ticketing_info: Optional[TicketingInfoRsType] = field(
                default=None,
                metadata={
                    "name": "TicketingInfo",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            multiple_tickets: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "MultipleTickets",
                    "type": "Attribute",
                }
            )

            @dataclass
            class AirItineraryPricingInfo(AirItineraryPricingInfoType):
                """
                Attributes
                    tickets: Pricing information for multiple separate tickets
                """
                tickets: Optional[TicketsPricingType] = field(
                    default=None,
                    metadata={
                        "name": "Tickets",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                    }
                )

        @dataclass
        class Ops:
            """
            Attributes
                fare_types:
                action_code: Corresponds to data in the Ops rule (action target: Ops Action). The numeric id corresponds to an action performed by Travelocity.
            """
            fare_types: Optional["PricedItineraryType.TpaExtensions.Ops.FareTypes"] = field(
                default=None,
                metadata={
                    "name": "FareTypes",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                }
            )
            action_code: Optional[int] = field(
                default=None,
                metadata={
                    "name": "ActionCode",
                    "type": "Attribute",
                    "required": True,
                }
            )

            @dataclass
            class FareTypes:
                fare_type: List["PricedItineraryType.TpaExtensions.Ops.FareTypes.FareType"] = field(
                    default_factory=list,
                    metadata={
                        "name": "FareType",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class FareType:
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Code",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"[0-9A-Z]{1,3}",
                        }
                    )

        @dataclass
        class ItinSource:
            """
            Attributes
                source: The name of the source.
            """
            source: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Source",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class ValueBucket:
            """
            Attributes
                price_time_value_rank: Price Time Value rank.
                value_bucket_number: Price Time Value Bucket number.
            """
            price_time_value_rank: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "PriceTimeValueRank",
                    "type": "Attribute",
                }
            )
            value_bucket_number: Optional[int] = field(
                default=None,
                metadata={
                    "name": "ValueBucketNumber",
                    "type": "Attribute",
                }
            )

        @dataclass
        class ValidatingCarrier:
            """
            Attributes
                code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[A-Z][0-9A-Z]|[0-9A-Z][A-Z][0-9A-Z]?|[A-Za-z]{0}",
                }
            )

        @dataclass
        class DiversitySwapper:
            """Attributes.

            weighed_price_amount: (Penalty * price / 10) -- by which itins are sorted in Diversity Swapper
            """
            weighed_price_amount: Optional[float] = field(
                default=None,
                metadata={
                    "name": "WeighedPriceAmount",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class Failed:
            """
            Attributes
                minimum_connect_time: Indicates that the itinerary does not fullfill the Minimum Connect Time requirement. It cannot be sold.
            """
            minimum_connect_time: Optional[bool] = field(
                default=None,
                metadata={
                    "name": "MinimumConnectTime",
                    "type": "Attribute",
                }
            )


@dataclass
class OtaAirLowFareSearchRs:
    """The Low Fare Search Response message contains a number of .Priced Itinerary.
    options. Each includes:

            - A set of available flights matching the client.s request.
            - Pricing information including taxes and full fare breakdown for each passenger type
            - Ticketing information
            - Fare Basis Codes and the information necessary to make a rules entry.
            This message contains similar information to a standard airline CRS or GDS Low Fare Search Response message.

    Attributes
        errors: In case of failure errors are returned.
        success: In case of success this element is returned.
        warnings: In case of any warnings this element is returned.
        priced_itineraries: Low Fare priced itineraries container.
        one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        departed_itineraries: Departed Itineraries
        sold_out_itineraries: Sold Out Itineraries
        available_itineraries: Available Itineraries
        tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
        echo_token: A sequence number for additional message identification, assigned by the requesting host system. When a request message includes an echo token the corresponding response message MUST include an echo token with an identical value.
        time_stamp: Indicates the creation date and time of the message in UTC using the following format specified by ISO 8601; YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes 2003-11-20T13:59:38Z).
        target: Used to indicate whether the request is for the Test or Production system.
        version: For all OTA versioned messages, the version of the message is indicated by a decimal value.
        transaction_identifier: A unique identifier to relate all messages within a transaction (e.g. this would be sent in all request and response messages that are part of an on-going transaction).
        sequence_nmbr: Used to identify the sequence number of the transaction as assigned by the sending system; allows for an application to process messages in a certain order or to request a resynchronization of messages in the event that a system has been off-line and needs to retrieve messages that were missed.
        transaction_status_code: This indicates where this message falls within a sequence of messages.
        primary_lang_id: Identifes the primary language preference for the form of travel represented in a collection. The human language is identified by ISO 639 codes.
        alt_lang_id:
        priced_itin_count: Itinerary count for Priced Round-Trip itineraries
        branded_one_way_itin_count: Itinerary count for Branded One-Way itineraries
        simple_one_way_itin_count: Itinerary count for Simple One-Way itineraries
        departed_itin_count: Itinerary count for departed itineraries returned
        sold_out_itin_count: Itinerary count for sold out itineraries returned
        available_itin_count: Itinerary count for available itineraries returned
    """
    class Meta:
        name = "OTA_AirLowFareSearchRS"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    errors: Optional[ErrorsType] = field(
        default=None,
        metadata={
            "name": "Errors",
            "type": "Element",
        }
    )
    success: Optional[str] = field(
        default=None,
        metadata={
            "name": "Success",
            "type": "Element",
        }
    )
    warnings: Optional[WarningsType] = field(
        default=None,
        metadata={
            "name": "Warnings",
            "type": "Element",
        }
    )
    priced_itineraries: Optional["OtaAirLowFareSearchRs.PricedItineraries"] = field(
        default=None,
        metadata={
            "name": "PricedItineraries",
            "type": "Element",
        }
    )
    one_way_itineraries: Optional["OtaAirLowFareSearchRs.OneWayItineraries"] = field(
        default=None,
        metadata={
            "name": "OneWayItineraries",
            "type": "Element",
        }
    )
    departed_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries"] = field(
        default=None,
        metadata={
            "name": "DepartedItineraries",
            "type": "Element",
        }
    )
    sold_out_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries"] = field(
        default=None,
        metadata={
            "name": "SoldOutItineraries",
            "type": "Element",
        }
    )
    available_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries"] = field(
        default=None,
        metadata={
            "name": "AvailableItineraries",
            "type": "Element",
        }
    )
    tpa_extensions: Optional["OtaAirLowFareSearchRs.TpaExtensions"] = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
        }
    )
    echo_token: Optional[str] = field(
        default=None,
        metadata={
            "name": "EchoToken",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeStamp",
            "type": "Attribute",
        }
    )
    target: OtaAirLowFareSearchRsTarget = field(
        default=OtaAirLowFareSearchRsTarget.PRODUCTION,
        metadata={
            "name": "Target",
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    transaction_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 32,
        }
    )
    sequence_nmbr: Optional[Union[int, bool]] = field(
        default=None,
        metadata={
            "name": "SequenceNmbr",
            "type": "Attribute",
        }
    )
    transaction_status_code: Optional["OtaAirLowFareSearchRs.TransactionStatusCode"] = field(
        default=None,
        metadata={
            "name": "TransactionStatusCode",
            "type": "Attribute",
        }
    )
    primary_lang_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PrimaryLangID",
            "type": "Attribute",
        }
    )
    alt_lang_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "AltLangID",
            "type": "Attribute",
        }
    )
    priced_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PricedItinCount",
            "type": "Attribute",
        }
    )
    branded_one_way_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "BrandedOneWayItinCount",
            "type": "Attribute",
        }
    )
    simple_one_way_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SimpleOneWayItinCount",
            "type": "Attribute",
        }
    )
    departed_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartedItinCount",
            "type": "Attribute",
        }
    )
    sold_out_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SoldOutItinCount",
            "type": "Attribute",
        }
    )
    available_itin_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AvailableItinCount",
            "type": "Attribute",
        }
    )

    @dataclass
    class PricedItineraries:
        """
        Attributes
            tpa_extensions:
            priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
        """
        tpa_extensions: Optional["OtaAirLowFareSearchRs.PricedItineraries.TpaExtensions"] = field(
            default=None,
            metadata={
                "name": "TPA_Extensions",
                "type": "Element",
            }
        )
        priced_itinerary: List[PricedItineraryType] = field(
            default_factory=list,
            metadata={
                "name": "PricedItinerary",
                "type": "Element",
                "min_occurs": 1,
            }
        )

        @dataclass
        class TpaExtensions:
            """
            Attributes
                processing_message: Container for itinerary message type.
            """
            processing_message: List[ComplexProcessingMessageType] = field(
                default_factory=list,
                metadata={
                    "name": "ProcessingMessage",
                    "type": "Element",
                }
            )

    @dataclass
    class OneWayItineraries:
        """
        Attributes
            branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
        """
        branded_one_way_itineraries: List["OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries"] = field(
            default_factory=list,
            metadata={
                "name": "BrandedOneWayItineraries",
                "type": "Element",
                "max_occurs": 10,
            }
        )
        simple_one_way_itineraries: List["OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries"] = field(
            default_factory=list,
            metadata={
                "name": "SimpleOneWayItineraries",
                "type": "Element",
                "max_occurs": 10,
            }
        )

        @dataclass
        class BrandedOneWayItineraries:
            """
            Attributes
                tpa_extensions:
                priced_itinerary: Container for priced itinerary type.
                rph: Leg ID from request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                }
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                }
            )
            rph: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RPH",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{1,8}",
                }
            )

            @dataclass
            class TpaExtensions:
                """
                Attributes
                    processing_message: Container for itinerary message type.
                """
                processing_message: List[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    }
                )

        @dataclass
        class SimpleOneWayItineraries:
            """
            Attributes
                tpa_extensions:
                priced_itinerary: Container for priced itinerary type.
                rph: Leg ID from request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                }
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                }
            )
            rph: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RPH",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9]{1,8}",
                }
            )

            @dataclass
            class TpaExtensions:
                """
                Attributes
                    processing_message: Container for itinerary message type.
                """
                processing_message: List[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    }
                )

    @dataclass
    class DepartedItineraries:
        """
        Attributes
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries"] = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            }
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries"] = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            }
        )

        @dataclass
        class PricedItineraries:
            """
            Attributes
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                }
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class TpaExtensions:
                """
                Attributes
                    processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    }
                )

        @dataclass
        class OneWayItineraries:
            """
            Attributes
                branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

    @dataclass
    class SoldOutItineraries:
        """
        Attributes
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries"] = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            }
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries"] = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            }
        )

        @dataclass
        class PricedItineraries:
            """
            Attributes
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                }
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class TpaExtensions:
                """
                Attributes
                    processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    }
                )

        @dataclass
        class OneWayItineraries:
            """
            Attributes
                branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

    @dataclass
    class AvailableItineraries:
        """
        Attributes
            priced_itineraries: Low Fare priced itineraries container.
            one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries"] = field(
            default=None,
            metadata={
                "name": "PricedItineraries",
                "type": "Element",
            }
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries"] = field(
            default=None,
            metadata={
                "name": "OneWayItineraries",
                "type": "Element",
            }
        )

        @dataclass
        class PricedItineraries:
            """
            Attributes
                tpa_extensions:
                priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata={
                    "name": "TPA_Extensions",
                    "type": "Element",
                }
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata={
                    "name": "PricedItinerary",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class TpaExtensions:
                """
                Attributes
                    processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata={
                        "name": "ProcessingMessage",
                        "type": "Element",
                    }
                )

        @dataclass
        class OneWayItineraries:
            """
            Attributes
                branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
                simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "BrandedOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata={
                    "name": "SimpleOneWayItineraries",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                Attributes
                    tpa_extensions:
                    priced_itinerary: Container for priced itinerary type.
                    rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata={
                        "name": "TPA_Extensions",
                        "type": "Element",
                    }
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata={
                        "name": "PricedItinerary",
                        "type": "Element",
                    }
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RPH",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9]{1,8}",
                    }
                )

                @dataclass
                class TpaExtensions:
                    """
                    Attributes
                        processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata={
                            "name": "ProcessingMessage",
                            "type": "Element",
                        }
                    )

    @dataclass
    class TpaExtensions:
        airline_order_list: Optional["OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList"] = field(
            default=None,
            metadata={
                "name": "AirlineOrderList",
                "type": "Element",
            }
        )

        @dataclass
        class AirlineOrderList:
            """
            Attributes
                airline_order: The airline that filed the fare(s).
            """
            airline_order: List["OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList.AirlineOrder"] = field(
                default_factory=list,
                metadata={
                    "name": "AirlineOrder",
                    "type": "Element",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class AirlineOrder(CompanyNameType):
                sequence_number: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "SequenceNumber",
                        "type": "Attribute",
                        "required": True,
                    }
                )

    class TransactionStatusCode(Enum):
        """
        Attributes
            START: This is the first message within a transaction.
            END: This is the last message within a transaction.
            ROLLBACK: This indicates that all messages within the current transaction must be ignored.
            IN_SERIES: This is any message that is not the first or last message within a transaction.
        """
        START = "Start"
        END = "End"
        ROLLBACK = "Rollback"
        IN_SERIES = "InSeries"


@dataclass
class PricedItinerariesType:
    """Container for priced itineraries.

    Attributes
        priced_itinerary: Container for priced itinerary type.
    """
    priced_itinerary: List[PricedItineraryType] = field(
        default_factory=list,
        metadata={
            "name": "PricedItinerary",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        }
    )
