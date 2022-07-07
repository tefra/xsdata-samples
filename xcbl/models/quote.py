from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    DeliveryDetail,
    Language,
    ListOfAttachment,
    ListOfDimension,
    Purpose,
    Reference,
    TermsOfDelivery,
)
from xcbl.models.goods_receipt import TransportRouting
from xcbl.models.order_request import (
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfAllowOrCharge,
    ListOfItemReferences,
    ListOfPackageDetail,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    ParentItemNumber,
    PaymentInstructions,
    PricingDetail,
    TaxReference,
    TotalQuantity,
)
from xcbl.models.request_for_quotation import (
    OrderParty,
    RequestQuoteReference,
)
from xcbl.models.sourcing_create import QuoteCurrency


@dataclass
class QuoteSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        }
    )


@dataclass
class QuoteType:
    quote_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    quote_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ListOfQuotePackageDetail:
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuotationReqReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteAllowanceOrCharge:
    list_of_allow_or_charge: Optional[ListOfAllowOrCharge] = field(
        default=None,
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteDeliveryDetail:
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteId:
    class Meta:
        name = "QuoteID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteItemListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteItemParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteItemReferences:
    request_quote_reference: Optional[RequestQuoteReference] = field(
        default=None,
        metadata={
            "name": "RequestQuoteReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteItemType:
    quote_type: Optional[QuoteType] = field(
        default=None,
        metadata={
            "name": "QuoteType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteLanguage:
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteListOfAttachment:
    list_of_attachment: Optional[ListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteParty:
    order_party: Optional[OrderParty] = field(
        default=None,
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuotePricingDetail:
    pricing_detail: Optional[PricingDetail] = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteTax:
    tax_reference: Optional[TaxReference] = field(
        default=None,
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteTermsOfDelivery:
    terms_of_delivery: Optional[TermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteTermsOfPayment:
    payment_instructions: Optional[PaymentInstructions] = field(
        default=None,
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuoteTransport:
    transport_routing: Optional[TransportRouting] = field(
        default=None,
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class QuotationRequestReference:
    quotation_req_reference: Optional[QuotationReqReference] = field(
        default=None,
        metadata={
            "name": "QuotationReqReference",
            "type": "Element",
            "required": True,
        }
    )
    reference_release_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReferenceReleaseNumber",
            "type": "Element",
        }
    )


@dataclass
class QuoteItemDetail:
    line_item_num: Optional[LineItemNum] = field(
        default=None,
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        }
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        }
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        }
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        }
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        }
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        }
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        }
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        }
    )
    quote_item_references: Optional[QuoteItemReferences] = field(
        default=None,
        metadata={
            "name": "QuoteItemReferences",
            "type": "Element",
        }
    )
    quote_item_party: Optional[QuoteItemParty] = field(
        default=None,
        metadata={
            "name": "QuoteItemParty",
            "type": "Element",
        }
    )


@dataclass
class QuoteDetails:
    quote_item_type: Optional[QuoteItemType] = field(
        default=None,
        metadata={
            "name": "QuoteItemType",
            "type": "Element",
            "required": True,
        }
    )
    quote_item_detail: Optional[QuoteItemDetail] = field(
        default=None,
        metadata={
            "name": "QuoteItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    quote_pricing_detail: Optional[QuotePricingDetail] = field(
        default=None,
        metadata={
            "name": "QuotePricingDetail",
            "type": "Element",
        }
    )
    quote_delivery_detail: Optional[QuoteDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "QuoteDeliveryDetail",
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
    quote_item_list_of_attachment: Optional[QuoteItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "QuoteItemListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class QuoteHeader:
    quote_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    quote_id: Optional[QuoteId] = field(
        default=None,
        metadata={
            "name": "QuoteID",
            "type": "Element",
            "required": True,
        }
    )
    quotation_request_reference: Optional[QuotationRequestReference] = field(
        default=None,
        metadata={
            "name": "QuotationRequestReference",
            "type": "Element",
        }
    )
    quote_type: Optional[QuoteType] = field(
        default=None,
        metadata={
            "name": "QuoteType",
            "type": "Element",
        }
    )
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        }
    )
    quote_party: Optional[QuoteParty] = field(
        default=None,
        metadata={
            "name": "QuoteParty",
            "type": "Element",
            "required": True,
        }
    )
    quote_transport: Optional[QuoteTransport] = field(
        default=None,
        metadata={
            "name": "QuoteTransport",
            "type": "Element",
        }
    )
    quote_currency: Optional[QuoteCurrency] = field(
        default=None,
        metadata={
            "name": "QuoteCurrency",
            "type": "Element",
        }
    )
    quote_allowance_or_charge: Optional[QuoteAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "QuoteAllowanceOrCharge",
            "type": "Element",
        }
    )
    quote_terms_of_payment: Optional[QuoteTermsOfPayment] = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfPayment",
            "type": "Element",
        }
    )
    quote_terms_of_delivery: Optional[QuoteTermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfDelivery",
            "type": "Element",
        }
    )
    quote_tax: List[QuoteTax] = field(
        default_factory=list,
        metadata={
            "name": "QuoteTax",
            "type": "Element",
        }
    )
    quote_language: Optional[QuoteLanguage] = field(
        default=None,
        metadata={
            "name": "QuoteLanguage",
            "type": "Element",
        }
    )
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
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
    quote_list_of_attachment: Optional[QuoteListOfAttachment] = field(
        default=None,
        metadata={
            "name": "QuoteListOfAttachment",
            "type": "Element",
        }
    )


@dataclass
class ListOfQuoteDetails:
    quote_details: List[QuoteDetails] = field(
        default_factory=list,
        metadata={
            "name": "QuoteDetails",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Quote:
    quote_header: Optional[QuoteHeader] = field(
        default=None,
        metadata={
            "name": "QuoteHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_quote_details: Optional[ListOfQuoteDetails] = field(
        default=None,
        metadata={
            "name": "ListOfQuoteDetails",
            "type": "Element",
        }
    )
    list_of_quote_package_detail: Optional[ListOfQuotePackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfQuotePackageDetail",
            "type": "Element",
        }
    )
    quote_summary: Optional[QuoteSummary] = field(
        default=None,
        metadata={
            "name": "QuoteSummary",
            "type": "Element",
        }
    )
