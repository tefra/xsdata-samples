from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional
from samples.sabre.output.bargain_finder_max_common_types_v1_9_7 import (
    AdvResTicketingType,
    AirTripType,
    CompanyNameType,
    EquipmentType,
    FareDirectionality,
    PassengerTypeQuantityType,
    StayRestrictionsType,
)


class ActionCodeType(Enum):
    """
    Identifies the action code for a booking - OK, Waitlist etc.
    :cvar OK:
    :cvar WAITLIST:
    :cvar OTHER:
    """
    OK = "OK"
    WAITLIST = "Waitlist"
    OTHER = "Other"


@dataclass
class AirFeeType:
    """Defines the data fields available for the fees.

    :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
    :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    :ivar amount:
    :ivar value:
    :ivar fee_code: Identifies the code for the fee.
    """
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DecimalPlaces",
            type="Attribute"
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    fee_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FeeCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=16.0
        )
    )


@dataclass
class AirTaxType:
    """Defines the data fields available for air tax.

    :ivar reissue_tax_type: Reissue tax type
    :ivar reissue_restriction_applies:
    :ivar reissue_tax_refundable:
    :ivar apply_to_reissue:
    :ivar reissue_max_amount:
    :ivar reissue_currency: Reissue tax max amount currency
    :ivar published_amount:
    :ivar published_currency:
    :ivar value:
    :ivar tax_code: Identifies the code for the tax.
    :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
    :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    :ivar amount:
    :ivar carrier_code: carrier used for this tax
    :ivar min_amount: Minumum tax amount
    :ivar max_amount: Maximum tax amount
    :ivar min_max_currency: Min/Max tax currency code
    :ivar rate_used: Tax rate used
    :ivar station_code: Airport code at which the tax or surcharge is being applied
    """
    reissue_tax_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReissueTaxType",
            type="Attribute",
            length=1
        )
    )
    reissue_restriction_applies: bool = field(
        default=False,
        metadata=dict(
            name="ReissueRestrictionApplies",
            type="Attribute"
        )
    )
    reissue_tax_refundable: bool = field(
        default=False,
        metadata=dict(
            name="ReissueTaxRefundable",
            type="Attribute"
        )
    )
    apply_to_reissue: bool = field(
        default=False,
        metadata=dict(
            name="ApplyToReissue",
            type="Attribute"
        )
    )
    reissue_max_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="ReissueMaxAmount",
            type="Attribute"
        )
    )
    reissue_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReissueCurrency",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    published_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="PublishedAmount",
            type="Attribute"
        )
    )
    published_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PublishedCurrency",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    tax_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TaxCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=16.0
        )
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DecimalPlaces",
            type="Attribute"
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )
    carrier_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CarrierCode",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    min_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="MinAmount",
            type="Attribute"
        )
    )
    max_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="MaxAmount",
            type="Attribute"
        )
    )
    min_max_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MinMaxCurrency",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    rate_used: Optional[float] = field(
        default=None,
        metadata=dict(
            name="RateUsed",
            type="Attribute"
        )
    )
    station_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StationCode",
            type="Attribute"
        )
    )


@dataclass
class BaggageInformationType:
    """Information about baggage.

    :ivar segment:
    :ivar allowance:
    """
    segment: List["BaggageInformationType.Segment"] = field(
        default_factory=list,
        metadata=dict(
            name="Segment",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    allowance: Optional["BaggageInformationType.Allowance"] = field(
        default=None,
        metadata=dict(
            name="Allowance",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )

    @dataclass
    class Segment:
        """
        :ivar id: Id of segment that current baggage information applies to.
        """
        id: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Id",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class Allowance:
        """
        :ivar pieces: Number of Pieces
        :ivar weight: Weight Limit
        :ivar unit: Units of the Weight Limit
        """
        pieces: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Pieces",
                type="Attribute"
            )
        )
        weight: Optional[int] = field(
            default=None,
            metadata=dict(
                name="Weight",
                type="Attribute"
            )
        )
        unit: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Unit",
                type="Attribute"
            )
        )


@dataclass
class CouponOfferType:
    """Not used.

    :ivar promo_id:
    :ivar corp_id:
    :ivar headline:
    :ivar discount_pctg:
    """
    promo_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="promo_id",
            type="Attribute"
        )
    )
    corp_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="corp_id",
            type="Attribute"
        )
    )
    headline: Optional[str] = field(
        default=None,
        metadata=dict(
            name="headline",
            type="Attribute"
        )
    )
    discount_pctg: Optional[str] = field(
        default=None,
        metadata=dict(
            name="discount_pctg",
            type="Attribute"
        )
    )


@dataclass
class CurrencyAmountType:
    """Provides a monetary amount and the code of the currency in which this amount
    is expressed.

    :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
    :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    :ivar amount:
    """
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DecimalPlaces",
            type="Attribute"
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )


@dataclass
class CurrencyConversionsType:
    """
    :ivar conversion:
    """
    conversion: Optional["CurrencyConversionsType.Conversion"] = field(
        default=None,
        metadata=dict(
            name="Conversion",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )

    @dataclass
    class Conversion:
        """
        :ivar from_value:
        :ivar to:
        :ivar rate_of_exchange: Exchange rate
        """
        from_value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="From",
                type="Attribute",
                pattern=r"[a-zA-Z]{3}"
            )
        )
        to: Optional[str] = field(
            default=None,
            metadata=dict(
                name="To",
                type="Attribute",
                pattern=r"[a-zA-Z]{3}"
            )
        )
        rate_of_exchange: Optional[float] = field(
            default=None,
            metadata=dict(
                name="RateOfExchange",
                type="Attribute"
            )
        )


@dataclass
class FareCalcLineType:
    """IntelliSell Type.

    :ivar info:
    """
    info: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Info",
            type="Attribute"
        )
    )


@dataclass
class FareComponentBreakdownType:
    """Fare Component Breakdown.

    :ivar fare_component_reference_id:
    :ivar fare_component_commission: Commission Amount per Fare Component
    :ivar rule_id: Commission Rule ID
    :ivar program_id: Commission Program ID
    :ivar contract_id: Commission Contract ID
    """
    fare_component_reference_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FareComponentReferenceID",
            type="Attribute"
        )
    )
    fare_component_commission: Optional[float] = field(
        default=None,
        metadata=dict(
            name="FareComponentCommission",
            type="Attribute",
            fraction_digits=3
        )
    )
    rule_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="RuleID",
            type="Attribute"
        )
    )
    program_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ProgramID",
            type="Attribute"
        )
    )
    contract_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ContractID",
            type="Attribute"
        )
    )


@dataclass
class FareGroupType:
    """IntelliSell Type.

    :ivar fare_type_name:
    """
    fare_type_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareTypeName",
            type="Attribute"
        )
    )


@dataclass
class FareMessagesType:
    """
    :ivar message:
    """
    message: Optional["FareMessagesType.Message"] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )

    @dataclass
    class Message:
        """
        :ivar airline_code:
        :ivar type:
        :ivar fail_code:
        :ivar info: Message text
        """
        airline_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="AirlineCode",
                type="Attribute",
                min_length=1.0,
                max_length=8.0
            )
        )
        type: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Type",
                type="Attribute",
                length=1
            )
        )
        fail_code: Optional[int] = field(
            default=None,
            metadata=dict(
                name="FailCode",
                type="Attribute"
            )
        )
        info: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Info",
                type="Attribute"
            )
        )


@dataclass
class FreeTextType:
    """Textual information to provide descriptions and/or additional information.

    :ivar language: Language identification.
    :ivar value:
    """
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Language",
            type="Attribute"
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class HandlingMarkupSummaryType:
    """
    :ivar type_code: Value M: Embedded Mark Up, J: Adjusted Selling, H: Handling Fee, G: GST Taxes
    :ivar description: Max 10 chars
    :ivar monetary_amount_value: Can be negative. This is in equivalent amount currency.
    """
    type_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TypeCode",
            type="Attribute",
            required=True,
            length=1
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            required=True
        )
    )
    monetary_amount_value: Optional[float] = field(
        default=None,
        metadata=dict(
            name="MonetaryAmountValue",
            type="Attribute",
            required=True,
            fraction_digits=3
        )
    )


class MessageClassType(Enum):
    """Definies the available messaage class type.

    :cvar E: Error
    :cvar W: Warrning
    :cvar D: Diagnostic
    :cvar I: Info
    """
    E = "E"
    W = "W"
    D = "D"
    I = "I"


@dataclass
class ObfeeType:
    """Defines the data fields available for the ob fees.

    :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
    :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    :ivar amount:
    :ivar type: OB Fee sub type code
    :ivar description: OB Fee description
    """
    class Meta:
        name = "OBFeeType"

    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DecimalPlaces",
            type="Attribute"
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )


@dataclass
class OcfeeType:
    """OC Fee details.

    :ivar amount: Fee amount
    :ivar description: Fee description
    :ivar origin_airport: Origin airport
    :ivar destination_airport: Destination airport
    :ivar carrier: Operating carrier code
    :ivar passenger_code: Ancillary fee code
    :ivar date: Date for this fee.
    :ivar start_segment: Start travel segment
    :ivar end_segment: End travel segment
    """
    class Meta:
        name = "OCFeeType"

    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            required=True,
            fraction_digits=3
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute"
        )
    )
    origin_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginAirport",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    destination_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DestinationAirport",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    passenger_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PassengerCode",
            type="Attribute",
            required=True,
            pattern=r"[A-Za-z0-9]{2,3}"
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Attribute"
        )
    )
    start_segment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="StartSegment",
            type="Attribute",
            required=True
        )
    )
    end_segment: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EndSegment",
            type="Attribute",
            required=True
        )
    )


class PollingStatusType(Enum):
    """
    :cvar RECEIVED:
    :cvar IN_PROGRESS:
    :cvar COMPLETE:
    :cvar ERROR:
    """
    RECEIVED = "received"
    IN_PROGRESS = "in progress"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass
class ProcessingMessageType:
    """Message generated per for particular date and leg.

    :ivar pricing_source: Pricing source.
    :ivar message: Message text
    """
    pricing_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingSource",
            type="Attribute",
            required=True,
            pattern=r"[0-9A-Z_]{1,13}"
        )
    )
    message: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            required=True
        )
    )


@dataclass
class RateOfExchangeType:
    """
    :ivar value: Exchange rate
    """
    value: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute"
        )
    )


@dataclass
class ReissueInfoType:
    """Defines the data fields available for the reissue info type.

    :ivar change_fees:
    :ivar residual_idicator:
    :ivar type_of_service_fee:
    :ivar type_of_reissue_transaction:
    :ivar reissue_result_from_tag:
    :ivar form_of_refund:
    :ivar reissue_requires_electronic_ticket:
    :ivar reissue_does_not_allow_electronic_ticket:
    :ivar tax_refundable:
    """
    change_fees: Optional["ReissueInfoType.ChangeFees"] = field(
        default=None,
        metadata=dict(
            name="ChangeFees",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    residual_idicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResidualIdicator",
            type="Attribute"
        )
    )
    type_of_service_fee: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TypeOfServiceFee",
            type="Attribute"
        )
    )
    type_of_reissue_transaction: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TypeOfReissueTransaction",
            type="Attribute"
        )
    )
    reissue_result_from_tag: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReissueResultFromTag",
            type="Attribute"
        )
    )
    form_of_refund: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FormOfRefund",
            type="Attribute"
        )
    )
    reissue_requires_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReissueRequiresElectronicTicket",
            type="Attribute"
        )
    )
    reissue_does_not_allow_electronic_ticket: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="ReissueDoesNotAllowElectronicTicket",
            type="Attribute"
        )
    )
    tax_refundable: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="TaxRefundable",
            type="Attribute"
        )
    )

    @dataclass
    class ChangeFees:
        """
        :ivar change_fee:
        """
        change_fee: Optional["ReissueInfoType.ChangeFees.ChangeFee"] = field(
            default=None,
            metadata=dict(
                name="ChangeFee",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                required=True
            )
        )

        @dataclass
        class ChangeFee:
            """
            :ivar highest_change_fee:
            :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
            :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
            :ivar amount:
            :ivar change_fee_waived:
            :ivar change_fee_not_applicable:
            """
            highest_change_fee: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="HighestChangeFee",
                    type="Attribute"
                )
            )
            currency_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CurrencyCode",
                    type="Attribute",
                    pattern=r"[a-zA-Z]{3}"
                )
            )
            decimal_places: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="DecimalPlaces",
                    type="Attribute"
                )
            )
            amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Amount",
                    type="Attribute",
                    fraction_digits=3
                )
            )
            change_fee_waived: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="ChangeFeeWaived",
                    type="Attribute"
                )
            )
            change_fee_not_applicable: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="ChangeFeeNotApplicable",
                    type="Attribute"
                )
            )


@dataclass
class ResponseLocationType:
    """Code and optional string to describe a location point.

    :ivar value:
    :ivar location_code: Location identifying code.
    :ivar code_context: Identifies the context of the identifying code, such as IATA, ARC, or internal code, etc.
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    location_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LocationCode",
            type="Attribute",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    code_context: str = field(
        default="IATA",
        metadata=dict(
            name="CodeContext",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class SuccessType:
    """Standard way to indicate successful processing of an OTA message. Returning
    an empty element of this type indicates success.

    :ivar value:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )


@dataclass
class SurchargesType:
    """
    :ivar value:
    :ivar ind:
    :ivar type:
    """
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Extension"
        )
    )
    ind: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Ind",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute"
        )
    )


class TicketType(Enum):
    """Paper or e-ticket.

    :cvar E_TICKET:
    :cvar PAPER:
    """
    E_TICKET = "eTicket"
    PAPER = "Paper"


@dataclass
class UnflownPriceType:
    """Totally Unflown Itinerary Price Information.

    :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
    :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
    :ivar amount:
    """
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            pattern=r"[a-zA-Z]{3}"
        )
    )
    decimal_places: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DecimalPlaces",
            type="Attribute"
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            fraction_digits=3
        )
    )


class ValidInterlineType(Enum):
    """
    :cvar YES:
    :cvar NO:
    :cvar UNKNOWN:
    """
    YES = "Yes"
    NO = "No"
    UNKNOWN = "Unknown"


@dataclass
class ValidatingCarrierInfoType:
    """
    :ivar default: Default validating carrier code
    :ivar alternate: Alternate validating carrier code
    :ivar settlement_method:
    :ivar new_vcx_process:
    """
    default: Optional["ValidatingCarrierInfoType.Default"] = field(
        default=None,
        metadata=dict(
            name="Default",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    alternate: List["ValidatingCarrierInfoType.Alternate"] = field(
        default_factory=list,
        metadata=dict(
            name="Alternate",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=24
        )
    )
    settlement_method: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SettlementMethod",
            type="Attribute",
            min_length=3.0,
            max_length=3.0
        )
    )
    new_vcx_process: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="NewVcxProcess",
            type="Attribute"
        )
    )

    @dataclass
    class Default:
        """
        :ivar country:
        :ivar code:
        """
        country: List["ValidatingCarrierInfoType.Default.Country"] = field(
            default_factory=list,
            metadata=dict(
                name="Country",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                pattern=r"[A-Za-z]{0}"
            )
        )

        @dataclass
        class Country:
            """
            :ivar code:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[a-zA-Z]{2}"
                )
            )

    @dataclass
    class Alternate:
        """
        :ivar country:
        :ivar code:
        """
        country: List["ValidatingCarrierInfoType.Alternate.Country"] = field(
            default_factory=list,
            metadata=dict(
                name="Country",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Code",
                type="Attribute",
                pattern=r"[0-9A-Z]{2,3}"
            )
        )

        @dataclass
        class Country:
            """
            :ivar code:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[a-zA-Z]{2}"
                )
            )


@dataclass
class AirlineLowestFaresType:
    """IntelliSell Type . lowest fare for airline. Currently not used.

    :ivar airline:
    :ivar no_stops:
    :ivar lowest_fare:
    :ivar itinerary_count:
    """
    airline: Optional[CompanyNameType] = field(
        default=None,
        metadata=dict(
            name="Airline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    no_stops: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NoStops",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="LowestFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    itinerary_count: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ItineraryCount",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )


@dataclass
class AirportInformationType(ResponseLocationType):
    """Code and optional string to describe a location point.

    :ivar terminal_id: Location terminal identifier.
    """
    terminal_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TerminalID",
            type="Attribute",
            pattern=r"[0-9A-Z]{1,}"
        )
    )


@dataclass
class AlternateDateLowestFaresType:
    """IntelliSell Type . lowest fare for alternate departure / return date times.

    :ivar departure_date_time:
    :ivar returnl_date_time:
    :ivar lowest_fare:
    """
    departure_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    returnl_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ReturnlDateTime",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="LowestFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )


@dataclass
class AlternateLocationLowestFaresType:
    """IntelliSell Type . lowest fare for alternate origin / destination pair.

    :ivar origin_location:
    :ivar destination_location:
    :ivar lowest_fare:
    """
    origin_location: Optional[ResponseLocationType] = field(
        default=None,
        metadata=dict(
            name="OriginLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    destination_location: Optional[ResponseLocationType] = field(
        default=None,
        metadata=dict(
            name="DestinationLocation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    lowest_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="LowestFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )


@dataclass
class BaggageInformationListType:
    """
    :ivar baggage_information:
    """
    baggage_information: List[BaggageInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageInformation",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ComplexProcessingMessageType(ProcessingMessageType):
    """
    :ivar leg: Optional list of departure dates for each leg
    """
    leg: List["ComplexProcessingMessageType.Leg"] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=10
        )
    )

    @dataclass
    class Leg:
        """
        :ivar departure_date: Departure date
        """
        departure_date: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DepartureDate",
                type="Attribute",
                required=True
            )
        )


@dataclass
class ErrorType(FreeTextType):
    """Standard way to indicate that an error occurred during the processing of an
    OTA message.

    :ivar type: The Error element MUST contain the Type attribute that uses a recommended set of values to indicate the error type. The validating XSD can expect to accept values that it has NOT been explicitly coded for and process them by using Type ="Unknown". Refer to OTA Code List Error Warning Type (EWT).
    :ivar short_text:
    :ivar code: If present, this refers to a table of coded values exchanged between applications to identify errors or warnings. Refer to OTA Code List Error Codes (ERR).
    :ivar doc_url: If present, this URL refers to an online description of the error that occurred.
    :ivar status: If present, recommended values are those enumerated in the OTA_ErrorRS, (NotProcessed | Incomplete | Complete | Unknown) however, the data type is designated as string data, recognizing that trading partners may identify additional status conditions not included in the enumeration.
    :ivar tag: If present, this attribute may identify an unknown or misspelled tag that caused an error in processing. It is recommended that the Tag attribute use XPath notation to identify the location of a tag in the event that more than one tag of the same name is present in the document. Alternatively, the tag name alone can be used to identify missing data [Type=ReqFieldMissing].
    :ivar record_id: If present, this attribute allows for batch processing and the identification of the record that failed amongst a group of records.
    :ivar message_class: If present specify the message class.
    :ivar node_list: An XPath expression that selects all the nodes whose data caused this error. Further, this expression should have an additional contraint which contains the data of the node. This will provide the offending data back to systems that cannot maintain the original message.
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )
    short_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ShortText",
            type="Attribute"
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )
    doc_url: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocURL",
            type="Attribute"
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    tag: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute"
        )
    )
    record_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RecordID",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    message_class: Optional[MessageClassType] = field(
        default=None,
        metadata=dict(
            name="MessageClass",
            type="Attribute"
        )
    )
    node_list: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NodeList",
            type="Attribute"
        )
    )


@dataclass
class FareComponentTaxesType:
    """
    :ivar flight_segment: A container for necessary data to describe one or more flight segments.
    :ivar tax: Any individual tax applied to the fare
    """
    flight_segment: List["FareComponentTaxesType.FlightSegment"] = field(
        default_factory=list,
        metadata=dict(
            name="FlightSegment",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    tax: List[AirTaxType] = field(
        default_factory=list,
        metadata=dict(
            name="Tax",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=99
        )
    )

    @dataclass
    class FlightSegment:
        """
        :ivar departure_airport_code: Departure point of flight segment.
        :ivar arrival_airport_code: Arrival point of flight segment.
        """
        departure_airport_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="DepartureAirportCode",
                type="Attribute"
            )
        )
        arrival_airport_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="ArrivalAirportCode",
                type="Attribute"
            )
        )


@dataclass
class OneWayProcessingMessageType(ProcessingMessageType):
    """
    :ivar departure_date: Departure date
    :ivar departure_airport: Location identifying code.
    :ivar arrival_airport: Location identifying code.
    """
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute"
        )
    )
    departure_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureAirport",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    arrival_airport: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalAirport",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )


@dataclass
class OperatingAirlineType(CompanyNameType):
    """This is an extension of CompanyNameType to include a FlightNumber.

    :ivar flight_number:
    """
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            pattern=r"[0-9]{1,4}[A-Z]?"
        )
    )


@dataclass
class RuleInfoType:
    """Contains summary fare rule information as well as detailed Rule Information
    for Fare Basis Codes. Information may be actual rules data or the results
    returned from a rules-based inquiry.

    :ivar res_ticketing_rules: General container for rules regarding fare reservation, ticketing and sale restrictions
    :ivar length_of_stay_rules: Rules providing minimum or maximum stay restrictions.
    """
    res_ticketing_rules: Optional["RuleInfoType.ResTicketingRules"] = field(
        default=None,
        metadata=dict(
            name="ResTicketingRules",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    length_of_stay_rules: Optional[StayRestrictionsType] = field(
        default=None,
        metadata=dict(
            name="LengthOfStayRules",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )

    @dataclass
    class ResTicketingRules:
        """
        :ivar adv_res_ticketing: Container for holding rules regarding advance reservation or ticketing restrictions.
        """
        adv_res_ticketing: Optional[AdvResTicketingType] = field(
            default=None,
            metadata=dict(
                name="AdvResTicketing",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )


@dataclass
class SellingFareDataType:
    """
    :ivar handling_markup_summary:
    :ivar layer_type_name:
    """
    handling_markup_summary: List[HandlingMarkupSummaryType] = field(
        default_factory=list,
        metadata=dict(
            name="HandlingMarkupSummary",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    layer_type_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LayerTypeName",
            type="Attribute",
            required=True
        )
    )


@dataclass
class TicketingInfoRsType:
    """Extends TicketingInfoType to provide an eTicketNumber.

    :ivar ticket_advisory: Open text field available for additional ticket information.
    :ivar tpa_extensions: Place holder for additional elements.
    :ivar e_ticket_number: If reservation is electronically ticketed at time of booking, this is the field for the eTicket number.
    :ivar ticket_time_limit: TicketTimeLimit - Indicates the ticketing arrangement, and allows for the requirement that an itinerary must be ticketed by a certain date and time.
    :ivar ticket_type: TicketType - Indicates the type of ticket (Paper, eTicket)
    :ivar valid_interline: ValidInterline - Indicates validation of interline ticketing aggrement, possible values (Yes, No, Unknown), default=unknown
    """
    class Meta:
        name = "TicketingInfoRS_Type"

    ticket_advisory: List[FreeTextType] = field(
        default_factory=list,
        metadata=dict(
            name="TicketAdvisory",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=10
        )
    )
    tpa_extensions: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    e_ticket_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="eTicketNumber",
            type="Attribute",
            pattern=r"[0-9a-zA-Z]{1,14}"
        )
    )
    ticket_time_limit: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TicketTimeLimit",
            type="Attribute"
        )
    )
    ticket_type: Optional[TicketType] = field(
        default=None,
        metadata=dict(
            name="TicketType",
            type="Attribute",
            required=True
        )
    )
    valid_interline: ValidInterlineType = field(
        default="Unknown",
        metadata=dict(
            name="ValidInterline",
            type="Attribute"
        )
    )


@dataclass
class VccinformationType:
    """Validating Carrier Commission Information.

    :ivar fare_component_breakdown:
    :ivar validating_carrier:
    :ivar commission_amount: Commission Amount (in equivalent amount currency)
    :ivar total_amount_including_mark_up: Total Commision amount including Mark-Up
    :ivar commission_percent:
    """
    class Meta:
        name = "VCCInformationType"

    fare_component_breakdown: List[FareComponentBreakdownType] = field(
        default_factory=list,
        metadata=dict(
            name="FareComponentBreakdown",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=24
        )
    )
    validating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ValidatingCarrier",
            type="Attribute",
            pattern=r"[0-9A-Z]{2,3}"
        )
    )
    commission_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="CommissionAmount",
            type="Attribute",
            required=True,
            fraction_digits=3
        )
    )
    total_amount_including_mark_up: Optional[float] = field(
        default=None,
        metadata=dict(
            name="TotalAmountIncludingMarkUp",
            type="Attribute",
            fraction_digits=3
        )
    )
    commission_percent: Optional[float] = field(
        default=None,
        metadata=dict(
            name="CommissionPercent",
            type="Attribute",
            fraction_digits=3
        )
    )


@dataclass
class WarningType(FreeTextType):
    """Standard way to indicate successful processing of an OTA message, but one in
    which warnings are generated.

    :ivar short_text:
    :ivar code: If present, this refers to a table of coded values exchanged between applications to identify errors or warnings. Refer to OTA Code List Error Codes (ERR).
    :ivar doc_url: If present, this URL refers to an online description of the error that occurred.
    :ivar status: If present, recommended values are those enumerated in the OTA_ErrorRS, (NotProcessed | Incomplete | Complete | Unknown) however, the data type is designated as string data, recognizing that trading partners may identify additional status conditions not included in the enumeration.
    :ivar tag: If present, this attribute may identify an unknown or misspelled tag that caused an error in processing. It is recommended that the Tag attribute use XPath notation to identify the location of a tag in the event that more than one tag of the same name is present in the document. Alternatively, the tag name alone can be used to identify missing data [Type=ReqFieldMissing].
    :ivar record_id: If present, this attribute allows for batch processing and the identification of the record that failed amongst a group of records.
    :ivar message_class: If present specify the message class.
    :ivar type: The Warning element MUST contain the Type attribute that uses a recommended set of values to indicate the warning type. The validating XSD can expect to accept values that it has NOT been explicitly coded for and process them by using Type ="Unknown". Refer to OTA Code List Error Warning Type (EWT).
    """
    short_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ShortText",
            type="Attribute"
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute"
        )
    )
    doc_url: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DocURL",
            type="Attribute"
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            min_length=1.0,
            max_length=64.0
        )
    )
    tag: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute"
        )
    )
    record_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RecordID",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    message_class: Optional[MessageClassType] = field(
        default=None,
        metadata=dict(
            name="MessageClass",
            type="Attribute"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            required=True
        )
    )


@dataclass
class BookFlightSegmentType:
    """Container for the flight segment data plus the MarriageGrp.

    :ivar departure_airport: Departure point of flight segment.
    :ivar arrival_airport: Arrival point of flight segment.
    :ivar operating_airline: The operating airline of the flight if it is a codeshare flight.
    :ivar equipment: The type of equipment used for the flight..
    :ivar marketing_airline: The marketing airline. This is required for use with scheduled airline messages but may be omitted for requests by tour operators.
    :ivar disclosure_airline: The disclosure airline. This is required by the DOT mandate.
    :ivar marriage_grp: Many airlines link connection flights together by terming them married segments. When two or more segments are married, they must be processed as one unit. The segments must be moved, cancelled, and/or priced together. The value of the marriage group must be the same for all segments.
    :ivar stop_airports:
    :ivar departure_time_zone:
    :ivar arrival_time_zone:
    :ivar on_time_performance:
    :ivar tpa_extensions:
    :ivar departure_date_time:
    :ivar arrival_date_time:
    :ivar stop_quantity: The number of stops the flight makes
    :ivar rph:
    :ivar info_source:
    :ivar flight_number: The flight number of the flight. This is required for use with scheduled airline messages but may be omitted for requests by tour operators.
    :ivar tour_operator_flight_id: ID of a flight in the Tour Operator's inventory. This flight is not necessarily in the inventory of an airline. Rather, it is a code created by tour operators.
    :ivar res_book_desig_code: Specific Booking Class for this segment.
    :ivar action_code:
    :ivar number_in_party:
    :ivar elapsed_time: Elapsed segment trip time.
    """
    departure_airport: Optional[AirportInformationType] = field(
        default=None,
        metadata=dict(
            name="DepartureAirport",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    arrival_airport: Optional[AirportInformationType] = field(
        default=None,
        metadata=dict(
            name="ArrivalAirport",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    operating_airline: Optional[OperatingAirlineType] = field(
        default=None,
        metadata=dict(
            name="OperatingAirline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    equipment: List[EquipmentType] = field(
        default_factory=list,
        metadata=dict(
            name="Equipment",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=2
        )
    )
    marketing_airline: Optional[CompanyNameType] = field(
        default=None,
        metadata=dict(
            name="MarketingAirline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    disclosure_airline: Optional[CompanyNameType] = field(
        default=None,
        metadata=dict(
            name="DisclosureAirline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    marriage_grp: Optional[str] = field(
        default=None,
        metadata=dict(
            name="MarriageGrp",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_length=1.0,
            max_length=16.0
        )
    )
    stop_airports: Optional["BookFlightSegmentType.StopAirports"] = field(
        default=None,
        metadata=dict(
            name="StopAirports",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    departure_time_zone: Optional["BookFlightSegmentType.DepartureTimeZone"] = field(
        default=None,
        metadata=dict(
            name="DepartureTimeZone",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    arrival_time_zone: Optional["BookFlightSegmentType.ArrivalTimeZone"] = field(
        default=None,
        metadata=dict(
            name="ArrivalTimeZone",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    on_time_performance: Optional["BookFlightSegmentType.OnTimePerformance"] = field(
        default=None,
        metadata=dict(
            name="OnTimePerformance",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["BookFlightSegmentType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    departure_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDateTime",
            type="Attribute",
            required=True
        )
    )
    arrival_date_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ArrivalDateTime",
            type="Attribute"
        )
    )
    stop_quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="StopQuantity",
            type="Attribute"
        )
    )
    rph: Optional[str] = field(
        default=None,
        metadata=dict(
            name="RPH",
            type="Attribute",
            pattern=r"[0-9]{1,8}"
        )
    )
    info_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="InfoSource",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    flight_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            pattern=r"[0-9]{1,4}[A-Z]?"
        )
    )
    tour_operator_flight_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TourOperatorFlightID",
            type="Attribute",
            min_length=1.0,
            max_length=8.0
        )
    )
    res_book_desig_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ResBookDesigCode",
            type="Attribute",
            pattern=r"[A-Z\s]{1,2}"
        )
    )
    action_code: Optional[ActionCodeType] = field(
        default=None,
        metadata=dict(
            name="ActionCode",
            type="Attribute"
        )
    )
    number_in_party: Optional[int] = field(
        default=None,
        metadata=dict(
            name="NumberInParty",
            type="Attribute"
        )
    )
    elapsed_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ElapsedTime",
            type="Attribute"
        )
    )

    @dataclass
    class StopAirports:
        """
        :ivar stop_airport: Stop point of flight segment.
        """
        stop_airport: List["BookFlightSegmentType.StopAirports.StopAirport"] = field(
            default_factory=list,
            metadata=dict(
                name="StopAirport",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class StopAirport(ResponseLocationType):
            """
            :ivar arrival_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
            :ivar departure_date_time: This date should be of the form YYYY-MM-DDTHH:MM:SS
            :ivar elapsed_time: Elapsed Time in minutes
            :ivar duration: Layover time in minutes
            :ivar gmtoffset:
            :ivar equipment: Equipment type
            """
            arrival_date_time: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ArrivalDateTime",
                    type="Attribute"
                )
            )
            departure_date_time: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="DepartureDateTime",
                    type="Attribute"
                )
            )
            elapsed_time: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="ElapsedTime",
                    type="Attribute"
                )
            )
            duration: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Duration",
                    type="Attribute"
                )
            )
            gmtoffset: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="GMTOffset",
                    type="Attribute"
                )
            )
            equipment: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Equipment",
                    type="Attribute"
                )
            )

    @dataclass
    class DepartureTimeZone:
        """
        :ivar gmtoffset:
        """
        gmtoffset: Optional[float] = field(
            default=None,
            metadata=dict(
                name="GMTOffset",
                type="Attribute"
            )
        )

    @dataclass
    class ArrivalTimeZone:
        """
        :ivar gmtoffset:
        """
        gmtoffset: Optional[float] = field(
            default=None,
            metadata=dict(
                name="GMTOffset",
                type="Attribute"
            )
        )

    @dataclass
    class OnTimePerformance:
        """
        :ivar level:
        :ivar percentage:
        """
        level: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Level",
                type="Attribute"
            )
        )
        percentage: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Percentage",
                type="Attribute"
            )
        )

    @dataclass
    class TpaExtensions:
        """
        :ivar e_ticket:
        :ivar data_element:
        :ivar message:
        """
        e_ticket: Optional["BookFlightSegmentType.TpaExtensions.ETicket"] = field(
            default=None,
            metadata=dict(
                name="eTicket",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        data_element: Optional["BookFlightSegmentType.TpaExtensions.DataElement"] = field(
            default=None,
            metadata=dict(
                name="DataElement",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        message: Optional["BookFlightSegmentType.TpaExtensions.Message"] = field(
            default=None,
            metadata=dict(
                name="Message",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class ETicket:
            """
            :ivar ind:
            """
            ind: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Ind",
                    type="Attribute"
                )
            )

        @dataclass
        class DataElement:
            """
            :ivar subject_to_government_approval:
            """
            subject_to_government_approval: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="SubjectToGovernmentApproval",
                    type="Attribute"
                )
            )

        @dataclass
        class Message:
            """
            :ivar type:
            :ivar text:
            """
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute"
                )
            )
            text: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Text",
                    type="Attribute"
                )
            )


@dataclass
class ErrorsType:
    """A collection of errors that occurred during the processing of a message.

    :ivar error: Describes an error that occurred during the processing of an OTA message
    """
    error: List[ErrorType] = field(
        default_factory=list,
        metadata=dict(
            name="Error",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class FareInfoType:
    """Rules for this priced option.

    :ivar negotiated_fare: Indicator to show if this is a private fare.
    :ivar negotiated_fare_code: Code used to identify the private fare.
    :ivar departure_date: Departure Date for this priced fare.
    :ivar fare_reference: FareReferenceCode can be used for either the Fare Basis Code or the Fare Class Code.
    :ivar rule_info: Information regarding restrictions governing use of the fare.
    :ivar marketing_airline: The marketing airline.
    :ivar departure_airport: Departure point of flight segment.
    :ivar arrival_airport: Arrival point of flight segment.
    """
    negotiated_fare: bool = field(
        default=False,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute"
        )
    )
    negotiated_fare_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NegotiatedFareCode",
            type="Attribute"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_reference: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareReference",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True,
            min_length=1.0,
            max_length=8.0
        )
    )
    rule_info: Optional[RuleInfoType] = field(
        default=None,
        metadata=dict(
            name="RuleInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    marketing_airline: List[CompanyNameType] = field(
        default_factory=list,
        metadata=dict(
            name="MarketingAirline",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    departure_airport: Optional[ResponseLocationType] = field(
        default=None,
        metadata=dict(
            name="DepartureAirport",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    arrival_airport: Optional[ResponseLocationType] = field(
        default=None,
        metadata=dict(
            name="ArrivalAirport",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )


@dataclass
class FareType:
    """Holds a base fare, tax, total and currency information on a price.

    :ivar negotiated_fare: Indicator to show if this is a private fare.
    :ivar negotiated_fare_code: Code used to identify the private fare.
    :ivar base_fare: Price of the inventory excluding taxes and fees.
    :ivar non_refundable_base_fare: Non-refundable base fare amount
    :ivar fare_construction: Fare construction total amount.
    :ivar equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
    :ivar taxes: This is a collection of Taxes
    :ivar fees: This is a collection of Fees
    :ivar obfees: This is a collection of ob Fees
    :ivar rate_of_exchange:
    :ivar currency_conversions:
    :ivar total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
    :ivar reissue_info_list: Reissue information
    :ivar penalties_info: Penalties information
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    """
    negotiated_fare: bool = field(
        default=False,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute"
        )
    )
    negotiated_fare_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="NegotiatedFareCode",
            type="Attribute"
        )
    )
    base_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    non_refundable_base_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="NonRefundableBaseFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_construction: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="FareConstruction",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    equiv_fare: Optional["FareType.EquivFare"] = field(
        default=None,
        metadata=dict(
            name="EquivFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    taxes: Optional["FareType.Taxes"] = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fees: Optional["FareType.Fees"] = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    obfees: Optional["FareType.Obfees"] = field(
        default=None,
        metadata=dict(
            name="OBFees",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    rate_of_exchange: Optional[RateOfExchangeType] = field(
        default=None,
        metadata=dict(
            name="RateOfExchange",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    currency_conversions: Optional[CurrencyConversionsType] = field(
        default=None,
        metadata=dict(
            name="CurrencyConversions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    total_fare: Optional[CurrencyAmountType] = field(
        default=None,
        metadata=dict(
            name="TotalFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    reissue_info_list: Optional["FareType.ReissueInfoList"] = field(
        default=None,
        metadata=dict(
            name="ReissueInfoList",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    penalties_info: Optional["FareType.PenaltiesInfo"] = field(
        default=None,
        metadata=dict(
            name="PenaltiesInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["FareType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )

    @dataclass
    class EquivFare(CurrencyAmountType):
        """
        :ivar effective_price_deviation: Effective Price Deviation
        """
        effective_price_deviation: Optional[float] = field(
            default=None,
            metadata=dict(
                name="EffectivePriceDeviation",
                type="Attribute",
                fraction_digits=3
            )
        )

    @dataclass
    class Taxes:
        """
        :ivar fare_components_taxes:
        :ivar legs_taxes:
        :ivar tax: Any individual tax applied to the fare
        :ivar total_tax: Total (summary) of taxes applied to the fare
        """
        fare_components_taxes: Optional["FareType.Taxes.FareComponentsTaxes"] = field(
            default=None,
            metadata=dict(
                name="FareComponentsTaxes",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        legs_taxes: Optional["FareType.Taxes.LegsTaxes"] = field(
            default=None,
            metadata=dict(
                name="LegsTaxes",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        tax: List[AirTaxType] = field(
            default_factory=list,
            metadata=dict(
                name="Tax",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=99
            )
        )
        total_tax: Optional[CurrencyAmountType] = field(
            default=None,
            metadata=dict(
                name="TotalTax",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class FareComponentsTaxes:
            """
            :ivar fare_component_taxes:
            """
            fare_component_taxes: List[FareComponentTaxesType] = field(
                default_factory=list,
                metadata=dict(
                    name="FareComponentTaxes",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=99
                )
            )

        @dataclass
        class LegsTaxes:
            """
            :ivar leg_taxes:
            """
            leg_taxes: List["FareType.Taxes.LegsTaxes.LegTaxes"] = field(
                default_factory=list,
                metadata=dict(
                    name="LegTaxes",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=99
                )
            )

            @dataclass
            class LegTaxes:
                """
                :ivar tax: Any individual tax applied to the fare
                :ivar number:
                """
                tax: List[AirTaxType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Tax",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=1,
                        max_occurs=99
                    )
                )
                number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )

    @dataclass
    class Fees:
        """
        :ivar fee: Any additional fee incurred by the passenger but not shown on the ticket.
        """
        fee: List[AirFeeType] = field(
            default_factory=list,
            metadata=dict(
                name="Fee",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=9
            )
        )

    @dataclass
    class Obfees:
        """
        :ivar obfee: OB fees
        :ivar ttype_amount: Total T-type OB Fee
        """
        obfee: List[ObfeeType] = field(
            default_factory=list,
            metadata=dict(
                name="OBFee",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        ttype_amount: Optional[float] = field(
            default=None,
            metadata=dict(
                name="TTypeAmount",
                type="Attribute",
                fraction_digits=3
            )
        )

    @dataclass
    class ReissueInfoList:
        """
        :ivar reissue_info: Reissue Info
        """
        reissue_info: List[ReissueInfoType] = field(
            default_factory=list,
            metadata=dict(
                name="ReissueInfo",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class PenaltiesInfo:
        """
        :ivar penalty: Penalty Info
        """
        penalty: List["FareType.PenaltiesInfo.Penalty"] = field(
            default_factory=list,
            metadata=dict(
                name="Penalty",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class Penalty:
            """
            :ivar cat16_text_only: Missing Data
            :ivar type:
            :ivar applicability:
            :ivar refundable:
            :ivar changeable:
            :ivar conditions_apply:
            :ivar currency_code: A currency code (e.g. USD, EUR, PLN)
            :ivar decimal_places: Indicates the number of decimal places for a particular currency. This is equivalent to the ISO 4217 standard "minor unit".
            :ivar amount:
            :ivar cat16_info:
            """
            cat16_text_only: List["FareType.PenaltiesInfo.Penalty.Cat16TextOnly"] = field(
                default_factory=list,
                metadata=dict(
                    name="Cat16TextOnly",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute"
                )
            )
            applicability: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Applicability",
                    type="Attribute"
                )
            )
            refundable: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Refundable",
                    type="Attribute"
                )
            )
            changeable: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Changeable",
                    type="Attribute"
                )
            )
            conditions_apply: bool = field(
                default=False,
                metadata=dict(
                    name="ConditionsApply",
                    type="Attribute"
                )
            )
            currency_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CurrencyCode",
                    type="Attribute",
                    pattern=r"[a-zA-Z]{3}"
                )
            )
            decimal_places: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="DecimalPlaces",
                    type="Attribute"
                )
            )
            amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Amount",
                    type="Attribute",
                    fraction_digits=3
                )
            )
            cat16_info: bool = field(
                default=False,
                metadata=dict(
                    name="Cat16Info",
                    type="Attribute"
                )
            )

            @dataclass
            class Cat16TextOnly:
                """
                :ivar fare_basis_code: Fare basis code
                :ivar fare_component_id: Fare component Id
                """
                fare_basis_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="FareBasisCode",
                        type="Attribute",
                        required=True,
                        min_length=1.0,
                        max_length=15.0,
                        pattern=r"[A-Z0-9]+(/[A-Z0-9]+)?"
                    )
                )
                fare_component_id: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="FareComponentID",
                        type="Attribute",
                        required=True
                    )
                )

    @dataclass
    class TpaExtensions:
        """
        :ivar surcharges: Surcharge information
        :ivar legs: This is a collection of Leg Information
        :ivar fare_components: A collection of additional information for each Fare Component
        :ivar messages:
        :ivar baggage_information_list:
        :ivar selling_fare_data_list:
        :ivar commission_data:
        """
        surcharges: List[SurchargesType] = field(
            default_factory=list,
            metadata=dict(
                name="Surcharges",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        legs: Optional["FareType.TpaExtensions.Legs"] = field(
            default=None,
            metadata=dict(
                name="Legs",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_components: Optional["FareType.TpaExtensions.FareComponents"] = field(
            default=None,
            metadata=dict(
                name="FareComponents",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        messages: Optional[FareMessagesType] = field(
            default=None,
            metadata=dict(
                name="Messages",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        baggage_information_list: Optional[BaggageInformationListType] = field(
            default=None,
            metadata=dict(
                name="BaggageInformationList",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        selling_fare_data_list: Optional["FareType.TpaExtensions.SellingFareDataList"] = field(
            default=None,
            metadata=dict(
                name="SellingFareDataList",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        commission_data: Optional["FareType.TpaExtensions.CommissionData"] = field(
            default=None,
            metadata=dict(
                name="CommissionData",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class Legs:
            """
            :ivar leg: Leg Information
            """
            leg: List["FareType.TpaExtensions.Legs.Leg"] = field(
                default_factory=list,
                metadata=dict(
                    name="Leg",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class Leg:
                """
                :ivar base_fare: Price of the inventory excluding taxes and fees.
                :ivar equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
                :ivar taxes: This is a collection of Taxes
                :ivar total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
                :ivar total_mileage:
                :ivar number:
                :ivar fare_status:
                """
                base_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata=dict(
                        name="BaseFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        required=True
                    )
                )
                equiv_fare: Optional["FareType.TpaExtensions.Legs.Leg.EquivFare"] = field(
                    default=None,
                    metadata=dict(
                        name="EquivFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                taxes: Optional["FareType.TpaExtensions.Legs.Leg.Taxes"] = field(
                    default=None,
                    metadata=dict(
                        name="Taxes",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                total_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata=dict(
                        name="TotalFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        required=True
                    )
                )
                total_mileage: Optional["FareType.TpaExtensions.Legs.Leg.TotalMileage"] = field(
                    default=None,
                    metadata=dict(
                        name="TotalMileage",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )
                fare_status: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="FareStatus",
                        type="Attribute"
                    )
                )

                @dataclass
                class EquivFare(CurrencyAmountType):
                    """
                    :ivar effective_price_deviation: Effective Price Deviation
                    """
                    effective_price_deviation: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="EffectivePriceDeviation",
                            type="Attribute",
                            fraction_digits=3
                        )
                    )

                @dataclass
                class Taxes:
                    """
                    :ivar tax: Any individual tax applied to the fare
                    """
                    tax: Optional[AirTaxType] = field(
                        default=None,
                        metadata=dict(
                            name="Tax",
                            type="Element",
                            namespace="http://www.opentravel.org/OTA/2003/05",
                            required=True
                        )
                    )

                @dataclass
                class TotalMileage:
                    """
                    :ivar amount:
                    """
                    amount: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Amount",
                            type="Attribute",
                            required=True
                        )
                    )

        @dataclass
        class FareComponents:
            """
            :ivar fare_component: Subtotal pricing summary for Fare Component.
            """
            fare_component: List["FareType.TpaExtensions.FareComponents.FareComponent"] = field(
                default_factory=list,
                metadata=dict(
                    name="FareComponent",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class FareComponent:
                """
                :ivar base_fare: Price of the inventory excluding taxes and fees.
                :ivar equiv_fare: Price of the inventory excluding taxes and fees in the payable currency.
                :ivar taxes: This is a collection of Taxes
                :ivar total_fare: The total price that the passenger would pay (includes fare, taxes, fees)
                :ivar segment:
                :ivar handling_markup_detail:
                :ivar fare_retailer_rule: Matched General Retailer Rule Code or Adjusted Selling Level Retailer Rule Code
                :ivar program_id:
                :ivar program_description: Used to indicate program description
                :ivar program_system_code:
                :ivar brand_id: Used to indicate brand code
                :ivar brand_name: Used to indicate brand name
                """
                base_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata=dict(
                        name="BaseFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                equiv_fare: Optional["FareType.TpaExtensions.FareComponents.FareComponent.EquivFare"] = field(
                    default=None,
                    metadata=dict(
                        name="EquivFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                taxes: Optional["FareType.TpaExtensions.FareComponents.FareComponent.Taxes"] = field(
                    default=None,
                    metadata=dict(
                        name="Taxes",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                total_fare: Optional[CurrencyAmountType] = field(
                    default=None,
                    metadata=dict(
                        name="TotalFare",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                segment: List["FareType.TpaExtensions.FareComponents.FareComponent.Segment"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Segment",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                handling_markup_detail: List["FareType.TpaExtensions.FareComponents.FareComponent.HandlingMarkupDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="HandlingMarkupDetail",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                fare_retailer_rule: List["FareType.TpaExtensions.FareComponents.FareComponent.FareRetailerRule"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="FareRetailerRule",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                program_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramID",
                        type="Attribute"
                    )
                )
                program_description: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramDescription",
                        type="Attribute"
                    )
                )
                program_system_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramSystemCode",
                        type="Attribute"
                    )
                )
                brand_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="BrandID",
                        type="Attribute"
                    )
                )
                brand_name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="BrandName",
                        type="Attribute"
                    )
                )

                @dataclass
                class EquivFare(CurrencyAmountType):
                    """
                    :ivar effective_price_deviation: Effective Price Deviation
                    """
                    effective_price_deviation: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="EffectivePriceDeviation",
                            type="Attribute",
                            fraction_digits=3
                        )
                    )

                @dataclass
                class Taxes:
                    """
                    :ivar tax: Any individual tax applied to the fare
                    """
                    tax: Optional[AirTaxType] = field(
                        default=None,
                        metadata=dict(
                            name="Tax",
                            type="Element",
                            namespace="http://www.opentravel.org/OTA/2003/05",
                            required=True
                        )
                    )

                @dataclass
                class Segment:
                    """
                    :ivar leg_index: Refers to OriginDestinationOption of current itinerary
                    :ivar flight_index: Refers to FlightSegment within OriginDestinationOption of current itinerary
                    """
                    leg_index: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="LegIndex",
                            type="Attribute",
                            required=True
                        )
                    )
                    flight_index: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="FlightIndex",
                            type="Attribute",
                            required=True
                        )
                    )

                @dataclass
                class HandlingMarkupDetail:
                    """
                    :ivar markup_handling_fee_app_id: Markup/Handling fee Application ID
                    :ivar markup_type_code: Markup type code, reserved for future extension
                    :ivar fare_amount_after_markup: Fare Amount after markup
                    :ivar markup_amount: Markup Amount
                    :ivar amount_currency: Markup currency
                    :ivar markup_rule_source_pcc: Markup Rule Source PCC
                    :ivar markup_rule_item_number: Markup Rule Item Number
                    """
                    markup_handling_fee_app_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="MarkupHandlingFeeAppID",
                            type="Attribute"
                        )
                    )
                    markup_type_code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="MarkupTypeCode",
                            type="Attribute"
                        )
                    )
                    fare_amount_after_markup: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="FareAmountAfterMarkup",
                            type="Attribute",
                            fraction_digits=3
                        )
                    )
                    markup_amount: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="MarkupAmount",
                            type="Attribute",
                            fraction_digits=3
                        )
                    )
                    amount_currency: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="AmountCurrency",
                            type="Attribute",
                            pattern=r"[a-zA-Z]{3}"
                        )
                    )
                    markup_rule_source_pcc: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="MarkupRuleSourcePCC",
                            type="Attribute",
                            pattern=r"[0-9A-Z]{3,4}"
                        )
                    )
                    markup_rule_item_number: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="MarkupRuleItemNumber",
                            type="Attribute"
                        )
                    )

                @dataclass
                class FareRetailerRule:
                    """
                    :ivar transaction_type: General or AdjustedSellingLevel
                    :ivar code:
                    """
                    transaction_type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="TransactionType",
                            type="Attribute",
                            required=True,
                            pattern=r"[0-9A-Za-z]+"
                        )
                    )
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Code",
                            type="Attribute",
                            required=True,
                            pattern=r"[0-9A-Za-z]{2,20}"
                        )
                    )

        @dataclass
        class SellingFareDataList:
            """
            :ivar selling_fare_data:
            """
            selling_fare_data: List[SellingFareDataType] = field(
                default_factory=list,
                metadata=dict(
                    name="SellingFareData",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

        @dataclass
        class CommissionData:
            """
            :ivar vccinformation:
            :ivar cat35_commission_percentage: Cat 35 Commission Percentage
            :ivar cat35_commission_amount: Cat 35 Commission Amount
            :ivar cat35_markup_amount: Cat 35 Markup Amount in equivalent amount currency
            :ivar commission_amount_in_equivalent: Commission Amount in equivalent amount currency
            :ivar commission_source: Commission Source [value C for Cat 35, A for AMC, M for Manual]
            """
            vccinformation: List[VccinformationType] = field(
                default_factory=list,
                metadata=dict(
                    name="VCCInformation",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=23
                )
            )
            cat35_commission_percentage: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Cat35CommissionPercentage",
                    type="Attribute"
                )
            )
            cat35_commission_amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Cat35CommissionAmount",
                    type="Attribute"
                )
            )
            cat35_markup_amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="Cat35MarkupAmount",
                    type="Attribute"
                )
            )
            commission_amount_in_equivalent: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="CommissionAmountInEquivalent",
                    type="Attribute"
                )
            )
            commission_source: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CommissionSource",
                    type="Attribute",
                    length=1
                )
            )


@dataclass
class WarningsType:
    """
    :ivar warning:
    """
    warning: List[WarningType] = field(
        default_factory=list,
        metadata=dict(
            name="Warning",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class ItinTotalFareType(FareType):
    """
    :ivar extras: Air Extras total summary amount
    :ivar total_with_extras: Total price with Air Extras
    :ivar total_mileage:
    :ivar service_fee:
    """
    extras: Optional["ItinTotalFareType.Extras"] = field(
        default=None,
        metadata=dict(
            name="Extras",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    total_with_extras: Optional["ItinTotalFareType.TotalWithExtras"] = field(
        default=None,
        metadata=dict(
            name="TotalWithExtras",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    total_mileage: Optional["ItinTotalFareType.TotalMileage"] = field(
        default=None,
        metadata=dict(
            name="TotalMileage",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    service_fee: Optional["ItinTotalFareType.ServiceFee"] = field(
        default=None,
        metadata=dict(
            name="ServiceFee",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )

    @dataclass
    class Extras:
        """
        :ivar amount:
        """
        amount: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Amount",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class TotalWithExtras:
        """
        :ivar amount:
        """
        amount: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Amount",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class TotalMileage:
        """
        :ivar amount:
        """
        amount: Optional[str] = field(
            default=None,
            metadata=dict(
                name="Amount",
                type="Attribute",
                required=True
            )
        )

    @dataclass
    class ServiceFee:
        """
        :ivar amount: Service Fee Amount
        :ivar tax_amount: Service Fee Tax
        """
        amount: Optional[float] = field(
            default=None,
            metadata=dict(
                name="Amount",
                type="Attribute",
                required=True,
                fraction_digits=3
            )
        )
        tax_amount: Optional[float] = field(
            default=None,
            metadata=dict(
                name="TaxAmount",
                type="Attribute",
                required=True,
                fraction_digits=3
            )
        )


@dataclass
class OriginDestinationOptionType:
    """A container for flight segments.

    :ivar flight_segment: A container for necessary data to describe one or more legs of a single flight number.
    :ivar elapsed_time: Elapsed leg trip time in minutes
    """
    flight_segment: List[BookFlightSegmentType] = field(
        default_factory=list,
        metadata=dict(
            name="FlightSegment",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=4
        )
    )
    elapsed_time: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ElapsedTime",
            type="Attribute"
        )
    )


@dataclass
class PtcfareBreakdownType:
    """Per passenger type code pricing for this itinerary. Set if fareBreakdown was
    requested.

    :ivar passenger_type_quantity: Number of individuals traveling under this PTC
    :ivar fare_basis_codes: This is a collection of Fare Basis Codes
    :ivar passenger_fare: The total passenger fare with cost breakdown.
    :ivar endorsements: Container for endorsements.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar fare_infos: This is a collection of FareInfo
    :ivar pricing_source: Indicates whether the fare is public or private.
    :ivar private_fare_type: Private fare type symbol.
    :ivar last_ticket_date: Last day to ticket.
    :ivar previous_exchange_date: Previous Exchange Date
    :ivar reissue_exchange: Indicates whether priced as Reissue or Exchange
    """
    class Meta:
        name = "PTCFareBreakdownType"

    passenger_type_quantity: Optional[PassengerTypeQuantityType] = field(
        default=None,
        metadata=dict(
            name="PassengerTypeQuantity",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    fare_basis_codes: Optional["PtcfareBreakdownType.FareBasisCodes"] = field(
        default=None,
        metadata=dict(
            name="FareBasisCodes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    passenger_fare: Optional[FareType] = field(
        default=None,
        metadata=dict(
            name="PassengerFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    endorsements: Optional["PtcfareBreakdownType.Endorsements"] = field(
        default=None,
        metadata=dict(
            name="Endorsements",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["PtcfareBreakdownType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_infos: Optional["PtcfareBreakdownType.FareInfos"] = field(
        default=None,
        metadata=dict(
            name="FareInfos",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    pricing_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingSource",
            type="Attribute",
            pattern=r"[0-9A-Z_]{1,13}"
        )
    )
    private_fare_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrivateFareType",
            type="Attribute",
            length=1
        )
    )
    last_ticket_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LastTicketDate",
            type="Attribute"
        )
    )
    previous_exchange_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PreviousExchangeDate",
            type="Attribute"
        )
    )
    reissue_exchange: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ReissueExchange",
            type="Attribute"
        )
    )

    @dataclass
    class FareBasisCodes:
        """
        :ivar fare_basis_code: Fare basis code for the price for this PTC
        """
        fare_basis_code: List["PtcfareBreakdownType.FareBasisCodes.FareBasisCode"] = field(
            default_factory=list,
            metadata=dict(
                name="FareBasisCode",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=400
            )
        )

        @dataclass
        class FareBasisCode:
            """
            :ivar value:
            :ivar private_fare_type: Private fare type symbol.
            :ivar fare_component_reference_id:
            :ivar account_code: Matched Account Code
            :ivar mileage: Mileage (AWARD Shopping)
            :ivar booking_code: Booking code
            :ivar availability_break: Availability break after this segment
            :ivar departure_airport_code: Departure point of flight segment.
            :ivar arrival_airport_code: Arrival point of flight segment.
            :ivar fare_component_begin_airport: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. It represents the origin airport of the fare component.
            :ivar fare_component_end_airport: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. It represents the destination airport of the fare component.
            :ivar fare_component_directionality: If this attribute is present, the enclosing FareBasisCode element is the first portion of a new fare component. If its value is "FROM" it means that fare component origin and destination are ordered the same as the departure and arival airports of the leg. Value "TO" means the opposite ordering of fare component origin and destination.
            :ivar gov_carrier: Governing carrier
            """
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="value",
                    type="Restriction",
                    min_length=1.0,
                    max_length=16.0
                )
            )
            private_fare_type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PrivateFareType",
                    type="Attribute",
                    length=1
                )
            )
            fare_component_reference_id: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="FareComponentReferenceID",
                    type="Attribute"
                )
            )
            account_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="AccountCode",
                    type="Attribute",
                    min_length=1.0,
                    max_length=20.0
                )
            )
            mileage: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="Mileage",
                    type="Attribute"
                )
            )
            booking_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="BookingCode",
                    type="Attribute",
                    length=1
                )
            )
            availability_break: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="AvailabilityBreak",
                    type="Attribute"
                )
            )
            departure_airport_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="DepartureAirportCode",
                    type="Attribute"
                )
            )
            arrival_airport_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ArrivalAirportCode",
                    type="Attribute"
                )
            )
            fare_component_begin_airport: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareComponentBeginAirport",
                    type="Attribute",
                    pattern=r"[A-Z]{3}"
                )
            )
            fare_component_end_airport: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareComponentEndAirport",
                    type="Attribute",
                    pattern=r"[A-Z]{3}"
                )
            )
            fare_component_directionality: Optional[FareDirectionality] = field(
                default=None,
                metadata=dict(
                    name="FareComponentDirectionality",
                    type="Attribute"
                )
            )
            gov_carrier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="GovCarrier",
                    type="Attribute",
                    pattern=r"[0-9A-Z]{2,3}"
                )
            )

    @dataclass
    class Endorsements:
        """
        :ivar endorsement: Specifies ticket endorsement information.
        :ivar tpa_extensions:
        :ivar non_refundable_indicator: Indicates whether the ticket is refundable. If true, the ticket is NOT refundable.
        :ivar non_endorsable_indicator: Indicates whether the ticket is endorsable. If true, the ticket is NOT endorsable.
        """
        endorsement: List["PtcfareBreakdownType.Endorsements.Endorsement"] = field(
            default_factory=list,
            metadata=dict(
                name="Endorsement",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9
            )
        )
        tpa_extensions: Optional[str] = field(
            default=None,
            metadata=dict(
                name="TPA_Extensions",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        non_refundable_indicator: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="NonRefundableIndicator",
                type="Attribute"
            )
        )
        non_endorsable_indicator: Optional[bool] = field(
            default=None,
            metadata=dict(
                name="NonEndorsableIndicator",
                type="Attribute"
            )
        )

        @dataclass
        class Endorsement(FreeTextType):
            pass

    @dataclass
    class TpaExtensions:
        """
        :ivar fare_calc_line: Fare calculation line.
        :ivar fare_type:
        """
        fare_calc_line: Optional[FareCalcLineType] = field(
            default=None,
            metadata=dict(
                name="FareCalcLine",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_type: Optional["PtcfareBreakdownType.TpaExtensions.FareType"] = field(
            default=None,
            metadata=dict(
                name="FareType",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class FareType:
            """
            :ivar value:
            :ivar name:
            """
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="value",
                    type="Extension"
                )
            )
            name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Name",
                    type="Attribute"
                )
            )

    @dataclass
    class FareInfos:
        """
        :ivar fare_info: Detailed information on individual priced fares
        """
        fare_info: List["PtcfareBreakdownType.FareInfos.FareInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="FareInfo",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=10
            )
        )

        @dataclass
        class FareInfo:
            """
            :ivar negotiated_fare: Indicator to show if this is a private fare.
            :ivar negotiated_fare_code: Code used to identify the private fare.
            :ivar departure_date: Departure Date for this priced fare.
            :ivar fare_reference: FareReference is the booking code.
            :ivar rule_info: Information regarding restrictions governing use of the fare.
            :ivar marketing_airline: The marketing airline.
            :ivar departure_airport: Departure point of flight segment.
            :ivar arrival_airport: Arrival point of flight segment.
            :ivar tpa_extensions:
            """
            negotiated_fare: bool = field(
                default=False,
                metadata=dict(
                    name="NegotiatedFare",
                    type="Attribute"
                )
            )
            negotiated_fare_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="NegotiatedFareCode",
                    type="Attribute"
                )
            )
            departure_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="DepartureDate",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            fare_reference: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareReference",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True,
                    min_length=1.0,
                    max_length=8.0
                )
            )
            rule_info: Optional[RuleInfoType] = field(
                default=None,
                metadata=dict(
                    name="RuleInfo",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            marketing_airline: List[CompanyNameType] = field(
                default_factory=list,
                metadata=dict(
                    name="MarketingAirline",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            departure_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata=dict(
                    name="DepartureAirport",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            arrival_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata=dict(
                    name="ArrivalAirport",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            tpa_extensions: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar seats_remaining:
                :ivar cabin:
                :ivar fare_note:
                :ivar meal:
                :ivar rule:
                """
                seats_remaining: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining"] = field(
                    default=None,
                    metadata=dict(
                        name="SeatsRemaining",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                cabin: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Cabin"] = field(
                    default=None,
                    metadata=dict(
                        name="Cabin",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                fare_note: List["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.FareNote"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="FareNote",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                meal: Optional["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Meal"] = field(
                    default=None,
                    metadata=dict(
                        name="Meal",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                rule: List["PtcfareBreakdownType.FareInfos.FareInfo.TpaExtensions.Rule"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Rule",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

                @dataclass
                class SeatsRemaining:
                    """
                    :ivar number:
                    :ivar below_min:
                    """
                    number: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="Number",
                            type="Attribute"
                        )
                    )
                    below_min: Optional[bool] = field(
                        default=None,
                        metadata=dict(
                            name="BelowMin",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Cabin:
                    """
                    :ivar cabin:
                    """
                    cabin: str = field(
                        default="Economy",
                        metadata=dict(
                            name="Cabin",
                            type="Attribute"
                        )
                    )

                @dataclass
                class FareNote:
                    """
                    :ivar fare_type_name:
                    :ivar priority_level:
                    :ivar content_id:
                    """
                    fare_type_name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="FareTypeName",
                            type="Attribute"
                        )
                    )
                    priority_level: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="PriorityLevel",
                            type="Attribute"
                        )
                    )
                    content_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ContentID",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Meal:
                    """
                    :ivar code:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Code",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Rule:
                    """
                    :ivar type:
                    :ivar id:
                    """
                    type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Type",
                            type="Attribute"
                        )
                    )
                    id: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="ID",
                            type="Attribute"
                        )
                    )


@dataclass
class AirItineraryPricingInfoType:
    """Pricing Information for an Air Itinerary.

    :ivar pricing_source: Used to indicate whether the pricing is public or private
    :ivar pricing_sub_source: Pricing sub source.
    :ivar pseudo_city_code: (MultiPCC) Information about Pseudo City Code for wich the fare was produced.
    :ivar brand_id: Used to indicate brand code (e.g. SS for SuperSaver) or type of Fare (e.g. Sale Fare or Full Coach and so on...)
    :ivar fare_returned: Boolean to indicate if a fare returned for the BrandID or not (true if fare is returned and false if no fare returned)
    :ivar fare_status: Detailed reason why fare could not be returned (when FareReturned="false"). "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable".
    :ivar cached_itin: Indicates whether the itin is from Cache. If true, it is from Cache.
    :ivar cache_partition: Indicates source partition of cached itin
    :ivar cache_partition_priority: Indicates source partition priority of cached itin
    :ivar cache_version: Indicates source version of cached itin
    :ivar time_to_live: Time to live in cache (in minutes).
    :ivar alternate_city_option: Indicates that this option is alternate dates option.
    :ivar previous_exchange_date: Previous Exchange Date
    :ivar reissue_exchange: Indicates whether priced as Reissue or Exchange
    :ivar advanced_purchase_date:
    :ivar purchase_by_date:
    :ivar itin_total_fare: Total price of the itinerary
    :ivar ptc_fare_breakdowns: This is a collection of PTC Fare Breakdowns
    :ivar fare_infos: This is a collection of FareInfo
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar last_ticket_date: Last day to ticket.
    :ivar private_fare_type: Private fare type symbol.
    :ivar spanish_family_discount_indicator: Spanish Discount indicator with values of "A", "B", "C" where "A" indicates Spanish Large Family discount only "B" indicates Spanish Large Family discount   Spanish Islander discount "C" indicates Spanish Islander discount only
    :ivar flexible_fare_id: If the fare is an additional flexible fare, this is the fare group ID
    """
    pricing_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingSource",
            type="Attribute",
            pattern=r"[0-9A-Z_]{1,13}"
        )
    )
    pricing_sub_source: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PricingSubSource",
            type="Attribute",
            min_length=1.0,
            pattern=r"[A-Z_]{1,}"
        )
    )
    pseudo_city_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute"
        )
    )
    brand_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute"
        )
    )
    fare_returned: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="FareReturned",
            type="Attribute"
        )
    )
    fare_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="FareStatus",
            type="Attribute"
        )
    )
    cached_itin: bool = field(
        default=False,
        metadata=dict(
            name="CachedItin",
            type="Attribute"
        )
    )
    cache_partition: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CachePartition",
            type="Attribute"
        )
    )
    cache_partition_priority: Optional[int] = field(
        default=None,
        metadata=dict(
            name="CachePartitionPriority",
            type="Attribute"
        )
    )
    cache_version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CacheVersion",
            type="Attribute"
        )
    )
    time_to_live: Optional[int] = field(
        default=None,
        metadata=dict(
            name="TimeToLive",
            type="Attribute"
        )
    )
    alternate_city_option: bool = field(
        default=False,
        metadata=dict(
            name="AlternateCityOption",
            type="Attribute"
        )
    )
    previous_exchange_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PreviousExchangeDate",
            type="Attribute"
        )
    )
    reissue_exchange: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ReissueExchange",
            type="Attribute"
        )
    )
    advanced_purchase_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AdvancedPurchaseDate",
            type="Attribute"
        )
    )
    purchase_by_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PurchaseByDate",
            type="Attribute"
        )
    )
    itin_total_fare: Optional[ItinTotalFareType] = field(
        default=None,
        metadata=dict(
            name="ItinTotalFare",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    ptc_fare_breakdowns: Optional["AirItineraryPricingInfoType.PtcFareBreakdowns"] = field(
        default=None,
        metadata=dict(
            name="PTC_FareBreakdowns",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    fare_infos: Optional["AirItineraryPricingInfoType.FareInfos"] = field(
        default=None,
        metadata=dict(
            name="FareInfos",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["AirItineraryPricingInfoType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    last_ticket_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="LastTicketDate",
            type="Attribute"
        )
    )
    private_fare_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrivateFareType",
            type="Attribute",
            length=1
        )
    )
    spanish_family_discount_indicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SpanishFamilyDiscountIndicator",
            type="Attribute"
        )
    )
    flexible_fare_id: Optional[int] = field(
        default=None,
        metadata=dict(
            name="FlexibleFareID",
            type="Attribute"
        )
    )

    @dataclass
    class PtcFareBreakdowns:
        """
        :ivar ptc_fare_breakdown:
        """
        ptc_fare_breakdown: List[PtcfareBreakdownType] = field(
            default_factory=list,
            metadata=dict(
                name="PTC_FareBreakdown",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=20
            )
        )

    @dataclass
    class FareInfos:
        """
        :ivar fare_info: Detailed information on individual priced fares
        """
        fare_info: List["AirItineraryPricingInfoType.FareInfos.FareInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="FareInfo",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=10
            )
        )

        @dataclass
        class FareInfo:
            """
            :ivar negotiated_fare: Indicator to show if this is a private fare.
            :ivar negotiated_fare_code: Code used to identify the private fare.
            :ivar departure_date: Departure Date for this priced fare.
            :ivar fare_reference: FareReference is the booking code.
            :ivar rule_info: Information regarding restrictions governing use of the fare.
            :ivar marketing_airline: The marketing airline.
            :ivar departure_airport: Departure point of flight segment.
            :ivar arrival_airport: Arrival point of flight segment.
            :ivar tpa_extensions:
            """
            negotiated_fare: bool = field(
                default=False,
                metadata=dict(
                    name="NegotiatedFare",
                    type="Attribute"
                )
            )
            negotiated_fare_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="NegotiatedFareCode",
                    type="Attribute"
                )
            )
            departure_date: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="DepartureDate",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            fare_reference: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareReference",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    required=True,
                    min_length=1.0,
                    max_length=8.0
                )
            )
            rule_info: Optional[RuleInfoType] = field(
                default=None,
                metadata=dict(
                    name="RuleInfo",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            marketing_airline: List[CompanyNameType] = field(
                default_factory=list,
                metadata=dict(
                    name="MarketingAirline",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            departure_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata=dict(
                    name="DepartureAirport",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            arrival_airport: Optional[ResponseLocationType] = field(
                default=None,
                metadata=dict(
                    name="ArrivalAirport",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            tpa_extensions: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar seats_remaining:
                :ivar cabin:
                :ivar fare_note:
                :ivar meal:
                :ivar rule:
                """
                seats_remaining: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.SeatsRemaining"] = field(
                    default=None,
                    metadata=dict(
                        name="SeatsRemaining",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                cabin: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Cabin"] = field(
                    default=None,
                    metadata=dict(
                        name="Cabin",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                fare_note: List["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.FareNote"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="FareNote",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                meal: Optional["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Meal"] = field(
                    default=None,
                    metadata=dict(
                        name="Meal",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )
                rule: List["AirItineraryPricingInfoType.FareInfos.FareInfo.TpaExtensions.Rule"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Rule",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

                @dataclass
                class SeatsRemaining:
                    """
                    :ivar number:
                    :ivar below_min:
                    """
                    number: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="Number",
                            type="Attribute"
                        )
                    )
                    below_min: Optional[bool] = field(
                        default=None,
                        metadata=dict(
                            name="BelowMin",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Cabin:
                    """
                    :ivar cabin:
                    """
                    cabin: str = field(
                        default="Economy",
                        metadata=dict(
                            name="Cabin",
                            type="Attribute"
                        )
                    )

                @dataclass
                class FareNote:
                    """
                    :ivar fare_type_name:
                    :ivar priority_level:
                    :ivar content_id:
                    """
                    fare_type_name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="FareTypeName",
                            type="Attribute"
                        )
                    )
                    priority_level: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="PriorityLevel",
                            type="Attribute"
                        )
                    )
                    content_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ContentID",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Meal:
                    """
                    :ivar code:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Code",
                            type="Attribute"
                        )
                    )

                @dataclass
                class Rule:
                    """
                    :ivar type:
                    :ivar id:
                    """
                    type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Type",
                            type="Attribute"
                        )
                    )
                    id: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="ID",
                            type="Attribute"
                        )
                    )

    @dataclass
    class TpaExtensions:
        """
        :ivar divide_in_party: Indicates if different passenger types are booked in different inventories.
        :ivar promo_offer: Promotional offer
        :ivar fare_note:
        :ivar promo_redemption: Populated if "Coupon Redemption" rule has been hit. This had been developed for Travelocity but never used.
        :ivar rule: Describes a rule that was hit.
        :ivar multiple_traveler_groups:
        :ivar ancillary_fee_groups: Ancillary fee groups returned
        :ivar legs: This is a collection of Leg Information
        :ivar unflown_price:
        :ivar validating_carrier:
        """
        divide_in_party: Optional["AirItineraryPricingInfoType.TpaExtensions.DivideInParty"] = field(
            default=None,
            metadata=dict(
                name="DivideInParty",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        promo_offer: Optional["AirItineraryPricingInfoType.TpaExtensions.PromoOffer"] = field(
            default=None,
            metadata=dict(
                name="PromoOffer",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        fare_note: List["AirItineraryPricingInfoType.TpaExtensions.FareNote"] = field(
            default_factory=list,
            metadata=dict(
                name="FareNote",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        promo_redemption: Optional["AirItineraryPricingInfoType.TpaExtensions.PromoRedemption"] = field(
            default=None,
            metadata=dict(
                name="PromoRedemption",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        rule: List["AirItineraryPricingInfoType.TpaExtensions.Rule"] = field(
            default_factory=list,
            metadata=dict(
                name="Rule",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        multiple_traveler_groups: Optional["AirItineraryPricingInfoType.TpaExtensions.MultipleTravelerGroups"] = field(
            default=None,
            metadata=dict(
                name="MultipleTravelerGroups",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        ancillary_fee_groups: Optional["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups"] = field(
            default=None,
            metadata=dict(
                name="AncillaryFeeGroups",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        legs: Optional["AirItineraryPricingInfoType.TpaExtensions.Legs"] = field(
            default=None,
            metadata=dict(
                name="Legs",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        unflown_price: Optional[UnflownPriceType] = field(
            default=None,
            metadata=dict(
                name="UnflownPrice",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        validating_carrier: List[ValidatingCarrierInfoType] = field(
            default_factory=list,
            metadata=dict(
                name="ValidatingCarrier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class DivideInParty:
            """
            :ivar indicator:
            """
            indicator: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Indicator",
                    type="Attribute"
                )
            )

        @dataclass
        class PromoOffer:
            """
            :ivar promo_id: Promotional offer identifier
            :ivar corp_id: Airline identifier.
            :ivar content_id: This information comes from Fare Notes Rule fired and is taken by Travelocity to look up detailed data on their database to put on the website.
            """
            promo_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PromoID",
                    type="Attribute"
                )
            )
            corp_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="CorpID",
                    type="Attribute"
                )
            )
            content_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ContentID",
                    type="Attribute"
                )
            )

        @dataclass
        class FareNote:
            """
            :ivar fare_type_name: Corresponds to data in the Fare Note rule (action target: Fare Type). For example: "PROMOTIONAL"
            :ivar priority_level: FareNote Itin priority
            :ivar content_id: Corresponds to data in the Fare Note rule (action target: Content ID Action). For example: "112"
            """
            fare_type_name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="FareTypeName",
                    type="Attribute"
                )
            )
            priority_level: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="PriorityLevel",
                    type="Attribute"
                )
            )
            content_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ContentID",
                    type="Attribute"
                )
            )

        @dataclass
        class PromoRedemption:
            """
            :ivar promo_id:
            :ivar eligible:
            :ivar content_id:
            """
            promo_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="PromoID",
                    type="Attribute"
                )
            )
            eligible: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="Eligible",
                    type="Attribute"
                )
            )
            content_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="ContentID",
                    type="Attribute"
                )
            )

        @dataclass
        class Rule:
            """
            :ivar type: Rule type. For example: "Fare Note Itin", "DRE"
            :ivar id: Rule ID
            """
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Type",
                    type="Attribute"
                )
            )
            id: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="ID",
                    type="Attribute"
                )
            )

        @dataclass
        class MultipleTravelerGroups:
            """
            :ivar group_number:
            :ivar primary_group:
            """
            group_number: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="GroupNumber",
                    type="Attribute"
                )
            )
            primary_group: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="PrimaryGroup",
                    type="Attribute"
                )
            )

        @dataclass
        class AncillaryFeeGroups:
            """
            :ivar ancillary_fee_group: Ancillary fee group returned
            :ivar message: Arbitrary message returned from MIP
            """
            ancillary_fee_group: List["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups.AncillaryFeeGroup"] = field(
                default_factory=list,
                metadata=dict(
                    name="AncillaryFeeGroup",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            message: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Message",
                    type="Attribute"
                )
            )

            @dataclass
            class AncillaryFeeGroup:
                """
                :ivar ancillary_fee_item: OC Fee returned
                :ivar code: Group code
                :ivar name: Group name
                :ivar message: Arbitrary message returned from MIP
                """
                ancillary_fee_item: List["AirItineraryPricingInfoType.TpaExtensions.AncillaryFeeGroups.AncillaryFeeGroup.AncillaryFeeItem"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="AncillaryFeeItem",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Code",
                        type="Attribute",
                        required=True
                    )
                )
                name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Name",
                        type="Attribute",
                        required=True
                    )
                )
                message: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Message",
                        type="Attribute"
                    )
                )

                @dataclass
                class AncillaryFeeItem(OcfeeType):
                    pass

        @dataclass
        class Legs:
            """
            :ivar leg:
            """
            leg: List["AirItineraryPricingInfoType.TpaExtensions.Legs.Leg"] = field(
                default_factory=list,
                metadata=dict(
                    name="Leg",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class Leg:
                """
                :ivar segment:
                :ivar number:
                :ivar brand_id:
                :ivar brand_description:
                :ivar program_name:
                :ivar program_id:
                :ivar program_code:
                :ivar program_system_code:
                :ivar fare_status: Detailed reason why fare could not be returned (when FareReturned="false"). "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable", "N" - unknown status.
                """
                segment: List["AirItineraryPricingInfoType.TpaExtensions.Legs.Leg.Segment"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="Segment",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="Number",
                        type="Attribute"
                    )
                )
                brand_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="BrandID",
                        type="Attribute"
                    )
                )
                brand_description: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="BrandDescription",
                        type="Attribute"
                    )
                )
                program_name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramName",
                        type="Attribute"
                    )
                )
                program_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramID",
                        type="Attribute"
                    )
                )
                program_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramCode",
                        type="Attribute"
                    )
                )
                program_system_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="ProgramSystemCode",
                        type="Attribute"
                    )
                )
                fare_status: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="FareStatus",
                        type="Attribute"
                    )
                )

                @dataclass
                class Segment:
                    """
                    :ivar number: Reference to the flight segment
                    :ivar program_id:
                    :ivar program_description:
                    :ivar program_system_code:
                    :ivar brand_id:
                    :ivar brand_name: Used to indicate brand name
                    :ivar fare_status: If possible detailed reason why fare could not be returned. "A" means "Class is not available", "O" - "Class is not offered", "F" - "No fare found or applicable", "N" - unknown status.
                    """
                    number: Optional[int] = field(
                        default=None,
                        metadata=dict(
                            name="Number",
                            type="Attribute"
                        )
                    )
                    program_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ProgramID",
                            type="Attribute"
                        )
                    )
                    program_description: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ProgramDescription",
                            type="Attribute"
                        )
                    )
                    program_system_code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ProgramSystemCode",
                            type="Attribute"
                        )
                    )
                    brand_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="BrandID",
                            type="Attribute"
                        )
                    )
                    brand_name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="BrandName",
                            type="Attribute"
                        )
                    )
                    fare_status: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="FareStatus",
                            type="Attribute"
                        )
                    )


@dataclass
class AirItineraryType:
    """Specifies the origin and destination of the traveler.

    :ivar origin_destination_options: A collection of OriginDestinationOption
    :ivar direction_ind: A directional indicator that identifies a type of air booking (e.g. one-way, round-trip, open-jaw).
    :ivar departure_date: Itinerary departure date
    """
    origin_destination_options: Optional["AirItineraryType.OriginDestinationOptions"] = field(
        default=None,
        metadata=dict(
            name="OriginDestinationOptions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    direction_ind: Optional[AirTripType] = field(
        default=None,
        metadata=dict(
            name="DirectionInd",
            type="Attribute"
        )
    )
    departure_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute"
        )
    )

    @dataclass
    class OriginDestinationOptions:
        """
        :ivar origin_destination_option: A container for flight segments.
        """
        origin_destination_option: List[OriginDestinationOptionType] = field(
            default_factory=list,
            metadata=dict(
                name="OriginDestinationOption",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=99
            )
        )


@dataclass
class TicketPricingType:
    """Pricing Information for Single Ticket.

    :ivar origin_destination_options:
    :ivar air_itinerary_pricing_info: Pricing Information for a Ticket.
    :ivar notes: Provides for free form descriptive information for the priced itinerary.
    :ivar ticketing_info: Container for TicketingInfoRS_Type.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar number: Ticket position related to entire itinerary
    """
    origin_destination_options: Optional["TicketPricingType.OriginDestinationOptions"] = field(
        default=None,
        metadata=dict(
            name="OriginDestinationOptions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    air_itinerary_pricing_info: Optional[AirItineraryPricingInfoType] = field(
        default=None,
        metadata=dict(
            name="AirItineraryPricingInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            required=True
        )
    )
    notes: List[FreeTextType] = field(
        default_factory=list,
        metadata=dict(
            name="Notes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5
        )
    )
    ticketing_info: Optional[TicketingInfoRsType] = field(
        default=None,
        metadata=dict(
            name="TicketingInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["TicketPricingType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            required=True
        )
    )

    @dataclass
    class OriginDestinationOptions:
        """Indicates which flights are covered by this ticket.

        :ivar origin_destination_option:
        """
        origin_destination_option: List["TicketPricingType.OriginDestinationOptions.OriginDestinationOption"] = field(
            default_factory=list,
            metadata=dict(
                name="OriginDestinationOption",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=1,
                max_occurs=99
            )
        )

        @dataclass
        class OriginDestinationOption:
            """
            :ivar flight_segment:
            """
            flight_segment: List["TicketPricingType.OriginDestinationOptions.OriginDestinationOption.FlightSegment"] = field(
                default_factory=list,
                metadata=dict(
                    name="FlightSegment",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=1,
                    max_occurs=4
                )
            )

            @dataclass
            class FlightSegment:
                """
                :ivar departure_airport: Departure point of flight segment.
                :ivar arrival_airport: Arrival point of flight segment.
                :ivar departure_date_time:
                """
                departure_airport: Optional[ResponseLocationType] = field(
                    default=None,
                    metadata=dict(
                        name="DepartureAirport",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        required=True
                    )
                )
                arrival_airport: Optional[ResponseLocationType] = field(
                    default=None,
                    metadata=dict(
                        name="ArrivalAirport",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        required=True
                    )
                )
                departure_date_time: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="DepartureDateTime",
                        type="Attribute",
                        required=True
                    )
                )

    @dataclass
    class TpaExtensions:
        """
        :ivar validating_carrier: Issuing airline whose numeric airline code is reflected in the electronic transaction for the flight/value coupon(s).The Validating Carrier shall be the controlling and authorising entity for Electronic Ticketing transactions..
        """
        validating_carrier: Optional["TicketPricingType.TpaExtensions.ValidatingCarrier"] = field(
            default=None,
            metadata=dict(
                name="ValidatingCarrier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class ValidatingCarrier:
            """
            :ivar code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    min_length=1.0,
                    max_length=8.0
                )
            )


@dataclass
class TicketsPricingType:
    """
    :ivar ticket:
    """
    ticket: List[TicketPricingType] = field(
        default_factory=list,
        metadata=dict(
            name="Ticket",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class PricedItineraryType:
    """Itinerary with pricing information.

    :ivar air_itinerary: Specifies the origin and destination of the traveler.
    :ivar air_itinerary_pricing_info: Pricing Information for an Air Itinerary.
    :ivar notes: Provides for free form descriptive information for the priced itinerary.
    :ivar ticketing_info: Container for TicketingInfoRS_Type.
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar is_from_custom_path: Indicates if itin come from custom carrier/routing path.
    :ivar sequence_number: Assigns a number to priced itineraries.
    :ivar origin_destination_rph: When a PricedItinerary element contains flights and pricing information for a single OriginDestinationPair from the OTA_LowFareSearchRQ message, this RPH attribute identifies that OriginDestinationPair from the RQ. When the PricedItinerary contains flights and pricing information for all OriginDestinationPairs from the OTA_LowFareSearchRQ message, this attribute should not be included.
    :ivar campaign_id: Program/campaign ID, which the downline clients need to determine which marketing text to display.
    :ivar alternate_airport: Alternate airport itineraries indicator
    :ivar multiple_tickets: Indicates that itinerary should be sold on multiple separate tickets
    """
    air_itinerary: Optional[AirItineraryType] = field(
        default=None,
        metadata=dict(
            name="AirItinerary",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    air_itinerary_pricing_info: List["PricedItineraryType.AirItineraryPricingInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="AirItineraryPricingInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    notes: List[FreeTextType] = field(
        default_factory=list,
        metadata=dict(
            name="Notes",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=0,
            max_occurs=5
        )
    )
    ticketing_info: Optional[TicketingInfoRsType] = field(
        default=None,
        metadata=dict(
            name="TicketingInfo",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    tpa_extensions: Optional["PricedItineraryType.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05"
        )
    )
    is_from_custom_path: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="isFromCustomPath",
            type="Attribute"
        )
    )
    sequence_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SequenceNumber",
            type="Attribute",
            required=True
        )
    )
    origin_destination_rph: Optional[str] = field(
        default=None,
        metadata=dict(
            name="OriginDestinationRPH",
            type="Attribute",
            pattern=r"[0-9]{1,8}"
        )
    )
    campaign_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="CampaignID",
            type="Attribute"
        )
    )
    alternate_airport: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="AlternateAirport",
            type="Attribute"
        )
    )
    multiple_tickets: Optional[bool] = field(
        default=None,
        metadata=dict(
            name="MultipleTickets",
            type="Attribute"
        )
    )

    @dataclass
    class AirItineraryPricingInfo(AirItineraryPricingInfoType):
        """
        :ivar tickets: Pricing information for multiple separate tickets
        """
        tickets: Optional[TicketsPricingType] = field(
            default=None,
            metadata=dict(
                name="Tickets",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

    @dataclass
    class TpaExtensions:
        """
        :ivar additional_fares:
        :ivar ops: Populated if an Ops rule has been hit.
        :ivar itin_source: The source of the itinerary
        :ivar value_bucket: Additional information for Value Bucket sorting
        :ivar validating_carrier: Issuing airline whose numeric airline code is reflected in the electronic transaction for the flight/value coupon(s).The Validating Carrier shall be the controlling and authorising entity for Electronic Ticketing transactions..
        :ivar unflown_price: Sum of AirItineraryPricingInfo/TPA_Extensions/UnflownPrice
        :ivar diversity_swapper:
        :ivar failed: Information on problems that occurred while processing this itinerary.
        """
        additional_fares: List["PricedItineraryType.TpaExtensions.AdditionalFares"] = field(
            default_factory=list,
            metadata=dict(
                name="AdditionalFares",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )
        ops: Optional["PricedItineraryType.TpaExtensions.Ops"] = field(
            default=None,
            metadata=dict(
                name="Ops",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        itin_source: Optional["PricedItineraryType.TpaExtensions.ItinSource"] = field(
            default=None,
            metadata=dict(
                name="ItinSource",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        value_bucket: Optional["PricedItineraryType.TpaExtensions.ValueBucket"] = field(
            default=None,
            metadata=dict(
                name="ValueBucket",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        validating_carrier: Optional["PricedItineraryType.TpaExtensions.ValidatingCarrier"] = field(
            default=None,
            metadata=dict(
                name="ValidatingCarrier",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        unflown_price: Optional[UnflownPriceType] = field(
            default=None,
            metadata=dict(
                name="UnflownPrice",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        diversity_swapper: Optional["PricedItineraryType.TpaExtensions.DiversitySwapper"] = field(
            default=None,
            metadata=dict(
                name="DiversitySwapper",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )
        failed: Optional["PricedItineraryType.TpaExtensions.Failed"] = field(
            default=None,
            metadata=dict(
                name="Failed",
                type="Element",
                namespace="http://www.opentravel.org/OTA/2003/05"
            )
        )

        @dataclass
        class AdditionalFares:
            """
            :ivar air_itinerary_pricing_info: Pricing Information for an Air Itinerary.
            :ivar notes: Provides for free form descriptive information for the priced itinerary.
            :ivar ticketing_info: Information about ticketing (including eTicketNumber).
            :ivar multiple_tickets: Indicates that itinerary should be sold on multiple separate tickets
            """
            air_itinerary_pricing_info: Optional["PricedItineraryType.TpaExtensions.AdditionalFares.AirItineraryPricingInfo"] = field(
                default=None,
                metadata=dict(
                    name="AirItineraryPricingInfo",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            notes: List[FreeTextType] = field(
                default_factory=list,
                metadata=dict(
                    name="Notes",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05",
                    min_occurs=0,
                    max_occurs=5
                )
            )
            ticketing_info: Optional[TicketingInfoRsType] = field(
                default=None,
                metadata=dict(
                    name="TicketingInfo",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            multiple_tickets: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="MultipleTickets",
                    type="Attribute"
                )
            )

            @dataclass
            class AirItineraryPricingInfo(AirItineraryPricingInfoType):
                """
                :ivar tickets: Pricing information for multiple separate tickets
                """
                tickets: Optional[TicketsPricingType] = field(
                    default=None,
                    metadata=dict(
                        name="Tickets",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05"
                    )
                )

        @dataclass
        class Ops:
            """
            :ivar fare_types:
            :ivar action_code: Corresponds to data in the Ops rule (action target: Ops Action). The numeric id corresponds to an action performed by Travelocity.
            """
            fare_types: Optional["PricedItineraryType.TpaExtensions.Ops.FareTypes"] = field(
                default=None,
                metadata=dict(
                    name="FareTypes",
                    type="Element",
                    namespace="http://www.opentravel.org/OTA/2003/05"
                )
            )
            action_code: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="ActionCode",
                    type="Attribute",
                    required=True
                )
            )

            @dataclass
            class FareTypes:
                """
                :ivar fare_type:
                """
                fare_type: List["PricedItineraryType.TpaExtensions.Ops.FareTypes.FareType"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="FareType",
                        type="Element",
                        namespace="http://www.opentravel.org/OTA/2003/05",
                        min_occurs=1,
                        max_occurs=9223372036854775807
                    )
                )

                @dataclass
                class FareType:
                    """
                    :ivar code:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Code",
                            type="Attribute",
                            required=True,
                            pattern=r"[0-9A-Z]{1,3}"
                        )
                    )

        @dataclass
        class ItinSource:
            """
            :ivar source: The name of the source.
            """
            source: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Source",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class ValueBucket:
            """
            :ivar price_time_value_rank: Price Time Value rank.
            :ivar value_bucket_number: Price Time Value Bucket number.
            """
            price_time_value_rank: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="PriceTimeValueRank",
                    type="Attribute"
                )
            )
            value_bucket_number: Optional[int] = field(
                default=None,
                metadata=dict(
                    name="ValueBucketNumber",
                    type="Attribute"
                )
            )

        @dataclass
        class ValidatingCarrier:
            """
            :ivar code: Identifies a company by the company code.
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Code",
                    type="Attribute",
                    required=True,
                    pattern=r"[A-Za-z]{0}"
                )
            )

        @dataclass
        class DiversitySwapper:
            """
            :ivar weighed_price_amount: (Penalty * price / 10) -- by which itins are sorted in Diversity Swapper
            """
            weighed_price_amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="WeighedPriceAmount",
                    type="Attribute",
                    required=True
                )
            )

        @dataclass
        class Failed:
            """
            :ivar minimum_connect_time: Indicates that the itinerary does not fullfill the Minimum Connect Time requirement. It cannot be sold.
            """
            minimum_connect_time: Optional[bool] = field(
                default=None,
                metadata=dict(
                    name="MinimumConnectTime",
                    type="Attribute"
                )
            )


@dataclass
class OtaAirLowFareSearchRs:
    """
    The Low Fare Search Response message contains a number of .Priced Itinerary. options. Each includes: - A set of available flights matching the client.s request. - Pricing information including taxes and full fare breakdown for each passenger type - Ticketing information - Fare Basis Codes and the information necessary to make a rules entry. This message contains similar information to a standard airline CRS or GDS Low Fare Search Response message.
    :ivar errors: In case of failure errors are returned.
    :ivar success: In case of success this element is returned.
    :ivar warnings: In case of any warnings this element is returned.
    :ivar priced_itineraries: Low Fare priced itineraries container.
    :ivar one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
    :ivar departed_itineraries: Departed Itineraries
    :ivar sold_out_itineraries: Sold Out Itineraries
    :ivar available_itineraries: Available Itineraries
    :ivar tpa_extensions: Additional elements and attributes to be included if required, per Trading Partner Agreement (TPA).
    :ivar primary_lang_id: Identifes the primary language preference for the form of travel represented in a collection. The human language is identified by ISO 639 codes.
    :ivar alt_lang_id:
    :ivar echo_token: A sequence number for additional message identification, assigned by the requesting host system. When a request message includes an echo token the corresponding response message MUST include an echo token with an identical value.
    :ivar time_stamp: Indicates the creation date and time of the message in UTC using the following format specified by ISO 8601; YYYY-MM-DDThh:mm:ssZ with time values using the 24 hour clock (e.g. 20 November 2003, 1:59:38 pm UTC becomes 2003-11-20T13:59:38Z).
    :ivar target: Used to indicate whether the request is for the Test or Production system.
    :ivar version: For all OTA versioned messages, the version of the message is indicated by a decimal value.
    :ivar transaction_identifier: A unique identifier to relate all messages within a transaction (e.g. this would be sent in all request and response messages that are part of an on-going transaction).
    :ivar sequence_nmbr: Used to identify the sequence number of the transaction as assigned by the sending system; allows for an application to process messages in a certain order or to request a resynchronization of messages in the event that a system has been off-line and needs to retrieve messages that were missed.
    :ivar transaction_status_code: This indicates where this message falls within a sequence of messages.
    :ivar priced_itin_count: Itinerary count for Priced Round-Trip itineraries
    :ivar branded_one_way_itin_count: Itinerary count for Branded One-Way itineraries
    :ivar simple_one_way_itin_count: Itinerary count for Simple One-Way itineraries
    :ivar departed_itin_count: Itinerary count for departed itineraries returned
    :ivar sold_out_itin_count: Itinerary count for sold out itineraries returned
    :ivar available_itin_count: Itinerary count for available itineraries returned
    """
    class Meta:
        name = "OTA_AirLowFareSearchRS"
        namespace = "http://www.opentravel.org/OTA/2003/05"

    errors: Optional[ErrorsType] = field(
        default=None,
        metadata=dict(
            name="Errors",
            type="Element"
        )
    )
    success: Optional[SuccessType] = field(
        default=None,
        metadata=dict(
            name="Success",
            type="Element"
        )
    )
    warnings: Optional[WarningsType] = field(
        default=None,
        metadata=dict(
            name="Warnings",
            type="Element"
        )
    )
    priced_itineraries: Optional["OtaAirLowFareSearchRs.PricedItineraries"] = field(
        default=None,
        metadata=dict(
            name="PricedItineraries",
            type="Element"
        )
    )
    one_way_itineraries: Optional["OtaAirLowFareSearchRs.OneWayItineraries"] = field(
        default=None,
        metadata=dict(
            name="OneWayItineraries",
            type="Element"
        )
    )
    departed_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries"] = field(
        default=None,
        metadata=dict(
            name="DepartedItineraries",
            type="Element"
        )
    )
    sold_out_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries"] = field(
        default=None,
        metadata=dict(
            name="SoldOutItineraries",
            type="Element"
        )
    )
    available_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries"] = field(
        default=None,
        metadata=dict(
            name="AvailableItineraries",
            type="Element"
        )
    )
    tpa_extensions: Optional["OtaAirLowFareSearchRs.TpaExtensions"] = field(
        default=None,
        metadata=dict(
            name="TPA_Extensions",
            type="Element"
        )
    )
    primary_lang_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="PrimaryLangID",
            type="Attribute"
        )
    )
    alt_lang_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="AltLangID",
            type="Attribute"
        )
    )
    echo_token: Optional[str] = field(
        default=None,
        metadata=dict(
            name="EchoToken",
            type="Attribute"
        )
    )
    time_stamp: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TimeStamp",
            type="Attribute"
        )
    )
    target: str = field(
        default="Production",
        metadata=dict(
            name="Target",
            type="Attribute"
        )
    )
    version: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Version",
            type="Attribute",
            required=True
        )
    )
    transaction_identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TransactionIdentifier",
            type="Attribute",
            min_length=1.0,
            max_length=32.0
        )
    )
    sequence_nmbr: Optional[str] = field(
        default=None,
        metadata=dict(
            name="SequenceNmbr",
            type="Attribute"
        )
    )
    transaction_status_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="TransactionStatusCode",
            type="Attribute"
        )
    )
    priced_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="PricedItinCount",
            type="Attribute"
        )
    )
    branded_one_way_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="BrandedOneWayItinCount",
            type="Attribute"
        )
    )
    simple_one_way_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SimpleOneWayItinCount",
            type="Attribute"
        )
    )
    departed_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="DepartedItinCount",
            type="Attribute"
        )
    )
    sold_out_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="SoldOutItinCount",
            type="Attribute"
        )
    )
    available_itin_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="AvailableItinCount",
            type="Attribute"
        )
    )

    @dataclass
    class PricedItineraries:
        """
        :ivar tpa_extensions:
        :ivar priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
        """
        tpa_extensions: Optional["OtaAirLowFareSearchRs.PricedItineraries.TpaExtensions"] = field(
            default=None,
            metadata=dict(
                name="TPA_Extensions",
                type="Element"
            )
        )
        priced_itinerary: List[PricedItineraryType] = field(
            default_factory=list,
            metadata=dict(
                name="PricedItinerary",
                type="Element",
                min_occurs=1,
                max_occurs=9223372036854775807
            )
        )

        @dataclass
        class TpaExtensions:
            """
            :ivar processing_message: Container for itinerary message type.
            """
            processing_message: List[ComplexProcessingMessageType] = field(
                default_factory=list,
                metadata=dict(
                    name="ProcessingMessage",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )

    @dataclass
    class OneWayItineraries:
        """
        :ivar branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
        :ivar simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
        """
        branded_one_way_itineraries: List["OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries"] = field(
            default_factory=list,
            metadata=dict(
                name="BrandedOneWayItineraries",
                type="Element",
                min_occurs=0,
                max_occurs=10
            )
        )
        simple_one_way_itineraries: List["OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries"] = field(
            default_factory=list,
            metadata=dict(
                name="SimpleOneWayItineraries",
                type="Element",
                min_occurs=0,
                max_occurs=10
            )
        )

        @dataclass
        class BrandedOneWayItineraries:
            """
            :ivar tpa_extensions:
            :ivar priced_itinerary: Container for priced itinerary type.
            :ivar rph: Leg ID from request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element"
                )
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata=dict(
                    name="PricedItinerary",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            rph: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="RPH",
                    type="Attribute",
                    required=True,
                    pattern=r"[0-9]{1,8}"
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar processing_message: Container for itinerary message type.
                """
                processing_message: List[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="ProcessingMessage",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

        @dataclass
        class SimpleOneWayItineraries:
            """
            :ivar tpa_extensions:
            :ivar priced_itinerary: Container for priced itinerary type.
            :ivar rph: Leg ID from request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element"
                )
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata=dict(
                    name="PricedItinerary",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9223372036854775807
                )
            )
            rph: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="RPH",
                    type="Attribute",
                    required=True,
                    pattern=r"[0-9]{1,8}"
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar processing_message: Container for itinerary message type.
                """
                processing_message: List[OneWayProcessingMessageType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="ProcessingMessage",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

    @dataclass
    class DepartedItineraries:
        """
        :ivar priced_itineraries: Low Fare priced itineraries container.
        :ivar one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries"] = field(
            default=None,
            metadata=dict(
                name="PricedItineraries",
                type="Element"
            )
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries"] = field(
            default=None,
            metadata=dict(
                name="OneWayItineraries",
                type="Element"
            )
        )

        @dataclass
        class PricedItineraries:
            """
            :ivar tpa_extensions:
            :ivar priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element"
                )
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata=dict(
                    name="PricedItinerary",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="ProcessingMessage",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

        @dataclass
        class OneWayItineraries:
            """
            :ivar branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            :ivar simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="BrandedOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="SimpleOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.DepartedItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

    @dataclass
    class SoldOutItineraries:
        """
        :ivar priced_itineraries: Low Fare priced itineraries container.
        :ivar one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries"] = field(
            default=None,
            metadata=dict(
                name="PricedItineraries",
                type="Element"
            )
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries"] = field(
            default=None,
            metadata=dict(
                name="OneWayItineraries",
                type="Element"
            )
        )

        @dataclass
        class PricedItineraries:
            """
            :ivar tpa_extensions:
            :ivar priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element"
                )
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata=dict(
                    name="PricedItinerary",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="ProcessingMessage",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

        @dataclass
        class OneWayItineraries:
            """
            :ivar branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            :ivar simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="BrandedOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="SimpleOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.SoldOutItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

    @dataclass
    class AvailableItineraries:
        """
        :ivar priced_itineraries: Low Fare priced itineraries container.
        :ivar one_way_itineraries: Successfull Low Fare priced itineraries in response to a Simplified One Way request.
        """
        priced_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries"] = field(
            default=None,
            metadata=dict(
                name="PricedItineraries",
                type="Element"
            )
        )
        one_way_itineraries: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries"] = field(
            default=None,
            metadata=dict(
                name="OneWayItineraries",
                type="Element"
            )
        )

        @dataclass
        class PricedItineraries:
            """
            :ivar tpa_extensions:
            :ivar priced_itinerary: Successfull Low Fare priced itineraries in response to a Low Fare Search request.
            """
            tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.PricedItineraries.TpaExtensions"] = field(
                default=None,
                metadata=dict(
                    name="TPA_Extensions",
                    type="Element"
                )
            )
            priced_itinerary: List[PricedItineraryType] = field(
                default_factory=list,
                metadata=dict(
                    name="PricedItinerary",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class TpaExtensions:
                """
                :ivar processing_message: Container for itinerary message type.
                """
                processing_message: List[ComplexProcessingMessageType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="ProcessingMessage",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )

        @dataclass
        class OneWayItineraries:
            """
            :ivar branded_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            :ivar simple_one_way_itineraries: Container for priced itineraries assigned to particular leg.
            """
            branded_one_way_itineraries: List["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="BrandedOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )
            simple_one_way_itineraries: List["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries"] = field(
                default_factory=list,
                metadata=dict(
                    name="SimpleOneWayItineraries",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class BrandedOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.BrandedOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

            @dataclass
            class SimpleOneWayItineraries:
                """
                :ivar tpa_extensions:
                :ivar priced_itinerary: Container for priced itinerary type.
                :ivar rph: Leg ID from request.
                """
                tpa_extensions: Optional["OtaAirLowFareSearchRs.AvailableItineraries.OneWayItineraries.SimpleOneWayItineraries.TpaExtensions"] = field(
                    default=None,
                    metadata=dict(
                        name="TPA_Extensions",
                        type="Element"
                    )
                )
                priced_itinerary: List[PricedItineraryType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="PricedItinerary",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9223372036854775807
                    )
                )
                rph: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="RPH",
                        type="Attribute",
                        required=True,
                        pattern=r"[0-9]{1,8}"
                    )
                )

                @dataclass
                class TpaExtensions:
                    """
                    :ivar processing_message: Container for itinerary message type.
                    """
                    processing_message: List[OneWayProcessingMessageType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="ProcessingMessage",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9223372036854775807
                        )
                    )

    @dataclass
    class TpaExtensions:
        """
        :ivar airline_order_list:
        """
        airline_order_list: Optional["OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList"] = field(
            default=None,
            metadata=dict(
                name="AirlineOrderList",
                type="Element"
            )
        )

        @dataclass
        class AirlineOrderList:
            """
            :ivar airline_order: The airline that filed the fare(s).
            """
            airline_order: List["OtaAirLowFareSearchRs.TpaExtensions.AirlineOrderList.AirlineOrder"] = field(
                default_factory=list,
                metadata=dict(
                    name="AirlineOrder",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9223372036854775807
                )
            )

            @dataclass
            class AirlineOrder(CompanyNameType):
                """
                :ivar sequence_number:
                """
                sequence_number: Optional[int] = field(
                    default=None,
                    metadata=dict(
                        name="SequenceNumber",
                        type="Attribute",
                        required=True
                    )
                )


@dataclass
class PricedItinerariesType:
    """Container for priced itineraries.

    :ivar priced_itinerary: Container for priced itinerary type.
    """
    priced_itinerary: List[PricedItineraryType] = field(
        default_factory=list,
        metadata=dict(
            name="PricedItinerary",
            type="Element",
            namespace="http://www.opentravel.org/OTA/2003/05",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
