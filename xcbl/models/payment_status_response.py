from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.remittance_advice import (
    PayerParty,
    PaymentParty,
)
from xcbl.models.request_for_quotation import (
    AccountDetail,
    CardInfo,
    FinancialInstitution,
    PaymentSystemCoded,
    PaymentSystemCodedOther,
)
from xcbl.models.sourcing_result import (
    ListOfDateCoded,
    ListOfNameValuePair,
    ListOfReference,
    MonetaryValue,
    NameValuePair,
    RateOfExchangeDetail,
)
from xcbl.models.sourcing_result_response import GeneralNote
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Identifier,
    Language,
)


@dataclass(kw_only=True)
class ConfirmationId:
    class Meta:
        name = "ConfirmationID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxvalueDate:
    class Meta:
        name = "FXValueDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PayBeforeDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentDueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentExceptionCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentExceptionCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentExceptionNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentStatusResponseIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestedPaymentDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SequenceNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SettlementDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalNumberPaymentRequests:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CreditAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DebitAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FiaccountDetail:
    class Meta:
        name = "FIAccountDetail"

    account_detail: AccountDetail = field(
        metadata={
            "name": "AccountDetail",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution: FinancialInstitution = field(
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfOtherPaymentInfo:
    list_of_name_value_pair: ListOfNameValuePair = field(
        metadata={
            "name": "ListOfNameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentDates:
    list_of_date_coded: ListOfDateCoded = field(
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentReferences:
    list_of_reference: ListOfReference = field(
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OffendingPaymentElement:
    name_value_pair: NameValuePair = field(
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ParticipantUserId:
    class Meta:
        name = "ParticipantUserID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentRequestId:
    class Meta:
        name = "PaymentRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusRequestId:
    class Meta:
        name = "PaymentStatusRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusRequestSummary:
    total_number_payment_requests: TotalNumberPaymentRequests | None = field(
        default=None,
        metadata={
            "name": "TotalNumberPaymentRequests",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentStatusResponseId:
    class Meta:
        name = "PaymentStatusResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SendingParty:
    payer_party: PayerParty = field(
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SettlementAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginatingFinancialInstitution:
    fiaccount_detail: FiaccountDetail = field(
        metadata={
            "name": "FIAccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentDates:
    payment_due_date: PaymentDueDate | None = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
        },
    )
    requested_payment_date: RequestedPaymentDate | None = field(
        default=None,
        metadata={
            "name": "RequestedPaymentDate",
            "type": "Element",
        },
    )
    pay_before_date: PayBeforeDate | None = field(
        default=None,
        metadata={
            "name": "PayBeforeDate",
            "type": "Element",
        },
    )
    list_of_payment_dates: ListOfPaymentDates | None = field(
        default=None,
        metadata={
            "name": "ListOfPaymentDates",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentException:
    payment_exception_coded: PaymentExceptionCoded = field(
        metadata={
            "name": "PaymentExceptionCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_exception_coded_other: PaymentExceptionCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentExceptionCodedOther",
            "type": "Element",
        },
    )
    payment_exception_note: PaymentExceptionNote | None = field(
        default=None,
        metadata={
            "name": "PaymentExceptionNote",
            "type": "Element",
        },
    )
    offending_payment_element: OffendingPaymentElement | None = field(
        default=None,
        metadata={
            "name": "OffendingPaymentElement",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentStatusResponseHeader:
    payment_status_request_id: PaymentStatusRequestId = field(
        metadata={
            "name": "PaymentStatusRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_id: PaymentStatusResponseId = field(
        metadata={
            "name": "PaymentStatusResponseID",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_issue_date: PaymentStatusResponseIssueDate = field(
        metadata={
            "name": "PaymentStatusResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    sending_party: SendingParty | None = field(
        default=None,
        metadata={
            "name": "SendingParty",
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
    general_note: GeneralNote | None = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentStatusResponseSummary:
    payment_status_request_summary: PaymentStatusRequestSummary = field(
        metadata={
            "name": "PaymentStatusRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceivingFinancialInstitution:
    fiaccount_detail: FiaccountDetail = field(
        metadata={
            "name": "FIAccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentException:
    payment_exception: list[PaymentException] = field(
        default_factory=list,
        metadata={
            "name": "PaymentException",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfPaymentResponse:
    list_of_payment_exception: ListOfPaymentException = field(
        metadata={
            "name": "ListOfPaymentException",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentStatusResponseDetail:
    payment_request_id: PaymentRequestId = field(
        metadata={
            "name": "PaymentRequestID",
            "type": "Element",
            "required": True,
        }
    )
    confirmation_id: ConfirmationId = field(
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    sequence_number: SequenceNumber | None = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        },
    )
    payment_dates: PaymentDates | None = field(
        default=None,
        metadata={
            "name": "PaymentDates",
            "type": "Element",
        },
    )
    settlement_date: SettlementDate | None = field(
        default=None,
        metadata={
            "name": "SettlementDate",
            "type": "Element",
        },
    )
    fxvalue_date: FxvalueDate | None = field(
        default=None,
        metadata={
            "name": "FXValueDate",
            "type": "Element",
        },
    )
    settlement_amount: SettlementAmount | None = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
        },
    )
    debit_amount: DebitAmount | None = field(
        default=None,
        metadata={
            "name": "DebitAmount",
            "type": "Element",
        },
    )
    credit_amount: CreditAmount | None = field(
        default=None,
        metadata={
            "name": "CreditAmount",
            "type": "Element",
        },
    )
    originating_financial_institution: (
        OriginatingFinancialInstitution | None
    ) = field(
        default=None,
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
        },
    )
    receiving_financial_institution: ReceivingFinancialInstitution | None = (
        field(
            default=None,
            metadata={
                "name": "ReceivingFinancialInstitution",
                "type": "Element",
            },
        )
    )
    card_info: CardInfo | None = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        },
    )
    payment_party: PaymentParty | None = field(
        default=None,
        metadata={
            "name": "PaymentParty",
            "type": "Element",
        },
    )
    participant_user_id: ParticipantUserId | None = field(
        default=None,
        metadata={
            "name": "ParticipantUserID",
            "type": "Element",
        },
    )
    rate_of_exchange_detail: RateOfExchangeDetail | None = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        },
    )
    payment_system_coded: PaymentSystemCoded | None = field(
        default=None,
        metadata={
            "name": "PaymentSystemCoded",
            "type": "Element",
        },
    )
    payment_system_coded_other: PaymentSystemCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentSystemCodedOther",
            "type": "Element",
        },
    )
    list_of_payment_references: ListOfPaymentReferences | None = field(
        default=None,
        metadata={
            "name": "ListOfPaymentReferences",
            "type": "Element",
        },
    )
    list_of_other_payment_info: ListOfOtherPaymentInfo | None = field(
        default=None,
        metadata={
            "name": "ListOfOtherPaymentInfo",
            "type": "Element",
        },
    )
    list_of_payment_response: ListOfPaymentResponse = field(
        metadata={
            "name": "ListOfPaymentResponse",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentStatusResponseDetail:
    payment_status_response_detail: list[PaymentStatusResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentStatusResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentStatusResponse:
    payment_status_response_header: PaymentStatusResponseHeader = field(
        metadata={
            "name": "PaymentStatusResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_status_response_detail: ListOfPaymentStatusResponseDetail = field(
        metadata={
            "name": "ListOfPaymentStatusResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_status_response_summary: PaymentStatusResponseSummary = field(
        metadata={
            "name": "PaymentStatusResponseSummary",
            "type": "Element",
            "required": True,
        }
    )
