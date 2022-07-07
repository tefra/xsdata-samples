from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Identifier,
    Language,
    ListOfDateCoded,
    ListOfReference,
    RateOfExchangeDetail,
    Reference,
)
from xcbl.models.order_request import (
    CardInfo,
    ListOfNameValuePair,
)
from xcbl.models.payment_request_acknowledgment import (
    CreditAmount,
    DebitAmount,
    ListOfPaymentException,
    OriginatingFinancialInstitution,
    PayerParty,
    PaymentParty,
    ReceivingFinancialInstitution,
    SettlementAmount,
)


@dataclass
class PaymentStatusRequestSummary:
    total_number_payment_requests: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalNumberPaymentRequests",
            "type": "Element",
        }
    )


@dataclass
class ListOfOtherPaymentInfo:
    list_of_name_value_pair: Optional[ListOfNameValuePair] = field(
        default=None,
        metadata={
            "name": "ListOfNameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentDates:
    list_of_date_coded: Optional[ListOfDateCoded] = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentReferences:
    list_of_reference: Optional[ListOfReference] = field(
        default=None,
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentResponse:
    list_of_payment_exception: Optional[ListOfPaymentException] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentException",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ParticipantUserId:
    class Meta:
        name = "ParticipantUserID"

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestId:
    class Meta:
        name = "PaymentRequestID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentStatusRequestId:
    class Meta:
        name = "PaymentStatusRequestID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentStatusResponseId:
    class Meta:
        name = "PaymentStatusResponseID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentStatusResponseSummary:
    payment_status_request_summary: Optional[PaymentStatusRequestSummary] = field(
        default=None,
        metadata={
            "name": "PaymentStatusRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SendingParty:
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentDates:
    payment_due_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
        }
    )
    requested_payment_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedPaymentDate",
            "type": "Element",
        }
    )
    pay_before_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PayBeforeDate",
            "type": "Element",
        }
    )
    list_of_payment_dates: Optional[ListOfPaymentDates] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentDates",
            "type": "Element",
        }
    )


@dataclass
class PaymentStatusResponseHeader:
    payment_status_request_id: Optional[PaymentStatusRequestId] = field(
        default=None,
        metadata={
            "name": "PaymentStatusRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_id: Optional[PaymentStatusResponseId] = field(
        default=None,
        metadata={
            "name": "PaymentStatusResponseID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentStatusResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sending_party: Optional[SendingParty] = field(
        default=None,
        metadata={
            "name": "SendingParty",
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
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )


@dataclass
class PaymentStatusResponseDetail:
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
    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
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
    settlement_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SettlementDate",
            "type": "Element",
        }
    )
    fxvalue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "FXValueDate",
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
    debit_amount: Optional[DebitAmount] = field(
        default=None,
        metadata={
            "name": "DebitAmount",
            "type": "Element",
        }
    )
    credit_amount: Optional[CreditAmount] = field(
        default=None,
        metadata={
            "name": "CreditAmount",
            "type": "Element",
        }
    )
    originating_financial_institution: Optional[OriginatingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
        }
    )
    receiving_financial_institution: Optional[ReceivingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "ReceivingFinancialInstitution",
            "type": "Element",
        }
    )
    card_info: Optional[CardInfo] = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        }
    )
    payment_party: Optional[PaymentParty] = field(
        default=None,
        metadata={
            "name": "PaymentParty",
            "type": "Element",
        }
    )
    participant_user_id: Optional[ParticipantUserId] = field(
        default=None,
        metadata={
            "name": "ParticipantUserID",
            "type": "Element",
        }
    )
    rate_of_exchange_detail: Optional[RateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        }
    )
    payment_system_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSystemCoded",
            "type": "Element",
        }
    )
    payment_system_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSystemCodedOther",
            "type": "Element",
        }
    )
    list_of_payment_references: Optional[ListOfPaymentReferences] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentReferences",
            "type": "Element",
        }
    )
    list_of_other_payment_info: Optional[ListOfOtherPaymentInfo] = field(
        default=None,
        metadata={
            "name": "ListOfOtherPaymentInfo",
            "type": "Element",
        }
    )
    list_of_payment_response: Optional[ListOfPaymentResponse] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentStatusResponseDetail:
    payment_status_response_detail: List[PaymentStatusResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentStatusResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentStatusResponse:
    payment_status_response_header: Optional[PaymentStatusResponseHeader] = field(
        default=None,
        metadata={
            "name": "PaymentStatusResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_status_response_detail: Optional[ListOfPaymentStatusResponseDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentStatusResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_summary: Optional[PaymentStatusResponseSummary] = field(
        default=None,
        metadata={
            "name": "PaymentStatusResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
