from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.remittance_advice import SupplierParty
from xcbl.models.sourcing_result import (
    BuyerParty,
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
    ListOfAttachment,
    ListOfItemReferences,
    ListOfQuantityCoded,
    MaxBackOrderQuantity,
    OffCatalogFlag,
    ParentItemNumber,
    Price,
    TotalQuantity,
    Transport,
)
from xcbl.models.time_series_response import (
    ListOfDimension,
    ListOfPartyCoded,
    Party,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class BuyerIdreferenceDate:
    class Meta:
        name = "BuyerIDReferenceDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CompletionText:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class GeneralLineItemNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LangString:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class MinRetrySecs:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Parameter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCheckItemError:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCheckResultIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PriceCheckResultNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SeverityCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SeverityCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SupplierIdreferenceDate:
    class Meta:
        name = "SupplierIDReferenceDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SwVendorErrorRef:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumberOfLineItem:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CheckResultTransport:
    transport: Transport = field(
        metadata={
            "name": "Transport",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LanguageString:
    lang_string: LangString = field(
        metadata={
            "name": "LangString",
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


@dataclass(kw_only=True)
class LineItemAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfParameter:
    parameter: list[Parameter] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PriceCheckCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckResultId:
    class Meta:
        name = "PriceCheckResultID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckResultLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckShipToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ResultListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ResultPrice:
    price: Price = field(
        metadata={
            "name": "Price",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Severity:
    severity_coded: SeverityCoded = field(
        metadata={
            "name": "SeverityCoded",
            "type": "Element",
            "required": True,
        }
    )
    severity_coded_other: SeverityCodedOther | None = field(
        default=None,
        metadata={
            "name": "SeverityCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CheckResultBaseItemDetail:
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
    check_result_transport: list[CheckResultTransport] = field(
        default_factory=list,
        metadata={
            "name": "CheckResultTransport",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CompletionMsg:
    language_string: LanguageString = field(
        metadata={
            "name": "LanguageString",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckResultHeader:
    price_check_result_id: PriceCheckResultId = field(
        metadata={
            "name": "PriceCheckResultID",
            "type": "Element",
            "required": True,
        }
    )
    price_check_result_issue_date: PriceCheckResultIssueDate = field(
        metadata={
            "name": "PriceCheckResultIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    supplier_party: SupplierParty = field(
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "required": True,
        }
    )
    supplier_idreference_date: SupplierIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
            "type": "Element",
        },
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_idreference_date: BuyerIdreferenceDate | None = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        },
    )
    price_check_ship_to_party: PriceCheckShipToParty = field(
        metadata={
            "name": "PriceCheckShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    price_check_currency: PriceCheckCurrency | None = field(
        default=None,
        metadata={
            "name": "PriceCheckCurrency",
            "type": "Element",
        },
    )
    quote_date: QuoteDate | None = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Element",
        },
    )
    price_check_result_language: PriceCheckResultLanguage | None = field(
        default=None,
        metadata={
            "name": "PriceCheckResultLanguage",
            "type": "Element",
        },
    )
    price_check_result_note: PriceCheckResultNote | None = field(
        default=None,
        metadata={
            "name": "PriceCheckResultNote",
            "type": "Element",
        },
    )
    result_list_of_attachment: ResultListOfAttachment | None = field(
        default=None,
        metadata={
            "name": "ResultListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ErrorInfo:
    completion_text: CompletionText = field(
        metadata={
            "name": "CompletionText",
            "type": "Element",
            "required": True,
        }
    )
    completion_msg: CompletionMsg = field(
        metadata={
            "name": "CompletionMsg",
            "type": "Element",
            "required": True,
        }
    )
    severity: Severity = field(
        metadata={
            "name": "Severity",
            "type": "Element",
            "required": True,
        }
    )
    list_of_parameter: ListOfParameter | None = field(
        default=None,
        metadata={
            "name": "ListOfParameter",
            "type": "Element",
        },
    )
    min_retry_secs: MinRetrySecs | None = field(
        default=None,
        metadata={
            "name": "MinRetrySecs",
            "type": "Element",
        },
    )
    sw_vendor_error_ref: SwVendorErrorRef | None = field(
        default=None,
        metadata={
            "name": "SwVendorErrorRef",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class QuotedItem:
    check_result_base_item_detail: CheckResultBaseItemDetail = field(
        metadata={
            "name": "CheckResultBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckSummaryErrorInfo:
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceErrorInfo:
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckResultItemDetail:
    quoted_item: QuotedItem = field(
        metadata={
            "name": "QuotedItem",
            "type": "Element",
            "required": True,
        }
    )
    result_price: ResultPrice = field(
        metadata={
            "name": "ResultPrice",
            "type": "Element",
            "required": True,
        }
    )
    price_error_info: PriceErrorInfo | None = field(
        default=None,
        metadata={
            "name": "PriceErrorInfo",
            "type": "Element",
        },
    )
    general_line_item_note: GeneralLineItemNote | None = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        },
    )
    line_item_attachment: LineItemAttachment | None = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PriceCheckResultSummary:
    price_check_item_error: PriceCheckItemError = field(
        metadata={
            "name": "PriceCheckItemError",
            "type": "Element",
            "required": True,
        }
    )
    price_check_summary_error_info: PriceCheckSummaryErrorInfo | None = field(
        default=None,
        metadata={
            "name": "PriceCheckSummaryErrorInfo",
            "type": "Element",
        },
    )
    total_number_of_line_item: TotalNumberOfLineItem | None = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPriceCheckResultItemDetail:
    price_check_result_item_detail: list[PriceCheckResultItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "PriceCheckResultItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PriceCheckResultDetail:
    list_of_price_check_result_item_detail: ListOfPriceCheckResultItemDetail = field(
        metadata={
            "name": "ListOfPriceCheckResultItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceCheckResult:
    price_check_result_header: PriceCheckResultHeader = field(
        metadata={
            "name": "PriceCheckResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    price_check_result_detail: PriceCheckResultDetail | None = field(
        default=None,
        metadata={
            "name": "PriceCheckResultDetail",
            "type": "Element",
        },
    )
    price_check_result_summary: PriceCheckResultSummary | None = field(
        default=None,
        metadata={
            "name": "PriceCheckResultSummary",
            "type": "Element",
        },
    )
