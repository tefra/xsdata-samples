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


@dataclass
class FinancialInstitutionCoded:
    financial_institution_qaulifier_coded: Optional[str] = field(
        default=None,
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
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfRemittanceAdviceDetail:
    remittance_advice_detail: List[RemittanceAdviceDetail] = field(
        default_factory=list,
        metadata={
            "name": "RemittanceAdviceDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfRemittanceAdviceReference:
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RemittanceAdviceAttachment:
    attachment: Optional[Attachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RemittanceAdvicePurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RemittanceAdviceSummary:
    payment_request_summary: Optional[PaymentRequestSummary] = field(
        default=None,
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TotalAmountDue:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TotalAmountPaid:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TraceReference:
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfFinancialInstitutionCoded:
    financial_institution_coded: List[FinancialInstitutionCoded] = field(
        default_factory=list,
        metadata={
            "name": "FinancialInstitutionCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class TraceType:
    trace_type_coded: Optional[str] = field(
        default=None,
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


@dataclass
class RemittanceAdviceHeader:
    remittance_advice_purpose: Optional[RemittanceAdvicePurpose] = field(
        default=None,
        metadata={
            "name": "RemittanceAdvicePurpose",
            "type": "Element",
            "required": True,
        }
    )
    remittace_advice_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RemittaceAdviceIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_id: Optional[RemittanceAdviceId] = field(
        default=None,
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
    total_amount_paid: Optional[TotalAmountPaid] = field(
        default=None,
        metadata={
            "name": "TotalAmountPaid",
            "type": "Element",
            "required": True,
        }
    )
    payment_currency: Optional[PaymentCurrency] = field(
        default=None,
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
    language: Optional[Language] = field(
        default=None,
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
    payment_party: Optional[PaymentParty] = field(
        default=None,
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


@dataclass
class RemittanceAdvice:
    remittance_advice_header: Optional[RemittanceAdviceHeader] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_remittance_advice_detail: Optional[ListOfRemittanceAdviceDetail] = field(
        default=None,
        metadata={
            "name": "ListOfRemittanceAdviceDetail",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_summary: Optional[RemittanceAdviceSummary] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceSummary",
            "type": "Element",
            "required": True,
        }
    )
