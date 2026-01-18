from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.fxrate_response import (
    ComputationalMethodCoded,
    ComputationalMethodCodedOther,
    FxquoteTypeCoded,
    FxquoteTypeCodedOther,
    FxrateRequestId,
    FxrateRequestSummary,
    IndicativeIndicator,
)
from xcbl.models.payment_status_response import (
    CreditAmount,
    DebitAmount,
    OriginatingFinancialInstitution,
    SequenceNumber,
    SettlementAmount,
)
from xcbl.models.remittance_advice import (
    PayeeParty,
    PayerParty,
)
from xcbl.models.request_for_quotation import (
    CardInfo,
    PaymentMeanCoded,
    PaymentMeanCodedOther,
)
from xcbl.models.sourcing_result import (
    ListOfReference,
    ReferenceCurrency,
    TargetCurrency,
)
from xcbl.models.sourcing_result_response import GeneralNote
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class FxrateRequestIssueDate:
    class Meta:
        name = "FXRateRequestIssueDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxrateRequestNote:
    class Meta:
        name = "FXRateRequestNote"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxrateRequestHeader:
    class Meta:
        name = "FXRateRequestHeader"

    fxrate_request_id: FxrateRequestId = field(
        metadata={
            "name": "FXRateRequestID",
            "type": "Element",
            "required": True,
        }
    )
    fxrate_request_issue_date: FxrateRequestIssueDate = field(
        metadata={
            "name": "FXRateRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean_coded: PaymentMeanCoded | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
        },
    )
    payment_mean_coded_other: PaymentMeanCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        },
    )
    payer_party: PayerParty | None = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        },
    )
    indicative_indicator: IndicativeIndicator = field(
        metadata={
            "name": "IndicativeIndicator",
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
class RateQuoteId:
    class Meta:
        name = "RateQuoteID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FxrateRequestDetail:
    class Meta:
        name = "FXRateRequestDetail"

    sequence_number: SequenceNumber | None = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
            "type": "Element",
        },
    )
    rate_quote_id: RateQuoteId | None = field(
        default=None,
        metadata={
            "name": "RateQuoteID",
            "type": "Element",
        },
    )
    reference_currency: ReferenceCurrency = field(
        metadata={
            "name": "ReferenceCurrency",
            "type": "Element",
            "required": True,
        }
    )
    target_currency: TargetCurrency = field(
        metadata={
            "name": "TargetCurrency",
            "type": "Element",
            "required": True,
        }
    )
    settlement_amount: SettlementAmount = field(
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
            "required": True,
        }
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
    card_info: CardInfo | None = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        },
    )
    computational_method_coded: ComputationalMethodCoded | None = field(
        default=None,
        metadata={
            "name": "ComputationalMethodCoded",
            "type": "Element",
        },
    )
    computational_method_coded_other: ComputationalMethodCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "ComputationalMethodCodedOther",
                "type": "Element",
            },
        )
    )
    fxquote_type_coded: FxquoteTypeCoded | None = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCoded",
            "type": "Element",
        },
    )
    fxquote_type_coded_other: FxquoteTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCodedOther",
            "type": "Element",
        },
    )
    list_of_reference: ListOfReference | None = field(
        default=None,
        metadata={
            "name": "ListOfReference",
            "type": "Element",
        },
    )
    payee_party: PayeeParty | None = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
        },
    )
    payer_party: PayerParty | None = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        },
    )
    fxrate_request_note: FxrateRequestNote | None = field(
        default=None,
        metadata={
            "name": "FXRateRequestNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfFxrateRequestDetail:
    class Meta:
        name = "ListOfFXRateRequestDetail"

    fxrate_request_detail: list[FxrateRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "FXRateRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class FxrateRequest:
    class Meta:
        name = "FXRateRequest"

    fxrate_request_header: FxrateRequestHeader = field(
        metadata={
            "name": "FXRateRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_fxrate_request_detail: ListOfFxrateRequestDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfFXRateRequestDetail",
            "type": "Element",
        },
    )
    fxrate_request_summary: FxrateRequestSummary | None = field(
        default=None,
        metadata={
            "name": "FXRateRequestSummary",
            "type": "Element",
        },
    )
