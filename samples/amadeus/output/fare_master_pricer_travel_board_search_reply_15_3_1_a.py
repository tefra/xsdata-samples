from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class AdditionalFareQualifierDetailsTypeI:
    """To specify the fare basis and ticket designator codes.

    :ivar rate_class: Rate class
    :ivar ticket_designator: Ticket designator.
    :ivar pricing_group: Pricing group
    :ivar second_rate_class: Second rate class
    """
    rate_class: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rateClass",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    ticket_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ticketDesignator",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )
    pricing_group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pricingGroup",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    second_rate_class: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="secondRateClass",
            type="Element",
            min_occurs=0,
            max_occurs=29,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class AdditionalProductDetailsType:
    """
    :ivar equipment_type: Type of aircraft
    :ivar operating_day: Day number of the week
    :ivar tech_stop_number: Number of stops made in a journey if different from 0
    :ivar location_id: Location places of the stops
    """
    equipment_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="equipmentType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    operating_day: Optional[str] = field(
        default=None,
        metadata=dict(
            name="operatingDay",
            type="Element",
            min_length=1.0,
            max_length=7.0
        )
    )
    tech_stop_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="techStopNumber",
            type="Element",
            pattern=r"-?[0-9]{1,2}"
        )
    )
    location_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="locationId",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class ApplicationErrorInformationType:
    """
    :ivar error: The code assigned by the receiver of a message for identification of a data validation error condition.
    """
    error: Optional[str] = field(
        default=None,
        metadata=dict(
            name="error",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=4.0
        )
    )


@dataclass
class AttributeInformationType:
    """To identify the type of attribute and the attribute.

    :ivar fee_parameter_type: Type of parameter.
    :ivar fee_parameter_description: Reference to company Id.
    """
    fee_parameter_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeParameterType",
            type="Element",
            min_length=3.0,
            max_length=3.0
        )
    )
    fee_parameter_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeParameterDescription",
            type="Element",
            min_length=1.0,
            max_length=15.0
        )
    )


@dataclass
class AttributeInformationTypeU:
    """To identify the type of attribute and the attribute.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """
    attribute_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=25.0
        )
    )
    attribute_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class AttributeInformationType97181C:
    """To identify the type of attribute and the attribute.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """
    class Meta:
        name = "AttributeInformationType_97181C"

    attribute_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=25.0
        )
    )
    attribute_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            min_length=1.0,
            max_length=256.0
        )
    )


@dataclass
class BaggageDetailsType:
    """To specify the number and weight of baggage.

    :ivar free_allowance: Number of pieces or weight
    :ivar quantity_code: Nature of the free allowance ( Number of pieces or weight)
    :ivar unit_qualifier: Unit qualifier
    """
    free_allowance: Optional[int] = field(
        default=None,
        metadata=dict(
            name="freeAllowance",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )
    quantity_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="quantityCode",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )
    unit_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="unitQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class BagtagDetailsType:
    """To identify baggage by company identification, serial numbers, and
    destination.

    :ivar identifier: Identifier
    :ivar number: Number
    """
    identifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="identifier",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )


@dataclass
class BucketInformationType:
    """
    :ivar number: Number
    :ivar name: Name
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Element",
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class CabinInformationType:
    """
    :ivar service: Identify the features associated to the cabin/class
    :ivar cabin: Cabin code designator
    """
    service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="service",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    cabin: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="cabin",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CabinProductDetailsType:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar booking_modifier: Reservation Booking Modifier
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """
    rbd: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    booking_modifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="bookingModifier",
            type="Element",
            min_length=0.0,
            max_length=1.0
        )
    )
    cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class CabinProductDetailsType195516C:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar booking_modifier: Reservation Booking Modifier
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """
    class Meta:
        name = "CabinProductDetailsType_195516C"

    rbd: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    booking_modifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="bookingModifier",
            type="Element",
            min_length=0.0,
            max_length=1.0
        )
    )
    cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            required=True,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class CabinProductDetailsType205138C:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar booking_modifier: Reservation Booking Modifier
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """
    class Meta:
        name = "CabinProductDetailsType_205138C"

    rbd: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    booking_modifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="bookingModifier",
            type="Element",
            pattern=r"[0-9A-Z]"
        )
    )
    cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )


@dataclass
class CabinProductDetailsType229142C:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """
    class Meta:
        name = "CabinProductDetailsType_229142C"

    rbd: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rbd",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    avl_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="avlStatus",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )


@dataclass
class CategoryDescriptionType:
    """
    :ivar number: Category number from ATPCO naming conventions (C05 for Advance Purchase restrictions, C06 for Minimun stay ...)
    :ivar code: Category Code (ATPCO component code, e.g ADV for Advance purchase, STP for stopover restrictions, ELG for eligibility restrictions...)
    """
    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{1,3}"
        )
    )
    code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="code",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ClassInformationType:
    """
    :ivar service: Identify the features associated to the cabin/class
    :ivar rbd: Class designator
    """
    service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="service",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    rbd: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="rbd",
            type="Element",
            min_occurs=0,
            max_occurs=26,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class CodedAttributeInformationType:
    """Convey coded key and corresponding value.

    :ivar attribute_type: Type of fee/reduction
    :ivar attribute_description: Fee Id Number
    """
    attribute_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    attribute_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class CodedAttributeInformationType270108C:
    """Convey coded key and corresponding value.

    :ivar attribute_type:
    :ivar attribute_description: Attribute description
    """
    class Meta:
        name = "CodedAttributeInformationType_270108C"

    attribute_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=5.0
        )
    )
    attribute_description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeDescription",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class CompanyIdentificationTextType:
    """Compagny identification text.

    :ivar text_ref_number: Company Id Text reference.
    :ivar company_text: Company id free text.
    """
    text_ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="textRefNumber",
            type="Element",
            pattern=r"-?[0-9]{0,4}"
        )
    )
    company_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="companyText",
            type="Element",
            min_length=0.0,
            max_length=70.0
        )
    )


@dataclass
class CompanyIdentificationType:
    """
    :ivar marketing_carrier: Marketing carrier
    :ivar operating_carrier: Operating carrier
    :ivar alliance: airline alliance code
    """
    marketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="marketingCarrier",
            type="Element",
            required=True,
            min_length=2.0,
            max_length=3.0
        )
    )
    operating_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="operatingCarrier",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    alliance: Optional[str] = field(
        default=None,
        metadata=dict(
            name="alliance",
            type="Element",
            min_length=1.0,
            max_length=2.0
        )
    )


@dataclass
class CompanyIdentificationTypeI:
    """Code or name to identify a company and any associated companies.

    :ivar marketing_company: Company
    :ivar operating_company: Company
    :ivar other_company: Company
    """
    marketing_company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="marketingCompany",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    operating_company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="operatingCompany",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    other_company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="otherCompany",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class CompanyRoleIdentificationType:
    """To indicate commercial agreements related to the service being provided.

    :ivar code_share_type: Type of code share agreement.
    :ivar airline_designator: company identification
    :ivar flight_number: flight number
    """
    code_share_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="codeShareType",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    airline_designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="airlineDesignator",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    flight_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="flightNumber",
            type="Element",
            pattern=r"-?[0-9]{1,4}"
        )
    )


@dataclass
class CompanyRoleIdentificationType120771C:
    """To indicate commercial agreements related to the service being provided.

    :ivar transport_stage_qualifier: Type of code share agreement.
    :ivar company: company identification
    """
    class Meta:
        name = "CompanyRoleIdentificationType_120771C"

    transport_stage_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="transportStageQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    company: Optional[str] = field(
        default=None,
        metadata=dict(
            name="company",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )


@dataclass
class ConversionRateDetailsTypeI:
    """
    :ivar conversion_type: Conversion type
    :ivar currency: Currency
    :ivar amount: amount
    """
    conversion_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="conversionType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            min_length=0.0,
            max_length=12.0
        )
    )


@dataclass
class ConversionRateDetailsTypeI179848C:
    """
    :ivar conversion_type: Conversion type
    :ivar currency: Currency
    :ivar rate: Conversion rate for pricing
    :ivar converted_amount_link: Converted value amount
    :ivar tax_qualifier: Applicable ISO country code or Tax designator code.
    """
    class Meta:
        name = "ConversionRateDetailsTypeI_179848C"

    conversion_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="conversionType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    rate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            min_length=0.0,
            max_length=18.0
        )
    )
    converted_amount_link: Optional[str] = field(
        default=None,
        metadata=dict(
            name="convertedAmountLink",
            type="Element",
            min_length=0.0,
            max_length=18.0
        )
    )
    tax_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="taxQualifier",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class CriteriaiDetaislType:
    """
    Criteria details : weights/parameters list
    :ivar type:
    :ivar value:
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )


@dataclass
class DataInformationType:
    """To identify specific data and a quantity related to the data.

    :ivar indicator: Ancillary services options
    """
    indicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="indicator",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DataTypeInformationType:
    """To identify the type of data to be sent and to qualify the data when
    required.

    :ivar sub_type: service group/sub-group/sub-code information
    :ivar option: Status (automated, manually added, exempted). Default is automated
    """
    sub_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="subType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option: Optional[str] = field(
        default=None,
        metadata=dict(
            name="option",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DateAndTimeDetailsType:
    """
    :ivar date_qualifier: Date time period qualifier
    :ivar date: First Date
    :ivar first_time: First Time
    :ivar equipement_type: Movement type.
    :ivar location_id: Place/location identification.
    """
    date_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dateQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            pattern=r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    first_time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="firstTime",
            type="Element",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    equipement_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="equipementType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            min_length=3.0,
            max_length=5.0
        )
    )


@dataclass
class DateAndTimeDetailsType256192C:
    """To provide date and time details relative to flight movements.

    :ivar qualifier:
    :ivar date:
    :ivar time: Time
    :ivar location: Location
    """
    class Meta:
        name = "DateAndTimeDetailsType_256192C"

    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="date",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    time: Optional[str] = field(
        default=None,
        metadata=dict(
            name="time",
            type="Element",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            min_length=1.0,
            max_length=25.0
        )
    )


@dataclass
class DateTimePeriodDetailsTypeI:
    """To indicate period of applicability.

    :ivar qualifier: Qualifier
    :ivar value: Value
    """
    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class DiscountPenaltyInformationType:
    """To indicate the discounts and penalties by fare type.

    :ivar fare_qualifier: Discounted fare,...
    :ivar rate_category: Dicount code,...
    :ivar amount: Amount
    :ivar percentage: Percentage
    """
    fare_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    rate_category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rateCategory",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element"
        )
    )
    percentage: Optional[float] = field(
        default=None,
        metadata=dict(
            name="percentage",
            type="Element"
        )
    )


@dataclass
class DiscountPenaltyMonetaryInformationType:
    """To specify the type of discount and penalty information, the monetary
    amount, and associated information.

    :ivar fee_type: Type of discount/penalty
    :ivar fee_amount_type: The amount Type can be a percentage or an amount
    :ivar fee_amount: specify the value
    :ivar fee_currency: Fee currency code.
    """
    fee_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fee_amount_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeAmountType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fee_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="feeAmount",
            type="Element"
        )
    )
    fee_currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeCurrency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class DummySegmentTypeI:
    """To serve the purpose of a mandatory segment at the beginning of a group and
    to avoid segment collision.

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
class FareCalculationCodeDetailsType:
    """To specify fare calculation information.

    :ivar qualifier: Qualifier of the amout or rate
    :ivar amount: Amount
    :ivar location_code: Location code
    :ivar other_location_code: Other location code
    :ivar rate: Rate
    """
    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element"
        )
    )
    location_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="locationCode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    other_location_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="otherLocationCode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    rate: Optional[float] = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element"
        )
    )


@dataclass
class FareCategoryCodesTypeI:
    """To designate non-system specific combinations of fare types.

    :ivar fare_type: Fare type
    :ivar other_fare_type: Other fare type
    """
    fare_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=20.0
        )
    )
    other_fare_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="otherFareType",
            type="Element",
            min_occurs=0,
            max_occurs=8,
            min_length=1.0,
            max_length=20.0
        )
    )


@dataclass
class FareDetailsType:
    """To specify the fare type and related information.

    :ivar passenger_type_qualifier: Passenger Type qualifier
    """
    passenger_type_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="passengerTypeQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FareDetailsTypeI:
    """To specify the fare type and related information.

    :ivar qualifier: Qualifier
    :ivar rate: Rate
    :ivar country: Country
    :ivar fare_category: Fare category
    """
    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    rate: Optional[float] = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element"
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareCategory",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FareDetailsType193037C:
    """
    :ivar qualifier: Qualifier
    :ivar rate: Rate
    :ivar country: Country
    :ivar fare_category: Fare Category
    """
    class Meta:
        name = "FareDetailsType_193037C"

    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )
    rate: Optional[int] = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            pattern=r"-?[0-9]{1,8}"
        )
    )
    country: Optional[str] = field(
        default=None,
        metadata=dict(
            name="country",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareCategory",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )


@dataclass
class FareFamilyDetailsType:
    """NEW FARE SEARCH.

    :ivar commercial_family: Commercial fare Family Short name
    """
    commercial_family: Optional[str] = field(
        default=None,
        metadata=dict(
            name="commercialFamily",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class FareInformationTypeI:
    """To specify fare details.

    :ivar value_qualifier: Value qualifier
    :ivar value: Value
    """
    value_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )


@dataclass
class FareProductDetailsType:
    """
    :ivar fare_basis: Fare basis code
    """
    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareBasis",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )


@dataclass
class FareProductDetailsType248552C:
    """
    :ivar fare_basis: Fare basis code
    :ivar passenger_type: PTC priced
    :ivar fare_type: Type of fare
    """
    class Meta:
        name = "FareProductDetailsType_248552C"

    fare_basis: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareBasis",
            type="Element",
            min_length=0.0,
            max_length=18.0
        )
    )
    passenger_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="passengerType",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    fare_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="fareType",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class FareTypeGroupingInformationType:
    """
    :ivar pricing_group: Pricing Group
    """
    pricing_group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pricingGroup",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FreeTextQualificationType:
    """
    :ivar text_subject_qualifier: Type of message
    :ivar information_type: Coded Text or type of information in 4440 (e.g. type of OSI or free text, canned message value)
    """
    text_subject_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="textSubjectQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    information_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="informationType",
            type="Element",
            min_length=1.0,
            max_length=4.0
        )
    )


@dataclass
class FreeTextQualificationTypeI:
    """To specify the type, purpose, and language of free text and whether any
    action is required.

    :ivar text_subject_qualifier: Text subject qualifier
    """
    text_subject_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="textSubjectQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FreeTextQualificationType120769C:
    """
    :ivar text_subject_qualifier: Type of message
    :ivar information_type: Coded Text or type of information in 4440 (e.g. type of OSI or free text, canned message value)
    :ivar language: ISO code for language of free text (default is English)
    """
    class Meta:
        name = "FreeTextQualificationType_120769C"

    text_subject_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="textSubjectQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    information_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="informationType",
            type="Element",
            min_length=1.0,
            max_length=4.0
        )
    )
    language: Optional[str] = field(
        default=None,
        metadata=dict(
            name="language",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FrequentTravellerIdentificationType:
    """
    :ivar carrier: Carrier where the FQTV is registered.
    :ivar number: Number
    :ivar tier_level: To specify a Tier linked to the FQTV
    :ivar priority_code: For example : priority code
    """
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=28.0
        )
    )
    tier_level: Optional[str] = field(
        default=None,
        metadata=dict(
            name="tierLevel",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    priority_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="priorityCode",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )


@dataclass
class ItemNumberIdentificationType:
    """Goods identification for a specified source.

    :ivar number: Ancillary Service number
    :ivar type: Type
    :ivar qualifier: Qualifier
    :ivar responsible_agency: Responsible agency
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=4.0
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    responsible_agency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="responsibleAgency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberIdentificationType191597C:
    """
    :ivar number: Item number.
    :ivar number_type: Indicates the item type .
    """
    class Meta:
        name = "ItemNumberIdentificationType_191597C"

    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    number_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="numberType",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberIdentificationType192331C:
    """Goods identification for a specified source.

    :ivar number: Service coverage number
    :ivar type: Type
    :ivar qualifier: Qualifier
    :ivar responsible_agency: Responsible agency
    """
    class Meta:
        name = "ItemNumberIdentificationType_192331C"

    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="qualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    responsible_agency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="responsibleAgency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberIdentificationType234878C:
    """Goods identification for a specified source.

    :ivar number: Number
    :ivar type: Type
    """
    class Meta:
        name = "ItemNumberIdentificationType_234878C"

    number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            pattern=r"-?[0-9]{1,6}"
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ItemNumberIdentificationType248537C:
    """Goods identification for a specified source.

    :ivar number:
    """
    class Meta:
        name = "ItemNumberIdentificationType_248537C"

    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class ItemReferencesAndVersionsType:
    """Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar ref_number: Unique fee reference.
    """
    reference_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceType",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )


@dataclass
class ItemReferencesAndVersionsType78536S:
    """Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar ref_number: Unique fee reference.
    """
    class Meta:
        name = "ItemReferencesAndVersionsType_78536S"

    reference_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )


@dataclass
class ItemReferencesAndVersionsType78564S:
    """Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar fee_ref_number: Unique fee reference.
    """
    class Meta:
        name = "ItemReferencesAndVersionsType_78564S"

    reference_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fee_ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="feeRefNumber",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )


@dataclass
class ItineraryDetailsType:
    """Forces arrival or departure to/from the same city or airport option.

    :ivar airport_city_qualifier: Airport/City Qualifier: the passenger wants to depart/arrive from/to the same airport or city in the specified requested segment
    :ivar segment_number: Requested segment number
    """
    airport_city_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=1.0
        )
    )
    segment_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="segmentNumber",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{1,3}"
        )
    )


@dataclass
class LocationIdentificationDetailsType:
    """
    :ivar location_id: 3 characters ATA/IATA airport/city code
    :ivar airport_city_qualifier: Airport/city qualifier: the requested point is an airport when ambiguity exists (e.g. HOU)
    :ivar terminal: Terminal information
    """
    location_id: Optional[str] = field(
        default=None,
        metadata=dict(
            name="locationId",
            type="Element",
            required=True,
            min_length=3.0,
            max_length=5.0
        )
    )
    airport_city_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="airportCityQualifier",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    terminal: Optional[str] = field(
        default=None,
        metadata=dict(
            name="terminal",
            type="Element",
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class MiniRulesDetailsType:
    """
    :ivar interpretation: Coded text (period or day)
    :ivar value: Data type coded or value of interpretation
    """
    interpretation: Optional[str] = field(
        default=None,
        metadata=dict(
            name="interpretation",
            type="Element",
            min_length=0.0,
            max_length=9.0
        )
    )
    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            min_occurs=0,
            max_occurs=10,
            min_length=0.0,
            max_length=5.0
        )
    )


@dataclass
class MiniRulesIndicatorType:
    """
    :ivar rule_indicator: See rule indicator and free form text indicator
    """
    rule_indicator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ruleIndicator",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class MiniRulesType:
    """To specify the restrictions.

    :ivar category: Categoty of restriction: PTC, Max Adv Pur, Days, ...
    """
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="category",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsType:
    """
    :ivar amount_type: To specify amount and percentage.
    :ivar amount: Amount
    :ivar currency: ISO currency code
    """
    amount_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="amountType",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            required=True
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsTypeI:
    """To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier: type Qualifier
    :ivar amount: Amount
    :ivar currency: Currency
    """
    type_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=6.0
        )
    )
    amount: Optional[str] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class MonetaryInformationDetailsType245528C:
    """To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier:
    :ivar amount: Amount
    :ivar currency: Currency
    :ivar location: location
    """
    class Meta:
        name = "MonetaryInformationDetailsType_245528C"

    type_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="typeQualifier",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="amount",
            type="Element"
        )
    )
    currency: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currency",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    location: Optional[str] = field(
        default=None,
        metadata=dict(
            name="location",
            type="Element",
            min_length=1.0,
            max_length=25.0
        )
    )


@dataclass
class OnTimePerformanceType:
    """
    :ivar date_time_period: Date time period
    :ivar percentage: Percentage
    :ivar accuracy: Accuracy
    """
    date_time_period: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dateTimePeriod",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    percentage: Optional[float] = field(
        default=None,
        metadata=dict(
            name="percentage",
            type="Element"
        )
    )
    accuracy: Optional[str] = field(
        default=None,
        metadata=dict(
            name="accuracy",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class OriginAndDestinationRequestType134833S:
    """To convey information regarding Requested Segments.

    :ivar seg_ref: Requested segment number
    """
    class Meta:
        name = "OriginAndDestinationRequestType_134833S"

    seg_ref: Optional[int] = field(
        default=None,
        metadata=dict(
            name="segRef",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{1,2}"
        )
    )


@dataclass
class OriginatorIdentificationDetailsTypeI:
    """To identify a user.

    :ivar office_name: Office Name.
    :ivar agent_signin: Agent Sign In .
    :ivar confidential_office: Confidential Office Name.
    :ivar other_office: Other Office Name
    """
    office_name: Optional[int] = field(
        default=None,
        metadata=dict(
            name="officeName",
            type="Element",
            pattern=r"-?[0-9]{1,9}"
        )
    )
    agent_signin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="agentSignin",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )
    confidential_office: Optional[str] = field(
        default=None,
        metadata=dict(
            name="confidentialOffice",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )
    other_office: Optional[str] = field(
        default=None,
        metadata=dict(
            name="otherOffice",
            type="Element",
            min_length=1.0,
            max_length=9.0
        )
    )


@dataclass
class PricingTicketingInformationType:
    """To specify indicators related to pricing and ticketing.

    :ivar price_type: Price type qualifier
    """
    price_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="priceType",
            type="Element",
            min_occurs=1,
            max_occurs=20,
            min_length=0.0,
            max_length=3.0
        )
    )


@dataclass
class PricingTicketingSubsequentType:
    """To convey additional information related to a ticket.

    :ivar pax_fare_num: Passenger fare product number
    """
    pax_fare_num: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="paxFareNum",
            type="Element",
            min_occurs=1,
            max_occurs=10,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProcessingInformationType:
    """To identify the action to be taken and the selection criteria.

    :ivar action_qualifier: Action qualifier
    :ivar reference_qualifier: Reference qualifier
    :ivar ref_num: Reference number
    """
    action_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="actionQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    reference_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_num: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refNum",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProductDateTimeType:
    """
    :ivar date_of_departure: Departure date
    :ivar time_of_departure: Departure time
    :ivar date_of_arrival: Arrival date
    :ivar time_of_arrival: Arrival time
    :ivar date_variation: Arrival date compared to departure date, only if different from 0
    """
    date_of_departure: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dateOfDeparture",
            type="Element",
            required=True,
            pattern=r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_departure: Optional[str] = field(
        default=None,
        metadata=dict(
            name="timeOfDeparture",
            type="Element",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_of_arrival: Optional[str] = field(
        default=None,
        metadata=dict(
            name="dateOfArrival",
            type="Element",
            pattern=r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}"
        )
    )
    time_of_arrival: Optional[str] = field(
        default=None,
        metadata=dict(
            name="timeOfArrival",
            type="Element",
            pattern=r"([0-1][0-9]|2[0-3])[0-5][0-9]"
        )
    )
    date_variation: Optional[int] = field(
        default=None,
        metadata=dict(
            name="dateVariation",
            type="Element",
            pattern=r"-?[0-9]{1,1}"
        )
    )


@dataclass
class ProductDetailsType:
    """To specify availability and additional services for a product class.

    :ivar designator:
    :ivar availability_status:
    :ivar special_service:
    :ivar option:
    """
    designator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="designator",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=17.0
        )
    )
    availability_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="availabilityStatus",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    special_service: Optional[str] = field(
        default=None,
        metadata=dict(
            name="specialService",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    option: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="option",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=7.0
        )
    )


@dataclass
class ProductFacilitiesType:
    """Level of access.

    :ivar last_seat_available: Yes-No indicator whether Last Seat Available
    :ivar level_of_access: Level of access
    :ivar electronic_ticketing: Yes-No indicator whether electronic ticketing
    :ivar operational_suffix: Product identification suffix
    :ivar product_detail_qualifier: Define whether a flight has been polled or not
    :ivar flight_characteristic: Add some flight restrictions (See code set list)
    """
    last_seat_available: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lastSeatAvailable",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    level_of_access: Optional[str] = field(
        default=None,
        metadata=dict(
            name="levelOfAccess",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    electronic_ticketing: Optional[str] = field(
        default=None,
        metadata=dict(
            name="electronicTicketing",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    operational_suffix: Optional[str] = field(
        default=None,
        metadata=dict(
            name="operationalSuffix",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    product_detail_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="productDetailQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    flight_characteristic: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProductTypeDetailsType:
    """To specify additional characteristics of a product or service.

    :ivar availability_cnx_type: Availability connection type.
    """
    availability_cnx_type: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="availabilityCnxType",
            type="Element",
            min_occurs=1,
            max_occurs=9,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ProductTypeDetailsType205137C:
    """To specify additional characteristics of a product or service.

    :ivar avl: indicates whether the flight is domestic or international
    """
    class Meta:
        name = "ProductTypeDetailsType_205137C"

    avl: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="avl",
            type="Element",
            min_occurs=1,
            max_occurs=9,
            min_length=1.0,
            max_length=6.0
        )
    )


@dataclass
class ProposedSegmentDetailsType:
    """
    :ivar ref: Flight proposal reference
    :ivar unit_qualifier: Elapse Flying Time
    """
    ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    unit_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="unitQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class ReferenceType:
    """To specify which number in a sequence of references and/or the reference
    number.

    :ivar ref_of_leg: Reference of leg
    :ivar first_item_identifier: Reference of segment starting range
    :ivar last_item_identifier: Reference of segment ending range
    """
    ref_of_leg: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refOfLeg",
            type="Element",
            min_length=1.0,
            max_length=6.0
        )
    )
    first_item_identifier: Optional[int] = field(
        default=None,
        metadata=dict(
            name="firstItemIdentifier",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )
    last_item_identifier: Optional[int] = field(
        default=None,
        metadata=dict(
            name="lastItemIdentifier",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )


@dataclass
class ReferencingDetailsType:
    """
    :ivar ref_qualifier: Reference qualifier
    :ivar ref_number: Requested segment reference
    """
    ref_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refQualifier",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{0,3}"
        )
    )


@dataclass
class ReferencingDetailsType191583C:
    """Referencing details.

    :ivar ref_qualifier: Service reference qualifier
    :ivar ref_number: Service reference
    """
    class Meta:
        name = "ReferencingDetailsType_191583C"

    ref_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{0,6}"
        )
    )


@dataclass
class ReferencingDetailsType195561C:
    """Referencing details.

    :ivar ref_qualifier: Segment reference qualifier
    :ivar ref_number: Flight or flight group reference
    """
    class Meta:
        name = "ReferencingDetailsType_195561C"

    ref_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="refQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{0,3}"
        )
    )


@dataclass
class ReferencingDetailsType234704C:
    """To provide reference identification.

    :ivar type: Type
    :ivar value: Value
    """
    class Meta:
        name = "ReferencingDetailsType_234704C"

    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=60.0
        )
    )


@dataclass
class SegmentRepetitionControlDetailsTypeI:
    """Information about the number of selection segments to be processed.

    :ivar quantity: traveller number
    :ivar number_of_units: range of traveller
    """
    quantity: Optional[int] = field(
        default=None,
        metadata=dict(
            name="quantity",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )
    number_of_units: Optional[int] = field(
        default=None,
        metadata=dict(
            name="numberOfUnits",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )


@dataclass
class SelectionDetailsInformationType:
    """To specify a selected option and associated information.

    :ivar type: Carrier fee type
    :ivar option_information: Carrier fee status
    """
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    option_information: Optional[str] = field(
        default=None,
        metadata=dict(
            name="optionInformation",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class SequenceInformationTypeU:
    """Identification of a sequence and source for sequencing.

    :ivar number: Number
    :ivar identification_code: Identification code
    """
    number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="number",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=10.0
        )
    )
    identification_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="identificationCode",
            type="Element",
            min_length=1.0,
            max_length=17.0
        )
    )


@dataclass
class ServicesReferences:
    """
    :ivar reference: Reference of the service
    :ivar status: Status of the service
    :ivar from_price: Service lowest price
    """
    reference: Optional[str] = field(
        default=None,
        metadata=dict(
            name="reference",
            type="Element",
            min_length=1.0,
            max_length=4.0
        )
    )
    status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="status",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    from_price: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fromPrice",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )


@dataclass
class SpecialRequirementsDataDetailsType:
    """Special requirements data details.

    :ivar seat_characteristics: SSR seat characteristic
    :ivar dummy_net:
    """
    seat_characteristics: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="seatCharacteristics",
            type="Element",
            min_occurs=0,
            max_occurs=5,
            min_length=1.0,
            max_length=2.0
        )
    )
    dummy_net: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class SpecialRequirementsTypeDetailsType:
    """
    :ivar service_classification: To specify the Service Classification of the Service Requirement.
    :ivar service_status: Status
    :ivar service_number_of_instances: To specify the number of items involved
    :ivar service_marketing_carrier: To specify to which marketing carrier the service applies
    :ivar service_group: Specify the Service group
    :ivar service_sub_group: Specify the Service Sub-Group
    :ivar service_free_text: Free Text attached to the Service.
    """
    service_classification: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceClassification",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=4.0
        )
    )
    service_status: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceStatus",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_number_of_instances: Optional[int] = field(
        default=None,
        metadata=dict(
            name="serviceNumberOfInstances",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )
    service_marketing_carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceMarketingCarrier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceGroup",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_sub_group: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceSubGroup",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    service_free_text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="serviceFreeText",
            type="Element",
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class SpecificTravellerDetailsType:
    """To specify additional details about a particular traveller.

    :ivar reference_number: Reference number
    """
    reference_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )


@dataclass
class StatusDetailsType:
    """
    :ivar advisory_type_info: Advisory type information, Fare Server
    :ivar notification: CPU time, user type
    :ivar notification2: CPU time,user type
    :ivar description: Capture and trace information
    """
    advisory_type_info: Optional[str] = field(
        default=None,
        metadata=dict(
            name="advisoryTypeInfo",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    notification: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notification",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    notification2: Optional[str] = field(
        default=None,
        metadata=dict(
            name="notification2",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class StatusDetailsType256255C:
    """To specify a status, the action to be taken, and an additional qualification
    of the status.

    :ivar indicator: list of status/qualifiers Either His for Historical or Crt for Current
    :ivar action:
    """
    class Meta:
        name = "StatusDetailsType_256255C"

    indicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="indicator",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    action: Optional[str] = field(
        default=None,
        metadata=dict(
            name="action",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TaxDetailsType:
    """To specify a rate, type of tax, and currency code.

    :ivar rate: Amount
    :ivar country_code: Country code
    :ivar currency_code: Currency code
    :ivar type: Type
    :ivar indicator: Indicator
    """
    rate: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rate",
            type="Element",
            min_length=1.0,
            max_length=12.0
        )
    )
    country_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="countryCode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    currency_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="currencyCode",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="type",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    indicator: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="indicator",
            type="Element",
            min_occurs=0,
            max_occurs=98,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class TravellerDetailsType:
    """
    :ivar ref: Direct reference of passenger assigned by requesting system.
    :ivar infant_indicator: Traveller is an infant
    """
    ref: Optional[int] = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            pattern=r"-?[0-9]{1,3}"
        )
    )
    infant_indicator: Optional[int] = field(
        default=None,
        metadata=dict(
            name="infantIndicator",
            type="Element",
            pattern=r"-?[0-9]{1,1}"
        )
    )


@dataclass
class ActionDetailsType:
    """To specify the action that should be taken on a selected reference number.

    :ivar number_of_items_details: Number of items details
    :ivar last_items_details: Range of segments
    """
    number_of_items_details: Optional[ProcessingInformationType] = field(
        default=None,
        metadata=dict(
            name="numberOfItemsDetails",
            type="Element"
        )
    )
    last_items_details: List[ReferenceType] = field(
        default_factory=list,
        metadata=dict(
            name="lastItemsDetails",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class ApplicationErrorInformationType78543S:
    """To identify the type of application error within a message.

    :ivar application_error_detail: Details on application error.
    """
    class Meta:
        name = "ApplicationErrorInformationType_78543S"

    application_error_detail: Optional[ApplicationErrorInformationType] = field(
        default=None,
        metadata=dict(
            name="applicationErrorDetail",
            type="Element",
            required=True
        )
    )


@dataclass
class AttributeType:
    """Used to have tag value without code list for tag.

    :ivar attribute_qualifier: Criteria Set Type
    :ivar attribute_details: Criteria details
    """
    attribute_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute_details: List[AttributeInformationType97181C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class AttributeTypeU:
    """
    :ivar attribute_function: provides the function of the attribute
    :ivar attribute_details: provides details for the Attribute
    """
    attribute_function: Optional[str] = field(
        default=None,
        metadata=dict(
            name="attributeFunction",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    attribute_details: Optional[AttributeInformationTypeU] = field(
        default=None,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class AttributeType78561S:
    """Used to have tag value without code list for tag.

    :ivar fee_parameter: Fee/reduction parameters.
    """
    class Meta:
        name = "AttributeType_78561S"

    fee_parameter: List[AttributeInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="feeParameter",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class CategDescrType:
    """To identify an ATPCO Fare Category.

    :ivar description_info: Category description information
    :ivar process_indicator: Category processing indicator
    """
    description_info: Optional[CategoryDescriptionType] = field(
        default=None,
        metadata=dict(
            name="descriptionInfo",
            type="Element",
            required=True
        )
    )
    process_indicator: Optional[str] = field(
        default=None,
        metadata=dict(
            name="processIndicator",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class CodedAttributeType:
    """Used to have tag value without code list for tag.

    :ivar attribute_details: Fee/reduction Id
    """
    attribute_details: List[CodedAttributeInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class CommercialAgreementsType:
    """To specify commercial agreements between two or more companies related to
    joint, shared, lease operations etc.

    :ivar codeshare_details: Codeshare Details
    :ivar other_codeshare_details: Other codeshare details
    """
    codeshare_details: Optional[CompanyRoleIdentificationType] = field(
        default=None,
        metadata=dict(
            name="codeshareDetails",
            type="Element"
        )
    )
    other_codeshare_details: List[CompanyRoleIdentificationType] = field(
        default_factory=list,
        metadata=dict(
            name="otherCodeshareDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class ConversionRateTypeI:
    """To specify conversion rate details.

    :ivar conversion_rate_detail: Detail of conversion rate of First Monetary Unit.
    """
    conversion_rate_detail: List[ConversionRateDetailsTypeI179848C] = field(
        default_factory=list,
        metadata=dict(
            name="conversionRateDetail",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class ConversionRateTypeI78562S:
    """To specify conversion rate details.

    :ivar conversion_rate_detail: Details of conversion
    """
    class Meta:
        name = "ConversionRateTypeI_78562S"

    conversion_rate_detail: List[ConversionRateDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="conversionRateDetail",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )


@dataclass
class DateAndTimeInformationType:
    """not the standard only used in fare quote message.

    :ivar stop_details: Details on date and time
    :ivar dummy_net:
    """
    stop_details: List[DateAndTimeDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="stopDetails",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )
    dummy_net: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class DateAndTimeInformationType182345S:
    """To convey information regarding estimated or actual dates and times of
    operational events.

    :ivar date_and_time_details: DATE AND TIME DETAILS
    :ivar dummy_net:
    """
    class Meta:
        name = "DateAndTimeInformationType_182345S"

    date_and_time_details: List[DateAndTimeDetailsType256192C] = field(
        default_factory=list,
        metadata=dict(
            name="dateAndTimeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=400
        )
    )
    dummy_net: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class DiscountAndPenaltyInformationType:
    """To specify information about discounts and penalties.

    :ivar fee_identification: Used to specify airline collected fee or agent collected fee.
    :ivar fee_information: Used to specify penalty information
    """
    fee_identification: Optional[str] = field(
        default=None,
        metadata=dict(
            name="feeIdentification",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fee_information: Optional[DiscountPenaltyMonetaryInformationType] = field(
        default=None,
        metadata=dict(
            name="feeInformation",
            type="Element"
        )
    )


@dataclass
class ExcessBaggageType:
    """
    :ivar baggage_details: Baggage details
    :ivar bag_tag_details: Free baggage allowance details
    """
    baggage_details: Optional[BaggageDetailsType] = field(
        default=None,
        metadata=dict(
            name="baggageDetails",
            type="Element"
        )
    )
    bag_tag_details: List[BagtagDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="bagTagDetails",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class FareFamilyType:
    """NEW FARE SEACH.

    :ivar ref_number: Fare Family Reference Number
    :ivar fare_familyname: Fare Family Short Name
    :ivar hierarchy: HIERARCHICAL ORDER WITHIN FARE FAMILY
    :ivar cabin: CABIN USED FOR FARE FAMILY
    :ivar commercial_family_details: Indicates Commercial Fare Family Short names
    :ivar description: Short description of the fare family
    :ivar carrier: Carrier code
    :ivar services: Reference to the services details
    """
    ref_number: Optional[int] = field(
        default=None,
        metadata=dict(
            name="refNumber",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{1,3}"
        )
    )
    fare_familyname: Optional[str] = field(
        default=None,
        metadata=dict(
            name="fareFamilyname",
            type="Element",
            min_length=1.0,
            max_length=10.0
        )
    )
    hierarchy: Optional[int] = field(
        default=None,
        metadata=dict(
            name="hierarchy",
            type="Element",
            pattern=r"-?[0-9]{1,4}"
        )
    )
    cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="cabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    commercial_family_details: List[FareFamilyDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="commercialFamilyDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            name="description",
            type="Element",
            min_length=1.0,
            max_length=100.0
        )
    )
    carrier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="carrier",
            type="Element",
            min_length=2.0,
            max_length=3.0
        )
    )
    services: List[ServicesReferences] = field(
        default_factory=list,
        metadata=dict(
            name="services",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class FareInformationType:
    """
    :ivar value_qualifier: Value Qualifier
    :ivar value: Value
    :ivar fare_details: Fare Details
    :ivar identity_number: Identity Number
    :ivar fare_type_grouping: Fare Type Grouping
    :ivar rate_category: Rate Category
    """
    value_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="valueQualifier",
            type="Element",
            pattern=r"[0-9A-Z]{1,3}"
        )
    )
    value: Optional[int] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            pattern=r"-?[0-9]{1,15}"
        )
    )
    fare_details: Optional[FareDetailsType193037C] = field(
        default=None,
        metadata=dict(
            name="fareDetails",
            type="Element"
        )
    )
    identity_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="identityNumber",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    fare_type_grouping: Optional[FareTypeGroupingInformationType] = field(
        default=None,
        metadata=dict(
            name="fareTypeGrouping",
            type="Element"
        )
    )
    rate_category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="rateCategory",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class FareInformationType80868S:
    """To specify fare details.

    :ivar fare_details: Fare details
    """
    class Meta:
        name = "FareInformationType_80868S"

    fare_details: Optional[FareDetailsType] = field(
        default=None,
        metadata=dict(
            name="fareDetails",
            type="Element"
        )
    )


@dataclass
class FareQualifierDetailsType:
    """To specify the details which qualify a fare.

    :ivar movement_type: Route Code
    :ivar fare_categories: Fare categories
    :ivar fare_details: Fare details
    :ivar additional_fare_details: Additional fare details
    :ivar discount_details: Discount details
    """
    movement_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="movementType",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    fare_categories: Optional[FareCategoryCodesTypeI] = field(
        default=None,
        metadata=dict(
            name="fareCategories",
            type="Element"
        )
    )
    fare_details: Optional[FareDetailsTypeI] = field(
        default=None,
        metadata=dict(
            name="fareDetails",
            type="Element"
        )
    )
    additional_fare_details: Optional[AdditionalFareQualifierDetailsTypeI] = field(
        default=None,
        metadata=dict(
            name="additionalFareDetails",
            type="Element"
        )
    )
    discount_details: List[DiscountPenaltyInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="discountDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class FlightCharacteristicsType:
    """Convey flight characteristics.

    :ivar on_time_performance: On-Time Performance
    :ivar in_flight_srv: In flight services
    """
    on_time_performance: Optional[OnTimePerformanceType] = field(
        default=None,
        metadata=dict(
            name="onTimePerformance",
            type="Element"
        )
    )
    in_flight_srv: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="inFlightSrv",
            type="Element",
            min_occurs=0,
            max_occurs=99,
            min_length=1.0,
            max_length=3.0
        )
    )


@dataclass
class FlightProductInformationType:
    """To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar context_details: To specify additional characteristics.
    """
    cabin_product: List[CabinProductDetailsType195516C] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    context_details: Optional[ProductTypeDetailsType] = field(
        default=None,
        metadata=dict(
            name="contextDetails",
            type="Element"
        )
    )


@dataclass
class FlightProductInformationType141442S:
    """To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar context_details: To specify additional characteristics.
    """
    class Meta:
        name = "FlightProductInformationType_141442S"

    cabin_product: List[CabinProductDetailsType205138C] = field(
        default_factory=list,
        metadata=dict(
            name="cabinProduct",
            type="Element",
            min_occurs=0,
            max_occurs=26
        )
    )
    context_details: Optional[ProductTypeDetailsType205137C] = field(
        default=None,
        metadata=dict(
            name="contextDetails",
            type="Element"
        )
    )


@dataclass
class FlightProductInformationType161491S:
    """To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar fare_product_detail: Fare product details
    """
    class Meta:
        name = "FlightProductInformationType_161491S"

    cabin_product: Optional[CabinProductDetailsType229142C] = field(
        default=None,
        metadata=dict(
            name="cabinProduct",
            type="Element"
        )
    )
    fare_product_detail: Optional[FareProductDetailsType] = field(
        default=None,
        metadata=dict(
            name="fareProductDetail",
            type="Element"
        )
    )


@dataclass
class FlightProductInformationType176659S:
    """To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar fare_product_detail: Fare product details
    :ivar corporate_id: Corporate number or name and number
    :ivar break_point: To determine if Fare Breaks at this segment
    :ivar context_details: To specify additional characteristics.
    """
    class Meta:
        name = "FlightProductInformationType_176659S"

    cabin_product: Optional[CabinProductDetailsType] = field(
        default=None,
        metadata=dict(
            name="cabinProduct",
            type="Element"
        )
    )
    fare_product_detail: Optional[FareProductDetailsType248552C] = field(
        default=None,
        metadata=dict(
            name="fareProductDetail",
            type="Element"
        )
    )
    corporate_id: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="corporateId",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=20.0
        )
    )
    break_point: Optional[str] = field(
        default=None,
        metadata=dict(
            name="breakPoint",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    context_details: Optional[ProductTypeDetailsType] = field(
        default=None,
        metadata=dict(
            name="contextDetails",
            type="Element"
        )
    )


@dataclass
class FlightServicesType:
    """Convey services for cabin or class.

    :ivar service_type: Type of service used
    :ivar cabin_info:
    :ivar class_info:
    """
    service_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="serviceType",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    cabin_info: List[CabinInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="cabinInfo",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    class_info: List[ClassInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="classInfo",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class FrequentTravellerIdentificationCodeType:
    """To specify frequent traveler information.

    :ivar frequent_traveller_details: Frequent Traveller Info
    """
    frequent_traveller_details: List[FrequentTravellerIdentificationType] = field(
        default_factory=list,
        metadata=dict(
            name="frequentTravellerDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class HeaderInformationTypeI:
    """To specify header information applicable to the entire message.

    :ivar status: Status
    :ivar date_time_period_details: Date and Time info
    :ivar reference_number: Reference number
    :ivar product_identification: Contains product identification such as UIC code...
    """
    status: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="status",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=3.0
        )
    )
    date_time_period_details: Optional[DateTimePeriodDetailsTypeI] = field(
        default=None,
        metadata=dict(
            name="dateTimePeriodDetails",
            type="Element"
        )
    )
    reference_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="referenceNumber",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    product_identification: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="productIdentification",
            type="Element",
            min_occurs=0,
            max_occurs=2,
            min_length=1.0,
            max_length=35.0
        )
    )


@dataclass
class InteractiveFreeTextType:
    """To provide free form or coded text information.

    :ivar free_text_qualification: Free text qualification
    :ivar free_text: Free text
    """
    free_text_qualification: Optional[FreeTextQualificationTypeI] = field(
        default=None,
        metadata=dict(
            name="freeTextQualification",
            type="Element"
        )
    )
    free_text: Optional[str] = field(
        default=None,
        metadata=dict(
            name="freeText",
            type="Element",
            min_length=1.0,
            max_length=50.0
        )
    )


@dataclass
class InteractiveFreeTextType78534S:
    """To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """
    class Meta:
        name = "InteractiveFreeTextType_78534S"

    free_text_qualification: Optional[FreeTextQualificationType] = field(
        default=None,
        metadata=dict(
            name="freeTextQualification",
            type="Element"
        )
    )
    description: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="description",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class InteractiveFreeTextType78544S:
    """To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """
    class Meta:
        name = "InteractiveFreeTextType_78544S"

    free_text_qualification: Optional[FreeTextQualificationType120769C] = field(
        default=None,
        metadata=dict(
            name="freeTextQualification",
            type="Element"
        )
    )
    description: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="description",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=70.0
        )
    )


@dataclass
class InteractiveFreeTextType78559S:
    """To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """
    class Meta:
        name = "InteractiveFreeTextType_78559S"

    free_text_qualification: Optional[FreeTextQualificationType120769C] = field(
        default=None,
        metadata=dict(
            name="freeTextQualification",
            type="Element"
        )
    )
    description: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="description",
            type="Element",
            min_occurs=0,
            max_occurs=9,
            min_length=1.0,
            max_length=500.0
        )
    )


@dataclass
class ItemNumberType:
    """To specify an item number.

    :ivar item_number: Item number details
    """
    item_number: Optional[ItemNumberIdentificationType192331C] = field(
        default=None,
        metadata=dict(
            name="itemNumber",
            type="Element",
            required=True
        )
    )


@dataclass
class ItemNumberType161497S:
    """To specify item numbers.

    :ivar item_number_id: Indicates the recommendation number.
    :ivar code_share_details: Code share details.
    :ivar price_ticketing: Pricing ticketind details.
    """
    class Meta:
        name = "ItemNumberType_161497S"

    item_number_id: Optional[ItemNumberIdentificationType191597C] = field(
        default=None,
        metadata=dict(
            name="itemNumberId",
            type="Element"
        )
    )
    code_share_details: List[CompanyRoleIdentificationType120771C] = field(
        default_factory=list,
        metadata=dict(
            name="codeShareDetails",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    price_ticketing: Optional[PricingTicketingInformationType] = field(
        default=None,
        metadata=dict(
            name="priceTicketing",
            type="Element"
        )
    )


@dataclass
class ItemNumberType166130S:
    """To specify an item number.

    :ivar item_number_details: Item number details
    """
    class Meta:
        name = "ItemNumberType_166130S"

    item_number_details: List[ItemNumberIdentificationType234878C] = field(
        default_factory=list,
        metadata=dict(
            name="itemNumberDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class ItemNumberType176648S:
    """To specify an item number.

    :ivar item_number_details:
    """
    class Meta:
        name = "ItemNumberType_176648S"

    item_number_details: List[ItemNumberIdentificationType248537C] = field(
        default_factory=list,
        metadata=dict(
            name="itemNumberDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class ItemNumberType80866S:
    """To specify an item number.

    :ivar item_number_details: Item number details
    """
    class Meta:
        name = "ItemNumberType_80866S"

    item_number_details: Optional[ItemNumberIdentificationType] = field(
        default=None,
        metadata=dict(
            name="itemNumberDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class MiniRulesType78547S:
    """To specify the restrictions.

    :ivar restriction_type: Type of restriction: PTC, Max Adv Res, Max Ticketing After Res, ...
    :ivar category: Categoty of restriction: PTC, Max Adv Pur, Days, ...
    :ivar indicator: Indicators
    :ivar mini_rules: Mini rules
    """
    class Meta:
        name = "MiniRulesType_78547S"

    restriction_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="restrictionType",
            type="Element",
            min_length=0.0,
            max_length=6.0
        )
    )
    category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="category",
            type="Element",
            required=True,
            min_length=0.0,
            max_length=3.0
        )
    )
    indicator: Optional[MiniRulesIndicatorType] = field(
        default=None,
        metadata=dict(
            name="indicator",
            type="Element"
        )
    )
    mini_rules: List[MiniRulesDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="miniRules",
            type="Element",
            min_occurs=0,
            max_occurs=5
        )
    )


@dataclass
class MonetaryInformationType:
    """To specify monetary information details.

    :ivar monetary_detail: Monetary information.
    """
    monetary_detail: List[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetail",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class MonetaryInformationTypeI:
    """To convey monetary amounts, rates and percentages.

    :ivar monetary_details: Monetary details
    """
    monetary_details: List[MonetaryInformationDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class MonetaryInformationType174241S:
    """To convey monetary amounts, rates and percentages.

    :ivar monetary_details:
    :ivar other_monetary_details:
    """
    class Meta:
        name = "MonetaryInformationType_174241S"

    monetary_details: Optional[MonetaryInformationDetailsType245528C] = field(
        default=None,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            required=True
        )
    )
    other_monetary_details: List[MonetaryInformationDetailsType245528C] = field(
        default_factory=list,
        metadata=dict(
            name="otherMonetaryDetails",
            type="Element",
            min_occurs=0,
            max_occurs=19
        )
    )


@dataclass
class MonetaryInformationType185955S:
    """To specify monetary information details.

    :ivar monetary_detail: Monetary information
    """
    class Meta:
        name = "MonetaryInformationType_185955S"

    monetary_detail: List[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetail",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )


@dataclass
class MonetaryInformationType193024S:
    """To specify monetary information details.

    :ivar monetary_detail: Monetary information.
    """
    class Meta:
        name = "MonetaryInformationType_193024S"

    monetary_detail: List[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetail",
            type="Element",
            min_occurs=0,
            max_occurs=30
        )
    )


@dataclass
class OriginAndDestinationRequestType:
    """To convey information regarding Requested Segments.

    :ivar seg_ref: Requested segment number
    :ivar location_forcing: Forces arrival or departure, from/to the same airport/city
    """
    seg_ref: Optional[int] = field(
        default=None,
        metadata=dict(
            name="segRef",
            type="Element",
            required=True,
            pattern=r"-?[0-9]{1,2}"
        )
    )
    location_forcing: List[ItineraryDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="locationForcing",
            type="Element",
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class PricingTicketingSubsequentType193023S:
    """To convey additional information related to a ticket.

    :ivar pax_fare_num: Passenger fare product number
    :ivar total_fare_amount: Total fare amount
    :ivar total_tax_amount: Total tax amount
    :ivar code_share_details: Code share details.
    :ivar monetary_details: Monetary information.
    :ivar pricing_ticketing: Pricing ticketing details.
    """
    class Meta:
        name = "PricingTicketingSubsequentType_193023S"

    pax_fare_num: Optional[str] = field(
        default=None,
        metadata=dict(
            name="paxFareNum",
            type="Element",
            required=True,
            min_length=1.0,
            max_length=3.0
        )
    )
    total_fare_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="totalFareAmount",
            type="Element",
            required=True
        )
    )
    total_tax_amount: Optional[float] = field(
        default=None,
        metadata=dict(
            name="totalTaxAmount",
            type="Element"
        )
    )
    code_share_details: List[CompanyRoleIdentificationType120771C] = field(
        default_factory=list,
        metadata=dict(
            name="codeShareDetails",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    monetary_details: List[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="monetaryDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    pricing_ticketing: Optional[PricingTicketingInformationType] = field(
        default=None,
        metadata=dict(
            name="pricingTicketing",
            type="Element"
        )
    )


@dataclass
class ProductInformationType:
    """To specify details related to routing status of a product.

    :ivar product_details_qualifier: value of the Qualifier: INT for International DOM for Domestic EUR for European otherwise CM#10569 INVALID INTERNATIONAL INDICATOR is returned.
    :ivar booking_class_details:
    """
    product_details_qualifier: Optional[str] = field(
        default=None,
        metadata=dict(
            name="productDetailsQualifier",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    booking_class_details: List[ProductDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="bookingClassDetails",
            type="Element",
            min_occurs=0,
            max_occurs=26
        )
    )


@dataclass
class ProposedSegmentType:
    """To specify the parameters used for product quality.

    :ivar flight_proposal: Parameters for proposed flight group
    :ivar flight_characteristic: Flight characteristics.
    :ivar maj_cabin: Majority cabin
    """
    flight_proposal: List[ProposedSegmentDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="flightProposal",
            type="Element",
            min_occurs=1,
            max_occurs=9
        )
    )
    flight_characteristic: Optional[str] = field(
        default=None,
        metadata=dict(
            name="flightCharacteristic",
            type="Element",
            min_length=0.0,
            max_length=3.0
        )
    )
    maj_cabin: Optional[str] = field(
        default=None,
        metadata=dict(
            name="majCabin",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )


@dataclass
class ReferenceInfoType:
    """To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    :ivar dummy_net:
    """
    referencing_detail: List[ReferencingDetailsType191583C] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=200
        )
    )
    dummy_net: Optional[str] = field(
        default=None,
        metadata=dict(
            name="Dummy.NET",
            type="Element"
        )
    )


@dataclass
class ReferenceInfoType133176S:
    """To specify an association between references given to travelers, to
    products, to services.

    :ivar referencing_detail: Referencing details
    """
    class Meta:
        name = "ReferenceInfoType_133176S"

    referencing_detail: List[ReferencingDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class ReferenceInfoType134839S:
    """To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    """
    class Meta:
        name = "ReferenceInfoType_134839S"

    referencing_detail: List[ReferencingDetailsType195561C] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class ReferenceInfoType134840S:
    """To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    """
    class Meta:
        name = "ReferenceInfoType_134840S"

    referencing_detail: List[ReferencingDetailsType195561C] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=200
        )
    )


@dataclass
class ReferenceInfoType165972S:
    """To provide specific Hotel reference identification.

    :ivar reference_details: Reference details
    """
    class Meta:
        name = "ReferenceInfoType_165972S"

    reference_details: List[ReferencingDetailsType234704C] = field(
        default_factory=list,
        metadata=dict(
            name="referenceDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class ReferenceInfoType176658S:
    """To specify an association between references given to travelers, to
    products, to services.

    :ivar referencing_detail: Referencing details
    """
    class Meta:
        name = "ReferenceInfoType_176658S"

    referencing_detail: List[ReferencingDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="referencingDetail",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )


@dataclass
class SegmentRepetitionControlTypeI:
    """To indicate the number of segment group repetitions.

    :ivar segment_control_details: Segment control details
    """
    segment_control_details: List[SegmentRepetitionControlDetailsTypeI] = field(
        default_factory=list,
        metadata=dict(
            name="segmentControlDetails",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class SelectionDetailsType:
    """To specify the details for making a selection.

    :ivar carrier_fee_details: Carrier fees options
    """
    carrier_fee_details: Optional[SelectionDetailsInformationType] = field(
        default=None,
        metadata=dict(
            name="carrierFeeDetails",
            type="Element",
            required=True
        )
    )


@dataclass
class SequenceDetailsTypeU:
    """To provide details relating to the sequence.

    :ivar sequence_details: Sequence details
    """
    sequence_details: Optional[SequenceInformationTypeU] = field(
        default=None,
        metadata=dict(
            name="sequenceDetails",
            type="Element"
        )
    )


@dataclass
class SpecialRequirementsDetailsType:
    """To specify special requests or service s information relating to a
    traveller.

    :ivar service_requirements_info: To specify the Service Requirement of the customer
    :ivar seat_details: Seat details
    """
    service_requirements_info: Optional[SpecialRequirementsTypeDetailsType] = field(
        default=None,
        metadata=dict(
            name="serviceRequirementsInfo",
            type="Element",
            required=True
        )
    )
    seat_details: List[SpecialRequirementsDataDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="seatDetails",
            type="Element",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class SpecificDataInformationType:
    """To specify miscellaneous data by first identifying the type of data to be
    sent and then the actual data.

    :ivar data_type_information: Carrier fee description
    :ivar data_information: Data information
    """
    data_type_information: Optional[DataTypeInformationType] = field(
        default=None,
        metadata=dict(
            name="dataTypeInformation",
            type="Element",
            required=True
        )
    )
    data_information: List[DataInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="dataInformation",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class SpecificTravellerType:
    """To specify additional details about a particular traveller.

    :ivar traveller_details: Traveller details
    """
    traveller_details: List[SpecificTravellerDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="travellerDetails",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class StatusType:
    """To advise the requester system the status of the reply.

    :ivar status: Status details
    """
    status: List[StatusDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="status",
            type="Element",
            min_occurs=1,
            max_occurs=10
        )
    )


@dataclass
class StatusType182386S:
    """To advise the requester system the status of the reply.

    :ivar status_information: STATUS DETAILS
    """
    class Meta:
        name = "StatusType_182386S"

    status_information: List[StatusDetailsType256255C] = field(
        default_factory=list,
        metadata=dict(
            name="statusInformation",
            type="Element",
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class TaxType:
    """To specify details relating to tax(es).

    :ivar tax_category: Tax category
    :ivar tax_details: Tax details
    """
    tax_category: Optional[str] = field(
        default=None,
        metadata=dict(
            name="taxCategory",
            type="Element",
            min_length=1.0,
            max_length=3.0
        )
    )
    tax_details: List[TaxDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="taxDetails",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class TransportIdentifierType:
    """To specify the transport service(s) which is /are to be updated or
    cancelled.

    :ivar company_identification: Company identification
    """
    company_identification: Optional[CompanyIdentificationTypeI] = field(
        default=None,
        metadata=dict(
            name="companyIdentification",
            type="Element"
        )
    )


@dataclass
class TravelProductType:
    """Contains flight travel (date, time, flight number,...) and posting
    avaibility information.

    :ivar product_date_time: Date and time of departure and arrival
    :ivar location: Location of departure and arrival
    :ivar company_id:
    :ivar flight_ortrain_number: Flight number or trainNumber
    :ivar product_detail: Product details
    :ivar add_product_detail: Additional product details
    :ivar attribute_details: Attribute details
    """
    product_date_time: Optional[ProductDateTimeType] = field(
        default=None,
        metadata=dict(
            name="productDateTime",
            type="Element",
            required=True
        )
    )
    location: List[LocationIdentificationDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="location",
            type="Element",
            min_occurs=1,
            max_occurs=2
        )
    )
    company_id: Optional[CompanyIdentificationType] = field(
        default=None,
        metadata=dict(
            name="companyId",
            type="Element"
        )
    )
    flight_ortrain_number: Optional[str] = field(
        default=None,
        metadata=dict(
            name="flightOrtrainNumber",
            type="Element",
            min_length=1.0,
            max_length=8.0
        )
    )
    product_detail: Optional[AdditionalProductDetailsType] = field(
        default=None,
        metadata=dict(
            name="productDetail",
            type="Element"
        )
    )
    add_product_detail: Optional[ProductFacilitiesType] = field(
        default=None,
        metadata=dict(
            name="addProductDetail",
            type="Element"
        )
    )
    attribute_details: List[CodedAttributeInformationType270108C] = field(
        default_factory=list,
        metadata=dict(
            name="attributeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )


@dataclass
class TravellerReferenceInformationType:
    """To specify traveller/personal details.

    :ivar ptc: Requested passenger type
    :ivar traveller: Traveller details
    """
    ptc: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="ptc",
            type="Element",
            min_occurs=0,
            max_occurs=3,
            min_length=1.0,
            max_length=6.0
        )
    )
    traveller: List[TravellerDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="traveller",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )


@dataclass
class UserIdentificationType:
    """User Identification.

    :ivar office_identification: Originator Identification Details
    :ivar office_type: Used to specify which kind of info is given in DE 9900.
    :ivar office_code: The code given to an agent by the originating reservation system.
    """
    office_identification: Optional[OriginatorIdentificationDetailsTypeI] = field(
        default=None,
        metadata=dict(
            name="officeIdentification",
            type="Element"
        )
    )
    office_type: Optional[str] = field(
        default=None,
        metadata=dict(
            name="officeType",
            type="Element",
            min_length=1.0,
            max_length=1.0
        )
    )
    office_code: Optional[str] = field(
        default=None,
        metadata=dict(
            name="officeCode",
            type="Element",
            min_length=1.0,
            max_length=30.0
        )
    )


@dataclass
class ValueSearchCriteriaType:
    """To specify Criteria with list of parameters.

    :ivar ref:
    :ivar value:
    :ivar criteria_details:
    """
    ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="ref",
            type="Element",
            min_length=1.0,
            max_length=35.0
        )
    )
    value: Optional[str] = field(
        default=None,
        metadata=dict(
            name="value",
            type="Element",
            min_length=1.0,
            max_length=18.0
        )
    )
    criteria_details: List[CriteriaiDetaislType] = field(
        default_factory=list,
        metadata=dict(
            name="criteriaDetails",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class FareMasterPricerTravelBoardSearchReply:
    """Master Pricer Travel Board Search Reply Flex Pricer Flex Pricer.

    :ivar reply_status: Gives status about reply : type of process, region , CPU etc..
    :ivar error_message: Error message
    :ivar conversion_rate: Specifies the currency used for pricing.
    :ivar solution_family: Solution Family
    :ivar family_information: Details of the fare families processed
    :ivar amount_info_for_all_pax: Amount information for all passengers
    :ivar amount_info_per_pax: Amount information per passengers
    :ivar fee_details: Fee/Reduction details.
    :ivar bucket_info: Bucket information
    :ivar company_id_text: Free text identifying an airline in a code share.
    :ivar office_id_details: List of Office Id Details
    :ivar flight_index: List of flights
    :ivar recommendation: Recommendation details
    :ivar other_solutions: Additional solutions, such as Rail solutions...
    :ivar warning_info: Warning information
    :ivar global_information: Global information
    :ivar service_fees_grp:
    :ivar value:
    :ivar mnr_grp:
    """
    class Meta:
        name = "Fare_MasterPricerTravelBoardSearchReply"
        namespace = "http://xml.amadeus.com/FMPTBR_15_3_1A"

    reply_status: Optional[StatusType] = field(
        default=None,
        metadata=dict(
            name="replyStatus",
            type="Element"
        )
    )
    error_message: Optional["FareMasterPricerTravelBoardSearchReply.ErrorMessage"] = field(
        default=None,
        metadata=dict(
            name="errorMessage",
            type="Element"
        )
    )
    conversion_rate: Optional[ConversionRateTypeI] = field(
        default=None,
        metadata=dict(
            name="conversionRate",
            type="Element"
        )
    )
    solution_family: List[FareInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="solutionFamily",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    family_information: List[FareFamilyType] = field(
        default_factory=list,
        metadata=dict(
            name="familyInformation",
            type="Element",
            min_occurs=0,
            max_occurs=200
        )
    )
    amount_info_for_all_pax: Optional["FareMasterPricerTravelBoardSearchReply.AmountInfoForAllPax"] = field(
        default=None,
        metadata=dict(
            name="amountInfoForAllPax",
            type="Element"
        )
    )
    amount_info_per_pax: List["FareMasterPricerTravelBoardSearchReply.AmountInfoPerPax"] = field(
        default_factory=list,
        metadata=dict(
            name="amountInfoPerPax",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    fee_details: List["FareMasterPricerTravelBoardSearchReply.FeeDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="feeDetails",
            type="Element",
            min_occurs=0,
            max_occurs=2099
        )
    )
    bucket_info: List[BucketInformationType] = field(
        default_factory=list,
        metadata=dict(
            name="bucketInfo",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    company_id_text: List[CompanyIdentificationTextType] = field(
        default_factory=list,
        metadata=dict(
            name="companyIdText",
            type="Element",
            min_occurs=0,
            max_occurs=5000
        )
    )
    office_id_details: List["FareMasterPricerTravelBoardSearchReply.OfficeIdDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="officeIdDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    flight_index: List["FareMasterPricerTravelBoardSearchReply.FlightIndex"] = field(
        default_factory=list,
        metadata=dict(
            name="flightIndex",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    recommendation: List["FareMasterPricerTravelBoardSearchReply.Recommendation"] = field(
        default_factory=list,
        metadata=dict(
            name="recommendation",
            type="Element",
            min_occurs=0,
            max_occurs=100000
        )
    )
    other_solutions: List["FareMasterPricerTravelBoardSearchReply.OtherSolutions"] = field(
        default_factory=list,
        metadata=dict(
            name="otherSolutions",
            type="Element",
            min_occurs=0,
            max_occurs=100009
        )
    )
    warning_info: List["FareMasterPricerTravelBoardSearchReply.WarningInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="warningInfo",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    global_information: List["FareMasterPricerTravelBoardSearchReply.GlobalInformation"] = field(
        default_factory=list,
        metadata=dict(
            name="globalInformation",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    service_fees_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp"] = field(
        default_factory=list,
        metadata=dict(
            name="serviceFeesGrp",
            type="Element",
            min_occurs=0,
            max_occurs=3
        )
    )
    value: List[ValueSearchCriteriaType] = field(
        default_factory=list,
        metadata=dict(
            name="value",
            type="Element",
            min_occurs=0,
            max_occurs=100009
        )
    )
    mnr_grp: Optional["FareMasterPricerTravelBoardSearchReply.MnrGrp"] = field(
        default=None,
        metadata=dict(
            name="mnrGrp",
            type="Element"
        )
    )

    @dataclass
    class ErrorMessage:
        """
        :ivar application_error: Application error details.
        :ivar error_message_text: Type of error message and free text
        """
        application_error: Optional[ApplicationErrorInformationType78543S] = field(
            default=None,
            metadata=dict(
                name="applicationError",
                type="Element",
                required=True
            )
        )
        error_message_text: Optional[InteractiveFreeTextType78544S] = field(
            default=None,
            metadata=dict(
                name="errorMessageText",
                type="Element"
            )
        )

    @dataclass
    class AmountInfoForAllPax:
        """
        :ivar itinerary_amounts: Itinerary amounts for all passengers
        :ivar amounts_per_sgt: Amounts information per segment
        """
        itinerary_amounts: Optional[MonetaryInformationType] = field(
            default=None,
            metadata=dict(
                name="itineraryAmounts",
                type="Element",
                required=True
            )
        )
        amounts_per_sgt: List["FareMasterPricerTravelBoardSearchReply.AmountInfoForAllPax.AmountsPerSgt"] = field(
            default_factory=list,
            metadata=dict(
                name="amountsPerSgt",
                type="Element",
                min_occurs=0,
                max_occurs=9
            )
        )

        @dataclass
        class AmountsPerSgt:
            """
            :ivar sgt_ref: Requested segment reference
            :ivar amounts: Amounts : Issue total amount, issue taxes amount, non refundable taxes amount
            """
            sgt_ref: Optional[ReferenceInfoType133176S] = field(
                default=None,
                metadata=dict(
                    name="sgtRef",
                    type="Element",
                    required=True
                )
            )
            amounts: Optional[MonetaryInformationType] = field(
                default=None,
                metadata=dict(
                    name="amounts",
                    type="Element"
                )
            )

    @dataclass
    class AmountInfoPerPax:
        """
        :ivar pax_ref: Passenger references
        :ivar pax_attributes: Passenger attributes : Infant indicator
        :ivar itinerary_amounts: Itinerary amounts information
        :ivar amounts_per_sgt: Amounts per segment
        """
        pax_ref: Optional[SpecificTravellerType] = field(
            default=None,
            metadata=dict(
                name="paxRef",
                type="Element",
                required=True
            )
        )
        pax_attributes: Optional[FareInformationType80868S] = field(
            default=None,
            metadata=dict(
                name="paxAttributes",
                type="Element"
            )
        )
        itinerary_amounts: Optional[MonetaryInformationType] = field(
            default=None,
            metadata=dict(
                name="itineraryAmounts",
                type="Element",
                required=True
            )
        )
        amounts_per_sgt: List["FareMasterPricerTravelBoardSearchReply.AmountInfoPerPax.AmountsPerSgt"] = field(
            default_factory=list,
            metadata=dict(
                name="amountsPerSgt",
                type="Element",
                min_occurs=0,
                max_occurs=9
            )
        )

        @dataclass
        class AmountsPerSgt:
            """
            :ivar sgt_ref: Requested segment reference
            :ivar amounts: Amounts : Issue total amount, issue taxes amount, non refundable taxes amount
            """
            sgt_ref: Optional[ReferenceInfoType133176S] = field(
                default=None,
                metadata=dict(
                    name="sgtRef",
                    type="Element",
                    required=True
                )
            )
            amounts: Optional[MonetaryInformationType] = field(
                default=None,
                metadata=dict(
                    name="amounts",
                    type="Element"
                )
            )

    @dataclass
    class FeeDetails:
        """
        :ivar fee_reference: Fee/Reduction Reference number.
        :ivar fee_information: Fee/Reduction information.
        :ivar fee_parameters: Fee/Reduction parameters.
        :ivar converted_or_original_info: To specify conversion rate details
        """
        fee_reference: Optional[ItemReferencesAndVersionsType78564S] = field(
            default=None,
            metadata=dict(
                name="feeReference",
                type="Element",
                required=True
            )
        )
        fee_information: Optional[DiscountAndPenaltyInformationType] = field(
            default=None,
            metadata=dict(
                name="feeInformation",
                type="Element"
            )
        )
        fee_parameters: Optional[AttributeType78561S] = field(
            default=None,
            metadata=dict(
                name="feeParameters",
                type="Element"
            )
        )
        converted_or_original_info: Optional[ConversionRateTypeI78562S] = field(
            default=None,
            metadata=dict(
                name="convertedOrOriginalInfo",
                type="Element"
            )
        )

    @dataclass
    class OfficeIdDetails:
        """
        :ivar office_id_information: Office Id Information
        :ivar office_id_reference: Office Id Reference Number
        """
        office_id_information: Optional[UserIdentificationType] = field(
            default=None,
            metadata=dict(
                name="officeIdInformation",
                type="Element",
                required=True
            )
        )
        office_id_reference: Optional[ItemReferencesAndVersionsType78536S] = field(
            default=None,
            metadata=dict(
                name="officeIdReference",
                type="Element",
                required=True
            )
        )

    @dataclass
    class FlightIndex:
        """
        :ivar requested_segment_ref: Indicates references and details about requested segments
        :ivar group_of_flights: List of flights per requested segment
        """
        requested_segment_ref: Optional[OriginAndDestinationRequestType] = field(
            default=None,
            metadata=dict(
                name="requestedSegmentRef",
                type="Element",
                required=True
            )
        )
        group_of_flights: List["FareMasterPricerTravelBoardSearchReply.FlightIndex.GroupOfFlights"] = field(
            default_factory=list,
            metadata=dict(
                name="groupOfFlights",
                type="Element",
                min_occurs=1,
                max_occurs=100000
            )
        )

        @dataclass
        class GroupOfFlights:
            """
            :ivar prop_flight_gr_detail: To indicate parameters for proposed flight group.
            :ivar flight_details: List of flight per Elapse Flying time
            """
            prop_flight_gr_detail: Optional[ProposedSegmentType] = field(
                default=None,
                metadata=dict(
                    name="propFlightGrDetail",
                    type="Element",
                    required=True
                )
            )
            flight_details: List["FareMasterPricerTravelBoardSearchReply.FlightIndex.GroupOfFlights.FlightDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="flightDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=4
                )
            )

            @dataclass
            class FlightDetails:
                """
                :ivar flight_information: Specification of details on the flight and posting availability
                :ivar avl_info: returns booking class and availability context
                :ivar technical_stop: Details on Flight date, time and location of technical stop or change of gauge
                :ivar commercial_agreement: Code Share Agreement description for current flight.
                :ivar add_info: Additional Info about flight, such as Reference number, and several options
                :ivar flight_characteristics: Flight characteristics
                :ivar flight_services: Flight Services by cabin/rbd
                """
                flight_information: Optional[TravelProductType] = field(
                    default=None,
                    metadata=dict(
                        name="flightInformation",
                        type="Element",
                        required=True
                    )
                )
                avl_info: List[FlightProductInformationType141442S] = field(
                    default_factory=list,
                    metadata=dict(
                        name="avlInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                technical_stop: List[DateAndTimeInformationType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="technicalStop",
                        type="Element",
                        min_occurs=0,
                        max_occurs=5
                    )
                )
                commercial_agreement: Optional[CommercialAgreementsType] = field(
                    default=None,
                    metadata=dict(
                        name="commercialAgreement",
                        type="Element"
                    )
                )
                add_info: Optional[HeaderInformationTypeI] = field(
                    default=None,
                    metadata=dict(
                        name="addInfo",
                        type="Element"
                    )
                )
                flight_characteristics: Optional[FlightCharacteristicsType] = field(
                    default=None,
                    metadata=dict(
                        name="flightCharacteristics",
                        type="Element"
                    )
                )
                flight_services: List[FlightServicesType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="flightServices",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9
                    )
                )

    @dataclass
    class Recommendation:
        """
        :ivar item_number: Specification of the item number
        :ivar warning_message: To describe type of recommendation
        :ivar fare_family_ref: Indicates the Fare family reference.
        :ivar rec_price_info: Recommendation Price and Taxes.
        :ivar mini_rule: Mini rules
        :ivar segment_flight_ref: Indicates reference of Flight or the fee reference valid for all pax (usage:start with the 1 possible Fee reference, then provide the segments references)
        :ivar recommandation_segments_fare_details: Fare details per reuqested segments for all passengers.
        :ivar pax_fare_product: Passenger fare product details
        :ivar specific_rec_details: Specific recommendation details
        """
        item_number: Optional[ItemNumberType161497S] = field(
            default=None,
            metadata=dict(
                name="itemNumber",
                type="Element",
                required=True
            )
        )
        warning_message: List[InteractiveFreeTextType78544S] = field(
            default_factory=list,
            metadata=dict(
                name="warningMessage",
                type="Element",
                min_occurs=0,
                max_occurs=4
            )
        )
        fare_family_ref: Optional[ReferenceInfoType133176S] = field(
            default=None,
            metadata=dict(
                name="fareFamilyRef",
                type="Element"
            )
        )
        rec_price_info: Optional[MonetaryInformationType193024S] = field(
            default=None,
            metadata=dict(
                name="recPriceInfo",
                type="Element",
                required=True
            )
        )
        mini_rule: List[MiniRulesType78547S] = field(
            default_factory=list,
            metadata=dict(
                name="miniRule",
                type="Element",
                min_occurs=0,
                max_occurs=9
            )
        )
        segment_flight_ref: List[ReferenceInfoType] = field(
            default_factory=list,
            metadata=dict(
                name="segmentFlightRef",
                type="Element",
                min_occurs=0,
                max_occurs=100009
            )
        )
        recommandation_segments_fare_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.RecommandationSegmentsFareDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="recommandationSegmentsFareDetails",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )
        pax_fare_product: List["FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct"] = field(
            default_factory=list,
            metadata=dict(
                name="paxFareProduct",
                type="Element",
                min_occurs=1,
                max_occurs=10
            )
        )
        specific_rec_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="specificRecDetails",
                type="Element",
                min_occurs=0,
                max_occurs=100000
            )
        )

        @dataclass
        class RecommandationSegmentsFareDetails:
            """
            :ivar recommendation_seg_ref: Reference and details about requested segments.
            :ivar segment_monetary_information: Amounts per requested segment.
            """
            recommendation_seg_ref: Optional[OriginAndDestinationRequestType] = field(
                default=None,
                metadata=dict(
                    name="recommendationSegRef",
                    type="Element",
                    required=True
                )
            )
            segment_monetary_information: Optional[MonetaryInformationType] = field(
                default=None,
                metadata=dict(
                    name="segmentMonetaryInformation",
                    type="Element"
                )
            )

        @dataclass
        class PaxFareProduct:
            """
            :ivar pax_fare_detail: Passenger Fare Details.
            :ivar fee_ref: Indicates Fee references (usage: start with the 1 possible Fee reference, then provide the segments references)
            :ivar pax_reference: Passenger Reference
            :ivar passenger_tax_details: add tax details for each passenger of each recommendations.
            :ivar fare: fare Details
            :ivar fare_details: Fare details by Requested segment number
            """
            pax_fare_detail: Optional[PricingTicketingSubsequentType193023S] = field(
                default=None,
                metadata=dict(
                    name="paxFareDetail",
                    type="Element",
                    required=True
                )
            )
            fee_ref: Optional[ReferenceInfoType134839S] = field(
                default=None,
                metadata=dict(
                    name="feeRef",
                    type="Element"
                )
            )
            pax_reference: List[TravellerReferenceInformationType] = field(
                default_factory=list,
                metadata=dict(
                    name="paxReference",
                    type="Element",
                    min_occurs=1,
                    max_occurs=6
                )
            )
            passenger_tax_details: Optional[TaxType] = field(
                default=None,
                metadata=dict(
                    name="passengerTaxDetails",
                    type="Element"
                )
            )
            fare: List["FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.Fare"] = field(
                default_factory=list,
                metadata=dict(
                    name="fare",
                    type="Element",
                    min_occurs=0,
                    max_occurs=7
                )
            )
            fare_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.FareDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="fareDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=6
                )
            )

            @dataclass
            class Fare:
                """
                :ivar pricing_message: Last Date to Ticket, Penalties
                :ivar monetary_information: Amount of penalties, Surcharges...
                """
                pricing_message: Optional[InteractiveFreeTextType78559S] = field(
                    default=None,
                    metadata=dict(
                        name="pricingMessage",
                        type="Element",
                        required=True
                    )
                )
                monetary_information: Optional[MonetaryInformationType185955S] = field(
                    default=None,
                    metadata=dict(
                        name="monetaryInformation",
                        type="Element"
                    )
                )

            @dataclass
            class FareDetails:
                """
                :ivar segment_ref: Reference of the Requested Segment
                :ivar group_of_fares: Contains the fare details as PTC,Fare Basis, Fare Family applied for each segment
                :ivar psg_seg_monetary_information: Amounts per passenger per requested segment.
                :ivar maj_cabin: Majority Cabin Info
                """
                segment_ref: Optional[OriginAndDestinationRequestType] = field(
                    default=None,
                    metadata=dict(
                        name="segmentRef",
                        type="Element",
                        required=True
                    )
                )
                group_of_fares: List["FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.FareDetails.GroupOfFares"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="groupOfFares",
                        type="Element",
                        min_occurs=0,
                        max_occurs=4
                    )
                )
                psg_seg_monetary_information: Optional[MonetaryInformationType] = field(
                    default=None,
                    metadata=dict(
                        name="psgSegMonetaryInformation",
                        type="Element"
                    )
                )
                maj_cabin: List[ProductInformationType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="majCabin",
                        type="Element",
                        min_occurs=0,
                        max_occurs=10
                    )
                )

                @dataclass
                class GroupOfFares:
                    """
                    :ivar product_information: Contains details of Flight and Fare
                    :ivar fare_calculation_code_details: Fare calculation code details
                    :ivar ticket_infos: Ticket designator, ticket code and fare basis.
                    :ivar fare_families_ref: Reference of Fare Family for each Fare Component
                    """
                    product_information: Optional[FlightProductInformationType176659S] = field(
                        default=None,
                        metadata=dict(
                            name="productInformation",
                            type="Element",
                            required=True
                        )
                    )
                    fare_calculation_code_details: List[FareCalculationCodeDetailsType] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareCalculationCodeDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9
                        )
                    )
                    ticket_infos: Optional[FareQualifierDetailsType] = field(
                        default=None,
                        metadata=dict(
                            name="ticketInfos",
                            type="Element"
                        )
                    )
                    fare_families_ref: Optional[ReferenceInfoType176658S] = field(
                        default=None,
                        metadata=dict(
                            name="fareFamiliesRef",
                            type="Element"
                        )
                    )

        @dataclass
        class SpecificRecDetails:
            """
            :ivar specific_rec_item: Recommendation details
            :ivar specific_product_details: Specific fare product details
            """
            specific_rec_item: Optional[ItemReferencesAndVersionsType] = field(
                default=None,
                metadata=dict(
                    name="specificRecItem",
                    type="Element",
                    required=True
                )
            )
            specific_product_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="specificProductDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class SpecificProductDetails:
                """
                :ivar product_references: Product details
                :ivar fare_context_details: Specific fare details per requested segments.
                """
                product_references: Optional[PricingTicketingSubsequentType] = field(
                    default=None,
                    metadata=dict(
                        name="productReferences",
                        type="Element",
                        required=True
                    )
                )
                fare_context_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails.FareContextDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="fareContextDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )

                @dataclass
                class FareContextDetails:
                    """
                    :ivar requested_segment_info: Reference of requested segment
                    :ivar cnx_context_details: Fare connection context details
                    """
                    requested_segment_info: Optional[OriginAndDestinationRequestType134833S] = field(
                        default=None,
                        metadata=dict(
                            name="requestedSegmentInfo",
                            type="Element",
                            required=True
                        )
                    )
                    cnx_context_details: List["FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails.FareContextDetails.CnxContextDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="cnxContextDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=4
                        )
                    )

                    @dataclass
                    class CnxContextDetails:
                        """
                        :ivar fare_cnx_info: Fare connection context details
                        """
                        fare_cnx_info: Optional[FlightProductInformationType] = field(
                            default=None,
                            metadata=dict(
                                name="fareCnxInfo",
                                type="Element",
                                required=True
                            )
                        )

    @dataclass
    class OtherSolutions:
        """
        :ivar reference: Reference to the current solution
        :ivar amt_group: Describes several amount for each sequence
        :ivar psg_info: Passenger Related info (discount card, PTC, fare info, amount ...)
        """
        reference: Optional[SequenceDetailsTypeU] = field(
            default=None,
            metadata=dict(
                name="reference",
                type="Element",
                required=True
            )
        )
        amt_group: List["FareMasterPricerTravelBoardSearchReply.OtherSolutions.AmtGroup"] = field(
            default_factory=list,
            metadata=dict(
                name="amtGroup",
                type="Element",
                min_occurs=0,
                max_occurs=10
            )
        )
        psg_info: List["FareMasterPricerTravelBoardSearchReply.OtherSolutions.PsgInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="psgInfo",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )

        @dataclass
        class AmtGroup:
            """
            :ivar ref: reference to the current amount (per bound, per segment...)
            :ivar amount: Amount Description
            """
            ref: Optional[ReferenceInfoType165972S] = field(
                default=None,
                metadata=dict(
                    name="ref",
                    type="Element",
                    required=True
                )
            )
            amount: Optional[MonetaryInformationTypeI] = field(
                default=None,
                metadata=dict(
                    name="amount",
                    type="Element"
                )
            )

        @dataclass
        class PsgInfo:
            """
            :ivar ref: passenger reference
            :ivar description: Passenger Description Info
            :ivar freq_traveller: Passenger frequent traveler info
            :ivar amount: amount per passenger or group of passenger
            :ivar fare: Fare description
            :ivar attribute: Additional Information
            """
            ref: Optional[SegmentRepetitionControlTypeI] = field(
                default=None,
                metadata=dict(
                    name="ref",
                    type="Element",
                    required=True
                )
            )
            description: Optional[FareInformationTypeI] = field(
                default=None,
                metadata=dict(
                    name="description",
                    type="Element"
                )
            )
            freq_traveller: Optional[FrequentTravellerIdentificationCodeType] = field(
                default=None,
                metadata=dict(
                    name="freqTraveller",
                    type="Element"
                )
            )
            amount: Optional[MonetaryInformationTypeI] = field(
                default=None,
                metadata=dict(
                    name="amount",
                    type="Element"
                )
            )
            fare: Optional[FlightProductInformationType161491S] = field(
                default=None,
                metadata=dict(
                    name="fare",
                    type="Element"
                )
            )
            attribute: List[AttributeTypeU] = field(
                default_factory=list,
                metadata=dict(
                    name="attribute",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

    @dataclass
    class WarningInfo:
        """
        :ivar global_message_marker: Dummy Segment
        :ivar global_message: Informative free text information
        """
        global_message_marker: Optional[DummySegmentTypeI] = field(
            default=None,
            metadata=dict(
                name="globalMessageMarker",
                type="Element",
                required=True
            )
        )
        global_message: Optional[InteractiveFreeTextType78534S] = field(
            default=None,
            metadata=dict(
                name="globalMessage",
                type="Element",
                required=True
            )
        )

    @dataclass
    class GlobalInformation:
        """
        :ivar attributes: Coded attributes
        """
        attributes: Optional[CodedAttributeType] = field(
            default=None,
            metadata=dict(
                name="attributes",
                type="Element",
                required=True
            )
        )

    @dataclass
    class ServiceFeesGrp:
        """
        :ivar service_type_info: Service fee type (OC)
        :ivar service_fee_ref_grp: Service fee reference (OC ,OCM, OCC)
        :ivar service_coverage_info_grp: Service coverage information per passenger
        :ivar global_message_marker: Globalmessage marker
        :ivar service_fee_info_grp: Service fee information per passenger
        :ivar service_details_grp: Description of applicable services
        :ivar free_bag_allowance_grp: Free baggage allowance information group
        """
        service_type_info: Optional[SelectionDetailsType] = field(
            default=None,
            metadata=dict(
                name="serviceTypeInfo",
                type="Element",
                required=True
            )
        )
        service_fee_ref_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeRefGrp"] = field(
            default_factory=list,
            metadata=dict(
                name="serviceFeeRefGrp",
                type="Element",
                min_occurs=0,
                max_occurs=100000
            )
        )
        service_coverage_info_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceCoverageInfoGrp"] = field(
            default_factory=list,
            metadata=dict(
                name="serviceCoverageInfoGrp",
                type="Element",
                min_occurs=0,
                max_occurs=100000
            )
        )
        global_message_marker: Optional[DummySegmentTypeI] = field(
            default=None,
            metadata=dict(
                name="globalMessageMarker",
                type="Element",
                required=True
            )
        )
        service_fee_info_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp"] = field(
            default_factory=list,
            metadata=dict(
                name="serviceFeeInfoGrp",
                type="Element",
                min_occurs=0,
                max_occurs=100000
            )
        )
        service_details_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceDetailsGrp"] = field(
            default_factory=list,
            metadata=dict(
                name="serviceDetailsGrp",
                type="Element",
                min_occurs=0,
                max_occurs=200
            )
        )
        free_bag_allowance_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.FreeBagAllowanceGrp"] = field(
            default_factory=list,
            metadata=dict(
                name="freeBagAllowanceGrp",
                type="Element",
                min_occurs=0,
                max_occurs=100000
            )
        )

        @dataclass
        class ServiceFeeRefGrp:
            """
            :ivar ref_info: Reference of service fee global information
            """
            ref_info: Optional[ReferenceInfoType] = field(
                default=None,
                metadata=dict(
                    name="refInfo",
                    type="Element",
                    required=True
                )
            )

        @dataclass
        class ServiceCoverageInfoGrp:
            """
            :ivar item_number_info: Item reference number for service coverage details
            :ivar service_cov_info_grp: Service coverage information group
            """
            item_number_info: Optional[ItemNumberType] = field(
                default=None,
                metadata=dict(
                    name="itemNumberInfo",
                    type="Element",
                    required=True
                )
            )
            service_cov_info_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceCoverageInfoGrp.ServiceCovInfoGrp"] = field(
                default_factory=list,
                metadata=dict(
                    name="serviceCovInfoGrp",
                    type="Element",
                    min_occurs=0,
                    max_occurs=200
                )
            )

            @dataclass
            class ServiceCovInfoGrp:
                """
                :ivar pax_ref_info: Passenger reference number
                :ivar coverage_per_flights_info: Service coverage information at flight level Matched seat characteristics
                :ivar carrier_info: Carrier information
                :ivar ref_info: Service reference number
                """
                pax_ref_info: Optional[SpecificTravellerType] = field(
                    default=None,
                    metadata=dict(
                        name="paxRefInfo",
                        type="Element",
                        required=True
                    )
                )
                coverage_per_flights_info: List[ActionDetailsType] = field(
                    default_factory=list,
                    metadata=dict(
                        name="coveragePerFlightsInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                carrier_info: Optional[TransportIdentifierType] = field(
                    default=None,
                    metadata=dict(
                        name="carrierInfo",
                        type="Element"
                    )
                )
                ref_info: Optional[ReferenceInfoType134840S] = field(
                    default=None,
                    metadata=dict(
                        name="refInfo",
                        type="Element"
                    )
                )

        @dataclass
        class ServiceFeeInfoGrp:
            """
            :ivar item_number_info: Item number details
            :ivar service_details_grp: Service fee informations
            """
            item_number_info: Optional[ItemNumberType] = field(
                default=None,
                metadata=dict(
                    name="itemNumberInfo",
                    type="Element",
                    required=True
                )
            )
            service_details_grp: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp.ServiceDetailsGrp"] = field(
                default_factory=list,
                metadata=dict(
                    name="serviceDetailsGrp",
                    type="Element",
                    min_occurs=0,
                    max_occurs=200
                )
            )

            @dataclass
            class ServiceDetailsGrp:
                """
                :ivar ref_info: Service reference number
                :ivar service_matched_info_group: Service matched information
                """
                ref_info: Optional[ReferenceInfoType134840S] = field(
                    default=None,
                    metadata=dict(
                        name="refInfo",
                        type="Element",
                        required=True
                    )
                )
                service_matched_info_group: List["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp.ServiceDetailsGrp.ServiceMatchedInfoGroup"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="serviceMatchedInfoGroup",
                        type="Element",
                        min_occurs=0,
                        max_occurs=99
                    )
                )

                @dataclass
                class ServiceMatchedInfoGroup:
                    """
                    :ivar pax_ref_info: Reference on pax number
                    :ivar pricing_info: Pricing oriented service matched information
                    :ivar amount_info: Informative Service amount
                    """
                    pax_ref_info: Optional[SpecificTravellerType] = field(
                        default=None,
                        metadata=dict(
                            name="paxRefInfo",
                            type="Element",
                            required=True
                        )
                    )
                    pricing_info: Optional[FareInformationType80868S] = field(
                        default=None,
                        metadata=dict(
                            name="pricingInfo",
                            type="Element"
                        )
                    )
                    amount_info: Optional[MonetaryInformationType193024S] = field(
                        default=None,
                        metadata=dict(
                            name="amountInfo",
                            type="Element"
                        )
                    )

        @dataclass
        class ServiceDetailsGrp:
            """
            :ivar service_option_info: Service sub-code and options (exclusion,inclusion, mode pushed,polled)
            :ivar fee_description_grp: Fee description
            """
            service_option_info: Optional[SpecificDataInformationType] = field(
                default=None,
                metadata=dict(
                    name="serviceOptionInfo",
                    type="Element",
                    required=True
                )
            )
            fee_description_grp: Optional["FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceDetailsGrp.FeeDescriptionGrp"] = field(
                default=None,
                metadata=dict(
                    name="feeDescriptionGrp",
                    type="Element"
                )
            )

            @dataclass
            class FeeDescriptionGrp:
                """
                :ivar item_number_info: Specification of the item number
                :ivar service_attributes_info: Attributes (SSR code EMD, RFIC, SSIM)
                :ivar service_description_info: Other service information (service description, ...)
                :ivar commercial_name: Commercial name
                """
                item_number_info: Optional[ItemNumberType80866S] = field(
                    default=None,
                    metadata=dict(
                        name="itemNumberInfo",
                        type="Element",
                        required=True
                    )
                )
                service_attributes_info: Optional[AttributeType] = field(
                    default=None,
                    metadata=dict(
                        name="serviceAttributesInfo",
                        type="Element"
                    )
                )
                service_description_info: Optional[SpecialRequirementsDetailsType] = field(
                    default=None,
                    metadata=dict(
                        name="serviceDescriptionInfo",
                        type="Element"
                    )
                )
                commercial_name: Optional[InteractiveFreeTextType] = field(
                    default=None,
                    metadata=dict(
                        name="commercialName",
                        type="Element"
                    )
                )

        @dataclass
        class FreeBagAllowanceGrp:
            """
            :ivar free_bag_allownce_info: Free baggage allownce information
            :ivar item_number_info: Item number information
            """
            free_bag_allownce_info: Optional[ExcessBaggageType] = field(
                default=None,
                metadata=dict(
                    name="freeBagAllownceInfo",
                    type="Element",
                    required=True
                )
            )
            item_number_info: Optional[ItemNumberType166130S] = field(
                default=None,
                metadata=dict(
                    name="itemNumberInfo",
                    type="Element"
                )
            )

    @dataclass
    class MnrGrp:
        """
        :ivar mnr:
        :ivar mnr_details:
        """
        mnr: Optional[MiniRulesType] = field(
            default=None,
            metadata=dict(
                name="mnr",
                type="Element",
                required=True
            )
        )
        mnr_details: List["FareMasterPricerTravelBoardSearchReply.MnrGrp.MnrDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="mnrDetails",
                type="Element",
                min_occurs=0,
                max_occurs=999
            )
        )

        @dataclass
        class MnrDetails:
            """
            :ivar mnr_ref:
            :ivar date_info:
            :ivar cat_grp: Categories
            """
            mnr_ref: Optional[ItemNumberType176648S] = field(
                default=None,
                metadata=dict(
                    name="mnrRef",
                    type="Element",
                    required=True
                )
            )
            date_info: List[DateAndTimeInformationType182345S] = field(
                default_factory=list,
                metadata=dict(
                    name="dateInfo",
                    type="Element",
                    min_occurs=0,
                    max_occurs=16
                )
            )
            cat_grp: List["FareMasterPricerTravelBoardSearchReply.MnrGrp.MnrDetails.CatGrp"] = field(
                default_factory=list,
                metadata=dict(
                    name="catGrp",
                    type="Element",
                    min_occurs=0,
                    max_occurs=5
                )
            )

            @dataclass
            class CatGrp:
                """
                :ivar cat_info: Category information
                :ivar mon_info: Monetary information
                :ivar status_info: Status information
                """
                cat_info: Optional[CategDescrType] = field(
                    default=None,
                    metadata=dict(
                        name="catInfo",
                        type="Element",
                        required=True
                    )
                )
                mon_info: Optional[MonetaryInformationType174241S] = field(
                    default=None,
                    metadata=dict(
                        name="monInfo",
                        type="Element"
                    )
                )
                status_info: Optional[StatusType182386S] = field(
                    default=None,
                    metadata=dict(
                        name="statusInfo",
                        type="Element"
                    )
                )
