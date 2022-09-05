from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Currency,
    Language,
    Party,
    Price,
    Reference,
)
from xcbl.models.availability_check_result import QuotedItem
from xcbl.models.order_request import BuyerParty
from xcbl.models.order_status_result import (
    ErrorInfo,
    LineItemAttachment,
    ResultListOfAttachment,
)
from xcbl.models.payment_request_acknowledgment import SupplierParty


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
class ResultPrice:
    price: Price = field(
        metadata={
            "name": "Price",
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
    price_check_result_issue_date: str = field(
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
    supplier_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierIDReferenceDate",
            "type": "Element",
        }
    )
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_idreference_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "BuyerIDReferenceDate",
            "type": "Element",
        }
    )
    price_check_ship_to_party: PriceCheckShipToParty = field(
        metadata={
            "name": "PriceCheckShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    price_check_currency: Optional[PriceCheckCurrency] = field(
        default=None,
        metadata={
            "name": "PriceCheckCurrency",
            "type": "Element",
        }
    )
    quote_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Element",
        }
    )
    price_check_result_language: Optional[PriceCheckResultLanguage] = field(
        default=None,
        metadata={
            "name": "PriceCheckResultLanguage",
            "type": "Element",
        }
    )
    price_check_result_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PriceCheckResultNote",
            "type": "Element",
        }
    )
    result_list_of_attachment: Optional[ResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ResultListOfAttachment",
            "type": "Element",
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
    price_error_info: Optional[PriceErrorInfo] = field(
        default=None,
        metadata={
            "name": "PriceErrorInfo",
            "type": "Element",
        }
    )
    general_line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        }
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PriceCheckResultSummary:
    price_check_item_error: str = field(
        metadata={
            "name": "PriceCheckItemError",
            "type": "Element",
            "required": True,
        }
    )
    price_check_summary_error_info: Optional[PriceCheckSummaryErrorInfo] = field(
        default=None,
        metadata={
            "name": "PriceCheckSummaryErrorInfo",
            "type": "Element",
        }
    )
    total_number_of_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfPriceCheckResultItemDetail:
    price_check_result_item_detail: List[PriceCheckResultItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "PriceCheckResultItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
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
    price_check_result_detail: Optional[PriceCheckResultDetail] = field(
        default=None,
        metadata={
            "name": "PriceCheckResultDetail",
            "type": "Element",
        }
    )
    price_check_result_summary: Optional[PriceCheckResultSummary] = field(
        default=None,
        metadata={
            "name": "PriceCheckResultSummary",
            "type": "Element",
        }
    )
