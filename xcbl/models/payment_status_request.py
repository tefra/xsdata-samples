from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfReference,
    ValidityDates,
)
from xcbl.models.payment_request_acknowledgment import (
    PayerParty,
    SettlementAmount,
)
from xcbl.models.payment_status_response import (
    PaymentDates,
    PaymentRequestId,
    PaymentStatusRequestId,
    PaymentStatusRequestSummary,
)


@dataclass(kw_only=True)
class ListOfPaymentRequestReferences:
    list_of_reference: ListOfReference = field(
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentDateRange:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusRequestHeader:
    payment_status_request_id: PaymentStatusRequestId = field(
        metadata={
            "name": "PaymentStatusRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_request_issue_date: str = field(
        metadata={
            "name": "PaymentStatusRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
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
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentStatusRequestDetail:
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        }
    )
    payment_request_id: Optional[PaymentRequestId] = field(
        default=None,
        metadata={
            "name": "PaymentRequestID",
            "type": "Element",
        }
    )
    confirmation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
        }
    )
    payment_date_range: Optional[PaymentDateRange] = field(
        default=None,
        metadata={
            "name": "PaymentDateRange",
            "type": "Element",
        }
    )
    payment_dates: Optional[PaymentDates] = field(
        default=None,
        metadata={
            "name": "PaymentDates",
            "type": "Element",
        }
    )
    settlement_amount: Optional[SettlementAmount] = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
        }
    )
    list_of_payment_request_references: Optional[ListOfPaymentRequestReferences] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentRequestReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentStatusRequestDetail:
    payment_status_request_detail: List[PaymentStatusRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentStatusRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusRequest:
    payment_status_request_header: PaymentStatusRequestHeader = field(
        metadata={
            "name": "PaymentStatusRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_status_request_detail: ListOfPaymentStatusRequestDetail = field(
        metadata={
            "name": "ListOfPaymentStatusRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_request_summary: PaymentStatusRequestSummary = field(
        metadata={
            "name": "PaymentStatusRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
