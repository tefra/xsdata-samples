from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Language,
    ListOfReference,
    Reference,
    ReferenceCurrency,
    TargetCurrency,
)
from xcbl.models.fxrate_response import (
    FxrateRequestId,
    FxrateRequestSummary,
)
from xcbl.models.order_request import CardInfo
from xcbl.models.payment_request_acknowledgment import (
    CreditAmount,
    DebitAmount,
    OriginatingFinancialInstitution,
    PayeeParty,
    PayerParty,
    SettlementAmount,
)


@dataclass
class FxrateRequestHeader:
    class Meta:
        name = "FXRateRequestHeader"

    fxrate_request_id: Optional[FxrateRequestId] = field(
        default=None,
        metadata={
            "name": "FXRateRequestID",
            "type": "Element",
            "required": True,
        }
    )
    fxrate_request_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "FXRateRequestIssueDate",
            "type": "Element",
            "required": True,
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
    payment_mean_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
        }
    )
    payment_mean_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        }
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        }
    )
    indicative_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicativeIndicator",
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
class RateQuoteId:
    class Meta:
        name = "RateQuoteID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FxrateRequestDetail:
    class Meta:
        name = "FXRateRequestDetail"

    sequence_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        }
    )
    rate_quote_id: Optional[RateQuoteId] = field(
        default=None,
        metadata={
            "name": "RateQuoteID",
            "type": "Element",
        }
    )
    reference_currency: Optional[ReferenceCurrency] = field(
        default=None,
        metadata={
            "name": "ReferenceCurrency",
            "type": "Element",
            "required": True,
        }
    )
    target_currency: Optional[TargetCurrency] = field(
        default=None,
        metadata={
            "name": "TargetCurrency",
            "type": "Element",
            "required": True,
        }
    )
    settlement_amount: Optional[SettlementAmount] = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
            "required": True,
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
    card_info: Optional[CardInfo] = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        }
    )
    computational_method_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComputationalMethodCoded",
            "type": "Element",
        }
    )
    computational_method_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ComputationalMethodCodedOther",
            "type": "Element",
        }
    )
    fxquote_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCoded",
            "type": "Element",
        }
    )
    fxquote_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCodedOther",
            "type": "Element",
        }
    )
    list_of_reference: Optional[ListOfReference] = field(
        default=None,
        metadata={
            "name": "ListOfReference",
            "type": "Element",
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
        }
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        }
    )
    fxrate_request_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "FXRateRequestNote",
            "type": "Element",
        }
    )


@dataclass
class ListOfFxrateRequestDetail:
    class Meta:
        name = "ListOfFXRateRequestDetail"

    fxrate_request_detail: List[FxrateRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "FXRateRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class FxrateRequest:
    class Meta:
        name = "FXRateRequest"

    fxrate_request_header: Optional[FxrateRequestHeader] = field(
        default=None,
        metadata={
            "name": "FXRateRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_fxrate_request_detail: Optional[ListOfFxrateRequestDetail] = field(
        default=None,
        metadata={
            "name": "ListOfFXRateRequestDetail",
            "type": "Element",
        }
    )
    fxrate_request_summary: Optional[FxrateRequestSummary] = field(
        default=None,
        metadata={
            "name": "FXRateRequestSummary",
            "type": "Element",
        }
    )
