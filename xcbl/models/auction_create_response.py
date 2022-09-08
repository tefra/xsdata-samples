from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_result import ListOfMvbvariables
from xcbl.models.auction_result_response import AuctionCreateReference
from xcbl.models.remittance_advice import ListOfValues
from xcbl.models.sourcing_create import (
    BaseCurrency,
    ListOfKeyVal,
    ListToInform,
    VisibilityRules,
)
from xcbl.models.sourcing_result import (
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfPrice,
    ListOfReferenceCoded,
    OrderDates,
    PartNumbers,
    Quantity,
    RateOfExchangeDetail,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfIdentifier,
    NameAddress,
    OrderContact,
    OtherContacts,
    PartyId,
    ReceivingContact,
    ShippingContact,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import (
    CorrespondenceLanguage,
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class AuctionCategory:
    auction_category_name: str = field(
        metadata={
            "name": "AuctionCategoryName",
            "type": "Element",
            "required": True,
        }
    )
    auction_category_level: str = field(
        metadata={
            "name": "AuctionCategoryLevel",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateSummary:
    total_number_of_auction_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfAuctionItems",
            "type": "Element",
        }
    )
    total_number_of_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfParticipants",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionItemComponentResponse:
    auction_create_response_detail: "AuctionCreateResponseDetail" = field(
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionSpecifications:
    auction_create_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateName",
            "type": "Element",
        }
    )
    auction_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionType",
            "type": "Element",
        }
    )
    auction_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionStatus",
            "type": "Element",
        }
    )
    partial_bid_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialBidIndicator",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Rule:
    rule_name: str = field(
        metadata={
            "name": "RuleName",
            "type": "Element",
            "required": True,
        }
    )
    rule_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleDescription",
            "type": "Element",
        }
    )
    rule_value: str = field(
        metadata={
            "name": "RuleValue",
            "type": "Element",
            "required": True,
        }
    )
    rule_formula: Optional[str] = field(
        default=None,
        metadata={
            "name": "RuleFormula",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionCreatListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreatePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponsePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseSummary:
    auction_create_summary: AuctionCreateSummary = field(
        metadata={
            "name": "AuctionCreateSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionItemAttribute:
    auction_attribute_name: str = field(
        metadata={
            "name": "AuctionAttributeName",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDescription",
            "type": "Element",
        }
    )
    auction_attribute_data_type_coded: str = field(
        metadata={
            "name": "AuctionAttributeDataTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_data_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDataTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_values: Optional[ListOfValues] = field(
        default=None,
        metadata={
            "name": "ListOfValues",
            "type": "Element",
        }
    )
    auction_attribute_field_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeFieldSize",
            "type": "Element",
        }
    )
    required_indicator: str = field(
        metadata={
            "name": "RequiredIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_attribute_default_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionAttributeDefaultValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionItemDates:
    order_dates: OrderDates = field(
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionPartners:
    party_id: PartyId = field(
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    group_indicator: str = field(
        metadata={
            "name": "GroupIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_key_val: Optional[ListOfKeyVal] = field(
        default=None,
        metadata={
            "name": "ListOfKeyVal",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionPricingDetail:
    open_price: str = field(
        metadata={
            "name": "OpenPrice",
            "type": "Element",
            "required": True,
        }
    )
    reserve_price: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReservePrice",
            "type": "Element",
        }
    )
    bid_increment: Optional[str] = field(
        default=None,
        metadata={
            "name": "BidIncrement",
            "type": "Element",
        }
    )
    list_of_price: Optional[ListOfPrice] = field(
        default=None,
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionValidityDates:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BidCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionCategory:
    auction_category: List[AuctionCategory] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCategory",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionItemComponentResponse:
    auction_item_component_response: List[AuctionItemComponentResponse] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemComponentResponse",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfRules:
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "name": "Rule",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionItemAttribute:
    auction_item_attribute: List[AuctionItemAttribute] = field(
        default_factory=list,
        metadata={
            "name": "AuctionItemAttribute",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionPartners:
    auction_partners: List[AuctionPartners] = field(
        default_factory=list,
        metadata={
            "name": "AuctionPartners",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class RulesProfile:
    bid_rule_coded: str = field(
        metadata={
            "name": "BidRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    bid_rule_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "BidRuleCodedOther",
            "type": "Element",
        }
    )
    mvbtemplate: Optional[str] = field(
        default=None,
        metadata={
            "name": "MVBTemplate",
            "type": "Element",
        }
    )
    win_rule_coded: str = field(
        metadata={
            "name": "WinRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    win_rule_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "WinRuleCodedOther",
            "type": "Element",
        }
    )
    visibility_rules: Optional[VisibilityRules] = field(
        default=None,
        metadata={
            "name": "VisibilityRules",
            "type": "Element",
        }
    )
    list_of_rules: Optional[ListOfRules] = field(
        default=None,
        metadata={
            "name": "ListOfRules",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ValidBidCurrency:
    bid_currency: BidCurrency = field(
        metadata={
            "name": "BidCurrency",
            "type": "Element",
            "required": True,
        }
    )
    rate_of_exchange_detail: Optional[RateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionItem:
    auction_item_id: str = field(
        metadata={
            "name": "AuctionItemID",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_name: str = field(
        metadata={
            "name": "AuctionItemName",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemDescription",
            "type": "Element",
        }
    )
    list_of_auction_category: ListOfAuctionCategory = field(
        metadata={
            "name": "ListOfAuctionCategory",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_item_attribute: Optional[ListOfAuctionItemAttribute] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemAttribute",
            "type": "Element",
        }
    )
    auction_item_hierarchy_level: str = field(
        metadata={
            "name": "AuctionItemHierarchyLevel",
            "type": "Element",
            "required": True,
        }
    )
    auction_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionLineItemNum",
            "type": "Element",
        }
    )
    auction_quantity: AuctionQuantity = field(
        metadata={
            "name": "AuctionQuantity",
            "type": "Element",
            "required": True,
        }
    )
    partial_bid_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialBidIndicator",
            "type": "Element",
        }
    )
    part_numbers: Optional[PartNumbers] = field(
        default=None,
        metadata={
            "name": "PartNumbers",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionParticipants:
    initiating_party: InitiatingParty = field(
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
            "required": True,
        }
    )
    community_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CommunityID",
            "type": "Element",
        }
    )
    list_to_inform: Optional[ListToInform] = field(
        default=None,
        metadata={
            "name": "ListToInform",
            "type": "Element",
        }
    )
    list_of_auction_partners: ListOfAuctionPartners = field(
        metadata={
            "name": "ListOfAuctionPartners",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfValidBidCurrency:
    valid_bid_currency: List[ValidBidCurrency] = field(
        default_factory=list,
        metadata={
            "name": "ValidBidCurrency",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AuctionCurrency:
    base_currency: BaseCurrency = field(
        metadata={
            "name": "BaseCurrency",
            "type": "Element",
            "required": True,
        }
    )
    list_of_valid_bid_currency: Optional[ListOfValidBidCurrency] = field(
        default=None,
        metadata={
            "name": "ListOfValidBidCurrency",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AuctionDetail:
    auction_item: AuctionItem = field(
        metadata={
            "name": "AuctionItem",
            "type": "Element",
            "required": True,
        }
    )
    list_of_mvbvariables: Optional[ListOfMvbvariables] = field(
        default=None,
        metadata={
            "name": "ListOfMVBVariables",
            "type": "Element",
        }
    )
    auction_pricing_detail: Optional[AuctionPricingDetail] = field(
        default=None,
        metadata={
            "name": "AuctionPricingDetail",
            "type": "Element",
        }
    )
    auction_item_dates: Optional[AuctionItemDates] = field(
        default=None,
        metadata={
            "name": "AuctionItemDates",
            "type": "Element",
        }
    )
    auction_delivery_detail: Optional[AuctionDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "AuctionDeliveryDetail",
            "type": "Element",
        }
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        }
    )
    component_auction_indicator: str = field(
        metadata={
            "name": "ComponentAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateHeader:
    auction_create_purpose: AuctionCreatePurpose = field(
        metadata={
            "name": "AuctionCreatePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_issue_date: str = field(
        metadata={
            "name": "AuctionCreateIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_id: str = field(
        metadata={
            "name": "AuctionCreateID",
            "type": "Element",
            "required": True,
        }
    )
    foward_auction_indicator: str = field(
        metadata={
            "name": "FowardAuctionIndicator",
            "type": "Element",
            "required": True,
        }
    )
    auction_validity_dates: AuctionValidityDates = field(
        metadata={
            "name": "AuctionValidityDates",
            "type": "Element",
            "required": True,
        }
    )
    decision_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DecisionDate",
            "type": "Element",
        }
    )
    rules_profile: RulesProfile = field(
        metadata={
            "name": "RulesProfile",
            "type": "Element",
            "required": True,
        }
    )
    auction_currency: Optional[AuctionCurrency] = field(
        default=None,
        metadata={
            "name": "AuctionCurrency",
            "type": "Element",
        }
    )
    auction_participants: AuctionParticipants = field(
        metadata={
            "name": "AuctionParticipants",
            "type": "Element",
            "required": True,
        }
    )
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateGeneralNotes",
            "type": "Element",
        }
    )
    auction_creat_list_of_attachment: Optional[AuctionCreatListOfAttachment] = field(
        default=None,
        metadata={
            "name": "AuctionCreatListOfAttachment",
            "type": "Element",
        }
    )
    auction_specifications: Optional[AuctionSpecifications] = field(
        default=None,
        metadata={
            "name": "AuctionSpecifications",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedAuctionCreateDetail:
    auction_detail: AuctionDetail = field(
        metadata={
            "name": "AuctionDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseDetail:
    auction_item_id: str = field(
        metadata={
            "name": "AuctionItemID",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_name: str = field(
        metadata={
            "name": "AuctionItemName",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemDescription",
            "type": "Element",
        }
    )
    auction_item_hierarchy_level: str = field(
        metadata={
            "name": "AuctionItemHierarchyLevel",
            "type": "Element",
            "required": True,
        }
    )
    auction_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionLineItemNum",
            "type": "Element",
        }
    )
    auction_item_response_coded: str = field(
        metadata={
            "name": "AuctionItemResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_item_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionItemResponseCodedOther",
            "type": "Element",
        }
    )
    changed_auction_create_detail: Optional[ChangedAuctionCreateDetail] = field(
        default=None,
        metadata={
            "name": "ChangedAuctionCreateDetail",
            "type": "Element",
        }
    )
    list_of_auction_item_component_response: Optional[ListOfAuctionItemComponentResponse] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionItemComponentResponse",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ChangedAuctionCreateHeader:
    auction_create_header: AuctionCreateHeader = field(
        metadata={
            "name": "AuctionCreateHeader",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponseHeader:
    auction_create_response_purpose: AuctionCreateResponsePurpose = field(
        metadata={
            "name": "AuctionCreateResponsePurpose",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_issue_date: str = field(
        metadata={
            "name": "AuctionCreateResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_id: str = field(
        metadata={
            "name": "AuctionCreateResponseID",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_reference: AuctionCreateReference = field(
        metadata={
            "name": "AuctionCreateReference",
            "type": "Element",
            "required": True,
        }
    )
    auction_response_coded: str = field(
        metadata={
            "name": "AuctionResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    auction_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionResponseCodedOther",
            "type": "Element",
        }
    )
    changed_auction_create_header: Optional[ChangedAuctionCreateHeader] = field(
        default=None,
        metadata={
            "name": "ChangedAuctionCreateHeader",
            "type": "Element",
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    auction_create_response_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuctionCreateResponseNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAuctionCreateResponseDetail:
    auction_create_response_detail: List[AuctionCreateResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "AuctionCreateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class AuctionCreateResponse:
    auction_create_response_header: AuctionCreateResponseHeader = field(
        metadata={
            "name": "AuctionCreateResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_auction_create_response_detail: Optional[ListOfAuctionCreateResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfAuctionCreateResponseDetail",
            "type": "Element",
        }
    )
    auction_create_response_summary: AuctionCreateResponseSummary = field(
        metadata={
            "name": "AuctionCreateResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
