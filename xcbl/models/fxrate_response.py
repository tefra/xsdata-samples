from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.payment_status_response import (
    ConfirmationId,
    CreditAmount,
    DebitAmount,
    FxvalueDate,
    ListOfOtherPaymentInfo,
    ListOfPaymentException,
    OriginatingFinancialInstitution,
    SendingParty,
    SequenceNumber,
    SettlementAmount,
)
from xcbl.models.remittance_advice import (
    CertificateAuthority,
    PayeeParty,
    PayerParty,
)
from xcbl.models.request_for_quotation import CardInfo
from xcbl.models.sourcing_result import (
    ListOfDateCoded,
    ListOfReference,
    MonetaryValue,
    ReferenceCurrency,
    TargetCurrency,
)
from xcbl.models.sourcing_result_response import GeneralNote
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Language


@dataclass(kw_only=True)
class Achindicator:
    class Meta:
        name = "ACHIndicator"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ComputationalMethodCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ComputationalMethodCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CurrencyDecimalPlaces:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CurrentDateTime:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxquoteTypeCoded:
    class Meta:
        name = "FXQuoteTypeCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxquoteTypeCodedOther:
    class Meta:
        name = "FXQuoteTypeCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Fxrate:
    class Meta:
        name = "FXRate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxrateResponseIssueDate:
    class Meta:
        name = "FXRateResponseIssueDate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxrateResponseNote:
    class Meta:
        name = "FXRateResponseNote"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxtransactionTypeCoded:
    class Meta:
        name = "FXTransactionTypeCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FxtransactionTypeCodedOther:
    class Meta:
        name = "FXTransactionTypeCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FeeType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FundsTransferIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IndicativeIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IndicativeRateRetrievedDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InverseFxrate:
    class Meta:
        name = "InverseFXRate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NumberOfFxrateRequest:
    class Meta:
        name = "NumberOfFXRateRequest"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OnsiteCheckIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OtherPaymentServiceNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class QuoteExpirationDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemitCurrencyIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemittanceDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemoteCheckIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CurrencyAvailabilityCheckList:
    funds_transfer_indicator: None | FundsTransferIndicator = field(
        default=None,
        metadata={
            "name": "FundsTransferIndicator",
            "type": "Element",
        },
    )
    remote_check_indicator: None | RemoteCheckIndicator = field(
        default=None,
        metadata={
            "name": "RemoteCheckIndicator",
            "type": "Element",
        },
    )
    onsite_check_indicator: None | OnsiteCheckIndicator = field(
        default=None,
        metadata={
            "name": "OnsiteCheckIndicator",
            "type": "Element",
        },
    )
    achindicator: None | Achindicator = field(
        default=None,
        metadata={
            "name": "ACHIndicator",
            "type": "Element",
        },
    )
    remit_currency_indicator: None | RemitCurrencyIndicator = field(
        default=None,
        metadata={
            "name": "RemitCurrencyIndicator",
            "type": "Element",
        },
    )
    other_payment_service_note: None | OtherPaymentServiceNote = field(
        default=None,
        metadata={
            "name": "OtherPaymentServiceNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Fxamounts:
    class Meta:
        name = "FXAmounts"

    settlement_amount: None | SettlementAmount = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
        },
    )
    debit_amount: DebitAmount = field(
        metadata={
            "name": "DebitAmount",
            "type": "Element",
            "required": True,
        }
    )
    credit_amount: None | CreditAmount = field(
        default=None,
        metadata={
            "name": "CreditAmount",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Fxdates:
    class Meta:
        name = "FXDates"

    fxvalue_date: None | FxvalueDate = field(
        default=None,
        metadata={
            "name": "FXValueDate",
            "type": "Element",
        },
    )
    remittance_date: None | RemittanceDate = field(
        default=None,
        metadata={
            "name": "RemittanceDate",
            "type": "Element",
        },
    )
    quote_expiration_date: None | QuoteExpirationDate = field(
        default=None,
        metadata={
            "name": "QuoteExpirationDate",
            "type": "Element",
        },
    )
    list_of_date_coded: None | ListOfDateCoded = field(
        default=None,
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FxidentificationData:
    class Meta:
        name = "FXIdentificationData"

    originating_financial_institution: (
        None | OriginatingFinancialInstitution
    ) = field(
        default=None,
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
        },
    )
    card_info: None | CardInfo = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        },
    )
    payee_party: None | PayeeParty = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FxrateRequestId:
    class Meta:
        name = "FXRateRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FxrateRequestSummary:
    class Meta:
        name = "FXRateRequestSummary"

    number_of_fxrate_request: None | NumberOfFxrateRequest = field(
        default=None,
        metadata={
            "name": "NumberOfFXRateRequest",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FxrateResponseId:
    class Meta:
        name = "FXRateResponseID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FxreferenceNumber:
    class Meta:
        name = "FXReferenceNumber"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FeeValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentReference:
    list_of_reference: ListOfReference = field(
        metadata={
            "name": "ListOfReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RateRequestId:
    class Meta:
        name = "RateRequestID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FxrateResponseHeader:
    class Meta:
        name = "FXRateResponseHeader"

    fxrate_response_id: FxrateResponseId = field(
        metadata={
            "name": "FXRateResponseID",
            "type": "Element",
            "required": True,
        }
    )
    fxrate_response_issue_date: FxrateResponseIssueDate = field(
        metadata={
            "name": "FXRateResponseIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    fxrate_request_id: FxrateRequestId = field(
        metadata={
            "name": "FXRateRequestID",
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
    sending_party: None | SendingParty = field(
        default=None,
        metadata={
            "name": "SendingParty",
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
    general_note: None | GeneralNote = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FxrateResponseSummary:
    class Meta:
        name = "FXRateResponseSummary"

    fxrate_request_summary: FxrateRequestSummary = field(
        metadata={
            "name": "FXRateRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Fee:
    fee_type: None | FeeType = field(
        default=None,
        metadata={
            "name": "FeeType",
            "type": "Element",
        },
    )
    fee_value: None | FeeValue = field(
        default=None,
        metadata={
            "name": "FeeValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class IndicativeRateDetail:
    currency_decimal_places: None | CurrencyDecimalPlaces = field(
        default=None,
        metadata={
            "name": "CurrencyDecimalPlaces",
            "type": "Element",
        },
    )
    currency_availability_check_list: None | CurrencyAvailabilityCheckList = (
        field(
            default=None,
            metadata={
                "name": "CurrencyAvailabilityCheckList",
                "type": "Element",
            },
        )
    )
    indicative_rate_retrieved_date: None | IndicativeRateRetrievedDate = field(
        default=None,
        metadata={
            "name": "IndicativeRateRetrievedDate",
            "type": "Element",
        },
    )
    current_date_time: None | CurrentDateTime = field(
        default=None,
        metadata={
            "name": "CurrentDateTime",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfFee:
    fee: list[Fee] = field(
        default_factory=list,
        metadata={
            "name": "Fee",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SpotRateDetail:
    rate_request_id: RateRequestId = field(
        metadata={
            "name": "RateRequestID",
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
    fxidentification_data: None | FxidentificationData = field(
        default=None,
        metadata={
            "name": "FXIdentificationData",
            "type": "Element",
        },
    )
    target_currency: None | TargetCurrency = field(
        default=None,
        metadata={
            "name": "TargetCurrency",
            "type": "Element",
        },
    )
    fxreference_number: None | FxreferenceNumber = field(
        default=None,
        metadata={
            "name": "FXReferenceNumber",
            "type": "Element",
        },
    )
    fxamounts: Fxamounts = field(
        metadata={
            "name": "FXAmounts",
            "type": "Element",
            "required": True,
        }
    )
    list_of_fee: None | ListOfFee = field(
        default=None,
        metadata={
            "name": "ListOfFee",
            "type": "Element",
        },
    )
    fxtransaction_type_coded: None | FxtransactionTypeCoded = field(
        default=None,
        metadata={
            "name": "FXTransactionTypeCoded",
            "type": "Element",
        },
    )
    fxtransaction_type_coded_other: None | FxtransactionTypeCodedOther = field(
        default=None,
        metadata={
            "name": "FXTransactionTypeCodedOther",
            "type": "Element",
        },
    )
    fxquote_type_coded: None | FxquoteTypeCoded = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCoded",
            "type": "Element",
        },
    )
    fxquote_type_coded_other: None | FxquoteTypeCodedOther = field(
        default=None,
        metadata={
            "name": "FXQuoteTypeCodedOther",
            "type": "Element",
        },
    )
    fxdates: None | Fxdates = field(
        default=None,
        metadata={
            "name": "FXDates",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FxrateResponseDetail:
    class Meta:
        name = "FXRateResponseDetail"

    sequence_number: None | SequenceNumber = field(
        default=None,
        metadata={
            "name": "SequenceNumber",
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
    computational_method_coded: None | ComputationalMethodCoded = field(
        default=None,
        metadata={
            "name": "ComputationalMethodCoded",
            "type": "Element",
        },
    )
    computational_method_coded_other: None | ComputationalMethodCodedOther = (
        field(
            default=None,
            metadata={
                "name": "ComputationalMethodCodedOther",
                "type": "Element",
            },
        )
    )
    fxrate: Fxrate = field(
        metadata={
            "name": "FXRate",
            "type": "Element",
            "required": True,
        }
    )
    inverse_fxrate: None | InverseFxrate = field(
        default=None,
        metadata={
            "name": "InverseFXRate",
            "type": "Element",
        },
    )
    payer_party: None | PayerParty = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        },
    )
    indicative_rate_detail: None | IndicativeRateDetail = field(
        default=None,
        metadata={
            "name": "IndicativeRateDetail",
            "type": "Element",
        },
    )
    spot_rate_detail: None | SpotRateDetail = field(
        default=None,
        metadata={
            "name": "SpotRateDetail",
            "type": "Element",
        },
    )
    list_of_payment_reference: None | ListOfPaymentReference = field(
        default=None,
        metadata={
            "name": "ListOfPaymentReference",
            "type": "Element",
        },
    )
    list_of_other_payment_info: None | ListOfOtherPaymentInfo = field(
        default=None,
        metadata={
            "name": "ListOfOtherPaymentInfo",
            "type": "Element",
        },
    )
    list_of_payment_exception: None | ListOfPaymentException = field(
        default=None,
        metadata={
            "name": "ListOfPaymentException",
            "type": "Element",
        },
    )
    certificate_authority: None | CertificateAuthority = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        },
    )
    fxrate_response_note: None | FxrateResponseNote = field(
        default=None,
        metadata={
            "name": "FXRateResponseNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfFxrateResponseDetail:
    class Meta:
        name = "ListOfFXRateResponseDetail"

    fxrate_response_detail: list[FxrateResponseDetail] = field(
        default_factory=list,
        metadata={
            "name": "FXRateResponseDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class FxrateResponse:
    class Meta:
        name = "FXRateResponse"

    fxrate_response_header: FxrateResponseHeader = field(
        metadata={
            "name": "FXRateResponseHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_fxrate_response_detail: ListOfFxrateResponseDetail = field(
        metadata={
            "name": "ListOfFXRateResponseDetail",
            "type": "Element",
            "required": True,
        }
    )
    fxrate_response_summary: None | FxrateResponseSummary = field(
        default=None,
        metadata={
            "name": "FXRateResponseSummary",
            "type": "Element",
        },
    )
