from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    BaseCurrency,
    CorrespondenceLanguage,
    Currency,
    DeliveryDetail,
    InitiatingParty,
    Language,
    ListOfAttachment,
    ListOfIdentifier,
    ListOfKeyVal,
    ListOfReferenceCoded,
    ListToInform,
    NameAddress,
    OrderContact,
    OtherContacts,
    PartNumbers,
    PartyId,
    Purpose,
    Quantity,
    RateOfExchangeDetail,
    ReceivingContact,
    ShippingContact,
    UnitPrice,
    ValidityDates,
)
from xcbl.models.order_request import ListOfStructuredNote
from xcbl.models.sourcing_create_response import SourcingCreateSummary


@dataclass
class AggregationType:
    aggregation_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AggregationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    aggregation_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AggregationTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class AttributeName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        }
    )


@dataclass
class Bundle:
    bundle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BundleName",
            "type": "Element",
            "required": True,
        }
    )
    line_item_number: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LineItemNumber",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class DropDownMenuValue:
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    credit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Credit",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingItemComponent:
    sourcing_create_detail: Optional["SourcingCreateDetail"] = field(
        default=None,
        metadata={
            "name": "SourcingCreateDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class VisibilityOfBuyer:
    buyer_contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerContactName",
            "type": "Element",
        }
    )
    contact_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactPhoneNumber",
            "type": "Element",
        }
    )
    contact_mobile: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactMobile",
            "type": "Element",
        }
    )
    contact_fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactFaxNumber",
            "type": "Element",
        }
    )
    contact_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactEmail",
            "type": "Element",
        }
    )
    alternative_buyer_contact_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeBuyerContactName",
            "type": "Element",
        }
    )
    alternative_contact_phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeContactPhoneNumber",
            "type": "Element",
        }
    )
    alternative_contact_mobile: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeContactMobile",
            "type": "Element",
        }
    )
    alternative_contact_fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeContactFaxNumber",
            "type": "Element",
        }
    )
    alternative_contact_email: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeContactEmail",
            "type": "Element",
        }
    )


@dataclass
class FormulaAttribute:
    attribute_name: Optional[AttributeName] = field(
        default=None,
        metadata={
            "name": "AttributeName",
            "type": "Element",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        }
    )


@dataclass
class ListOfBundle:
    bundle: List[Bundle] = field(
        default_factory=list,
        metadata={
            "name": "Bundle",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfDropDownMenuValue:
    drop_down_menu_value: List[DropDownMenuValue] = field(
        default_factory=list,
        metadata={
            "name": "DropDownMenuValue",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfSourcingItemComponent:
    sourcing_item_component: List[SourcingItemComponent] = field(
        default_factory=list,
        metadata={
            "name": "SourcingItemComponent",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Project:
    project_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProjectName",
            "type": "Element",
            "required": True,
        }
    )
    revision_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionNumber",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )


@dataclass
class QuoteCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingCreateListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingCreatePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingPartners:
    party_id: Optional[PartyId] = field(
        default=None,
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
    group_indicator: Optional[str] = field(
        default=None,
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


@dataclass
class SourcingQuantity:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingValidityDates:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SourcingVisibilityRules:
    visibility_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityIndicator",
            "type": "Element",
        }
    )
    visibility_of_comments: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfComments",
            "type": "Element",
        }
    )
    visibility_of_amounts: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfAmounts",
            "type": "Element",
        }
    )
    visibility_of_quantities: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfQuantities",
            "type": "Element",
        }
    )
    visibility_of_participants: Optional[str] = field(
        default=None,
        metadata={
            "name": "VisibilityOfParticipants",
            "type": "Element",
        }
    )
    visibility_of_buyer: Optional[VisibilityOfBuyer] = field(
        default=None,
        metadata={
            "name": "VisibilityOfBuyer",
            "type": "Element",
        }
    )


@dataclass
class AdditionalAttribute:
    operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "required": True,
        }
    )
    formula_attribute: Optional[FormulaAttribute] = field(
        default=None,
        metadata={
            "name": "FormulaAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfSourcingPartners:
    sourcing_partners: List[SourcingPartners] = field(
        default_factory=list,
        metadata={
            "name": "SourcingPartners",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingAttribute:
    sourcing_attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeName",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeDescription",
            "type": "Element",
        }
    )
    sourcing_attribute_data_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeDataTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_data_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeDataTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_drop_down_menu_value: Optional[ListOfDropDownMenuValue] = field(
        default=None,
        metadata={
            "name": "ListOfDropDownMenuValue",
            "type": "Element",
        }
    )
    sourcing_attribute_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeType",
            "type": "Element",
        }
    )
    required_to_respond: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredToRespond",
            "type": "Element",
            "required": True,
        }
    )
    supplier_view: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierView",
            "type": "Element",
        }
    )
    weighting: Optional[str] = field(
        default=None,
        metadata={
            "name": "Weighting",
            "type": "Element",
        }
    )
    preferred_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "PreferredUOM",
            "type": "Element",
        }
    )
    attribute_characteristic: Optional[str] = field(
        default=None,
        metadata={
            "name": "AttributeCharacteristic",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_field_size: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeFieldSize",
            "type": "Element",
        }
    )


@dataclass
class SourcingRulesProfile:
    quote_win_rule_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteWinRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    quote_win_rule_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteWinRuleCodedOther",
            "type": "Element",
        }
    )
    sourcing_visibility_rules: Optional[SourcingVisibilityRules] = field(
        default=None,
        metadata={
            "name": "SourcingVisibilityRules",
            "type": "Element",
        }
    )


@dataclass
class ValidQuoteCurrency:
    quote_currency: Optional[QuoteCurrency] = field(
        default=None,
        metadata={
            "name": "QuoteCurrency",
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


@dataclass
class Formula:
    formula_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FormulaName",
            "type": "Element",
            "required": True,
        }
    )
    formula_attribute: Optional[FormulaAttribute] = field(
        default=None,
        metadata={
            "name": "FormulaAttribute",
            "type": "Element",
            "required": True,
        }
    )
    additional_attribute: List[AdditionalAttribute] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAttribute",
            "type": "Element",
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "AggregationType",
            "type": "Element",
        }
    )


@dataclass
class ListOfValidQuoteCurrency:
    valid_quote_currency: List[ValidQuoteCurrency] = field(
        default_factory=list,
        metadata={
            "name": "ValidQuoteCurrency",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingParticipants:
    initiating_party: Optional[InitiatingParty] = field(
        default=None,
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
    list_of_sourcing_partners: Optional[ListOfSourcingPartners] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingPartners",
            "type": "Element",
        }
    )


@dataclass
class SourcingSpecifications:
    sourcing_create_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateName",
            "type": "Element",
        }
    )
    sourcing_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingType",
            "type": "Element",
        }
    )
    sourcing_status: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingStatus",
            "type": "Element",
        }
    )
    partial_quote_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialQuoteIndicator",
            "type": "Element",
        }
    )
    all_or_nothing: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllOrNothing",
            "type": "Element",
        }
    )
    sourcing_attribute: List[SourcingAttribute] = field(
        default_factory=list,
        metadata={
            "name": "SourcingAttribute",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingCurrency:
    base_currency: Optional[BaseCurrency] = field(
        default=None,
        metadata={
            "name": "BaseCurrency",
            "type": "Element",
            "required": True,
        }
    )
    list_of_valid_quote_currency: Optional[ListOfValidQuoteCurrency] = field(
        default=None,
        metadata={
            "name": "ListOfValidQuoteCurrency",
            "type": "Element",
        }
    )


@dataclass
class SourcingItem:
    sourcing_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemName",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingItemDescription",
            "type": "Element",
        }
    )
    item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemNumber",
            "type": "Element",
        }
    )
    parent_item_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParentItemIdentifier",
            "type": "Element",
        }
    )
    bundle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "BundleName",
            "type": "Element",
        }
    )
    sourcing_attribute: List[SourcingAttribute] = field(
        default_factory=list,
        metadata={
            "name": "SourcingAttribute",
            "type": "Element",
        }
    )
    formula: List[Formula] = field(
        default_factory=list,
        metadata={
            "name": "Formula",
            "type": "Element",
        }
    )
    sourcing_quantity: Optional[SourcingQuantity] = field(
        default=None,
        metadata={
            "name": "SourcingQuantity",
            "type": "Element",
        }
    )
    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        }
    )
    unit_price: Optional[UnitPrice] = field(
        default=None,
        metadata={
            "name": "UnitPrice",
            "type": "Element",
        }
    )
    partial_quote_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialQuoteIndicator",
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


@dataclass
class SourcingCreateDetail:
    sourcing_item: Optional[SourcingItem] = field(
        default=None,
        metadata={
            "name": "SourcingItem",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_delivery_detail: Optional[SourcingDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "SourcingDeliveryDetail",
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
    component_sourcing_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComponentSourcingIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_item_component: Optional[ListOfSourcingItemComponent] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingItemComponent",
            "type": "Element",
        }
    )


@dataclass
class SourcingCreateHeader:
    sourcing_create_purpose: Optional[SourcingCreatePurpose] = field(
        default=None,
        metadata={
            "name": "SourcingCreatePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateID",
            "type": "Element",
            "required": True,
        }
    )
    project: Optional[Project] = field(
        default=None,
        metadata={
            "name": "Project",
            "type": "Element",
        }
    )
    requisition_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequisitionNumber",
            "type": "Element",
        }
    )
    sourcing_validity_dates: Optional[SourcingValidityDates] = field(
        default=None,
        metadata={
            "name": "SourcingValidityDates",
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
    sourcing_rules_profile: Optional[SourcingRulesProfile] = field(
        default=None,
        metadata={
            "name": "SourcingRulesProfile",
            "type": "Element",
        }
    )
    sourcing_currency: Optional[SourcingCurrency] = field(
        default=None,
        metadata={
            "name": "SourcingCurrency",
            "type": "Element",
        }
    )
    list_of_bundle: Optional[ListOfBundle] = field(
        default=None,
        metadata={
            "name": "ListOfBundle",
            "type": "Element",
        }
    )
    sourcing_participants: Optional[SourcingParticipants] = field(
        default=None,
        metadata={
            "name": "SourcingParticipants",
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
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourcingCreateGeneralNotes",
            "type": "Element",
        }
    )
    sourcing_create_list_of_attachment: Optional[SourcingCreateListOfAttachment] = field(
        default=None,
        metadata={
            "name": "SourcingCreateListOfAttachment",
            "type": "Element",
        }
    )
    sourcing_specifications: Optional[SourcingSpecifications] = field(
        default=None,
        metadata={
            "name": "SourcingSpecifications",
            "type": "Element",
        }
    )


@dataclass
class ListOfSourcingCreateDetail:
    sourcing_create_detail: List[SourcingCreateDetail] = field(
        default_factory=list,
        metadata={
            "name": "SourcingCreateDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class SourcingCreate:
    sourcing_create_header: Optional[SourcingCreateHeader] = field(
        default=None,
        metadata={
            "name": "SourcingCreateHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_create_detail: Optional[ListOfSourcingCreateDetail] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingCreateDetail",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_summary: Optional[SourcingCreateSummary] = field(
        default=None,
        metadata={
            "name": "SourcingCreateSummary",
            "type": "Element",
            "required": True,
        }
    )
