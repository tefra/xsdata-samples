from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.additional_info import AdditionalInfo
from travelport.models.branding_info import BrandingInfo
from travelport.models.bundled_services import BundledServices
from travelport.models.emd import Emd
from travelport.models.fee_application import FeeApplication
from travelport.models.fee_info import FeeInfo
from travelport.models.price_range import PriceRange
from travelport.models.remark_1 import Remark1
from travelport.models.service_data_1 import ServiceData1
from travelport.models.service_info_1 import ServiceInfo1
from travelport.models.tax_info import TaxInfo
from travelport.models.text import Text
from travelport.models.title import Title
from travelport.models.tour_code import TourCode
from travelport.models.type_assess_indicator import TypeAssessIndicator
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_purchase_window import TypePurchaseWindow

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class OptionalService1:
    """
    Parameters
    ----------
    service_data
    service_info
    remark
        Information regarding any specific for this service.
    tax_info
    fee_info
    emd
    bundled_services
    additional_info
    fee_application
        Specifies how the Optional Service fee is to be applied.  The
        choices are Per One Way, Per Round Trip, Per Item (Per Piece), Per
        Travel, Per Ticket, Per 1 Kilo, Per 5 Kilos.  Provider: 1G, 1V, 1P
    text
    price_range
    tour_code
    branding_info
    title
    provider_code
    supplier_code
    optional_services_rule_ref
        UniqueID to associate a rule to the Optional Service
    type_value
        Specify the type of service offered (e.g. seats, baggage, etc.)
    confirmation
        Confirmation number provided by the supplier
    secondary_type
        The secondary option code type required for certain options
    purchase_window
        Describes when the Service is available for confirmation or purchase
        (e.g. Booking Only, Check-in Only, Anytime, etc.)
    priority
        Numeric value that represents the priority order of the Service
    available
        Boolean to describe whether the Service is available for sale or not
    entitled
        Boolean to describe whether the passenger is entitled for the
        service without charge or not
    per_traveler
        Boolean to describe whether the Amount on the Service is charged per
        traveler.
    create_date
        Timestamp when this service/offer got created.
    payment_ref
        Reference to a payment for merchandising services.
    service_status
        Specify the service status (e.g. active, canceled, etc.)
    quantity
        The number of units availed for each optional service (e.g. 2
        baggage availed will be specified as 2 in quantity for optional
        service BAGGAGE)
    sequence_number
        The sequence number associated with the OptionalService
    service_sub_code
        The service subcode associated with the OptionalService
    ssrcode
        The SSR Code associated with the OptionalService
    issuance_reason
        A one-letter code specifying the reason for issuance of the
        OptionalService
    provider_defined_type
        Original Type as sent by the provider
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    key
    assess_indicator
        Indicates whether price is assessed by mileage or currency or both
    mileage
        Indicates mileage fee/amount
    applicable_fflevel
        Numerical value of the loyalty card level for which this service is
        available.
    private
        Describes if service is private or not.
    ssrfree_text
        Certain SSR types sent in OptionalService SSRCode require a free
        text message. For example, PETC Pet in Cabin.
    is_pricing_approximate
        When set to True indicates that the pricing returned is approximate.
        Supported providers are MCH/ACH
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    chargeable
        Indicates if the optional service is not offered, is available for a
        charge, or is included in the brand
    inclusive_of_tax
        Identifies if the service was filed with a fee that is inclusive of
        tax.
    interline_settlement_allowed
        Identifies if the interline settlement is allowed in service .
    geography_specification
        Sector, Portion, Journey.
    excess_weight_rate
        The cost of the bag per unit weight.
    source
        The Source of the optional service. The source can be ACH, MCE, or
        MCH.
    viewable_only
        Describes if the OptionalService is viewable only or not. If
        viewable only then the service cannot be sold.
    display_text
        Title of the Optional Service.  Provider: ACH
    weight_in_excess
        The excess weight of a bag. Providers: 1G, 1V, 1P
    total_weight
        The total weight of a bag. Providers: 1G, 1V, 1P
    baggage_unit_price
        The per unit price of baggage. Providers: 1G, 1V, 1P
    first_piece
        Indicates the minimum occurrence of excess baggage.Provider: 1G, 1V,
        1P.
    last_piece
        Indicates the maximum occurrence of excess baggage. Provider: 1G,
        1V, 1P.
    restricted
        When set to “true”, the Optional Service is restricted by an
        embargo. Provider: 1G, 1V, 1P
    is_reprice_required
        When set to “true”, the Optional Service must be re-priced.
        Provider: 1G, 1V, 1P
    booked_quantity
        Indicates the Optional Service quantity already booked. Provider:
        1G, 1V, 1P
    group
        Associates Optional Services with the same ServiceSub Code, Air
        Segment, Passenger, and EMD Associated Item. Provider:1G, 1V, 1P
    pseudo_city_code
        The PCC or SID that booked the Optional Service.
    tag
        Optional service group name.
    display_order
        Optional service group display order.
    """

    class Meta:
        name = "OptionalService"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    service_data: list[ServiceData1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    service_info: None | ServiceInfo1 = field(
        default=None,
        metadata={
            "name": "ServiceInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    remark: list[Remark1] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    emd: None | Emd = field(
        default=None,
        metadata={
            "name": "EMD",
            "type": "Element",
        },
    )
    bundled_services: None | BundledServices = field(
        default=None,
        metadata={
            "name": "BundledServices",
            "type": "Element",
        },
    )
    additional_info: list[AdditionalInfo] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInfo",
            "type": "Element",
            "max_occurs": 16,
        },
    )
    fee_application: None | FeeApplication = field(
        default=None,
        metadata={
            "name": "FeeApplication",
            "type": "Element",
        },
    )
    text: list[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 4,
        },
    )
    price_range: list[PriceRange] = field(
        default_factory=list,
        metadata={
            "name": "PriceRange",
            "type": "Element",
            "max_occurs": 5,
        },
    )
    tour_code: None | TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        },
    )
    branding_info: None | BrandingInfo = field(
        default=None,
        metadata={
            "name": "BrandingInfo",
            "type": "Element",
        },
    )
    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    optional_services_rule_ref: None | str = field(
        default=None,
        metadata={
            "name": "OptionalServicesRuleRef",
            "type": "Attribute",
        },
    )
    type_value: str = field(
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        }
    )
    confirmation: None | str = field(
        default=None,
        metadata={
            "name": "Confirmation",
            "type": "Attribute",
        },
    )
    secondary_type: None | str = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
        },
    )
    purchase_window: None | TypePurchaseWindow = field(
        default=None,
        metadata={
            "name": "PurchaseWindow",
            "type": "Attribute",
        },
    )
    priority: None | int = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Attribute",
        },
    )
    available: None | bool = field(
        default=None,
        metadata={
            "name": "Available",
            "type": "Attribute",
        },
    )
    entitled: None | bool = field(
        default=None,
        metadata={
            "name": "Entitled",
            "type": "Attribute",
        },
    )
    per_traveler: bool = field(
        default=True,
        metadata={
            "name": "PerTraveler",
            "type": "Attribute",
        },
    )
    create_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        },
    )
    payment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        },
    )
    service_status: None | str = field(
        default=None,
        metadata={
            "name": "ServiceStatus",
            "type": "Attribute",
        },
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        },
    )
    sequence_number: None | int = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Attribute",
        },
    )
    service_sub_code: None | str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    ssrcode: None | str = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        },
    )
    issuance_reason: None | str = field(
        default=None,
        metadata={
            "name": "IssuanceReason",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1,
        },
    )
    provider_defined_type: None | str = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        },
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        },
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        },
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        },
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        },
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        },
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        },
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        },
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        },
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    assess_indicator: None | TypeAssessIndicator = field(
        default=None,
        metadata={
            "name": "AssessIndicator",
            "type": "Attribute",
        },
    )
    mileage: None | int = field(
        default=None,
        metadata={
            "name": "Mileage",
            "type": "Attribute",
        },
    )
    applicable_fflevel: None | int = field(
        default=None,
        metadata={
            "name": "ApplicableFFLevel",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 9,
        },
    )
    private: None | bool = field(
        default=None,
        metadata={
            "name": "Private",
            "type": "Attribute",
        },
    )
    ssrfree_text: None | str = field(
        default=None,
        metadata={
            "name": "SSRFreeText",
            "type": "Attribute",
        },
    )
    is_pricing_approximate: None | bool = field(
        default=None,
        metadata={
            "name": "IsPricingApproximate",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
    chargeable: None | str = field(
        default=None,
        metadata={
            "name": "Chargeable",
            "type": "Attribute",
        },
    )
    inclusive_of_tax: None | bool = field(
        default=None,
        metadata={
            "name": "InclusiveOfTax",
            "type": "Attribute",
        },
    )
    interline_settlement_allowed: None | bool = field(
        default=None,
        metadata={
            "name": "InterlineSettlementAllowed",
            "type": "Attribute",
        },
    )
    geography_specification: None | str = field(
        default=None,
        metadata={
            "name": "GeographySpecification",
            "type": "Attribute",
        },
    )
    excess_weight_rate: None | str = field(
        default=None,
        metadata={
            "name": "ExcessWeightRate",
            "type": "Attribute",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
        },
    )
    viewable_only: None | bool = field(
        default=None,
        metadata={
            "name": "ViewableOnly",
            "type": "Attribute",
        },
    )
    display_text: None | str = field(
        default=None,
        metadata={
            "name": "DisplayText",
            "type": "Attribute",
        },
    )
    weight_in_excess: None | str = field(
        default=None,
        metadata={
            "name": "WeightInExcess",
            "type": "Attribute",
        },
    )
    total_weight: None | str = field(
        default=None,
        metadata={
            "name": "TotalWeight",
            "type": "Attribute",
        },
    )
    baggage_unit_price: None | str = field(
        default=None,
        metadata={
            "name": "BaggageUnitPrice",
            "type": "Attribute",
        },
    )
    first_piece: None | int = field(
        default=None,
        metadata={
            "name": "FirstPiece",
            "type": "Attribute",
        },
    )
    last_piece: None | int = field(
        default=None,
        metadata={
            "name": "LastPiece",
            "type": "Attribute",
        },
    )
    restricted: bool = field(
        default=False,
        metadata={
            "name": "Restricted",
            "type": "Attribute",
        },
    )
    is_reprice_required: bool = field(
        default=False,
        metadata={
            "name": "IsRepriceRequired",
            "type": "Attribute",
        },
    )
    booked_quantity: None | str = field(
        default=None,
        metadata={
            "name": "BookedQuantity",
            "type": "Attribute",
        },
    )
    group: None | str = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    tag: None | str = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
    display_order: None | int = field(
        default=None,
        metadata={
            "name": "DisplayOrder",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        },
    )
