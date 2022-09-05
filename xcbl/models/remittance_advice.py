from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Attachment,
    Language,
    ListOfPrice,
    ListOfReferenceCoded,
    Purpose,
    Reference,
)
from xcbl.models.invoice import PaymentCurrency
from xcbl.models.order_request import (
    FinancialInstitution,
    MonetaryValue,
    PaymentInstructions,
)
from xcbl.models.payment_request import (
    RemittanceAdviceDetail,
    RemittanceAdviceId,
)
from xcbl.models.payment_request_acknowledgment import (
    ListOfRateOfExchangeDetail,
    PaymentParty,
    PaymentRequestSummary,
)


@dataclass(kw_only=True)
class FinancialInstitutionCoded:
    financial_institution_qaulifier_coded: str = field(
        metadata={
            "name": "FinancialInstitutionQaulifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution_qaulifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionQaulifierCodedOther",
            "type": "Element",
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
class ListOfRemittanceAdviceDetail:
    remittance_advice_detail: List[RemittanceAdviceDetail] = field(
        default_factory=list,
        metadata={
            "name": "RemittanceAdviceDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfRemittanceAdviceReference:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdviceAttachment:
    attachment: Attachment = field(
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdvicePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdviceSummary:
    payment_request_summary: PaymentRequestSummary = field(
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountDue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountPaid:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TraceReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfFinancialInstitutionCoded:
    financial_institution_coded: List[FinancialInstitutionCoded] = field(
        default_factory=list,
        metadata={
            "name": "FinancialInstitutionCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class TraceType:
    trace_type_coded: str = field(
        metadata={
            "name": "TraceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trace_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TraceTypeCodedOther",
            "type": "Element",
        }
    )
    trace_reference: Optional[TraceReference] = field(
        default=None,
        metadata={
            "name": "TraceReference",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RemittanceAdviceHeader:
    remittance_advice_purpose: RemittanceAdvicePurpose = field(
        metadata={
            "name": "RemittanceAdvicePurpose",
            "type": "Element",
            "required": True,
        }
    )
    remittace_advice_issue_date: str = field(
        metadata={
            "name": "RemittaceAdviceIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_id: RemittanceAdviceId = field(
        metadata={
            "name": "RemittanceAdviceID",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceStatusCoded",
            "type": "Element",
        }
    )
    remittance_advice_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceStatusCodedOther",
            "type": "Element",
        }
    )
    payment_settlement_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSettlementDate",
            "type": "Element",
        }
    )
    total_amount_due: Optional[TotalAmountDue] = field(
        default=None,
        metadata={
            "name": "TotalAmountDue",
            "type": "Element",
        }
    )
    total_amount_paid: TotalAmountPaid = field(
        metadata={
            "name": "TotalAmountPaid",
            "type": "Element",
            "required": True,
        }
    )
    payment_currency: PaymentCurrency = field(
        metadata={
            "name": "PaymentCurrency",
            "type": "Element",
            "required": True,
        }
    )
    list_of_rate_of_exchange_detail: Optional[ListOfRateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        }
    )
    list_of_price: Optional[ListOfPrice] = field(
        default=None,
        metadata={
            "name": "ListOfPrice",
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
    is_credit: Optional[str] = field(
        default=None,
        metadata={
            "name": "IsCredit",
            "type": "Element",
        }
    )
    payment_instructions: Optional[PaymentInstructions] = field(
        default=None,
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
        }
    )
    list_of_financial_institution_coded: Optional[ListOfFinancialInstitutionCoded] = field(
        default=None,
        metadata={
            "name": "ListOfFinancialInstitutionCoded",
            "type": "Element",
        }
    )
    payment_party: PaymentParty = field(
        metadata={
            "name": "PaymentParty",
            "type": "Element",
            "required": True,
        }
    )
    payment_reason_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentReasonCoded",
            "type": "Element",
        }
    )
    payment_reason_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentReasonCodedOther",
            "type": "Element",
        }
    )
    transaction_handling_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionHandlingCoded",
            "type": "Element",
        }
    )
    transaction_handling_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransactionHandlingCodedOther",
            "type": "Element",
        }
    )
    trace_type: Optional[TraceType] = field(
        default=None,
        metadata={
            "name": "TraceType",
            "type": "Element",
        }
    )
    list_of_remittance_advice_reference: Optional[ListOfRemittanceAdviceReference] = field(
        default=None,
        metadata={
            "name": "ListOfRemittanceAdviceReference",
            "type": "Element",
        }
    )
    remittance_advice_attachment: Optional[RemittanceAdviceAttachment] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceAttachment",
            "type": "Element",
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RemittanceAdvice:
    remittance_advice_header: RemittanceAdviceHeader = field(
        metadata={
            "name": "RemittanceAdviceHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_remittance_advice_detail: ListOfRemittanceAdviceDetail = field(
        metadata={
            "name": "ListOfRemittanceAdviceDetail",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_summary: RemittanceAdviceSummary = field(
        metadata={
            "name": "RemittanceAdviceSummary",
            "type": "Element",
            "required": True,
        }
    )
