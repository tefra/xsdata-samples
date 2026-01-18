from dataclasses import dataclass, field

from xcbl.models.request_for_quotation import (
    PaymentInstructions,
    RequestQuoteReference,
)
from xcbl.models.shipping_schedule import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import (
    TotalNumberOfLineItems,
    TransportRouting,
)
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
    OffCatalogFlag,
    OrderParty,
    ParentItemNumber,
    PricingDetail,
    ReasonTaxExemptCoded,
    ReasonTaxExemptCodedOther,
    TaxableAmount,
    TaxableAmountInTaxAccountingCurrency,
    TaxAmount,
    TaxAmountInTaxAccountingCurrency,
    TaxCategoryCoded,
    TaxCategoryCodedOther,
    TaxFunctionQualifierCoded,
    TaxFunctionQualifierCodedOther,
    TaxLocation,
    TaxPaymentMethodCoded,
    TaxPaymentMethodCodedOther,
    TaxPercent,
    TaxTypeCoded,
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
from xcbl.models.trading_partner_user_information import (
    GeneralNotes,
    Language,
)


@dataclass(kw_only=True)
class QuoteIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReferenceReleaseNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TaxTreatmentCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TaxTreatmentCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
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
class QuoteSummary:
    total_number_of_line_items: TotalNumberOfLineItems | None = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        },
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
class QuoteType:
    quote_type_coded: QuoteTypeCoded = field(
        metadata={
            "name": "QuoteTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    quote_type_coded_other: QuoteTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "QuoteTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TaxReference:
    tax_function_qualifier_coded: TaxFunctionQualifierCoded = field(
        metadata={
            "name": "TaxFunctionQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_function_qualifier_coded_other: (
        TaxFunctionQualifierCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "TaxFunctionQualifierCodedOther",
            "type": "Element",
        },
    )
    tax_category_coded: TaxCategoryCoded = field(
        metadata={
            "name": "TaxCategoryCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_category_coded_other: TaxCategoryCodedOther | None = field(
        default=None,
        metadata={
            "name": "TaxCategoryCodedOther",
            "type": "Element",
        },
    )
    reason_tax_exempt_coded: ReasonTaxExemptCoded | None = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCoded",
            "type": "Element",
        },
    )
    reason_tax_exempt_coded_other: ReasonTaxExemptCodedOther | None = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCodedOther",
            "type": "Element",
        },
    )
    tax_type_coded: TaxTypeCoded = field(
        metadata={
            "name": "TaxTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_type_coded_other: TaxTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "TaxTypeCodedOther",
            "type": "Element",
        },
    )
    tax_percent: TaxPercent | None = field(
        default=None,
        metadata={
            "name": "TaxPercent",
            "type": "Element",
        },
    )
    tax_payment_method_coded: TaxPaymentMethodCoded | None = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCoded",
            "type": "Element",
        },
    )
    tax_payment_method_coded_other: TaxPaymentMethodCodedOther | None = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCodedOther",
            "type": "Element",
        },
    )
    taxable_amount: TaxableAmount | None = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
        },
    )
    taxable_amount_in_tax_accounting_currency: (
        TaxableAmountInTaxAccountingCurrency | None
    ) = field(
        default=None,
        metadata={
            "name": "TaxableAmountInTaxAccountingCurrency",
            "type": "Element",
        },
    )
    tax_amount: TaxAmount = field(
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax_amount_in_tax_accounting_currency: (
        TaxAmountInTaxAccountingCurrency | None
    ) = field(
        default=None,
        metadata={
            "name": "TaxAmountInTaxAccountingCurrency",
            "type": "Element",
        },
    )
    tax_location: TaxLocation | None = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        },
    )
    tax_treatment_coded: TaxTreatmentCoded = field(
        metadata={
            "name": "TaxTreatmentCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_treatment_coded_other: TaxTreatmentCodedOther | None = field(
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
    reference_release_number: ReferenceReleaseNumber | None = field(
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
    line_item_type: LineItemType | None = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        },
    )
    parent_item_number: ParentItemNumber | None = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: ItemIdentifiers | None = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        },
    )
    list_of_dimension: ListOfDimension | None = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    total_quantity: TotalQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: MaxBackOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: ListOfQuantityCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: OffCatalogFlag | None = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: CatalogReference | None = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: ItemContractReferences | None = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: ListOfItemReferences | None = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: CountryOfOrigin | None = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: CountryOfDestination | None = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: FinalRecipient | None = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: ConditionsOfSale | None = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: HazardousMaterials | None = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    quote_item_references: QuoteItemReferences | None = field(
        default=None,
        metadata={
            "name": "QuoteItemReferences",
            "type": "Element",
        },
    )
    quote_item_party: QuoteItemParty | None = field(
        default=None,
        metadata={
            "name": "QuoteItemParty",
            "type": "Element",
        },
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
    quote_pricing_detail: QuotePricingDetail | None = field(
        default=None,
        metadata={
            "name": "QuotePricingDetail",
            "type": "Element",
        },
    )
    quote_delivery_detail: QuoteDeliveryDetail | None = field(
        default=None,
        metadata={
            "name": "QuoteDeliveryDetail",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    quote_item_list_of_attachment: QuoteItemListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "QuoteItemListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuoteHeader:
    quote_issue_date: QuoteIssueDate = field(
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
    quotation_request_reference: QuotationRequestReference | None = field(
        default=None,
        metadata={
            "name": "QuotationRequestReference",
            "type": "Element",
        },
    )
    quote_type: QuoteType | None = field(
        default=None,
        metadata={
            "name": "QuoteType",
            "type": "Element",
        },
    )
    purpose: Purpose | None = field(
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
    quote_transport: QuoteTransport | None = field(
        default=None,
        metadata={
            "name": "QuoteTransport",
            "type": "Element",
        },
    )
    quote_currency: QuoteCurrency | None = field(
        default=None,
        metadata={
            "name": "QuoteCurrency",
            "type": "Element",
        },
    )
    quote_allowance_or_charge: QuoteAllowanceOrCharge | None = field(
        default=None,
        metadata={
            "name": "QuoteAllowanceOrCharge",
            "type": "Element",
        },
    )
    quote_terms_of_payment: QuoteTermsOfPayment | None = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfPayment",
            "type": "Element",
        },
    )
    quote_terms_of_delivery: QuoteTermsOfDelivery | None = field(
        default=None,
        metadata={
            "name": "QuoteTermsOfDelivery",
            "type": "Element",
        },
    )
    quote_tax: list[QuoteTax] = field(
        default_factory=list,
        metadata={
            "name": "QuoteTax",
            "type": "Element",
        },
    )
    quote_language: QuoteLanguage | None = field(
        default=None,
        metadata={
            "name": "QuoteLanguage",
            "type": "Element",
        },
    )
    general_notes: GeneralNotes | None = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )
    list_of_structured_note: ListOfStructuredNote | None = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    quote_list_of_attachment: QuoteListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "QuoteListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfQuoteDetails:
    quote_details: list[QuoteDetails] = field(
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
    list_of_quote_details: ListOfQuoteDetails | None = field(
        default=None,
        metadata={
            "name": "ListOfQuoteDetails",
            "type": "Element",
        },
    )
    list_of_quote_package_detail: ListOfQuotePackageDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfQuotePackageDetail",
            "type": "Element",
        },
    )
    quote_summary: QuoteSummary | None = field(
        default=None,
        metadata={
            "name": "QuoteSummary",
            "type": "Element",
        },
    )
