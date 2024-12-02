from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.payment_status_response import (
    ConfirmationId,
    PaymentDates,
    PaymentRequestId,
    PaymentStatusRequestId,
    PaymentStatusRequestSummary,
    SequenceNumber,
    SettlementAmount,
)
from xcbl.models.remittance_advice import PayerParty
from xcbl.models.sourcing_result import ListOfReference
from xcbl.models.trading_partner_user_information import (
    GeneralNotes,
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class PaymentStatusRequestIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
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
    payment_status_request_issue_date: PaymentStatusRequestIssueDate = field(
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
        },
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    general_notes: Optional[GeneralNotes] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentStatusRequestDetail:
    sequence_number: Optional[SequenceNumber] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        },
    )
    payment_request_id: Optional[PaymentRequestId] = field(
        default=None,
        metadata={
            "name": "PaymentRequestID",
            "type": "Element",
        },
    )
    confirmation_id: Optional[ConfirmationId] = field(
        default=None,
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
        },
    )
    payment_date_range: Optional[PaymentDateRange] = field(
        default=None,
        metadata={
            "name": "PaymentDateRange",
            "type": "Element",
        },
    )
    payment_dates: Optional[PaymentDates] = field(
        default=None,
        metadata={
            "name": "PaymentDates",
            "type": "Element",
        },
    )
    settlement_amount: Optional[SettlementAmount] = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
        },
    )
    list_of_payment_request_references: Optional[
        ListOfPaymentRequestReferences
    ] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentRequestReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPaymentStatusRequestDetail:
    payment_status_request_detail: list[PaymentStatusRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentStatusRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
    list_of_payment_status_request_detail: ListOfPaymentStatusRequestDetail = (
        field(
            metadata={
                "name": "ListOfPaymentStatusRequestDetail",
                "type": "Element",
                "required": True,
            }
        )
    )
    payment_status_request_summary: PaymentStatusRequestSummary = field(
        metadata={
            "name": "PaymentStatusRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
