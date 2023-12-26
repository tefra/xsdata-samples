from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.payment_status_response import (
    CreditAmount,
    DebitAmount,
    ListOfPaymentException,
    OriginatingFinancialInstitution,
    ReceivingFinancialInstitution,
    SettlementAmount,
)
from xcbl.models.remittance_advice import (
    EncryptedInfo,
    ListOfRateOfExchangeDetail,
    PaymentParty,
    PaymentRequestSummary,
)
from xcbl.models.request_for_quotation import (
    AccountDetail,
    FinancialInstitution,
)
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class FiaccountData:
    class Meta:
        name = "FIAccountData"

    account_detail: Optional[AccountDetail] = field(
        default=None,
        metadata={
            "name": "AccountDetail",
            "type": "Element",
        },
    )
    financial_institution: FinancialInstitution = field(
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        },
    )
    finote: Optional[str] = field(
        default=None,
        metadata={
            "name": "FINote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentDocumentId:
    class Meta:
        name = "PaymentDocumentID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentRequestAcknSummary:
    payment_request_summary: PaymentRequestSummary = field(
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentRequestIdreference:
    class Meta:
        name = "PaymentRequestIDReference"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfFiaccount:
    class Meta:
        name = "ListOfFIAccount"

    fiaccount_data: List[FiaccountData] = field(
        default_factory=list,
        metadata={
            "name": "FIAccountData",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRequestAcknHeader:
    payment_request_ackn_coded: str = field(
        metadata={
            "name": "PaymentRequestAcknCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_ackn_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknCodedOther",
            "type": "Element",
        },
    )
    payment_request_ackn_issue_date: str = field(
        metadata={
            "name": "PaymentRequestAcknIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_ackn_id: str = field(
        metadata={
            "name": "PaymentRequestAcknID",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_idreference: Optional[PaymentRequestIdreference] = field(
        default=None,
        metadata={
            "name": "PaymentRequestIDReference",
            "type": "Element",
        },
    )
    certificate_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        },
    )
    successful_recept_indicator: str = field(
        metadata={
            "name": "SuccessfulReceptIndicator",
            "type": "Element",
            "required": True,
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
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


@dataclass(kw_only=True)
class ListOfFinancialInstitutions:
    list_of_fiaccount: ListOfFiaccount = field(
        metadata={
            "name": "ListOfFIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FinancialInstitutionDetail:
    originating_financial_institution: OriginatingFinancialInstitution = field(
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    receiving_financial_institution: ReceivingFinancialInstitution = field(
        metadata={
            "name": "ReceivingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    list_of_financial_institutions: Optional[
        ListOfFinancialInstitutions
    ] = field(
        default=None,
        metadata={
            "name": "ListOfFinancialInstitutions",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentRequestAcknDetail:
    confirmation_id: str = field(
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    payment_document_id: PaymentDocumentId = field(
        metadata={
            "name": "PaymentDocumentID",
            "type": "Element",
            "required": True,
        }
    )
    payment_sequence_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSequenceNo",
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
    debit_amount: Optional[DebitAmount] = field(
        default=None,
        metadata={
            "name": "DebitAmount",
            "type": "Element",
        },
    )
    credit_amount: Optional[CreditAmount] = field(
        default=None,
        metadata={
            "name": "CreditAmount",
            "type": "Element",
        },
    )
    payment_party: Optional[PaymentParty] = field(
        default=None,
        metadata={
            "name": "PaymentParty",
            "type": "Element",
        },
    )
    financial_institution_detail: Optional[FinancialInstitutionDetail] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionDetail",
            "type": "Element",
        },
    )
    list_of_rate_of_exchange_detail: Optional[
        ListOfRateOfExchangeDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        },
    )
    excpetion_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExcpetionNote",
            "type": "Element",
        },
    )
    payment_request_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestNote",
            "type": "Element",
        },
    )
    list_of_payment_exception: Optional[ListOfPaymentException] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentException",
            "type": "Element",
        },
    )
    encrypted_info: Optional[EncryptedInfo] = field(
        default=None,
        metadata={
            "name": "EncryptedInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPaymentRequestAcknDetail:
    payment_request_ackn_detail: List[PaymentRequestAcknDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRequestAcknDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRequestAcknowledgment:
    payment_request_ackn_header: PaymentRequestAcknHeader = field(
        metadata={
            "name": "PaymentRequestAcknHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_request_ackn_detail: ListOfPaymentRequestAcknDetail = (
        field(
            metadata={
                "name": "ListOfPaymentRequestAcknDetail",
                "type": "Element",
                "required": True,
            }
        )
    )
    payment_request_ackn_summary: PaymentRequestAcknSummary = field(
        metadata={
            "name": "PaymentRequestAcknSummary",
            "type": "Element",
            "required": True,
        }
    )
