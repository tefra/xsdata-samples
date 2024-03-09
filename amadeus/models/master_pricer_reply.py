from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://xml.amadeus.com/FMPTBR_15_3_1A"


@dataclass
class AdditionalFareQualifierDetailsTypeI:
    """
    To specify the fare basis and ticket designator codes.

    :ivar rate_class: Rate class
    :ivar ticket_designator: Ticket designator.
    :ivar pricing_group: Pricing group
    :ivar second_rate_class: Second rate class
    """

    rate_class: None | str = field(
        default=None,
        metadata={
            "name": "rateClass",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "ticketDesignator",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 18,
        },
    )
    pricing_group: None | str = field(
        default=None,
        metadata={
            "name": "pricingGroup",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    second_rate_class: list[str] = field(
        default_factory=list,
        metadata={
            "name": "secondRateClass",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 29,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class AdditionalProductDetailsType:
    """
    :ivar equipment_type: Type of aircraft
    :ivar operating_day: Day number of the week
    :ivar tech_stop_number: Number of stops made in a journey if
        different from 0
    :ivar location_id: Location places of the stops
    """

    equipment_type: None | str = field(
        default=None,
        metadata={
            "name": "equipmentType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    operating_day: None | str = field(
        default=None,
        metadata={
            "name": "operatingDay",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 7,
        },
    )
    tech_stop_number: None | str = field(
        default=None,
        metadata={
            "name": "techStopNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,2}",
        },
    )
    location_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "locationId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 3,
            "min_length": 3,
            "max_length": 5,
        },
    )


@dataclass
class ApplicationErrorInformationType:
    """
    :ivar error: The code assigned by the receiver of a message for
        identification of a data validation error condition.
    """

    error: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class AttributeInformationType:
    """
    To identify the type of attribute and the attribute.

    :ivar fee_parameter_type: Type of parameter.
    :ivar fee_parameter_description: Reference to company Id.
    """

    fee_parameter_type: None | str = field(
        default=None,
        metadata={
            "name": "feeParameterType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 3,
            "max_length": 3,
        },
    )
    fee_parameter_description: None | str = field(
        default=None,
        metadata={
            "name": "feeParameterDescription",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 15,
        },
    )


@dataclass
class AttributeInformationTypeU:
    """
    To identify the type of attribute and the attribute.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """

    attribute_type: None | str = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    attribute_description: None | str = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class AttributeInformationType97181C:
    """
    To identify the type of attribute and the attribute.

    :ivar attribute_type: Attribute type
    :ivar attribute_description: Attribute description
    """

    class Meta:
        name = "AttributeInformationType_97181C"

    attribute_type: None | str = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    attribute_description: None | str = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 256,
        },
    )


@dataclass
class BaggageDetailsType:
    """
    To specify the number and weight of baggage.

    :ivar free_allowance: Number of pieces or weight
    :ivar quantity_code: Nature of the free allowance ( Number of pieces
        or weight)
    :ivar unit_qualifier: Unit qualifier
    """

    free_allowance: None | str = field(
        default=None,
        metadata={
            "name": "freeAllowance",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )
    quantity_code: None | str = field(
        default=None,
        metadata={
            "name": "quantityCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
    )
    unit_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "unitQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class BagtagDetailsType:
    """
    To identify baggage by company identification, serial numbers, and destination.

    :ivar identifier: Identifier
    :ivar number: Number
    """

    identifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )


@dataclass
class BucketInformationType:
    """
    :ivar number: Number
    :ivar name: Name
    """

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 20,
        },
    )


@dataclass
class CabinInformationType:
    """
    :ivar service: Identify the features associated to the cabin/class
    :ivar cabin: Cabin code designator
    """

    service: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    cabin: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 1,
        },
    )


@dataclass
class CabinProductDetailsType:
    """
    :ivar rbd: Reservation booking designator - RBD
    :ivar booking_modifier: Reservation Booking Modifier
    :ivar cabin: Indicates the cabin related to the Booking code
    :ivar avl_status: Availibility status : posting level
    """

    rbd: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 1,
        },
    )
    booking_modifier: None | str = field(
        default=None,
        metadata={
            "name": "bookingModifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 1,
        },
    )
    cabin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    avl_status: None | str = field(
        default=None,
        metadata={
            "name": "avlStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
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

    rbd: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    booking_modifier: None | str = field(
        default=None,
        metadata={
            "name": "bookingModifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 1,
        },
    )
    cabin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    avl_status: None | str = field(
        default=None,
        metadata={
            "name": "avlStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 0,
            "max_length": 3,
        },
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

    rbd: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 1,
        },
    )
    booking_modifier: None | str = field(
        default=None,
        metadata={
            "name": "bookingModifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]",
        },
    )
    cabin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    avl_status: None | str = field(
        default=None,
        metadata={
            "name": "avlStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
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

    rbd: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 1,
        },
    )
    cabin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    avl_status: None | str = field(
        default=None,
        metadata={
            "name": "avlStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
    )


@dataclass
class CategoryDescriptionType:
    """
    :ivar number: Category number from ATPCO naming conventions (C05 for
        Advance Purchase restrictions, C06 for Minimun stay ...)
    :ivar code: Category Code (ATPCO component code, e.g ADV for Advance
        purchase, STP for stopover restrictions, ELG for eligibility
        restrictions...)
    """

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{1,3}",
        },
    )
    code: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ClassInformationType:
    """
    :ivar service: Identify the features associated to the cabin/class
    :ivar rbd: Class designator
    """

    service: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    rbd: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 26,
            "min_length": 1,
            "max_length": 1,
        },
    )


@dataclass
class CodedAttributeInformationType:
    """
    Convey coded key and corresponding value.

    :ivar attribute_type: Type of fee/reduction
    :ivar attribute_description: Fee Id Number
    """

    attribute_type: None | str = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    attribute_description: None | str = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class CodedAttributeInformationType270108C:
    """
    Convey coded key and corresponding value.

    :ivar attribute_type:
    :ivar attribute_description: Attribute description
    """

    class Meta:
        name = "CodedAttributeInformationType_270108C"

    attribute_type: None | str = field(
        default=None,
        metadata={
            "name": "attributeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 5,
        },
    )
    attribute_description: None | str = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 10,
        },
    )


@dataclass
class CompanyIdentificationTextType:
    """
    Compagny identification text.

    :ivar text_ref_number: Company Id Text reference.
    :ivar company_text: Company id free text.
    """

    text_ref_number: None | str = field(
        default=None,
        metadata={
            "name": "textRefNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{0,4}",
        },
    )
    company_text: None | str = field(
        default=None,
        metadata={
            "name": "companyText",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 70,
        },
    )


@dataclass
class CompanyIdentificationType:
    """
    :ivar marketing_carrier: Marketing carrier
    :ivar operating_carrier: Operating carrier
    :ivar alliance: airline alliance code
    """

    marketing_carrier: None | str = field(
        default=None,
        metadata={
            "name": "marketingCarrier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 2,
            "max_length": 3,
        },
    )
    operating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "operatingCarrier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )
    alliance: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 2,
        },
    )


@dataclass
class CompanyIdentificationTypeI:
    """
    Code or name to identify a company and any associated companies.

    :ivar marketing_company: Company
    :ivar operating_company: Company
    :ivar other_company: Company
    """

    marketing_company: None | str = field(
        default=None,
        metadata={
            "name": "marketingCompany",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )
    operating_company: None | str = field(
        default=None,
        metadata={
            "name": "operatingCompany",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )
    other_company: None | str = field(
        default=None,
        metadata={
            "name": "otherCompany",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )


@dataclass
class CompanyRoleIdentificationType:
    """
    To indicate commercial agreements related to the service being provided.

    :ivar code_share_type: Type of code share agreement.
    :ivar airline_designator: company identification
    :ivar flight_number: flight number
    """

    code_share_type: None | str = field(
        default=None,
        metadata={
            "name": "codeShareType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    airline_designator: None | str = field(
        default=None,
        metadata={
            "name": "airlineDesignator",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "flightNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,4}",
        },
    )


@dataclass
class CompanyRoleIdentificationType120771C:
    """
    To indicate commercial agreements related to the service being provided.

    :ivar transport_stage_qualifier: Type of code share agreement.
    :ivar company: company identification
    """

    class Meta:
        name = "CompanyRoleIdentificationType_120771C"

    transport_stage_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "transportStageQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    company: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )


@dataclass
class ConversionRateDetailsTypeI:
    """
    :ivar conversion_type: Conversion type
    :ivar currency: Currency
    :ivar amount: amount
    """

    conversion_type: None | str = field(
        default=None,
        metadata={
            "name": "conversionType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 12,
        },
    )


@dataclass
class ConversionRateDetailsTypeI179848C:
    """
    :ivar conversion_type: Conversion type
    :ivar currency: Currency
    :ivar rate: Conversion rate for pricing
    :ivar converted_amount_link: Converted value amount
    :ivar tax_qualifier: Applicable ISO country code or Tax designator
        code.
    """

    class Meta:
        name = "ConversionRateDetailsTypeI_179848C"

    conversion_type: None | str = field(
        default=None,
        metadata={
            "name": "conversionType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    rate: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 18,
        },
    )
    converted_amount_link: None | str = field(
        default=None,
        metadata={
            "name": "convertedAmountLink",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 18,
        },
    )
    tax_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "taxQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
    )


@dataclass
class CriteriaDetailsType:
    """Criteria details : weights/parameters list"""

    class Meta:
        name = "CriteriaiDetaislType"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 18,
        },
    )


@dataclass
class DataInformationType:
    """
    To identify specific data and a quantity related to the data.

    :ivar indicator: Ancillary services options
    """

    indicator: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class DataTypeInformationType:
    """
    To identify the type of data to be sent and to qualify the data when required.

    :ivar sub_type: service group/sub-group/sub-code information
    :ivar option: Status (automated, manually added, exempted). Default
        is automated
    """

    sub_type: None | str = field(
        default=None,
        metadata={
            "name": "subType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    option: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
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

    date_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "dateQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    date: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}",
        },
    )
    first_time: None | str = field(
        default=None,
        metadata={
            "name": "firstTime",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    equipement_type: None | str = field(
        default=None,
        metadata={
            "name": "equipementType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    location_id: None | str = field(
        default=None,
        metadata={
            "name": "locationId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 3,
            "max_length": 5,
        },
    )


@dataclass
class DateAndTimeDetailsType256192C:
    """
    To provide date and time details relative to flight movements.

    :ivar qualifier:
    :ivar date:
    :ivar time: Time
    :ivar location: Location
    """

    class Meta:
        name = "DateAndTimeDetailsType_256192C"

    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    date: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    time: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class DateTimePeriodDetailsTypeI:
    """
    To indicate period of applicability.

    :ivar qualifier: Qualifier
    :ivar value: Value
    """

    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class DiscountPenaltyInformationType:
    """
    To indicate the discounts and penalties by fare type.

    :ivar fare_qualifier: Discounted fare,...
    :ivar rate_category: Dicount code,...
    :ivar amount: Amount
    :ivar percentage: Percentage
    """

    fare_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "fareQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    rate_category: None | str = field(
        default=None,
        metadata={
            "name": "rateCategory",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    percentage: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class DiscountPenaltyMonetaryInformationType:
    """
    To specify the type of discount and penalty information, the monetary amount,
    and associated information.

    :ivar fee_type: Type of discount/penalty
    :ivar fee_amount_type: The amount Type can be a percentage or an
        amount
    :ivar fee_amount: specify the value
    :ivar fee_currency: Fee currency code.
    """

    fee_type: None | str = field(
        default=None,
        metadata={
            "name": "feeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fee_amount_type: None | str = field(
        default=None,
        metadata={
            "name": "feeAmountType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fee_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "feeAmount",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    fee_currency: None | str = field(
        default=None,
        metadata={
            "name": "feeCurrency",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class DummySegmentTypeI:
    """
    To serve the purpose of a mandatory segment at the beginning of a group and to
    avoid segment collision.
    """


@dataclass
class FareCalculationCodeDetailsType:
    """
    To specify fare calculation information.

    :ivar qualifier: Qualifier of the amout or rate
    :ivar amount: Amount
    :ivar location_code: Location code
    :ivar other_location_code: Other location code
    :ivar rate: Rate
    """

    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    location_code: None | str = field(
        default=None,
        metadata={
            "name": "locationCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    other_location_code: None | str = field(
        default=None,
        metadata={
            "name": "otherLocationCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    rate: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FareCategoryCodesTypeI:
    """
    To designate non-system specific combinations of fare types.

    :ivar fare_type: Fare type
    :ivar other_fare_type: Other fare type
    """

    fare_type: None | str = field(
        default=None,
        metadata={
            "name": "fareType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 20,
        },
    )
    other_fare_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "otherFareType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 8,
            "min_length": 1,
            "max_length": 20,
        },
    )


@dataclass
class FareDetailsType:
    """
    To specify the fare type and related information.

    :ivar passenger_type_qualifier: Passenger Type qualifier
    """

    passenger_type_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "passengerTypeQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class FareDetailsTypeI:
    """
    To specify the fare type and related information.

    :ivar qualifier: Qualifier
    :ivar rate: Rate
    :ivar country: Country
    :ivar fare_category: Fare category
    """

    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    rate: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fare_category: None | str = field(
        default=None,
        metadata={
            "name": "fareCategory",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
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

    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
    )
    rate: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,8}",
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fare_category: None | str = field(
        default=None,
        metadata={
            "name": "fareCategory",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
    )


@dataclass
class FareFamilyDetailsType:
    """
    NEW FARE SEARCH.

    :ivar commercial_family: Commercial fare Family Short name
    """

    commercial_family: None | str = field(
        default=None,
        metadata={
            "name": "commercialFamily",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )


@dataclass
class FareInformationTypeI:
    """
    To specify fare details.

    :ivar value_qualifier: Value qualifier
    :ivar value: Value
    """

    value_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "valueQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )


@dataclass
class FareProductDetailsType:
    """
    :ivar fare_basis: Fare basis code
    """

    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "fareBasis",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 18,
        },
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

    fare_basis: None | str = field(
        default=None,
        metadata={
            "name": "fareBasis",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 18,
        },
    )
    passenger_type: None | str = field(
        default=None,
        metadata={
            "name": "passengerType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    fare_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "fareType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 0,
            "max_length": 3,
        },
    )


@dataclass
class FareTypeGroupingInformationType:
    """
    :ivar pricing_group: Pricing Group
    """

    pricing_group: None | str = field(
        default=None,
        metadata={
            "name": "pricingGroup",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FreeTextQualificationType:
    """
    :ivar text_subject_qualifier: Type of message
    :ivar information_type: Coded Text or type of information in 4440
        (e.g. type of OSI or free text, canned message value)
    """

    text_subject_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "textSubjectQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    information_type: None | str = field(
        default=None,
        metadata={
            "name": "informationType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 4,
        },
    )


@dataclass
class FreeTextQualificationTypeI:
    """
    To specify the type, purpose, and language of free text and whether any action
    is required.

    :ivar text_subject_qualifier: Text subject qualifier
    """

    text_subject_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "textSubjectQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class FreeTextQualificationType120769C:
    """
    :ivar text_subject_qualifier: Type of message
    :ivar information_type: Coded Text or type of information in 4440
        (e.g. type of OSI or free text, canned message value)
    :ivar language: ISO code for language of free text (default is
        English)
    """

    class Meta:
        name = "FreeTextQualificationType_120769C"

    text_subject_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "textSubjectQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    information_type: None | str = field(
        default=None,
        metadata={
            "name": "informationType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 4,
        },
    )
    language: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class FrequentTravellerIdentificationType:
    """
    :ivar carrier: Carrier where the FQTV is registered.
    :ivar number: Number
    :ivar tier_level: To specify a Tier linked to the FQTV
    :ivar priority_code: For example : priority code
    """

    carrier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 28,
        },
    )
    tier_level: None | str = field(
        default=None,
        metadata={
            "name": "tierLevel",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    priority_code: None | str = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 12,
        },
    )


@dataclass
class ItemNumberIdentificationType:
    """
    Goods identification for a specified source.

    :ivar number: Ancillary Service number
    :ivar type_value: Type
    :ivar qualifier: Qualifier
    :ivar responsible_agency: Responsible agency
    """

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 4,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    responsible_agency: None | str = field(
        default=None,
        metadata={
            "name": "responsibleAgency",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ItemNumberIdentificationType191597C:
    """
    :ivar number: Item number.
    :ivar number_type: Indicates the item type .
    """

    class Meta:
        name = "ItemNumberIdentificationType_191597C"

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    number_type: None | str = field(
        default=None,
        metadata={
            "name": "numberType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
    )


@dataclass
class ItemNumberIdentificationType192331C:
    """
    Goods identification for a specified source.

    :ivar number: Service coverage number
    :ivar type_value: Type
    :ivar qualifier: Qualifier
    :ivar responsible_agency: Responsible agency
    """

    class Meta:
        name = "ItemNumberIdentificationType_192331C"

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    qualifier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    responsible_agency: None | str = field(
        default=None,
        metadata={
            "name": "responsibleAgency",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ItemNumberIdentificationType234878C:
    """
    Goods identification for a specified source.

    :ivar number: Number
    :ivar type_value: Type
    """

    class Meta:
        name = "ItemNumberIdentificationType_234878C"

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,6}",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ItemNumberIdentificationType248537C:
    """
    Goods identification for a specified source.
    """

    class Meta:
        name = "ItemNumberIdentificationType_248537C"

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class ItemReferencesAndVersionsType:
    """
    Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar ref_number: Unique fee reference.
    """

    reference_type: None | str = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )


@dataclass
class ItemReferencesAndVersionsType78536S:
    """
    Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar ref_number: Unique fee reference.
    """

    class Meta:
        name = "ItemReferencesAndVersionsType_78536S"

    reference_type: None | str = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )


@dataclass
class ItemReferencesAndVersionsType78564S:
    """
    Exchange and link unique identifiers.

    :ivar reference_type: Qualifies the type of the reference used.
    :ivar fee_ref_number: Unique fee reference.
    """

    class Meta:
        name = "ItemReferencesAndVersionsType_78564S"

    reference_type: None | str = field(
        default=None,
        metadata={
            "name": "referenceType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fee_ref_number: None | str = field(
        default=None,
        metadata={
            "name": "feeRefNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )


@dataclass
class ItineraryDetailsType:
    """
    Forces arrival or departure to/from the same city or airport option.

    :ivar airport_city_qualifier: Airport/City Qualifier: the passenger
        wants to depart/arrive from/to the same airport or city in the
        specified requested segment
    :ivar segment_number: Requested segment number
    """

    airport_city_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "airportCityQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 1,
        },
    )
    segment_number: None | str = field(
        default=None,
        metadata={
            "name": "segmentNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{1,3}",
        },
    )


@dataclass
class LocationIdentificationDetailsType:
    """
    :ivar location_id: 3 characters ATA/IATA airport/city code
    :ivar airport_city_qualifier: Airport/city qualifier: the requested
        point is an airport when ambiguity exists (e.g. HOU)
    :ivar terminal: Terminal information
    """

    location_id: None | str = field(
        default=None,
        metadata={
            "name": "locationId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 3,
            "max_length": 5,
        },
    )
    airport_city_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "airportCityQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    terminal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 5,
        },
    )


@dataclass
class MiniRulesDetailsType:
    """
    :ivar interpretation: Coded text (period or day)
    :ivar value: Data type coded or value of interpretation
    """

    interpretation: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 9,
        },
    )
    value: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 10,
            "min_length": 0,
            "max_length": 5,
        },
    )


@dataclass
class MiniRulesIndicatorType:
    """
    :ivar rule_indicator: See rule indicator and free form text
        indicator
    """

    rule_indicator: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ruleIndicator",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 1,
        },
    )


@dataclass
class MiniRulesType:
    """
    To specify the restrictions.

    :ivar category: Categoty of restriction: PTC, Max Adv Pur, Days, ...
    """

    category: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class MonetaryInformationDetailsType:
    """
    :ivar amount_type: To specify amount and percentage.
    :ivar amount: Amount
    :ivar currency: ISO currency code
    """

    amount_type: None | str = field(
        default=None,
        metadata={
            "name": "amountType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class MonetaryInformationDetailsTypeI:
    """
    To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier: type Qualifier
    :ivar amount: Amount
    :ivar currency: Currency
    """

    type_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "typeQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 6,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class MonetaryInformationDetailsType245528C:
    """
    To specify the type of monetary amount, the amount, and the currency code.

    :ivar type_qualifier:
    :ivar amount: Amount
    :ivar currency: Currency
    :ivar location: location
    """

    class Meta:
        name = "MonetaryInformationDetailsType_245528C"

    type_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "typeQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    amount: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 25,
        },
    )


@dataclass
class OnTimePerformanceType:
    """
    :ivar date_time_period: Date time period
    :ivar percentage: Percentage
    :ivar accuracy: Accuracy
    """

    date_time_period: None | str = field(
        default=None,
        metadata={
            "name": "dateTimePeriod",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    percentage: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    accuracy: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class OriginAndDestinationRequestType134833S:
    """
    To convey information regarding Requested Segments.

    :ivar seg_ref: Requested segment number
    """

    class Meta:
        name = "OriginAndDestinationRequestType_134833S"

    seg_ref: None | str = field(
        default=None,
        metadata={
            "name": "segRef",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{1,2}",
        },
    )


@dataclass
class OriginatorIdentificationDetailsTypeI:
    """
    To identify a user.

    :ivar office_name: Office Name.
    :ivar agent_signin: Agent Sign In .
    :ivar confidential_office: Confidential Office Name.
    :ivar other_office: Other Office Name
    """

    office_name: None | str = field(
        default=None,
        metadata={
            "name": "officeName",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,9}",
        },
    )
    agent_signin: None | str = field(
        default=None,
        metadata={
            "name": "agentSignin",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 9,
        },
    )
    confidential_office: None | str = field(
        default=None,
        metadata={
            "name": "confidentialOffice",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 9,
        },
    )
    other_office: None | str = field(
        default=None,
        metadata={
            "name": "otherOffice",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 9,
        },
    )


@dataclass
class PricingTicketingInformationType:
    """
    To specify indicators related to pricing and ticketing.

    :ivar price_type: Price type qualifier
    """

    price_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "priceType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 20,
            "min_length": 0,
            "max_length": 3,
        },
    )


@dataclass
class PricingTicketingSubsequentType:
    """
    To convey additional information related to a ticket.

    :ivar pax_fare_num: Passenger fare product number
    """

    pax_fare_num: list[str] = field(
        default_factory=list,
        metadata={
            "name": "paxFareNum",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 10,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ProcessingInformationType:
    """
    To identify the action to be taken and the selection criteria.

    :ivar action_qualifier: Action qualifier
    :ivar reference_qualifier: Reference qualifier
    :ivar ref_num: Reference number
    """

    action_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "actionQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    reference_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "referenceQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    ref_num: None | str = field(
        default=None,
        metadata={
            "name": "refNum",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )


@dataclass
class ProductDateTimeType:
    """
    :ivar date_of_departure: Departure date
    :ivar time_of_departure: Departure time
    :ivar date_of_arrival: Arrival date
    :ivar time_of_arrival: Arrival time
    :ivar date_variation: Arrival date compared to departure date, only
        if different from 0
    """

    date_of_departure: None | str = field(
        default=None,
        metadata={
            "name": "dateOfDeparture",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}",
        },
    )
    time_of_departure: None | str = field(
        default=None,
        metadata={
            "name": "timeOfDeparture",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    date_of_arrival: None | str = field(
        default=None,
        metadata={
            "name": "dateOfArrival",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"(0[1-9]|[1-2][0-9]|3[0-1])(0[1-9]|1[0-2])[0-9]{2}",
        },
    )
    time_of_arrival: None | str = field(
        default=None,
        metadata={
            "name": "timeOfArrival",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
        },
    )
    date_variation: None | str = field(
        default=None,
        metadata={
            "name": "dateVariation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,1}",
        },
    )


@dataclass
class ProductDetailsType:
    """
    To specify availability and additional services for a product class.
    """

    designator: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 17,
        },
    )
    availability_status: None | str = field(
        default=None,
        metadata={
            "name": "availabilityStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    special_service: None | str = field(
        default=None,
        metadata={
            "name": "specialService",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    option: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 7,
        },
    )


@dataclass
class ProductFacilitiesType:
    """
    Level of access.

    :ivar last_seat_available: Yes-No indicator whether Last Seat
        Available
    :ivar level_of_access: Level of access
    :ivar electronic_ticketing: Yes-No indicator whether electronic
        ticketing
    :ivar operational_suffix: Product identification suffix
    :ivar product_detail_qualifier: Define whether a flight has been
        polled or not
    :ivar flight_characteristic: Add some flight restrictions (See code
        set list)
    """

    last_seat_available: None | str = field(
        default=None,
        metadata={
            "name": "lastSeatAvailable",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    level_of_access: None | str = field(
        default=None,
        metadata={
            "name": "levelOfAccess",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    electronic_ticketing: None | str = field(
        default=None,
        metadata={
            "name": "electronicTicketing",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    operational_suffix: None | str = field(
        default=None,
        metadata={
            "name": "operationalSuffix",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    product_detail_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "productDetailQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    flight_characteristic: list[str] = field(
        default_factory=list,
        metadata={
            "name": "flightCharacteristic",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ProductTypeDetailsType:
    """
    To specify additional characteristics of a product or service.

    :ivar availability_cnx_type: Availability connection type.
    """

    availability_cnx_type: list[str] = field(
        default_factory=list,
        metadata={
            "name": "availabilityCnxType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ProductTypeDetailsType205137C:
    """
    To specify additional characteristics of a product or service.

    :ivar avl: indicates whether the flight is domestic or international
    """

    class Meta:
        name = "ProductTypeDetailsType_205137C"

    avl: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 6,
        },
    )


@dataclass
class ProposedSegmentDetailsType:
    """
    :ivar ref: Flight proposal reference
    :ivar unit_qualifier: Elapse Flying Time
    """

    ref: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    unit_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "unitQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class ReferenceType:
    """
    To specify which number in a sequence of references and/or the reference
    number.

    :ivar ref_of_leg: Reference  of leg
    :ivar first_item_identifier: Reference of segment starting range
    :ivar last_item_identifier: Reference of segment ending range
    """

    ref_of_leg: None | str = field(
        default=None,
        metadata={
            "name": "refOfLeg",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 6,
        },
    )
    first_item_identifier: None | str = field(
        default=None,
        metadata={
            "name": "firstItemIdentifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )
    last_item_identifier: None | str = field(
        default=None,
        metadata={
            "name": "lastItemIdentifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )


@dataclass
class ReferencingDetailsType:
    """
    :ivar ref_qualifier: Reference qualifier
    :ivar ref_number: Requested segment reference
    """

    ref_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "refQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
    )
    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{0,3}",
        },
    )


@dataclass
class ReferencingDetailsType191583C:
    """
    Referencing details.

    :ivar ref_qualifier: Service reference qualifier
    :ivar ref_number: Service reference
    """

    class Meta:
        name = "ReferencingDetailsType_191583C"

    ref_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "refQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{0,6}",
        },
    )


@dataclass
class ReferencingDetailsType195561C:
    """
    Referencing details.

    :ivar ref_qualifier: Segment reference qualifier
    :ivar ref_number: Flight or flight group reference
    """

    class Meta:
        name = "ReferencingDetailsType_195561C"

    ref_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "refQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{0,3}",
        },
    )


@dataclass
class ReferencingDetailsType234704C:
    """
    To provide reference identification.

    :ivar type_value: Type
    :ivar value: Value
    """

    class Meta:
        name = "ReferencingDetailsType_234704C"

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 10,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 60,
        },
    )


@dataclass
class SegmentRepetitionControlDetailsTypeI:
    """
    Information about the number of selection segments to be processed.

    :ivar quantity: traveller number
    :ivar number_of_units: range of traveller
    """

    quantity: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )
    number_of_units: None | str = field(
        default=None,
        metadata={
            "name": "numberOfUnits",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )


@dataclass
class SelectionDetailsInformationType:
    """
    To specify a selected option and associated information.

    :ivar type_value: Carrier fee type
    :ivar option_information: Carrier fee status
    """

    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    option_information: None | str = field(
        default=None,
        metadata={
            "name": "optionInformation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class SequenceInformationTypeU:
    """
    Identification of a sequence and source for sequencing.

    :ivar number: Number
    :ivar identification_code: Identification code
    """

    number: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 10,
        },
    )
    identification_code: None | str = field(
        default=None,
        metadata={
            "name": "identificationCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 17,
        },
    )


@dataclass
class ServicesReferences:
    """
    :ivar reference: Reference of the service
    :ivar status: Status of the service
    :ivar from_price: Service lowest price
    """

    reference: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 4,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    from_price: None | str = field(
        default=None,
        metadata={
            "name": "fromPrice",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 18,
        },
    )


@dataclass
class SpecialRequirementsDataDetailsType:
    """
    Special requirements data details.

    :ivar seat_characteristics: SSR seat characteristic
    """

    seat_characteristics: list[str] = field(
        default_factory=list,
        metadata={
            "name": "seatCharacteristics",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 5,
            "min_length": 1,
            "max_length": 2,
        },
    )


@dataclass
class SpecialRequirementsTypeDetailsType:
    """
    :ivar service_classification: To specify the Service Classification
        of the Service Requirement.
    :ivar service_status: Status
    :ivar service_number_of_instances: To specify the number of items
        involved
    :ivar service_marketing_carrier: To specify to which marketing
        carrier the service applies
    :ivar service_group: Specify the Service group
    :ivar service_sub_group: Specify the Service Sub-Group
    :ivar service_free_text: Free Text attached to the Service.
    """

    service_classification: None | str = field(
        default=None,
        metadata={
            "name": "serviceClassification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 4,
        },
    )
    service_status: None | str = field(
        default=None,
        metadata={
            "name": "serviceStatus",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    service_number_of_instances: None | str = field(
        default=None,
        metadata={
            "name": "serviceNumberOfInstances",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )
    service_marketing_carrier: None | str = field(
        default=None,
        metadata={
            "name": "serviceMarketingCarrier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    service_group: None | str = field(
        default=None,
        metadata={
            "name": "serviceGroup",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    service_sub_group: None | str = field(
        default=None,
        metadata={
            "name": "serviceSubGroup",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    service_free_text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "serviceFreeText",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class SpecificTravellerDetailsType:
    """
    To specify additional details about a particular traveller.

    :ivar reference_number: Reference number
    """

    reference_number: None | str = field(
        default=None,
        metadata={
            "name": "referenceNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 10,
        },
    )


@dataclass
class StatusDetailsType:
    """
    :ivar advisory_type_info: Advisory type information, Fare Server
    :ivar notification: CPU time, user type
    :ivar notification2: CPU time,user type
    :ivar description: Capture and trace information
    """

    advisory_type_info: None | str = field(
        default=None,
        metadata={
            "name": "advisoryTypeInfo",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    notification: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    notification2: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class StatusDetailsType256255C:
    """
    To specify a status, the action to be taken, and an additional qualification of
    the status.

    :ivar indicator: list of status/qualifiers Either His for Historical
        or     Crt for Current
    :ivar action:
    """

    class Meta:
        name = "StatusDetailsType_256255C"

    indicator: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    action: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class TaxDetailsType:
    """
    To specify a rate, type of tax, and currency code.

    :ivar rate: Amount
    :ivar country_code: Country code
    :ivar currency_code: Currency code
    :ivar type_value: Type
    :ivar indicator: Indicator
    """

    rate: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 12,
        },
    )
    country_code: None | str = field(
        default=None,
        metadata={
            "name": "countryCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    currency_code: None | str = field(
        default=None,
        metadata={
            "name": "currencyCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    indicator: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 98,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class TravellerDetailsType:
    """
    :ivar ref: Direct reference of passenger assigned by requesting
        system.
    :ivar infant_indicator: Traveller is an infant
    """

    ref: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,3}",
        },
    )
    infant_indicator: None | str = field(
        default=None,
        metadata={
            "name": "infantIndicator",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,1}",
        },
    )


@dataclass
class ActionDetailsType:
    """
    To specify the action that should be taken on a selected reference number.

    :ivar number_of_items_details: Number of items details
    :ivar last_items_details: Range of segments
    """

    number_of_items_details: None | ProcessingInformationType = field(
        default=None,
        metadata={
            "name": "numberOfItemsDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    last_items_details: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "name": "lastItemsDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class ApplicationErrorInformationType78543S:
    """
    To identify the type of application error within a message.

    :ivar application_error_detail: Details on application error.
    """

    class Meta:
        name = "ApplicationErrorInformationType_78543S"

    application_error_detail: None | ApplicationErrorInformationType = field(
        default=None,
        metadata={
            "name": "applicationErrorDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )


@dataclass
class AttributeType:
    """
    Used to have tag value without code list for tag.

    :ivar attribute_qualifier: Criteria Set Type
    :ivar attribute_details: Criteria details
    """

    attribute_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "attributeQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    attribute_details: list[AttributeInformationType97181C] = field(
        default_factory=list,
        metadata={
            "name": "attributeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass
class AttributeTypeU:
    """
    :ivar attribute_function: provides the function of the attribute
    :ivar attribute_details: provides details for the Attribute
    """

    attribute_function: None | str = field(
        default=None,
        metadata={
            "name": "attributeFunction",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    attribute_details: None | AttributeInformationTypeU = field(
        default=None,
        metadata={
            "name": "attributeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )


@dataclass
class AttributeType78561S:
    """
    Used to have tag value without code list for tag.

    :ivar fee_parameter: Fee/reduction parameters.
    """

    class Meta:
        name = "AttributeType_78561S"

    fee_parameter: list[AttributeInformationType] = field(
        default_factory=list,
        metadata={
            "name": "feeParameter",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )


@dataclass
class CategDescrType:
    """
    To identify an ATPCO Fare Category.

    :ivar description_info: Category description information
    :ivar process_indicator: Category processing indicator
    """

    description_info: None | CategoryDescriptionType = field(
        default=None,
        metadata={
            "name": "descriptionInfo",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    process_indicator: None | str = field(
        default=None,
        metadata={
            "name": "processIndicator",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class CodedAttributeType:
    """
    Used to have tag value without code list for tag.

    :ivar attribute_details: Fee/reduction Id
    """

    attribute_details: list[CodedAttributeInformationType] = field(
        default_factory=list,
        metadata={
            "name": "attributeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )


@dataclass
class CommercialAgreementsType:
    """
    To specify commercial agreements between two  or more companies related to
    joint, shared, lease operations etc.

    :ivar codeshare_details: Codeshare Details
    :ivar other_codeshare_details: Other codeshare details
    """

    codeshare_details: None | CompanyRoleIdentificationType = field(
        default=None,
        metadata={
            "name": "codeshareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    other_codeshare_details: list[CompanyRoleIdentificationType] = field(
        default_factory=list,
        metadata={
            "name": "otherCodeshareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
        },
    )


@dataclass
class ConversionRateTypeI:
    """
    To specify conversion rate details.

    :ivar conversion_rate_detail: Detail of conversion rate of First
        Monetary Unit.
    """

    conversion_rate_detail: list[ConversionRateDetailsTypeI179848C] = field(
        default_factory=list,
        metadata={
            "name": "conversionRateDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )


@dataclass
class ConversionRateTypeI78562S:
    """
    To specify conversion rate details.

    :ivar conversion_rate_detail: Details of conversion
    """

    class Meta:
        name = "ConversionRateTypeI_78562S"

    conversion_rate_detail: list[ConversionRateDetailsTypeI] = field(
        default_factory=list,
        metadata={
            "name": "conversionRateDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )


@dataclass
class DateAndTimeInformationType:
    """
    Not the standard only used in fare quote message.

    :ivar stop_details: Details on date and time
    """

    stop_details: list[DateAndTimeDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "stopDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class DateAndTimeInformationType182345S:
    """
    To convey information regarding estimated or actual dates and times of
    operational events.

    :ivar date_and_time_details: DATE AND TIME DETAILS
    """

    class Meta:
        name = "DateAndTimeInformationType_182345S"

    date_and_time_details: list[DateAndTimeDetailsType256192C] = field(
        default_factory=list,
        metadata={
            "name": "dateAndTimeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 400,
        },
    )


@dataclass
class DiscountAndPenaltyInformationType:
    """
    To specify information about discounts and penalties.

    :ivar fee_identification: Used to specify airline collected fee or
        agent collected fee.
    :ivar fee_information: Used to specify penalty information
    """

    fee_identification: None | str = field(
        default=None,
        metadata={
            "name": "feeIdentification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fee_information: None | DiscountPenaltyMonetaryInformationType = field(
        default=None,
        metadata={
            "name": "feeInformation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class ExcessBaggageType:
    """
    :ivar baggage_details: Baggage details
    :ivar bag_tag_details: Free baggage allowance details
    """

    baggage_details: None | BaggageDetailsType = field(
        default=None,
        metadata={
            "name": "baggageDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    bag_tag_details: list[BagtagDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "bagTagDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class FareFamilyType:
    """
    NEW FARE SEACH.

    :ivar ref_number: Fare Family Reference Number
    :ivar fare_familyname: Fare Family Short Name
    :ivar hierarchy: HIERARCHICAL ORDER WITHIN FARE FAMILY
    :ivar cabin: CABIN USED FOR FARE FAMILY
    :ivar commercial_family_details: Indicates Commercial Fare Family
        Short names
    :ivar description: Short description of the fare family
    :ivar carrier: Carrier code
    :ivar services: Reference to the services details
    """

    ref_number: None | str = field(
        default=None,
        metadata={
            "name": "refNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{1,3}",
        },
    )
    fare_familyname: None | str = field(
        default=None,
        metadata={
            "name": "fareFamilyname",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 10,
        },
    )
    hierarchy: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,4}",
        },
    )
    cabin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    commercial_family_details: list[FareFamilyDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "commercialFamilyDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 100,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 2,
            "max_length": 3,
        },
    )
    services: list[ServicesReferences] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
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

    value_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "valueQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"[0-9A-Z]{1,3}",
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "pattern": r"-?[0-9]{1,15}",
        },
    )
    fare_details: None | FareDetailsType193037C = field(
        default=None,
        metadata={
            "name": "fareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    identity_number: None | str = field(
        default=None,
        metadata={
            "name": "identityNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    fare_type_grouping: None | FareTypeGroupingInformationType = field(
        default=None,
        metadata={
            "name": "fareTypeGrouping",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    rate_category: None | str = field(
        default=None,
        metadata={
            "name": "rateCategory",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class FareInformationType80868S:
    """
    To specify fare details.

    :ivar fare_details: Fare details
    """

    class Meta:
        name = "FareInformationType_80868S"

    fare_details: None | FareDetailsType = field(
        default=None,
        metadata={
            "name": "fareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FareQualifierDetailsType:
    """
    To specify the details which qualify a fare.

    :ivar movement_type: Route Code
    :ivar fare_categories: Fare categories
    :ivar fare_details: Fare details
    :ivar additional_fare_details: Additional fare details
    :ivar discount_details: Discount details
    """

    movement_type: None | str = field(
        default=None,
        metadata={
            "name": "movementType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    fare_categories: None | FareCategoryCodesTypeI = field(
        default=None,
        metadata={
            "name": "fareCategories",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    fare_details: None | FareDetailsTypeI = field(
        default=None,
        metadata={
            "name": "fareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    additional_fare_details: None | AdditionalFareQualifierDetailsTypeI = (
        field(
            default=None,
            metadata={
                "name": "additionalFareDetails",
                "type": "Element",
                "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            },
        )
    )
    discount_details: list[DiscountPenaltyInformationType] = field(
        default_factory=list,
        metadata={
            "name": "discountDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
        },
    )


@dataclass
class FlightCharacteristicsType:
    """
    Convey flight characteristics.

    :ivar on_time_performance: On-Time Performance
    :ivar in_flight_srv: In flight services
    """

    on_time_performance: None | OnTimePerformanceType = field(
        default=None,
        metadata={
            "name": "onTimePerformance",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    in_flight_srv: list[str] = field(
        default_factory=list,
        metadata={
            "name": "inFlightSrv",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
            "min_length": 1,
            "max_length": 3,
        },
    )


@dataclass
class FlightProductInformationType:
    """
    To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar context_details: To specify additional characteristics.
    """

    cabin_product: list[CabinProductDetailsType195516C] = field(
        default_factory=list,
        metadata={
            "name": "cabinProduct",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 6,
        },
    )
    context_details: None | ProductTypeDetailsType = field(
        default=None,
        metadata={
            "name": "contextDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FlightProductInformationType141442S:
    """
    To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar context_details: To specify additional characteristics.
    """

    class Meta:
        name = "FlightProductInformationType_141442S"

    cabin_product: list[CabinProductDetailsType205138C] = field(
        default_factory=list,
        metadata={
            "name": "cabinProduct",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 26,
        },
    )
    context_details: None | ProductTypeDetailsType205137C = field(
        default=None,
        metadata={
            "name": "contextDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FlightProductInformationType161491S:
    """
    To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar fare_product_detail: Fare product details
    """

    class Meta:
        name = "FlightProductInformationType_161491S"

    cabin_product: None | CabinProductDetailsType229142C = field(
        default=None,
        metadata={
            "name": "cabinProduct",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    fare_product_detail: None | FareProductDetailsType = field(
        default=None,
        metadata={
            "name": "fareProductDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FlightProductInformationType176659S:
    """
    To specify flight product information details.

    :ivar cabin_product: Indicates flight cabin details
    :ivar fare_product_detail: Fare product details
    :ivar corporate_id: Corporate number or name and number
    :ivar break_point: To determine if Fare Breaks at this segment
    :ivar context_details: To specify additional characteristics.
    """

    class Meta:
        name = "FlightProductInformationType_176659S"

    cabin_product: None | CabinProductDetailsType = field(
        default=None,
        metadata={
            "name": "cabinProduct",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    fare_product_detail: None | FareProductDetailsType248552C = field(
        default=None,
        metadata={
            "name": "fareProductDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    corporate_id: list[str] = field(
        default_factory=list,
        metadata={
            "name": "corporateId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 20,
        },
    )
    break_point: None | str = field(
        default=None,
        metadata={
            "name": "breakPoint",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    context_details: None | ProductTypeDetailsType = field(
        default=None,
        metadata={
            "name": "contextDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class FlightServicesType:
    """
    Convey services for cabin or class.

    :ivar service_type: Type of service used
    :ivar cabin_info:
    :ivar class_info:
    """

    service_type: None | str = field(
        default=None,
        metadata={
            "name": "serviceType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    cabin_info: list[CabinInformationType] = field(
        default_factory=list,
        metadata={
            "name": "cabinInfo",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )
    class_info: list[ClassInformationType] = field(
        default_factory=list,
        metadata={
            "name": "classInfo",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class FrequentTravellerIdentificationCodeType:
    """
    To specify frequent traveler information.

    :ivar frequent_traveller_details: Frequent Traveller Info
    """

    frequent_traveller_details: list[FrequentTravellerIdentificationType] = (
        field(
            default_factory=list,
            metadata={
                "name": "frequentTravellerDetails",
                "type": "Element",
                "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
                "min_occurs": 1,
                "max_occurs": 99,
            },
        )
    )


@dataclass
class HeaderInformationTypeI:
    """
    To specify header information applicable to the entire message.

    :ivar status: Status
    :ivar date_time_period_details: Date and Time info
    :ivar reference_number: Reference number
    :ivar product_identification: Contains product identification such
        as UIC code...
    """

    status: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 3,
        },
    )
    date_time_period_details: None | DateTimePeriodDetailsTypeI = field(
        default=None,
        metadata={
            "name": "dateTimePeriodDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    reference_number: None | str = field(
        default=None,
        metadata={
            "name": "referenceNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    product_identification: list[str] = field(
        default_factory=list,
        metadata={
            "name": "productIdentification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 35,
        },
    )


@dataclass
class InteractiveFreeTextType:
    """
    To provide free form or coded text information.

    :ivar free_text_qualification: Free text qualification
    :ivar free_text: Free text
    """

    free_text_qualification: None | FreeTextQualificationTypeI = field(
        default=None,
        metadata={
            "name": "freeTextQualification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    free_text: None | str = field(
        default=None,
        metadata={
            "name": "freeText",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 50,
        },
    )


@dataclass
class InteractiveFreeTextType78534S:
    """
    To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """

    class Meta:
        name = "InteractiveFreeTextType_78534S"

    free_text_qualification: None | FreeTextQualificationType = field(
        default=None,
        metadata={
            "name": "freeTextQualification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    description: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class InteractiveFreeTextType78544S:
    """
    To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """

    class Meta:
        name = "InteractiveFreeTextType_78544S"

    free_text_qualification: None | FreeTextQualificationType120769C = field(
        default=None,
        metadata={
            "name": "freeTextQualification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    description: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 70,
        },
    )


@dataclass
class InteractiveFreeTextType78559S:
    """
    To provide free form or coded text information.

    :ivar free_text_qualification: Details on interactive free text
    :ivar description: Free text
    """

    class Meta:
        name = "InteractiveFreeTextType_78559S"

    free_text_qualification: None | FreeTextQualificationType120769C = field(
        default=None,
        metadata={
            "name": "freeTextQualification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    description: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass
class ItemNumberType:
    """
    To specify an item number.

    :ivar item_number: Item number details
    """

    item_number: None | ItemNumberIdentificationType192331C = field(
        default=None,
        metadata={
            "name": "itemNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )


@dataclass
class ItemNumberType161497S:
    """
    To specify item numbers.

    :ivar item_number_id: Indicates the recommendation number.
    :ivar code_share_details: Code share details.
    :ivar price_ticketing: Pricing ticketind details.
    """

    class Meta:
        name = "ItemNumberType_161497S"

    item_number_id: None | ItemNumberIdentificationType191597C = field(
        default=None,
        metadata={
            "name": "itemNumberId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    code_share_details: list[CompanyRoleIdentificationType120771C] = field(
        default_factory=list,
        metadata={
            "name": "codeShareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 6,
        },
    )
    price_ticketing: None | PricingTicketingInformationType = field(
        default=None,
        metadata={
            "name": "priceTicketing",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class ItemNumberType166130S:
    """
    To specify an item number.

    :ivar item_number_details: Item number details
    """

    class Meta:
        name = "ItemNumberType_166130S"

    item_number_details: list[ItemNumberIdentificationType234878C] = field(
        default_factory=list,
        metadata={
            "name": "itemNumberDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass
class ItemNumberType176648S:
    """
    To specify an item number.
    """

    class Meta:
        name = "ItemNumberType_176648S"

    item_number_details: list[ItemNumberIdentificationType248537C] = field(
        default_factory=list,
        metadata={
            "name": "itemNumberDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass
class ItemNumberType80866S:
    """
    To specify an item number.

    :ivar item_number_details: Item number details
    """

    class Meta:
        name = "ItemNumberType_80866S"

    item_number_details: None | ItemNumberIdentificationType = field(
        default=None,
        metadata={
            "name": "itemNumberDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )


@dataclass
class MiniRulesType78547S:
    """
    To specify the restrictions.

    :ivar restriction_type: Type of restriction: PTC, Max Adv Res, Max
        Ticketing After Res, ...
    :ivar category: Categoty of restriction: PTC, Max Adv Pur, Days, ...
    :ivar indicator: Indicators
    :ivar mini_rules: Mini rules
    """

    class Meta:
        name = "MiniRulesType_78547S"

    restriction_type: None | str = field(
        default=None,
        metadata={
            "name": "restrictionType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 6,
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 0,
            "max_length": 3,
        },
    )
    indicator: None | MiniRulesIndicatorType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    mini_rules: list[MiniRulesDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "miniRules",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 5,
        },
    )


@dataclass
class MonetaryInformationType:
    """
    To specify monetary information details.

    :ivar monetary_detail: Monetary information.
    """

    monetary_detail: list[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "monetaryDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )


@dataclass
class MonetaryInformationTypeI:
    """
    To convey monetary amounts, rates and percentages.

    :ivar monetary_details: Monetary details
    """

    monetary_details: list[MonetaryInformationDetailsTypeI] = field(
        default_factory=list,
        metadata={
            "name": "monetaryDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass
class MonetaryInformationType174241S:
    """
    To convey monetary amounts, rates and percentages.
    """

    class Meta:
        name = "MonetaryInformationType_174241S"

    monetary_details: None | MonetaryInformationDetailsType245528C = field(
        default=None,
        metadata={
            "name": "monetaryDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    other_monetary_details: list[MonetaryInformationDetailsType245528C] = (
        field(
            default_factory=list,
            metadata={
                "name": "otherMonetaryDetails",
                "type": "Element",
                "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
                "max_occurs": 19,
            },
        )
    )


@dataclass
class MonetaryInformationType185955S:
    """
    To specify monetary information details.

    :ivar monetary_detail: Monetary information
    """

    class Meta:
        name = "MonetaryInformationType_185955S"

    monetary_detail: list[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "monetaryDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class MonetaryInformationType193024S:
    """
    To specify monetary information details.

    :ivar monetary_detail: Monetary information.
    """

    class Meta:
        name = "MonetaryInformationType_193024S"

    monetary_detail: list[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "monetaryDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 30,
        },
    )


@dataclass
class OriginAndDestinationRequestType:
    """
    To convey information regarding Requested Segments.

    :ivar seg_ref: Requested segment number
    :ivar location_forcing: Forces arrival or departure, from/to the
        same airport/city
    """

    seg_ref: None | str = field(
        default=None,
        metadata={
            "name": "segRef",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "pattern": r"-?[0-9]{1,2}",
        },
    )
    location_forcing: list[ItineraryDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "locationForcing",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 2,
        },
    )


@dataclass
class PricingTicketingSubsequentType193023S:
    """
    To convey additional information related to a ticket.

    :ivar pax_fare_num: Passenger fare product number
    :ivar total_fare_amount: Total fare amount
    :ivar total_tax_amount: Total tax amount
    :ivar code_share_details: Code share details.
    :ivar monetary_details: Monetary information.
    :ivar pricing_ticketing: Pricing ticketing details.
    """

    class Meta:
        name = "PricingTicketingSubsequentType_193023S"

    pax_fare_num: None | str = field(
        default=None,
        metadata={
            "name": "paxFareNum",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
            "min_length": 1,
            "max_length": 3,
        },
    )
    total_fare_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "totalFareAmount",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    total_tax_amount: None | Decimal = field(
        default=None,
        metadata={
            "name": "totalTaxAmount",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    code_share_details: list[CompanyRoleIdentificationType120771C] = field(
        default_factory=list,
        metadata={
            "name": "codeShareDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 6,
        },
    )
    monetary_details: list[MonetaryInformationDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "monetaryDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )
    pricing_ticketing: None | PricingTicketingInformationType = field(
        default=None,
        metadata={
            "name": "pricingTicketing",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class ProductInformationType:
    """
    To specify details related to routing status of a product.

    :ivar product_details_qualifier: value of the Qualifier: INT for
        International DOM for Domestic EUR for European  otherwise
        CM#10569 INVALID INTERNATIONAL INDICATOR is returned.
    :ivar booking_class_details:
    """

    product_details_qualifier: None | str = field(
        default=None,
        metadata={
            "name": "productDetailsQualifier",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    booking_class_details: list[ProductDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "bookingClassDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 26,
        },
    )


@dataclass
class ProposedSegmentType:
    """
    To specify the parameters used for product quality.

    :ivar flight_proposal: Parameters for proposed flight group
    :ivar flight_characteristic: Flight characteristics.
    :ivar maj_cabin: Majority cabin
    """

    flight_proposal: list[ProposedSegmentDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "flightProposal",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )
    flight_characteristic: None | str = field(
        default=None,
        metadata={
            "name": "flightCharacteristic",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 0,
            "max_length": 3,
        },
    )
    maj_cabin: None | str = field(
        default=None,
        metadata={
            "name": "majCabin",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )


@dataclass
class ReferenceInfoType:
    """
    To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    """

    referencing_detail: list[ReferencingDetailsType191583C] = field(
        default_factory=list,
        metadata={
            "name": "referencingDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 200,
        },
    )


@dataclass
class ReferenceInfoType133176S:
    """
    To specify an association between references given to travelers, to products,
    to services.

    :ivar referencing_detail: Referencing details
    """

    class Meta:
        name = "ReferenceInfoType_133176S"

    referencing_detail: list[ReferencingDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "referencingDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class ReferenceInfoType134839S:
    """
    To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    """

    class Meta:
        name = "ReferenceInfoType_134839S"

    referencing_detail: list[ReferencingDetailsType195561C] = field(
        default_factory=list,
        metadata={
            "name": "referencingDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class ReferenceInfoType134840S:
    """
    To provide specific reference identification for a traveller.

    :ivar referencing_detail: Referencing details
    """

    class Meta:
        name = "ReferenceInfoType_134840S"

    referencing_detail: list[ReferencingDetailsType195561C] = field(
        default_factory=list,
        metadata={
            "name": "referencingDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 200,
        },
    )


@dataclass
class ReferenceInfoType165972S:
    """
    To provide specific Hotel reference identification.

    :ivar reference_details: Reference details
    """

    class Meta:
        name = "ReferenceInfoType_165972S"

    reference_details: list[ReferencingDetailsType234704C] = field(
        default_factory=list,
        metadata={
            "name": "referenceDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )


@dataclass
class ReferenceInfoType176658S:
    """
    To specify an association between references given to travelers, to products,
    to services.

    :ivar referencing_detail: Referencing details
    """

    class Meta:
        name = "ReferenceInfoType_176658S"

    referencing_detail: list[ReferencingDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "referencingDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 6,
        },
    )


@dataclass
class SegmentRepetitionControlTypeI:
    """
    To indicate the number of segment group repetitions.

    :ivar segment_control_details: Segment control details
    """

    segment_control_details: list[SegmentRepetitionControlDetailsTypeI] = (
        field(
            default_factory=list,
            metadata={
                "name": "segmentControlDetails",
                "type": "Element",
                "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
                "max_occurs": 9,
            },
        )
    )


@dataclass
class SelectionDetailsType:
    """
    To specify the details for making a selection.

    :ivar carrier_fee_details: Carrier fees options
    """

    carrier_fee_details: None | SelectionDetailsInformationType = field(
        default=None,
        metadata={
            "name": "carrierFeeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )


@dataclass
class SequenceDetailsTypeU:
    """
    To provide details relating to the sequence.

    :ivar sequence_details: Sequence details
    """

    sequence_details: None | SequenceInformationTypeU = field(
        default=None,
        metadata={
            "name": "sequenceDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class SpecialRequirementsDetailsType:
    """
    To specify special requests or service s information relating to a traveller.

    :ivar service_requirements_info: To specify the Service Requirement
        of the customer
    :ivar seat_details: Seat details
    """

    service_requirements_info: None | SpecialRequirementsTypeDetailsType = (
        field(
            default=None,
            metadata={
                "name": "serviceRequirementsInfo",
                "type": "Element",
                "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
                "required": True,
            },
        )
    )
    seat_details: list[SpecialRequirementsDataDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "seatDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 999,
        },
    )


@dataclass
class SpecificDataInformationType:
    """
    To specify miscellaneous data by first identifying the type of data to be sent
    and then the actual data.

    :ivar data_type_information: Carrier fee description
    :ivar data_information: Data information
    """

    data_type_information: None | DataTypeInformationType = field(
        default=None,
        metadata={
            "name": "dataTypeInformation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    data_information: list[DataInformationType] = field(
        default_factory=list,
        metadata={
            "name": "dataInformation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class SpecificTravellerType:
    """
    To specify additional details about a particular traveller.

    :ivar traveller_details: Traveller details
    """

    traveller_details: list[SpecificTravellerDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "travellerDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class StatusType:
    """
    To advise the requester system the status of the reply.

    :ivar status: Status details
    """

    status: list[StatusDetailsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )


@dataclass
class StatusType182386S:
    """
    To advise the requester system the status of the reply.

    :ivar status_information: STATUS DETAILS
    """

    class Meta:
        name = "StatusType_182386S"

    status_information: list[StatusDetailsType256255C] = field(
        default_factory=list,
        metadata={
            "name": "statusInformation",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass
class TaxType:
    """
    To specify details relating to tax(es).

    :ivar tax_category: Tax category
    :ivar tax_details: Tax details
    """

    tax_category: None | str = field(
        default=None,
        metadata={
            "name": "taxCategory",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 3,
        },
    )
    tax_details: list[TaxDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "taxDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 99,
        },
    )


@dataclass
class TransportIdentifierType:
    """
    To specify the transport service(s) which is /are to be updated or cancelled.

    :ivar company_identification: Company identification
    """

    company_identification: None | CompanyIdentificationTypeI = field(
        default=None,
        metadata={
            "name": "companyIdentification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )


@dataclass
class TravelProductType:
    """
    Contains flight travel (date, time, flight number,...) and posting avaibility
    information.

    :ivar product_date_time: Date and time of departure and arrival
    :ivar location: Location of departure and arrival
    :ivar company_id:
    :ivar flight_ortrain_number: Flight number or trainNumber
    :ivar product_detail: Product details
    :ivar add_product_detail: Additional product details
    :ivar attribute_details: Attribute details
    """

    product_date_time: None | ProductDateTimeType = field(
        default=None,
        metadata={
            "name": "productDateTime",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "required": True,
        },
    )
    location: list[LocationIdentificationDetailsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    company_id: None | CompanyIdentificationType = field(
        default=None,
        metadata={
            "name": "companyId",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    flight_ortrain_number: None | str = field(
        default=None,
        metadata={
            "name": "flightOrtrainNumber",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 8,
        },
    )
    product_detail: None | AdditionalProductDetailsType = field(
        default=None,
        metadata={
            "name": "productDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    add_product_detail: None | ProductFacilitiesType = field(
        default=None,
        metadata={
            "name": "addProductDetail",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    attribute_details: list[CodedAttributeInformationType270108C] = field(
        default_factory=list,
        metadata={
            "name": "attributeDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 20,
        },
    )


@dataclass
class TravellerReferenceInformationType:
    """
    To specify traveller/personal details.

    :ivar ptc: Requested passenger type
    :ivar traveller: Traveller details
    """

    ptc: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 3,
            "min_length": 1,
            "max_length": 6,
        },
    )
    traveller: list[TravellerDetailsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 9,
        },
    )


@dataclass
class UserIdentificationType:
    """
    User Identification.

    :ivar office_identification: Originator Identification Details
    :ivar office_type: Used to specify which kind of info is given in DE
        9900.
    :ivar office_code: The code given to an agent by the originating
        reservation system.
    """

    office_identification: None | OriginatorIdentificationDetailsTypeI = field(
        default=None,
        metadata={
            "name": "officeIdentification",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
        },
    )
    office_type: None | str = field(
        default=None,
        metadata={
            "name": "officeType",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 1,
        },
    )
    office_code: None | str = field(
        default=None,
        metadata={
            "name": "officeCode",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 30,
        },
    )


@dataclass
class ValueSearchCriteriaType:
    """
    To specify Criteria with list of parameters.
    """

    ref: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 35,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "min_length": 1,
            "max_length": 18,
        },
    )
    criteria_details: list[CriteriaDetailsType] = field(
        default_factory=list,
        metadata={
            "name": "criteriaDetails",
            "type": "Element",
            "namespace": "http://xml.amadeus.com/FMPTBR_15_3_1A",
            "max_occurs": 10,
        },
    )


@dataclass
class FareMasterPricerTravelBoardSearchReply:
    """
    Master Pricer Travel Board Search Reply Flex Pricer Flex Pricer.

    :ivar reply_status: Gives status about reply : type of process,
        region , CPU etc..
    :ivar error_message: Error message
    :ivar conversion_rate: Specifies the currency used for pricing.
    :ivar solution_family: Solution Family
    :ivar family_information: Details of the fare families processed
    :ivar amount_info_for_all_pax: Amount information for all passengers
    :ivar amount_info_per_pax: Amount information per passengers
    :ivar fee_details: Fee/Reduction details.
    :ivar bucket_info: Bucket information
    :ivar company_id_text: Free text identifying an airline in a code
        share.
    :ivar office_id_details: List of Office Id Details
    :ivar flight_index: List of flights
    :ivar recommendation: Recommendation details
    :ivar other_solutions: Additional solutions, such as Rail
        solutions...
    :ivar warning_info: Warning information
    :ivar global_information: Global information
    :ivar service_fees_grp:
    :ivar value:
    :ivar mnr_grp:
    """

    class Meta:
        name = "Fare_MasterPricerTravelBoardSearchReply"
        namespace = "http://xml.amadeus.com/FMPTBR_15_3_1A"

    reply_status: None | StatusType = field(
        default=None,
        metadata={
            "name": "replyStatus",
            "type": "Element",
        },
    )
    error_message: (
        None | FareMasterPricerTravelBoardSearchReply.ErrorMessage
    ) = field(
        default=None,
        metadata={
            "name": "errorMessage",
            "type": "Element",
        },
    )
    conversion_rate: None | ConversionRateTypeI = field(
        default=None,
        metadata={
            "name": "conversionRate",
            "type": "Element",
        },
    )
    solution_family: list[FareInformationType] = field(
        default_factory=list,
        metadata={
            "name": "solutionFamily",
            "type": "Element",
            "max_occurs": 20,
        },
    )
    family_information: list[FareFamilyType] = field(
        default_factory=list,
        metadata={
            "name": "familyInformation",
            "type": "Element",
            "max_occurs": 200,
        },
    )
    amount_info_for_all_pax: (
        None | FareMasterPricerTravelBoardSearchReply.AmountInfoForAllPax
    ) = field(
        default=None,
        metadata={
            "name": "amountInfoForAllPax",
            "type": "Element",
        },
    )
    amount_info_per_pax: list[
        FareMasterPricerTravelBoardSearchReply.AmountInfoPerPax
    ] = field(
        default_factory=list,
        metadata={
            "name": "amountInfoPerPax",
            "type": "Element",
            "max_occurs": 20,
        },
    )
    fee_details: list[FareMasterPricerTravelBoardSearchReply.FeeDetails] = (
        field(
            default_factory=list,
            metadata={
                "name": "feeDetails",
                "type": "Element",
                "max_occurs": 2099,
            },
        )
    )
    bucket_info: list[BucketInformationType] = field(
        default_factory=list,
        metadata={
            "name": "bucketInfo",
            "type": "Element",
            "max_occurs": 10,
        },
    )
    company_id_text: list[CompanyIdentificationTextType] = field(
        default_factory=list,
        metadata={
            "name": "companyIdText",
            "type": "Element",
            "max_occurs": 5000,
        },
    )
    office_id_details: list[
        FareMasterPricerTravelBoardSearchReply.OfficeIdDetails
    ] = field(
        default_factory=list,
        metadata={
            "name": "officeIdDetails",
            "type": "Element",
            "max_occurs": 20,
        },
    )
    flight_index: list[FareMasterPricerTravelBoardSearchReply.FlightIndex] = (
        field(
            default_factory=list,
            metadata={
                "name": "flightIndex",
                "type": "Element",
                "max_occurs": 6,
            },
        )
    )
    recommendation: list[
        FareMasterPricerTravelBoardSearchReply.Recommendation
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100000,
        },
    )
    other_solutions: list[
        FareMasterPricerTravelBoardSearchReply.OtherSolutions
    ] = field(
        default_factory=list,
        metadata={
            "name": "otherSolutions",
            "type": "Element",
            "max_occurs": 100009,
        },
    )
    warning_info: list[FareMasterPricerTravelBoardSearchReply.WarningInfo] = (
        field(
            default_factory=list,
            metadata={
                "name": "warningInfo",
                "type": "Element",
                "max_occurs": 9,
            },
        )
    )
    global_information: list[
        FareMasterPricerTravelBoardSearchReply.GlobalInformation
    ] = field(
        default_factory=list,
        metadata={
            "name": "globalInformation",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    service_fees_grp: list[
        FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp
    ] = field(
        default_factory=list,
        metadata={
            "name": "serviceFeesGrp",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    value: list[ValueSearchCriteriaType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100009,
        },
    )
    mnr_grp: None | FareMasterPricerTravelBoardSearchReply.MnrGrp = field(
        default=None,
        metadata={
            "name": "mnrGrp",
            "type": "Element",
        },
    )

    @dataclass
    class ErrorMessage:
        """
        :ivar application_error: Application error details.
        :ivar error_message_text: Type of error message and free text
        """

        application_error: None | ApplicationErrorInformationType78543S = (
            field(
                default=None,
                metadata={
                    "name": "applicationError",
                    "type": "Element",
                    "required": True,
                },
            )
        )
        error_message_text: None | InteractiveFreeTextType78544S = field(
            default=None,
            metadata={
                "name": "errorMessageText",
                "type": "Element",
            },
        )

    @dataclass
    class AmountInfoForAllPax:
        """
        :ivar itinerary_amounts: Itinerary amounts for all passengers
        :ivar amounts_per_sgt: Amounts information per segment
        """

        itinerary_amounts: None | MonetaryInformationType = field(
            default=None,
            metadata={
                "name": "itineraryAmounts",
                "type": "Element",
                "required": True,
            },
        )
        amounts_per_sgt: list[
            FareMasterPricerTravelBoardSearchReply.AmountInfoForAllPax.AmountsPerSgt
        ] = field(
            default_factory=list,
            metadata={
                "name": "amountsPerSgt",
                "type": "Element",
                "max_occurs": 9,
            },
        )

        @dataclass
        class AmountsPerSgt:
            """
            :ivar sgt_ref: Requested segment reference
            :ivar amounts: Amounts : Issue total amount, issue taxes
                amount, non refundable taxes amount
            """

            sgt_ref: None | ReferenceInfoType133176S = field(
                default=None,
                metadata={
                    "name": "sgtRef",
                    "type": "Element",
                    "required": True,
                },
            )
            amounts: None | MonetaryInformationType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

    @dataclass
    class AmountInfoPerPax:
        """
        :ivar pax_ref: Passenger references
        :ivar pax_attributes: Passenger attributes : Infant indicator
        :ivar itinerary_amounts: Itinerary amounts information
        :ivar amounts_per_sgt: Amounts per segment
        """

        pax_ref: None | SpecificTravellerType = field(
            default=None,
            metadata={
                "name": "paxRef",
                "type": "Element",
                "required": True,
            },
        )
        pax_attributes: None | FareInformationType80868S = field(
            default=None,
            metadata={
                "name": "paxAttributes",
                "type": "Element",
            },
        )
        itinerary_amounts: None | MonetaryInformationType = field(
            default=None,
            metadata={
                "name": "itineraryAmounts",
                "type": "Element",
                "required": True,
            },
        )
        amounts_per_sgt: list[
            FareMasterPricerTravelBoardSearchReply.AmountInfoPerPax.AmountsPerSgt
        ] = field(
            default_factory=list,
            metadata={
                "name": "amountsPerSgt",
                "type": "Element",
                "max_occurs": 9,
            },
        )

        @dataclass
        class AmountsPerSgt:
            """
            :ivar sgt_ref: Requested segment reference
            :ivar amounts: Amounts : Issue total amount, issue taxes
                amount, non refundable taxes amount
            """

            sgt_ref: None | ReferenceInfoType133176S = field(
                default=None,
                metadata={
                    "name": "sgtRef",
                    "type": "Element",
                    "required": True,
                },
            )
            amounts: None | MonetaryInformationType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )

    @dataclass
    class FeeDetails:
        """
        :ivar fee_reference: Fee/Reduction Reference number.
        :ivar fee_information: Fee/Reduction information.
        :ivar fee_parameters: Fee/Reduction parameters.
        :ivar converted_or_original_info: To specify conversion rate
            details
        """

        fee_reference: None | ItemReferencesAndVersionsType78564S = field(
            default=None,
            metadata={
                "name": "feeReference",
                "type": "Element",
                "required": True,
            },
        )
        fee_information: None | DiscountAndPenaltyInformationType = field(
            default=None,
            metadata={
                "name": "feeInformation",
                "type": "Element",
            },
        )
        fee_parameters: None | AttributeType78561S = field(
            default=None,
            metadata={
                "name": "feeParameters",
                "type": "Element",
            },
        )
        converted_or_original_info: None | ConversionRateTypeI78562S = field(
            default=None,
            metadata={
                "name": "convertedOrOriginalInfo",
                "type": "Element",
            },
        )

    @dataclass
    class OfficeIdDetails:
        """
        :ivar office_id_information: Office Id Information
        :ivar office_id_reference: Office Id Reference Number
        """

        office_id_information: None | UserIdentificationType = field(
            default=None,
            metadata={
                "name": "officeIdInformation",
                "type": "Element",
                "required": True,
            },
        )
        office_id_reference: None | ItemReferencesAndVersionsType78536S = (
            field(
                default=None,
                metadata={
                    "name": "officeIdReference",
                    "type": "Element",
                    "required": True,
                },
            )
        )

    @dataclass
    class FlightIndex:
        """
        :ivar requested_segment_ref: Indicates references and details
            about requested segments
        :ivar group_of_flights: List of flights per requested segment
        """

        requested_segment_ref: None | OriginAndDestinationRequestType = field(
            default=None,
            metadata={
                "name": "requestedSegmentRef",
                "type": "Element",
                "required": True,
            },
        )
        group_of_flights: list[
            FareMasterPricerTravelBoardSearchReply.FlightIndex.GroupOfFlights
        ] = field(
            default_factory=list,
            metadata={
                "name": "groupOfFlights",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 100000,
            },
        )

        @dataclass
        class GroupOfFlights:
            """
            :ivar prop_flight_gr_detail: To indicate parameters for
                proposed flight group.
            :ivar flight_details: List of flight per Elapse Flying time
            """

            prop_flight_gr_detail: None | ProposedSegmentType = field(
                default=None,
                metadata={
                    "name": "propFlightGrDetail",
                    "type": "Element",
                    "required": True,
                },
            )
            flight_details: list[
                FareMasterPricerTravelBoardSearchReply.FlightIndex.GroupOfFlights.FlightDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "flightDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 4,
                },
            )

            @dataclass
            class FlightDetails:
                """
                :ivar flight_information: Specification of details on
                    the flight and posting availability
                :ivar avl_info: returns booking class and availability
                    context
                :ivar technical_stop: Details on Flight date, time and
                    location of technical stop or change of gauge
                :ivar commercial_agreement: Code Share Agreement
                    description for current flight.
                :ivar add_info: Additional Info about flight, such as
                    Reference number, and several options
                :ivar flight_characteristics: Flight characteristics
                :ivar flight_services: Flight Services by cabin/rbd
                """

                flight_information: None | TravelProductType = field(
                    default=None,
                    metadata={
                        "name": "flightInformation",
                        "type": "Element",
                        "required": True,
                    },
                )
                avl_info: list[FlightProductInformationType141442S] = field(
                    default_factory=list,
                    metadata={
                        "name": "avlInfo",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                technical_stop: list[DateAndTimeInformationType] = field(
                    default_factory=list,
                    metadata={
                        "name": "technicalStop",
                        "type": "Element",
                        "max_occurs": 5,
                    },
                )
                commercial_agreement: None | CommercialAgreementsType = field(
                    default=None,
                    metadata={
                        "name": "commercialAgreement",
                        "type": "Element",
                    },
                )
                add_info: None | HeaderInformationTypeI = field(
                    default=None,
                    metadata={
                        "name": "addInfo",
                        "type": "Element",
                    },
                )
                flight_characteristics: None | FlightCharacteristicsType = (
                    field(
                        default=None,
                        metadata={
                            "name": "flightCharacteristics",
                            "type": "Element",
                        },
                    )
                )
                flight_services: list[FlightServicesType] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightServices",
                        "type": "Element",
                        "max_occurs": 9,
                    },
                )

    @dataclass
    class Recommendation:
        """
        :ivar item_number: Specification of the item number
        :ivar warning_message: To describe type of recommendation
        :ivar fare_family_ref: Indicates the Fare family reference.
        :ivar rec_price_info: Recommendation Price and Taxes.
        :ivar mini_rule: Mini rules
        :ivar segment_flight_ref: Indicates reference of Flight or the
            fee reference valid for all pax (usage:start with the 1
            possible Fee reference, then provide the segments
            references)
        :ivar recommandation_segments_fare_details: Fare details per
            reuqested segments for all passengers.
        :ivar pax_fare_product: Passenger fare product details
        :ivar specific_rec_details: Specific recommendation details
        """

        item_number: None | ItemNumberType161497S = field(
            default=None,
            metadata={
                "name": "itemNumber",
                "type": "Element",
                "required": True,
            },
        )
        warning_message: list[InteractiveFreeTextType78544S] = field(
            default_factory=list,
            metadata={
                "name": "warningMessage",
                "type": "Element",
                "max_occurs": 4,
            },
        )
        fare_family_ref: None | ReferenceInfoType133176S = field(
            default=None,
            metadata={
                "name": "fareFamilyRef",
                "type": "Element",
            },
        )
        rec_price_info: None | MonetaryInformationType193024S = field(
            default=None,
            metadata={
                "name": "recPriceInfo",
                "type": "Element",
                "required": True,
            },
        )
        mini_rule: list[MiniRulesType78547S] = field(
            default_factory=list,
            metadata={
                "name": "miniRule",
                "type": "Element",
                "max_occurs": 9,
            },
        )
        segment_flight_ref: list[ReferenceInfoType] = field(
            default_factory=list,
            metadata={
                "name": "segmentFlightRef",
                "type": "Element",
                "max_occurs": 100009,
            },
        )
        recommandation_segments_fare_details: list[
            FareMasterPricerTravelBoardSearchReply.Recommendation.RecommandationSegmentsFareDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "recommandationSegmentsFareDetails",
                "type": "Element",
                "max_occurs": 6,
            },
        )
        pax_fare_product: list[
            FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct
        ] = field(
            default_factory=list,
            metadata={
                "name": "paxFareProduct",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 10,
            },
        )
        specific_rec_details: list[
            FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "specificRecDetails",
                "type": "Element",
                "max_occurs": 100000,
            },
        )

        @dataclass
        class RecommandationSegmentsFareDetails:
            """
            :ivar recommendation_seg_ref: Reference and details about
                requested segments.
            :ivar segment_monetary_information: Amounts per requested
                segment.
            """

            recommendation_seg_ref: None | OriginAndDestinationRequestType = (
                field(
                    default=None,
                    metadata={
                        "name": "recommendationSegRef",
                        "type": "Element",
                        "required": True,
                    },
                )
            )
            segment_monetary_information: None | MonetaryInformationType = (
                field(
                    default=None,
                    metadata={
                        "name": "segmentMonetaryInformation",
                        "type": "Element",
                    },
                )
            )

        @dataclass
        class PaxFareProduct:
            """
            :ivar pax_fare_detail: Passenger Fare Details.
            :ivar fee_ref: Indicates Fee references (usage: start with
                the 1 possible Fee reference, then provide the segments
                references)
            :ivar pax_reference: Passenger Reference
            :ivar passenger_tax_details: add tax details for each
                passenger of each recommendations.
            :ivar fare: fare Details
            :ivar fare_details: Fare details by Requested segment number
            """

            pax_fare_detail: None | PricingTicketingSubsequentType193023S = (
                field(
                    default=None,
                    metadata={
                        "name": "paxFareDetail",
                        "type": "Element",
                        "required": True,
                    },
                )
            )
            fee_ref: None | ReferenceInfoType134839S = field(
                default=None,
                metadata={
                    "name": "feeRef",
                    "type": "Element",
                },
            )
            pax_reference: list[TravellerReferenceInformationType] = field(
                default_factory=list,
                metadata={
                    "name": "paxReference",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 6,
                },
            )
            passenger_tax_details: None | TaxType = field(
                default=None,
                metadata={
                    "name": "passengerTaxDetails",
                    "type": "Element",
                },
            )
            fare: list[
                FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.Fare
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 7,
                },
            )
            fare_details: list[
                FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.FareDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "fareDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 6,
                },
            )

            @dataclass
            class Fare:
                """
                :ivar pricing_message: Last Date to Ticket, Penalties
                :ivar monetary_information: Amount of penalties,
                    Surcharges...
                """

                pricing_message: None | InteractiveFreeTextType78559S = field(
                    default=None,
                    metadata={
                        "name": "pricingMessage",
                        "type": "Element",
                        "required": True,
                    },
                )
                monetary_information: None | MonetaryInformationType185955S = (
                    field(
                        default=None,
                        metadata={
                            "name": "monetaryInformation",
                            "type": "Element",
                        },
                    )
                )

            @dataclass
            class FareDetails:
                """
                :ivar segment_ref: Reference of the Requested Segment
                :ivar group_of_fares: Contains the fare details as
                    PTC,Fare Basis, Fare Family applied for each segment
                :ivar psg_seg_monetary_information: Amounts per
                    passenger per requested segment.
                :ivar maj_cabin: Majority Cabin Info
                """

                segment_ref: None | OriginAndDestinationRequestType = field(
                    default=None,
                    metadata={
                        "name": "segmentRef",
                        "type": "Element",
                        "required": True,
                    },
                )
                group_of_fares: list[
                    FareMasterPricerTravelBoardSearchReply.Recommendation.PaxFareProduct.FareDetails.GroupOfFares
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "groupOfFares",
                        "type": "Element",
                        "max_occurs": 4,
                    },
                )
                psg_seg_monetary_information: (
                    None | MonetaryInformationType
                ) = field(
                    default=None,
                    metadata={
                        "name": "psgSegMonetaryInformation",
                        "type": "Element",
                    },
                )
                maj_cabin: list[ProductInformationType] = field(
                    default_factory=list,
                    metadata={
                        "name": "majCabin",
                        "type": "Element",
                        "max_occurs": 10,
                    },
                )

                @dataclass
                class GroupOfFares:
                    """
                    :ivar product_information: Contains details of
                        Flight and Fare
                    :ivar fare_calculation_code_details: Fare
                        calculation code details
                    :ivar ticket_infos: Ticket designator, ticket code
                        and fare basis.
                    :ivar fare_families_ref: Reference of Fare Family
                        for each Fare Component
                    """

                    product_information: (
                        None | FlightProductInformationType176659S
                    ) = field(
                        default=None,
                        metadata={
                            "name": "productInformation",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    fare_calculation_code_details: list[
                        FareCalculationCodeDetailsType
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareCalculationCodeDetails",
                            "type": "Element",
                            "max_occurs": 9,
                        },
                    )
                    ticket_infos: None | FareQualifierDetailsType = field(
                        default=None,
                        metadata={
                            "name": "ticketInfos",
                            "type": "Element",
                        },
                    )
                    fare_families_ref: None | ReferenceInfoType176658S = field(
                        default=None,
                        metadata={
                            "name": "fareFamiliesRef",
                            "type": "Element",
                        },
                    )

        @dataclass
        class SpecificRecDetails:
            """
            :ivar specific_rec_item: Recommendation details
            :ivar specific_product_details: Specific fare product
                details
            """

            specific_rec_item: None | ItemReferencesAndVersionsType = field(
                default=None,
                metadata={
                    "name": "specificRecItem",
                    "type": "Element",
                    "required": True,
                },
            )
            specific_product_details: list[
                FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "specificProductDetails",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass
            class SpecificProductDetails:
                """
                :ivar product_references: Product details
                :ivar fare_context_details: Specific fare details per
                    requested segments.
                """

                product_references: None | PricingTicketingSubsequentType = (
                    field(
                        default=None,
                        metadata={
                            "name": "productReferences",
                            "type": "Element",
                            "required": True,
                        },
                    )
                )
                fare_context_details: list[
                    FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails.FareContextDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareContextDetails",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )

                @dataclass
                class FareContextDetails:
                    """
                    :ivar requested_segment_info: Reference of requested
                        segment
                    :ivar cnx_context_details: Fare connection context
                        details
                    """

                    requested_segment_info: (
                        None | OriginAndDestinationRequestType134833S
                    ) = field(
                        default=None,
                        metadata={
                            "name": "requestedSegmentInfo",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    cnx_context_details: list[
                        FareMasterPricerTravelBoardSearchReply.Recommendation.SpecificRecDetails.SpecificProductDetails.FareContextDetails.CnxContextDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "cnxContextDetails",
                            "type": "Element",
                            "max_occurs": 4,
                        },
                    )

                    @dataclass
                    class CnxContextDetails:
                        """
                        :ivar fare_cnx_info: Fare connection context
                            details
                        """

                        fare_cnx_info: None | FlightProductInformationType = (
                            field(
                                default=None,
                                metadata={
                                    "name": "fareCnxInfo",
                                    "type": "Element",
                                    "required": True,
                                },
                            )
                        )

    @dataclass
    class OtherSolutions:
        """
        :ivar reference: Reference to the current solution
        :ivar amt_group: Describes several amount for each sequence
        :ivar psg_info: Passenger Related info (discount card, PTC, fare
            info, amount ...)
        """

        reference: None | SequenceDetailsTypeU = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        amt_group: list[
            FareMasterPricerTravelBoardSearchReply.OtherSolutions.AmtGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "amtGroup",
                "type": "Element",
                "max_occurs": 10,
            },
        )
        psg_info: list[
            FareMasterPricerTravelBoardSearchReply.OtherSolutions.PsgInfo
        ] = field(
            default_factory=list,
            metadata={
                "name": "psgInfo",
                "type": "Element",
                "max_occurs": 99,
            },
        )

        @dataclass
        class AmtGroup:
            """
            :ivar ref: reference to the current amount (per bound, per
                segment...)
            :ivar amount: Amount Description
            """

            ref: None | ReferenceInfoType165972S = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            amount: None | MonetaryInformationTypeI = field(
                default=None,
                metadata={
                    "type": "Element",
                },
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

            ref: None | SegmentRepetitionControlTypeI = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            description: None | FareInformationTypeI = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            freq_traveller: None | FrequentTravellerIdentificationCodeType = (
                field(
                    default=None,
                    metadata={
                        "name": "freqTraveller",
                        "type": "Element",
                    },
                )
            )
            amount: None | MonetaryInformationTypeI = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            fare: None | FlightProductInformationType161491S = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            attribute: list[AttributeTypeU] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

    @dataclass
    class WarningInfo:
        """
        :ivar global_message_marker: Dummy Segment
        :ivar global_message: Informative free text information
        """

        global_message_marker: None | DummySegmentTypeI = field(
            default=None,
            metadata={
                "name": "globalMessageMarker",
                "type": "Element",
                "required": True,
            },
        )
        global_message: None | InteractiveFreeTextType78534S = field(
            default=None,
            metadata={
                "name": "globalMessage",
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class GlobalInformation:
        """
        :ivar attributes: Coded attributes
        """

        attributes: None | CodedAttributeType = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

    @dataclass
    class ServiceFeesGrp:
        """
        :ivar service_type_info: Service fee type (OC)
        :ivar service_fee_ref_grp: Service fee reference  (OC ,OCM, OCC)
        :ivar service_coverage_info_grp: Service coverage information
            per passenger
        :ivar global_message_marker: Globalmessage marker
        :ivar service_fee_info_grp: Service fee information per
            passenger
        :ivar service_details_grp: Description of applicable services
        :ivar free_bag_allowance_grp: Free baggage allowance information
            group
        """

        service_type_info: None | SelectionDetailsType = field(
            default=None,
            metadata={
                "name": "serviceTypeInfo",
                "type": "Element",
                "required": True,
            },
        )
        service_fee_ref_grp: list[
            FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeRefGrp
        ] = field(
            default_factory=list,
            metadata={
                "name": "serviceFeeRefGrp",
                "type": "Element",
                "max_occurs": 100000,
            },
        )
        service_coverage_info_grp: list[
            FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceCoverageInfoGrp
        ] = field(
            default_factory=list,
            metadata={
                "name": "serviceCoverageInfoGrp",
                "type": "Element",
                "max_occurs": 100000,
            },
        )
        global_message_marker: None | DummySegmentTypeI = field(
            default=None,
            metadata={
                "name": "globalMessageMarker",
                "type": "Element",
                "required": True,
            },
        )
        service_fee_info_grp: list[
            FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp
        ] = field(
            default_factory=list,
            metadata={
                "name": "serviceFeeInfoGrp",
                "type": "Element",
                "max_occurs": 100000,
            },
        )
        service_details_grp: list[
            FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceDetailsGrp
        ] = field(
            default_factory=list,
            metadata={
                "name": "serviceDetailsGrp",
                "type": "Element",
                "max_occurs": 200,
            },
        )
        free_bag_allowance_grp: list[
            FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.FreeBagAllowanceGrp
        ] = field(
            default_factory=list,
            metadata={
                "name": "freeBagAllowanceGrp",
                "type": "Element",
                "max_occurs": 100000,
            },
        )

        @dataclass
        class ServiceFeeRefGrp:
            """
            :ivar ref_info: Reference of service fee global information
            """

            ref_info: None | ReferenceInfoType = field(
                default=None,
                metadata={
                    "name": "refInfo",
                    "type": "Element",
                    "required": True,
                },
            )

        @dataclass
        class ServiceCoverageInfoGrp:
            """
            :ivar item_number_info: Item reference number for service
                coverage details
            :ivar service_cov_info_grp: Service coverage information
                group
            """

            item_number_info: None | ItemNumberType = field(
                default=None,
                metadata={
                    "name": "itemNumberInfo",
                    "type": "Element",
                    "required": True,
                },
            )
            service_cov_info_grp: list[
                FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceCoverageInfoGrp.ServiceCovInfoGrp
            ] = field(
                default_factory=list,
                metadata={
                    "name": "serviceCovInfoGrp",
                    "type": "Element",
                    "max_occurs": 200,
                },
            )

            @dataclass
            class ServiceCovInfoGrp:
                """
                :ivar pax_ref_info: Passenger reference number
                :ivar coverage_per_flights_info: Service coverage
                    information at flight level Matched seat
                    characteristics
                :ivar carrier_info: Carrier information
                :ivar ref_info: Service reference number
                """

                pax_ref_info: None | SpecificTravellerType = field(
                    default=None,
                    metadata={
                        "name": "paxRefInfo",
                        "type": "Element",
                        "required": True,
                    },
                )
                coverage_per_flights_info: list[ActionDetailsType] = field(
                    default_factory=list,
                    metadata={
                        "name": "coveragePerFlightsInfo",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                carrier_info: None | TransportIdentifierType = field(
                    default=None,
                    metadata={
                        "name": "carrierInfo",
                        "type": "Element",
                    },
                )
                ref_info: None | ReferenceInfoType134840S = field(
                    default=None,
                    metadata={
                        "name": "refInfo",
                        "type": "Element",
                    },
                )

        @dataclass
        class ServiceFeeInfoGrp:
            """
            :ivar item_number_info: Item number details
            :ivar service_details_grp: Service fee informations
            """

            item_number_info: None | ItemNumberType = field(
                default=None,
                metadata={
                    "name": "itemNumberInfo",
                    "type": "Element",
                    "required": True,
                },
            )
            service_details_grp: list[
                FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp.ServiceDetailsGrp
            ] = field(
                default_factory=list,
                metadata={
                    "name": "serviceDetailsGrp",
                    "type": "Element",
                    "max_occurs": 200,
                },
            )

            @dataclass
            class ServiceDetailsGrp:
                """
                :ivar ref_info: Service reference number
                :ivar service_matched_info_group: Service matched
                    information
                """

                ref_info: None | ReferenceInfoType134840S = field(
                    default=None,
                    metadata={
                        "name": "refInfo",
                        "type": "Element",
                        "required": True,
                    },
                )
                service_matched_info_group: list[
                    FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceFeeInfoGrp.ServiceDetailsGrp.ServiceMatchedInfoGroup
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "serviceMatchedInfoGroup",
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass
                class ServiceMatchedInfoGroup:
                    """
                    :ivar pax_ref_info: Reference on pax number
                    :ivar pricing_info: Pricing oriented service matched
                        information
                    :ivar amount_info: Informative Service amount
                    """

                    pax_ref_info: None | SpecificTravellerType = field(
                        default=None,
                        metadata={
                            "name": "paxRefInfo",
                            "type": "Element",
                            "required": True,
                        },
                    )
                    pricing_info: None | FareInformationType80868S = field(
                        default=None,
                        metadata={
                            "name": "pricingInfo",
                            "type": "Element",
                        },
                    )
                    amount_info: None | MonetaryInformationType193024S = field(
                        default=None,
                        metadata={
                            "name": "amountInfo",
                            "type": "Element",
                        },
                    )

        @dataclass
        class ServiceDetailsGrp:
            """
            :ivar service_option_info: Service sub-code and options
                (exclusion,inclusion, mode pushed,polled)
            :ivar fee_description_grp: Fee description
            """

            service_option_info: None | SpecificDataInformationType = field(
                default=None,
                metadata={
                    "name": "serviceOptionInfo",
                    "type": "Element",
                    "required": True,
                },
            )
            fee_description_grp: (
                None
                | FareMasterPricerTravelBoardSearchReply.ServiceFeesGrp.ServiceDetailsGrp.FeeDescriptionGrp
            ) = field(
                default=None,
                metadata={
                    "name": "feeDescriptionGrp",
                    "type": "Element",
                },
            )

            @dataclass
            class FeeDescriptionGrp:
                """
                :ivar item_number_info: Specification of the item number
                :ivar service_attributes_info: Attributes  (SSR code
                    EMD, RFIC, SSIM)
                :ivar service_description_info: Other service
                    information (service description, ...)
                :ivar commercial_name: Commercial name
                """

                item_number_info: None | ItemNumberType80866S = field(
                    default=None,
                    metadata={
                        "name": "itemNumberInfo",
                        "type": "Element",
                        "required": True,
                    },
                )
                service_attributes_info: None | AttributeType = field(
                    default=None,
                    metadata={
                        "name": "serviceAttributesInfo",
                        "type": "Element",
                    },
                )
                service_description_info: (
                    None | SpecialRequirementsDetailsType
                ) = field(
                    default=None,
                    metadata={
                        "name": "serviceDescriptionInfo",
                        "type": "Element",
                    },
                )
                commercial_name: None | InteractiveFreeTextType = field(
                    default=None,
                    metadata={
                        "name": "commercialName",
                        "type": "Element",
                    },
                )

        @dataclass
        class FreeBagAllowanceGrp:
            """
            :ivar free_bag_allownce_info: Free baggage allownce
                information
            :ivar item_number_info: Item number information
            """

            free_bag_allownce_info: None | ExcessBaggageType = field(
                default=None,
                metadata={
                    "name": "freeBagAllownceInfo",
                    "type": "Element",
                    "required": True,
                },
            )
            item_number_info: None | ItemNumberType166130S = field(
                default=None,
                metadata={
                    "name": "itemNumberInfo",
                    "type": "Element",
                },
            )

    @dataclass
    class MnrGrp:
        mnr: None | MiniRulesType = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        mnr_details: list[
            FareMasterPricerTravelBoardSearchReply.MnrGrp.MnrDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "mnrDetails",
                "type": "Element",
                "max_occurs": 999,
            },
        )

        @dataclass
        class MnrDetails:
            """
            :ivar mnr_ref:
            :ivar date_info:
            :ivar cat_grp: Categories
            """

            mnr_ref: None | ItemNumberType176648S = field(
                default=None,
                metadata={
                    "name": "mnrRef",
                    "type": "Element",
                    "required": True,
                },
            )
            date_info: list[DateAndTimeInformationType182345S] = field(
                default_factory=list,
                metadata={
                    "name": "dateInfo",
                    "type": "Element",
                    "max_occurs": 16,
                },
            )
            cat_grp: list[
                FareMasterPricerTravelBoardSearchReply.MnrGrp.MnrDetails.CatGrp
            ] = field(
                default_factory=list,
                metadata={
                    "name": "catGrp",
                    "type": "Element",
                    "max_occurs": 5,
                },
            )

            @dataclass
            class CatGrp:
                """
                :ivar cat_info: Category information
                :ivar mon_info: Monetary information
                :ivar status_info: Status information
                """

                cat_info: None | CategDescrType = field(
                    default=None,
                    metadata={
                        "name": "catInfo",
                        "type": "Element",
                        "required": True,
                    },
                )
                mon_info: None | MonetaryInformationType174241S = field(
                    default=None,
                    metadata={
                        "name": "monInfo",
                        "type": "Element",
                    },
                )
                status_info: None | StatusType182386S = field(
                    default=None,
                    metadata={
                        "name": "statusInfo",
                        "type": "Element",
                    },
                )
