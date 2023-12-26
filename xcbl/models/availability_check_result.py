from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.availability_to_promise_response import (
    AvailabilityShipToParty,
)
from xcbl.models.order_response import AvailabilityErrorInfo
from xcbl.models.price_check_result import (
    ErrorInfo,
    LineItemAttachment,
    QuotedItem,
    ResultListOfAttachment,
)
from xcbl.models.remittance_advice import SupplierParty
from xcbl.models.sourcing_result import (
    BuyerParty,
    Quantity,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AvailabilityCheckResultId:
    class Meta:
        name = "AvailabilityCheckResultID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailableQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SummaryErrorInfo:
    error_info: ErrorInfo = field(
        metadata={
            "name": "ErrorInfo",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultHeader:
    availability_check_result_id: AvailabilityCheckResultId = field(
        metadata={
            "name": "AvailabilityCheckResultID",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_issue_date: str = field(
        metadata={
            "name": "AvailabilityCheckResultIssueDate",
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
        },
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
        },
    )
    availability_ship_to_party: AvailabilityShipToParty = field(
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_language: Optional[
        AvailabilityCheckResultLanguage
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultLanguage",
            "type": "Element",
        },
    )
    availability_check_result_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultNote",
            "type": "Element",
        },
    )
    result_list_of_attachment: Optional[ResultListOfAttachment] = field(
        default=None,
        metadata={
            "name": "ResultListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultItemDetail:
    quoted_item: QuotedItem = field(
        metadata={
            "name": "QuotedItem",
            "type": "Element",
            "required": True,
        }
    )
    available_quantity: AvailableQuantity = field(
        metadata={
            "name": "AvailableQuantity",
            "type": "Element",
            "required": True,
        }
    )
    delivery_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    availability_error_info: Optional[AvailabilityErrorInfo] = field(
        default=None,
        metadata={
            "name": "AvailabilityErrorInfo",
            "type": "Element",
        },
    )
    general_line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralLineItemNote",
            "type": "Element",
        },
    )
    line_item_attachment: Optional[LineItemAttachment] = field(
        default=None,
        metadata={
            "name": "LineItemAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultSummary:
    availability_item_errors: str = field(
        metadata={
            "name": "AvailabilityItemErrors",
            "type": "Element",
            "required": True,
        }
    )
    summary_error_info: Optional[SummaryErrorInfo] = field(
        default=None,
        metadata={
            "name": "SummaryErrorInfo",
            "type": "Element",
        },
    )
    total_number_of_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItem",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfAvailabilityCheckResultItemDetail:
    availability_check_result_item_detail: List[
        AvailabilityCheckResultItemDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCheckResultItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultDetail:
    list_of_availability_check_result_item_detail: ListOfAvailabilityCheckResultItemDetail = field(
        metadata={
            "name": "ListOfAvailabilityCheckResultItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AvailabilityCheckResult:
    availability_check_result_header: AvailabilityCheckResultHeader = field(
        metadata={
            "name": "AvailabilityCheckResultHeader",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_detail: Optional[
        AvailabilityCheckResultDetail
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultDetail",
            "type": "Element",
        },
    )
    availability_check_result_summary: Optional[
        AvailabilityCheckResultSummary
    ] = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultSummary",
            "type": "Element",
        },
    )
