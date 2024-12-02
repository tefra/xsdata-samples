from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.sourcing_create_response import (
    ItemNumber,
    ParentItemIdentifier,
    SourcingCreateSummary,
    SourcingItemId,
    SourcingItemName,
)
from xcbl.models.sourcing_result import (
    DeliveryDetail,
    InitiatingParty,
    ListOfAttachment,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    PartNumbers,
    Quantity,
    RateOfExchangeDetail,
    RevisionNumber,
    UnitPrice,
    Value,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfIdentifier,
    Mdfbusiness,
    NameAddress,
    OrderContact,
    OtherContacts,
    Party,
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
class AggregationTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AggregationTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AllOrNothing:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AlternativeBuyerContactName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AlternativeContactEmail:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AlternativeContactFaxNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AlternativeContactMobile:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AlternativeContactPhoneNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttributeCharacteristic:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AttributeName:
    lang: str = field(
        default="en",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
            "required": True,
        },
    )
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BundleName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BuyerContactName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CommunityId:
    class Meta:
        name = "CommunityID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ComponentSourcingIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactEmail:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactFaxNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactMobile:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ContactPhoneNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Credit:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DecisionDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FormulaName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GroupIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class KeyValString:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Keyword:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LineItemNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Operator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartialQuoteIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PreferredUom:
    class Meta:
        name = "PreferredUOM"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ProjectName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteWinRuleCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteWinRuleCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequiredToRespond:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequisitionNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeDataTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeDataTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeFieldSize:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingAttributeType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateGeneralNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateId:
    class Meta:
        name = "SourcingCreateID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingItemDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingStatus:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SourcingType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SupplierView:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VisibilityIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VisibilityOfAmounts:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VisibilityOfComments:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VisibilityOfParticipants:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class VisibilityOfQuantities:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Weighting:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AggregationType:
    aggregation_type_coded: AggregationTypeCoded = field(
        metadata={
            "name": "AggregationTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    aggregation_type_coded_other: Optional[AggregationTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "AggregationTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class BaseCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Bundle:
    bundle_name: BundleName = field(
        metadata={
            "name": "BundleName",
            "type": "Element",
            "required": True,
        }
    )
    line_item_number: list[LineItemNumber] = field(
        default_factory=list,
        metadata={
            "name": "LineItemNumber",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class DropDownMenuValue:
    value: Value = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    credit: Credit = field(
        metadata={
            "name": "Credit",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FormulaAttribute:
    attribute_name: Optional[AttributeName] = field(
        default=None,
        metadata={
            "name": "AttributeName",
            "type": "Element",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class KeyVal:
    key_val_string: KeyValString = field(
        metadata={
            "name": "KeyValString",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    keyword: Keyword = field(
        metadata={
            "name": "Keyword",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfParty:
    party: list[Party] = field(
        default_factory=list,
        metadata={
            "name": "Party",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Project:
    project_name: ProjectName = field(
        metadata={
            "name": "ProjectName",
            "type": "Element",
            "required": True,
        }
    )
    revision_number: Optional[RevisionNumber] = field(
        default=None,
        metadata={
            "name": "RevisionNumber",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuoteCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingCreateListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingCreatePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingValidityDates:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class VisibilityOfBuyer:
    buyer_contact_name: Optional[BuyerContactName] = field(
        default=None,
        metadata={
            "name": "BuyerContactName",
            "type": "Element",
        },
    )
    contact_phone_number: Optional[ContactPhoneNumber] = field(
        default=None,
        metadata={
            "name": "ContactPhoneNumber",
            "type": "Element",
        },
    )
    contact_mobile: Optional[ContactMobile] = field(
        default=None,
        metadata={
            "name": "ContactMobile",
            "type": "Element",
        },
    )
    contact_fax_number: Optional[ContactFaxNumber] = field(
        default=None,
        metadata={
            "name": "ContactFaxNumber",
            "type": "Element",
        },
    )
    contact_email: Optional[ContactEmail] = field(
        default=None,
        metadata={
            "name": "ContactEmail",
            "type": "Element",
        },
    )
    alternative_buyer_contact_name: Optional[AlternativeBuyerContactName] = (
        field(
            default=None,
            metadata={
                "name": "AlternativeBuyerContactName",
                "type": "Element",
            },
        )
    )
    alternative_contact_phone_number: Optional[
        AlternativeContactPhoneNumber
    ] = field(
        default=None,
        metadata={
            "name": "AlternativeContactPhoneNumber",
            "type": "Element",
        },
    )
    alternative_contact_mobile: Optional[AlternativeContactMobile] = field(
        default=None,
        metadata={
            "name": "AlternativeContactMobile",
            "type": "Element",
        },
    )
    alternative_contact_fax_number: Optional[AlternativeContactFaxNumber] = (
        field(
            default=None,
            metadata={
                "name": "AlternativeContactFaxNumber",
                "type": "Element",
            },
        )
    )
    alternative_contact_email: Optional[AlternativeContactEmail] = field(
        default=None,
        metadata={
            "name": "AlternativeContactEmail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class VisibilityRules:
    visibility_indicator: Optional[VisibilityIndicator] = field(
        default=None,
        metadata={
            "name": "VisibilityIndicator",
            "type": "Element",
        },
    )
    visibility_of_comments: Optional[VisibilityOfComments] = field(
        default=None,
        metadata={
            "name": "VisibilityOfComments",
            "type": "Element",
        },
    )
    visibility_of_amounts: Optional[VisibilityOfAmounts] = field(
        default=None,
        metadata={
            "name": "VisibilityOfAmounts",
            "type": "Element",
        },
    )
    visibility_of_quantities: Optional[VisibilityOfQuantities] = field(
        default=None,
        metadata={
            "name": "VisibilityOfQuantities",
            "type": "Element",
        },
    )
    visibility_of_participants: Optional[VisibilityOfParticipants] = field(
        default=None,
        metadata={
            "name": "VisibilityOfParticipants",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AdditionalAttribute:
    operator: Operator = field(
        metadata={
            "name": "Operator",
            "type": "Element",
            "required": True,
        }
    )
    formula_attribute: FormulaAttribute = field(
        metadata={
            "name": "FormulaAttribute",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfBundle:
    bundle: list[Bundle] = field(
        default_factory=list,
        metadata={
            "name": "Bundle",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfDropDownMenuValue:
    drop_down_menu_value: list[DropDownMenuValue] = field(
        default_factory=list,
        metadata={
            "name": "DropDownMenuValue",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfKeyVal:
    key_val: list[KeyVal] = field(
        default_factory=list,
        metadata={
            "name": "KeyVal",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListToInform:
    list_of_party: ListOfParty = field(
        metadata={
            "name": "ListOfParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SourcingVisibilityRules:
    visibility_indicator: Optional[VisibilityIndicator] = field(
        default=None,
        metadata={
            "name": "VisibilityIndicator",
            "type": "Element",
        },
    )
    visibility_of_comments: Optional[VisibilityOfComments] = field(
        default=None,
        metadata={
            "name": "VisibilityOfComments",
            "type": "Element",
        },
    )
    visibility_of_amounts: Optional[VisibilityOfAmounts] = field(
        default=None,
        metadata={
            "name": "VisibilityOfAmounts",
            "type": "Element",
        },
    )
    visibility_of_quantities: Optional[VisibilityOfQuantities] = field(
        default=None,
        metadata={
            "name": "VisibilityOfQuantities",
            "type": "Element",
        },
    )
    visibility_of_participants: Optional[VisibilityOfParticipants] = field(
        default=None,
        metadata={
            "name": "VisibilityOfParticipants",
            "type": "Element",
        },
    )
    visibility_of_buyer: Optional[VisibilityOfBuyer] = field(
        default=None,
        metadata={
            "name": "VisibilityOfBuyer",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ValidQuoteCurrency:
    quote_currency: QuoteCurrency = field(
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
        },
    )


@dataclass(kw_only=True)
class Formula:
    formula_name: FormulaName = field(
        metadata={
            "name": "FormulaName",
            "type": "Element",
            "required": True,
        }
    )
    formula_attribute: FormulaAttribute = field(
        metadata={
            "name": "FormulaAttribute",
            "type": "Element",
            "required": True,
        }
    )
    additional_attribute: list[AdditionalAttribute] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAttribute",
            "type": "Element",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "AggregationType",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfValidQuoteCurrency:
    valid_quote_currency: list[ValidQuoteCurrency] = field(
        default_factory=list,
        metadata={
            "name": "ValidQuoteCurrency",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingAttribute:
    sourcing_attribute_name: SourcingAttributeName = field(
        metadata={
            "name": "SourcingAttributeName",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_description: Optional[SourcingAttributeDescription] = (
        field(
            default=None,
            metadata={
                "name": "SourcingAttributeDescription",
                "type": "Element",
            },
        )
    )
    sourcing_attribute_data_type_coded: SourcingAttributeDataTypeCoded = field(
        metadata={
            "name": "SourcingAttributeDataTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_data_type_coded_other: Optional[
        SourcingAttributeDataTypeCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeDataTypeCodedOther",
            "type": "Element",
        },
    )
    list_of_drop_down_menu_value: Optional[ListOfDropDownMenuValue] = field(
        default=None,
        metadata={
            "name": "ListOfDropDownMenuValue",
            "type": "Element",
        },
    )
    sourcing_attribute_type: Optional[SourcingAttributeType] = field(
        default=None,
        metadata={
            "name": "SourcingAttributeType",
            "type": "Element",
        },
    )
    required_to_respond: RequiredToRespond = field(
        metadata={
            "name": "RequiredToRespond",
            "type": "Element",
            "required": True,
        }
    )
    supplier_view: Optional[SupplierView] = field(
        default=None,
        metadata={
            "name": "SupplierView",
            "type": "Element",
        },
    )
    weighting: Optional[Weighting] = field(
        default=None,
        metadata={
            "name": "Weighting",
            "type": "Element",
        },
    )
    preferred_uom: Optional[PreferredUom] = field(
        default=None,
        metadata={
            "name": "PreferredUOM",
            "type": "Element",
        },
    )
    attribute_characteristic: AttributeCharacteristic = field(
        metadata={
            "name": "AttributeCharacteristic",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_attribute_field_size: Optional[SourcingAttributeFieldSize] = (
        field(
            default=None,
            metadata={
                "name": "SourcingAttributeFieldSize",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class SourcingPartners:
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
        },
    )
    mdfbusiness: Optional[Mdfbusiness] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    group_indicator: GroupIndicator = field(
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
        },
    )


@dataclass(kw_only=True)
class SourcingRulesProfile:
    quote_win_rule_coded: QuoteWinRuleCoded = field(
        metadata={
            "name": "QuoteWinRuleCoded",
            "type": "Element",
            "required": True,
        }
    )
    quote_win_rule_coded_other: Optional[QuoteWinRuleCodedOther] = field(
        default=None,
        metadata={
            "name": "QuoteWinRuleCodedOther",
            "type": "Element",
        },
    )
    sourcing_visibility_rules: Optional[SourcingVisibilityRules] = field(
        default=None,
        metadata={
            "name": "SourcingVisibilityRules",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfSourcingPartners:
    sourcing_partners: list[SourcingPartners] = field(
        default_factory=list,
        metadata={
            "name": "SourcingPartners",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCurrency:
    base_currency: BaseCurrency = field(
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
        },
    )


@dataclass(kw_only=True)
class SourcingItem:
    sourcing_item_id: SourcingItemId = field(
        metadata={
            "name": "SourcingItemID",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_name: SourcingItemName = field(
        metadata={
            "name": "SourcingItemName",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_item_description: Optional[SourcingItemDescription] = field(
        default=None,
        metadata={
            "name": "SourcingItemDescription",
            "type": "Element",
        },
    )
    item_number: Optional[ItemNumber] = field(
        default=None,
        metadata={
            "name": "ItemNumber",
            "type": "Element",
        },
    )
    parent_item_identifier: Optional[ParentItemIdentifier] = field(
        default=None,
        metadata={
            "name": "ParentItemIdentifier",
            "type": "Element",
        },
    )
    bundle_name: Optional[BundleName] = field(
        default=None,
        metadata={
            "name": "BundleName",
            "type": "Element",
        },
    )
    sourcing_attribute: list[SourcingAttribute] = field(
        default_factory=list,
        metadata={
            "name": "SourcingAttribute",
            "type": "Element",
        },
    )
    formula: list[Formula] = field(
        default_factory=list,
        metadata={
            "name": "Formula",
            "type": "Element",
        },
    )
    sourcing_quantity: Optional[SourcingQuantity] = field(
        default=None,
        metadata={
            "name": "SourcingQuantity",
            "type": "Element",
        },
    )
    delivery_date: Optional[DeliveryDate] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    unit_price: Optional[UnitPrice] = field(
        default=None,
        metadata={
            "name": "UnitPrice",
            "type": "Element",
        },
    )
    partial_quote_indicator: Optional[PartialQuoteIndicator] = field(
        default=None,
        metadata={
            "name": "PartialQuoteIndicator",
            "type": "Element",
        },
    )
    part_numbers: Optional[PartNumbers] = field(
        default=None,
        metadata={
            "name": "PartNumbers",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingSpecifications:
    sourcing_create_name: Optional[SourcingCreateName] = field(
        default=None,
        metadata={
            "name": "SourcingCreateName",
            "type": "Element",
        },
    )
    sourcing_type: Optional[SourcingType] = field(
        default=None,
        metadata={
            "name": "SourcingType",
            "type": "Element",
        },
    )
    sourcing_status: Optional[SourcingStatus] = field(
        default=None,
        metadata={
            "name": "SourcingStatus",
            "type": "Element",
        },
    )
    partial_quote_indicator: Optional[PartialQuoteIndicator] = field(
        default=None,
        metadata={
            "name": "PartialQuoteIndicator",
            "type": "Element",
        },
    )
    all_or_nothing: Optional[AllOrNothing] = field(
        default=None,
        metadata={
            "name": "AllOrNothing",
            "type": "Element",
        },
    )
    sourcing_attribute: list[SourcingAttribute] = field(
        default_factory=list,
        metadata={
            "name": "SourcingAttribute",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateDetail:
    sourcing_item: SourcingItem = field(
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
        },
    )
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
        },
    )
    component_sourcing_indicator: ComponentSourcingIndicator = field(
        metadata={
            "name": "ComponentSourcingIndicator",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_item_component: Optional[
        "ListOfSourcingItemComponent"
    ] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingItemComponent",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingParticipants:
    initiating_party: InitiatingParty = field(
        metadata={
            "name": "InitiatingParty",
            "type": "Element",
            "required": True,
        }
    )
    community_id: Optional[CommunityId] = field(
        default=None,
        metadata={
            "name": "CommunityID",
            "type": "Element",
        },
    )
    list_to_inform: Optional[ListToInform] = field(
        default=None,
        metadata={
            "name": "ListToInform",
            "type": "Element",
        },
    )
    list_of_sourcing_partners: Optional[ListOfSourcingPartners] = field(
        default=None,
        metadata={
            "name": "ListOfSourcingPartners",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfSourcingCreateDetail:
    sourcing_create_detail: list[SourcingCreateDetail] = field(
        default_factory=list,
        metadata={
            "name": "SourcingCreateDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCreateHeader:
    sourcing_create_purpose: SourcingCreatePurpose = field(
        metadata={
            "name": "SourcingCreatePurpose",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_issue_date: SourcingCreateIssueDate = field(
        metadata={
            "name": "SourcingCreateIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_id: SourcingCreateId = field(
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
        },
    )
    requisition_number: Optional[RequisitionNumber] = field(
        default=None,
        metadata={
            "name": "RequisitionNumber",
            "type": "Element",
        },
    )
    sourcing_validity_dates: SourcingValidityDates = field(
        metadata={
            "name": "SourcingValidityDates",
            "type": "Element",
            "required": True,
        }
    )
    decision_date: Optional[DecisionDate] = field(
        default=None,
        metadata={
            "name": "DecisionDate",
            "type": "Element",
        },
    )
    sourcing_rules_profile: Optional[SourcingRulesProfile] = field(
        default=None,
        metadata={
            "name": "SourcingRulesProfile",
            "type": "Element",
        },
    )
    sourcing_currency: Optional[SourcingCurrency] = field(
        default=None,
        metadata={
            "name": "SourcingCurrency",
            "type": "Element",
        },
    )
    list_of_bundle: Optional[ListOfBundle] = field(
        default=None,
        metadata={
            "name": "ListOfBundle",
            "type": "Element",
        },
    )
    sourcing_participants: SourcingParticipants = field(
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
        },
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_general_notes: Optional[SourcingCreateGeneralNotes] = (
        field(
            default=None,
            metadata={
                "name": "SourcingCreateGeneralNotes",
                "type": "Element",
            },
        )
    )
    sourcing_create_list_of_attachment: Optional[
        SourcingCreateListOfAttachment
    ] = field(
        default=None,
        metadata={
            "name": "SourcingCreateListOfAttachment",
            "type": "Element",
        },
    )
    sourcing_specifications: Optional[SourcingSpecifications] = field(
        default=None,
        metadata={
            "name": "SourcingSpecifications",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class SourcingItemComponent:
    sourcing_create_detail: SourcingCreateDetail = field(
        metadata={
            "name": "SourcingCreateDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSourcingItemComponent:
    sourcing_item_component: list[SourcingItemComponent] = field(
        default_factory=list,
        metadata={
            "name": "SourcingItemComponent",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SourcingCreate:
    sourcing_create_header: SourcingCreateHeader = field(
        metadata={
            "name": "SourcingCreateHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_sourcing_create_detail: ListOfSourcingCreateDetail = field(
        metadata={
            "name": "ListOfSourcingCreateDetail",
            "type": "Element",
            "required": True,
        }
    )
    sourcing_create_summary: SourcingCreateSummary = field(
        metadata={
            "name": "SourcingCreateSummary",
            "type": "Element",
            "required": True,
        }
    )
