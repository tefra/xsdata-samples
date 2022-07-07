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


@dataclass
class ListOfPaymentRequestReferences:
    list_of_reference: Optional[ListOfReference] = field(
        default=None,
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentDateRange:
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentStatusRequestHeader:
    payment_status_request_id: Optional[PaymentStatusRequestId] = field(
        default=None,
        metadata={
            "name": "PaymentStatusRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_request_issue_date: Optional[str] = field(
        default=None,
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
    language: Optional[Language] = field(
        default=None,
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


@dataclass
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
            "required": True,
        }
    )
    confirmation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    payment_date_range: Optional[PaymentDateRange] = field(
        default=None,
        metadata={
            "name": "PaymentDateRange",
            "type": "Element",
            "required": True,
        }
    )
    payment_dates: Optional[PaymentDates] = field(
        default=None,
        metadata={
            "name": "PaymentDates",
            "type": "Element",
            "required": True,
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


@dataclass
class ListOfPaymentStatusRequestDetail:
    payment_status_request_detail: List[PaymentStatusRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentStatusRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentStatusRequest:
    payment_status_request_header: Optional[PaymentStatusRequestHeader] = field(
        default=None,
        metadata={
            "name": "PaymentStatusRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_status_request_detail: Optional[ListOfPaymentStatusRequestDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentStatusRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_request_summary: Optional[PaymentStatusRequestSummary] = field(
        default=None,
        metadata={
            "name": "PaymentStatusRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
