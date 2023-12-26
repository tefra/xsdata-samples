from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_code_1 import AccountCode1
from travelport.models.brand_modifiers import BrandModifiers
from travelport.models.contract_code import ContractCode
from travelport.models.discount_card_1 import DiscountCard1
from travelport.models.exempt_taxes import ExemptTaxes
from travelport.models.fare_rule_category import FareRuleCategory
from travelport.models.manual_fare_adjustment import ManualFareAdjustment
from travelport.models.multi_gdssearch_indicator import MultiGdssearchIndicator
from travelport.models.penalty_fare_information import PenaltyFareInformation
from travelport.models.permitted_cabins import PermittedCabins
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.preferred_cabins import PreferredCabins
from travelport.models.promo_code import PromoCode
from travelport.models.type_eticketability import TypeEticketability
from travelport.models.type_fares_indicator import TypeFaresIndicator
from travelport.models.type_inventory_request import TypeInventoryRequest

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingModifiers:
    """
    Controls and switches for a Air Search request that contains Pricing
    Information.

    Parameters
    ----------
    prohibited_rule_categories
    account_codes
    permitted_cabins
    contract_codes
    exempt_taxes
    penalty_fare_information
        Request Fares with specific Penalty Information.
    discount_card
        Discount request for rail.
    promo_codes
    manual_fare_adjustment
        Represents increment/discount applied manually by agent.
    point_of_sale
        User can use this node to send a specific PCC to access fares
        allowed only for that PCC. This node gives the capability for fare
        redistribution at stored fare level. As multiple UAPI
        AirPricingInfos (all having same AirPricingInfoGroup) can converge
        to a single stored fare, UAPI will map PoinOfSale information from
        the first available one from each group
    brand_modifiers
        Used to specify the level of branding requested.
    multi_gdssearch_indicator
    preferred_cabins
    prohibit_min_stay_fares
    prohibit_max_stay_fares
    currency_type
    prohibit_advance_purchase_fares
    prohibit_non_refundable_fares
    prohibit_restricted_fares
    fares_indicator
        Indicates whether only public fares should be returned or specific
        type of private fares
    filed_currency
        Currency in which Fares/Prices will be filed if supported by the
        supplier else approximated to.
    plating_carrier
        The Plating Carrier for this journey.
    override_carrier
        The Plating Carrier for this journey.
    eticketability
        Request a search based on whether only E-ticketable fares are
        required.
    account_code_fares_only
        Indicates whether or not the private fares returned should be
        restricted to only those specific to the input account code and
        contract code.
    key
    prohibit_non_exchangeable_fares
    force_segment_select
        This indicator allows agent to force segment select option in host
        while selecting all air segments to store price on a PNR. This is
        relevent only when agent selects all air segmnets to price. if agent
        selects specific segments to price then this attribute will be
        ignored by the system. This is currently used by Worldspan only.
    inventory_request_type
        This allows user to make request for a particular source of
        inventory for pricing modifier purposes.
    one_way_shop
        Via this attribute one way shop can be requested. Applicable
        provider is 1G
    prohibit_unbundled_fare_types
        A "True" value wiill remove fares with EOU and ERU fare types from
        consideration. A "False" value is the same as no value.  Default is
        no value. Applicable providers:  1P/1G/1V
    return_services
        When set to false, ATPCO filed Optional Services will not be
        returned. Default is false. Provider: 1G, 1V, 1P
    channel_id
        A Channel ID is 2 to 4 alpha-numeric characters used to activate the
        Search Control Console filter for a specific group of travelers
        being served by the agency credential.
    return_fare_attributes
        Returns attributes that are associated to a fare
    sell_check
        Checks if the segment is bookable before pricing
    return_failed_segments
        If "true", returns failed segments information.
    sell_city
        City Code identifying where the ticket is to be sold.
    ticketing_city
        City Code identifying where the ticket will be issued.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    prohibited_rule_categories: None | AirPricingModifiers.ProhibitedRuleCategories = field(
        default=None,
        metadata={
            "name": "ProhibitedRuleCategories",
            "type": "Element",
        },
    )
    account_codes: None | AirPricingModifiers.AccountCodes = field(
        default=None,
        metadata={
            "name": "AccountCodes",
            "type": "Element",
        },
    )
    permitted_cabins: None | PermittedCabins = field(
        default=None,
        metadata={
            "name": "PermittedCabins",
            "type": "Element",
        },
    )
    contract_codes: None | AirPricingModifiers.ContractCodes = field(
        default=None,
        metadata={
            "name": "ContractCodes",
            "type": "Element",
        },
    )
    exempt_taxes: None | ExemptTaxes = field(
        default=None,
        metadata={
            "name": "ExemptTaxes",
            "type": "Element",
        },
    )
    penalty_fare_information: None | PenaltyFareInformation = field(
        default=None,
        metadata={
            "name": "PenaltyFareInformation",
            "type": "Element",
        },
    )
    discount_card: list[DiscountCard1] = field(
        default_factory=list,
        metadata={
            "name": "DiscountCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 9,
        },
    )
    promo_codes: None | AirPricingModifiers.PromoCodes = field(
        default=None,
        metadata={
            "name": "PromoCodes",
            "type": "Element",
        },
    )
    manual_fare_adjustment: list[ManualFareAdjustment] = field(
        default_factory=list,
        metadata={
            "name": "ManualFareAdjustment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    point_of_sale: None | PointOfSale1 = field(
        default=None,
        metadata={
            "name": "PointOfSale",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    brand_modifiers: None | BrandModifiers = field(
        default=None,
        metadata={
            "name": "BrandModifiers",
            "type": "Element",
        },
    )
    multi_gdssearch_indicator: list[MultiGdssearchIndicator] = field(
        default_factory=list,
        metadata={
            "name": "MultiGDSSearchIndicator",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    preferred_cabins: list[PreferredCabins] = field(
        default_factory=list,
        metadata={
            "name": "PreferredCabins",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    prohibit_min_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMinStayFares",
            "type": "Attribute",
        },
    )
    prohibit_max_stay_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitMaxStayFares",
            "type": "Attribute",
        },
    )
    currency_type: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyType",
            "type": "Attribute",
            "length": 3,
        },
    )
    prohibit_advance_purchase_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitAdvancePurchaseFares",
            "type": "Attribute",
        },
    )
    prohibit_non_refundable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonRefundableFares",
            "type": "Attribute",
        },
    )
    prohibit_restricted_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitRestrictedFares",
            "type": "Attribute",
        },
    )
    fares_indicator: None | TypeFaresIndicator = field(
        default=None,
        metadata={
            "name": "FaresIndicator",
            "type": "Attribute",
        },
    )
    filed_currency: None | str = field(
        default=None,
        metadata={
            "name": "FiledCurrency",
            "type": "Attribute",
            "length": 3,
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    override_carrier: None | str = field(
        default=None,
        metadata={
            "name": "OverrideCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    eticketability: None | TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        },
    )
    account_code_fares_only: None | bool = field(
        default=None,
        metadata={
            "name": "AccountCodeFaresOnly",
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
    prohibit_non_exchangeable_fares: bool = field(
        default=False,
        metadata={
            "name": "ProhibitNonExchangeableFares",
            "type": "Attribute",
        },
    )
    force_segment_select: bool = field(
        default=False,
        metadata={
            "name": "ForceSegmentSelect",
            "type": "Attribute",
        },
    )
    inventory_request_type: None | TypeInventoryRequest = field(
        default=None,
        metadata={
            "name": "InventoryRequestType",
            "type": "Attribute",
        },
    )
    one_way_shop: bool = field(
        default=False,
        metadata={
            "name": "OneWayShop",
            "type": "Attribute",
        },
    )
    prohibit_unbundled_fare_types: None | bool = field(
        default=None,
        metadata={
            "name": "ProhibitUnbundledFareTypes",
            "type": "Attribute",
        },
    )
    return_services: bool = field(
        default=False,
        metadata={
            "name": "ReturnServices",
            "type": "Attribute",
        },
    )
    channel_id: None | str = field(
        default=None,
        metadata={
            "name": "ChannelId",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 4,
        },
    )
    return_fare_attributes: bool = field(
        default=False,
        metadata={
            "name": "ReturnFareAttributes",
            "type": "Attribute",
        },
    )
    sell_check: bool = field(
        default=False,
        metadata={
            "name": "SellCheck",
            "type": "Attribute",
        },
    )
    return_failed_segments: bool = field(
        default=False,
        metadata={
            "name": "ReturnFailedSegments",
            "type": "Attribute",
        },
    )
    sell_city: None | str = field(
        default=None,
        metadata={
            "name": "SellCity",
            "type": "Attribute",
            "length": 3,
        },
    )
    ticketing_city: None | str = field(
        default=None,
        metadata={
            "name": "TicketingCity",
            "type": "Attribute",
            "length": 3,
        },
    )

    @dataclass
    class ProhibitedRuleCategories:
        fare_rule_category: list[FareRuleCategory] = field(
            default_factory=list,
            metadata={
                "name": "FareRuleCategory",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class AccountCodes:
        """
        Parameters
        ----------
        account_code
            Used to get negotiated pricing. Provider:ACH.
        """

        account_code: list[AccountCode1] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class ContractCodes:
        contract_code: list[ContractCode] = field(
            default_factory=list,
            metadata={
                "name": "ContractCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class PromoCodes:
        promo_code: list[PromoCode] = field(
            default_factory=list,
            metadata={
                "name": "PromoCode",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
