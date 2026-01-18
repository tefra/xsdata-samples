from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.availability_to_promise_response import (
    AvailabilityShipToParty,
)
from xcbl.models.order_response import AvailabilityErrorInfo
from xcbl.models.price_check_result import (
    BuyerIdreferenceDate,
    ErrorInfo,
    GeneralLineItemNote,
    LineItemAttachment,
    QuotedItem,
    ResultListOfAttachment,
    SupplierIdreferenceDate,
    TotalNumberOfLineItem,
)
from xcbl.models.remittance_advice import SupplierParty
from xcbl.models.sourcing_create import DeliveryDate
from xcbl.models.sourcing_result import (
    BuyerParty,
    Quantity,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class AvailabilityCheckResultIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityCheckResultNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AvailabilityItemErrors:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
    availability_check_result_issue_date: AvailabilityCheckResultIssueDate = (
        field(
            metadata={
                "name": "AvailabilityCheckResultIssueDate",
                "type": "Element",
                "required": True,
            }
        )
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
    availability_ship_to_party: AvailabilityShipToParty = field(
        metadata={
            "name": "AvailabilityShipToParty",
            "type": "Element",
            "required": True,
        }
    )
    availability_check_result_language: (
        AvailabilityCheckResultLanguage | None
    ) = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultLanguage",
            "type": "Element",
        },
    )
    availability_check_result_note: AvailabilityCheckResultNote | None = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultNote",
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
    delivery_date: DeliveryDate | None = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    availability_error_info: AvailabilityErrorInfo | None = field(
        default=None,
        metadata={
            "name": "AvailabilityErrorInfo",
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
class AvailabilityCheckResultSummary:
    availability_item_errors: AvailabilityItemErrors = field(
        metadata={
            "name": "AvailabilityItemErrors",
            "type": "Element",
            "required": True,
        }
    )
    summary_error_info: SummaryErrorInfo | None = field(
        default=None,
        metadata={
            "name": "SummaryErrorInfo",
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
class ListOfAvailabilityCheckResultItemDetail:
    availability_check_result_item_detail: list[
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
    availability_check_result_detail: AvailabilityCheckResultDetail | None = (
        field(
            default=None,
            metadata={
                "name": "AvailabilityCheckResultDetail",
                "type": "Element",
            },
        )
    )
    availability_check_result_summary: (
        AvailabilityCheckResultSummary | None
    ) = field(
        default=None,
        metadata={
            "name": "AvailabilityCheckResultSummary",
            "type": "Element",
        },
    )
