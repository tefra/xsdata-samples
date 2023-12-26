from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.request_for_quotation import (
    PaymentInstructions,
    RequestQuoteReference,
)
from xcbl.models.shipping_schedule import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import TransportRouting
from xcbl.models.sourcing_create import QuoteCurrency
from xcbl.models.sourcing_result import (
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    DeliveryDetail,
    FinalRecipient,
    HazardousMaterials,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemNum,
    LineItemType,
    ListOfAllowOrCharge,
    ListOfAttachment,
    ListOfItemReferences,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    OrderParty,
    ParentItemNumber,
    PricingDetail,
    TaxLocation,
    TaxTypeCodedOther,
    TermsOfDelivery,
    TotalQuantity,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class QuoteSummary:
    total_number_of_line_items: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuoteType:
    quote_type_coded: str = field(
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
        },
    )


@dataclass(kw_only=True)
class ListOfQuotePackageDetail:
    list_of_package_detail: ListOfPackageDetail = field(
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuotationReqReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteAllowanceOrCharge:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteId:
    class Meta:
        name = "QuoteID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteItemParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteItemReferences:
    request_quote_reference: RequestQuoteReference = field(
        metadata={
            "name": "RequestQuoteReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteItemType:
    quote_type: QuoteType = field(
        metadata={
            "name": "QuoteType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuotePricingDetail:
    pricing_detail: PricingDetail = field(
        metadata={
            "name": "PricingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteTermsOfPayment:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxReference:
    tax_function_qualifier_coded: str = field(
        metadata={
            "name": "TaxFunctionQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_function_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxFunctionQualifierCodedOther",
            "type": "Element",
        },
    )
    tax_category_coded: str = field(
        metadata={
            "name": "TaxCategoryCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_category_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCategoryCodedOther",
            "type": "Element",
        },
    )
    reason_tax_exempt_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCoded",
            "type": "Element",
        },
    )
    reason_tax_exempt_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCodedOther",
            "type": "Element",
        },
    )
    tax_type_coded: str = field(
        metadata={
            "name": "TaxTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_type_coded_other: Optional[TaxTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "TaxTypeCodedOther",
            "type": "Element",
        },
    )
    tax_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPercent",
            "type": "Element",
        },
    )
    tax_payment_method_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCoded",
            "type": "Element",
        },
    )
    tax_payment_method_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCodedOther",
            "type": "Element",
        },
    )
    taxable_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
        },
    )
    taxable_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmountInTaxAccountingCurrency",
            "type": "Element",
        },
    )
    tax_amount: str = field(
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxAmountInTaxAccountingCurrency",
            "type": "Element",
        },
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        },
    )
    tax_treatment_coded: str = field(
        metadata={
            "name": "TaxTreatmentCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_treatment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTreatmentCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuotationRequestReference:
    quotation_req_reference: QuotationReqReference = field(
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
        },
    )


@dataclass(kw_only=True)
class QuoteItemDetail:
    line_item_num: LineItemNum = field(
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
        },
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    quote_item_references: Optional[QuoteItemReferences] = field(
        default=None,
        metadata={
            "name": "QuoteItemReferences",
            "type": "Element",
        },
    )
    quote_item_party: Optional[QuoteItemParty] = field(
        default=None,
        metadata={
            "name": "QuoteItemParty",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuoteTax:
    tax_reference: TaxReference = field(
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuoteDetails:
    quote_item_type: QuoteItemType = field(
        metadata={
            "name": "QuoteItemType",
            "type": "Element",
            "required": True,
        }
    )
    quote_item_detail: QuoteItemDetail = field(
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
        },
    )
    quote_delivery_detail: Optional[QuoteDeliveryDetail] = field(
        default=None,
        metadata={
            "name": "QuoteDeliveryDetail",
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
    quote_item_list_of_attachment: Optional[QuoteItemListOfAttachment] = field(
        default=None,
        metadata={
            "name": "QuoteItemListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuoteHeader:
    quote_issue_date: str = field(
        metadata={
            "name": "QuoteIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    quote_id: QuoteId = field(
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
        },
    )
    quote_type: Optional[QuoteType] = field(
        default=None,
        metadata={
            "name": "QuoteType",
            "type": "Element",
        },
    )
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        },
    )
    quote_party: QuoteParty = field(
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
        },
    )
    quote_currency: Optional[QuoteCurrency] = field(
        default=None,
        metadata={
            "name": "QuoteCurrency",
            "type": "Element",
        },
    )
    quote_allowance_or_charge: Optional[QuoteAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "QuoteAllowanceOrCharge",
            "type": "Element",
        },
    )
    quote_terms_of_payment: Optional[QuoteTermsOfPayment] = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfPayment",
            "type": "Element",
        },
    )
    quote_terms_of_delivery: Optional[QuoteTermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfDelivery",
            "type": "Element",
        },
    )
    quote_tax: List[QuoteTax] = field(
        default_factory=list,
        metadata={
            "name": "QuoteTax",
            "type": "Element",
        },
    )
    quote_language: Optional[QuoteLanguage] = field(
        default=None,
        metadata={
            "name": "QuoteLanguage",
            "type": "Element",
        },
    )
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
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
    quote_list_of_attachment: Optional[QuoteListOfAttachment] = field(
        default=None,
        metadata={
            "name": "QuoteListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfQuoteDetails:
    quote_details: List[QuoteDetails] = field(
        default_factory=list,
        metadata={
            "name": "QuoteDetails",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Quote:
    quote_header: QuoteHeader = field(
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
        },
    )
    list_of_quote_package_detail: Optional[ListOfQuotePackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfQuotePackageDetail",
            "type": "Element",
        },
    )
    quote_summary: Optional[QuoteSummary] = field(
        default=None,
        metadata={
            "name": "QuoteSummary",
            "type": "Element",
        },
    )
