from __future__ import annotations

from dataclasses import dataclass, field

from xcbl.models.payment_request_acknowledgment import (
    FinancialInstitutionDetail,
    PaymentDocumentId,
    PaymentSequenceNo,
)
from xcbl.models.payment_status_response import (
    OriginatingFinancialInstitution,
    PaymentDates,
    PaymentRequestId,
    ReceivingFinancialInstitution,
    SettlementAmount,
)
from xcbl.models.remittance_advice import (
    IsCredit,
    ListOfRateOfExchangeDetail,
    PayeeParty,
    PayerParty,
    PaymentReasonCoded,
    PaymentReasonCodedOther,
    PaymentRequestSummary,
    RemittanceAdviceDetail,
    SupplierParty,
)
from xcbl.models.request_for_quotation import (
    AccountDetail,
    CardInfo,
    FinancialInstitution,
    PaymentMeanCoded,
    PaymentMeanCodedOther,
    PaymentMeanReference,
    PaymentSystemCoded,
    PaymentSystemCodedOther,
)
from xcbl.models.sourcing_result import (
    Attachment,
    BillToParty,
    BuyerParty,
    ListOfReferenceCoded,
    MonetaryValue,
)
from xcbl.models.sourcing_result_response import Purpose
from xcbl.models.time_series_response import (
    ListOfIdentifier,
    ListOfPartyCoded,
    Mdfbusiness,
    NameAddress,
    OrderContact,
    OtherContacts,
    Party,
    PartyId,
    ReceivingContact,
    ShippingContact,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_user_information import (
    CorrespondenceLanguage,
    Country,
    GeneralNotes,
    Language,
)


@dataclass(kw_only=True)
class AcceptFxmarketRate:
    class Meta:
        name = "AcceptFXMarketRate"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChargeRegulationCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChargeRegulationCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IndustrySectorCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IndustrySectorCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InternationalPaymentIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IntraCompanyPaymentIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LegalReportingDescription:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LegalReportingImportDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LegalReportingIndicator:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LegalReportingPaymentDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LegalReportingSupplementalCode:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentInstructionNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentRequestIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentUrgencyCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentUrgencyCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RepetitiveCode:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ChargeAccount:
    account_detail: AccountDetail = field(
        metadata={
            "name": "AccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ChargeFinancialInstitution:
    financial_institution: FinancialInstitution = field(
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Company:
    party_id: PartyId = field(
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: ListOfIdentifier | None = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        },
    )
    mdfbusiness: Mdfbusiness | None = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: NameAddress | None = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: OrderContact | None = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: ReceivingContact | None = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: ShippingContact | None = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: OtherContacts | None = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: CorrespondenceLanguage | None = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    industry_sector_coded: IndustrySectorCoded | None = field(
        default=None,
        metadata={
            "name": "IndustrySectorCoded",
            "type": "Element",
        },
    )
    industry_sector_coded_other: IndustrySectorCodedOther | None = field(
        default=None,
        metadata={
            "name": "IndustrySectorCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FeeAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LegalReportingInvoicedAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LegalReportingPayeeCountry:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LegalReportingPaymentAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LegalReportingSupplyingCountry:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginatingFispecificId:
    class Meta:
        name = "OriginatingFISpecificID"

    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentDetailAttachment:
    attachment: Attachment = field(
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentDocumentDetail:
    remittance_advice_detail: RemittanceAdviceDetail = field(
        metadata={
            "name": "RemittanceAdviceDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentReference:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentRequestAttachment:
    attachment: Attachment = field(
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentRequestParty:
    payer_party: PayerParty | None = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        },
    )
    payee_party: PayeeParty = field(
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_party: BuyerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    supplier_party: SupplierParty | None = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
        },
    )
    bill_to_party: BillToParty | None = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    list_of_party_coded: ListOfPartyCoded | None = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentRequestPurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceivingFispecificId:
    class Meta:
        name = "ReceivingFISpecificID"

    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SettlementCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FinancialChargesAllocation:
    charge_regulation_coded: ChargeRegulationCoded = field(
        metadata={
            "name": "ChargeRegulationCoded",
            "type": "Element",
            "required": True,
        }
    )
    charge_regulation_coded_other: ChargeRegulationCodedOther | None = field(
        default=None,
        metadata={
            "name": "ChargeRegulationCodedOther",
            "type": "Element",
        },
    )
    fee_amount: FeeAmount | None = field(
        default=None,
        metadata={
            "name": "FeeAmount",
            "type": "Element",
        },
    )
    charge_account: ChargeAccount | None = field(
        default=None,
        metadata={
            "name": "ChargeAccount",
            "type": "Element",
        },
    )
    charge_financial_institution: ChargeFinancialInstitution | None = field(
        default=None,
        metadata={
            "name": "ChargeFinancialInstitution",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LegalReportingParty:
    company: Company = field(
        metadata={
            "name": "Company",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfPaymentDocumentDetail:
    payment_document_detail: list[PaymentDocumentDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDocumentDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRequestHeader:
    payment_request_purpose: PaymentRequestPurpose = field(
        metadata={
            "name": "PaymentRequestPurpose",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_issue_date: PaymentRequestIssueDate = field(
        metadata={
            "name": "PaymentRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_id: PaymentRequestId = field(
        metadata={
            "name": "PaymentRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payer_party: PayerParty = field(
        metadata={
            "name": "PayerParty",
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
    general_notes: GeneralNotes | None = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        },
    )
    payment_request_attachment: PaymentRequestAttachment | None = field(
        default=None,
        metadata={
            "name": "PaymentRequestAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LegalReportingInformation:
    legal_reporting_indicator: LegalReportingIndicator = field(
        metadata={
            "name": "LegalReportingIndicator",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_supplemental_code: (
        LegalReportingSupplementalCode | None
    ) = field(
        default=None,
        metadata={
            "name": "LegalReportingSupplementalCode",
            "type": "Element",
        },
    )
    legal_reporting_party: LegalReportingParty | None = field(
        default=None,
        metadata={
            "name": "LegalReportingParty",
            "type": "Element",
        },
    )
    legal_reporting_invoiced_amount: LegalReportingInvoicedAmount = field(
        metadata={
            "name": "LegalReportingInvoicedAmount",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_payment_amount: LegalReportingPaymentAmount | None = field(
        default=None,
        metadata={
            "name": "LegalReportingPaymentAmount",
            "type": "Element",
        },
    )
    legal_reporting_supplying_country: (
        LegalReportingSupplyingCountry | None
    ) = field(
        default=None,
        metadata={
            "name": "LegalReportingSupplyingCountry",
            "type": "Element",
        },
    )
    legal_reporting_payee_country: LegalReportingPayeeCountry | None = field(
        default=None,
        metadata={
            "name": "LegalReportingPayeeCountry",
            "type": "Element",
        },
    )
    legal_reporting_import_date: LegalReportingImportDate | None = field(
        default=None,
        metadata={
            "name": "LegalReportingImportDate",
            "type": "Element",
        },
    )
    legal_reporting_payment_date: LegalReportingPaymentDate | None = field(
        default=None,
        metadata={
            "name": "LegalReportingPaymentDate",
            "type": "Element",
        },
    )
    legal_reporting_description: LegalReportingDescription | None = field(
        default=None,
        metadata={
            "name": "LegalReportingDescription",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentRequestDetail:
    payment_document_id: PaymentDocumentId = field(
        metadata={
            "name": "PaymentDocumentID",
            "type": "Element",
            "required": True,
        }
    )
    payment_sequence_no: PaymentSequenceNo | None = field(
        default=None,
        metadata={
            "name": "PaymentSequenceNo",
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
    financial_institution_detail: FinancialInstitutionDetail | None = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionDetail",
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
    receiving_fispecific_id: list[ReceivingFispecificId] = field(
        default_factory=list,
        metadata={
            "name": "ReceivingFISpecificID",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    originating_fispecific_id: OriginatingFispecificId | None = field(
        default=None,
        metadata={
            "name": "OriginatingFISpecificID",
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
    settlement_amount: SettlementAmount = field(
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
            "required": True,
        }
    )
    settlement_currency: SettlementCurrency = field(
        metadata={
            "name": "SettlementCurrency",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_party: PaymentRequestParty = field(
        metadata={
            "name": "PaymentRequestParty",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_information: LegalReportingInformation | None = field(
        default=None,
        metadata={
            "name": "LegalReportingInformation",
            "type": "Element",
        },
    )
    payment_reason_coded: PaymentReasonCoded | None = field(
        default=None,
        metadata={
            "name": "PaymentReasonCoded",
            "type": "Element",
        },
    )
    payment_reason_coded_other: PaymentReasonCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentReasonCodedOther",
            "type": "Element",
        },
    )
    payment_urgency_coded: PaymentUrgencyCoded | None = field(
        default=None,
        metadata={
            "name": "PaymentUrgencyCoded",
            "type": "Element",
        },
    )
    payment_urgency_coded_other: PaymentUrgencyCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentUrgencyCodedOther",
            "type": "Element",
        },
    )
    international_payment_indicator: InternationalPaymentIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "InternationalPaymentIndicator",
                "type": "Element",
            },
        )
    )
    intra_company_payment_indicator: IntraCompanyPaymentIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "IntraCompanyPaymentIndicator",
                "type": "Element",
            },
        )
    )
    payment_mean_coded: PaymentMeanCoded = field(
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean_coded_other: PaymentMeanCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        },
    )
    payment_mean_reference: PaymentMeanReference | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanReference",
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
    payment_reference: PaymentReference | None = field(
        default=None,
        metadata={
            "name": "PaymentReference",
            "type": "Element",
        },
    )
    accept_fxmarket_rate: AcceptFxmarketRate | None = field(
        default=None,
        metadata={
            "name": "AcceptFXMarketRate",
            "type": "Element",
        },
    )
    list_of_rate_of_exchange_detail: ListOfRateOfExchangeDetail | None = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        },
    )
    payment_detail_attachment: PaymentDetailAttachment | None = field(
        default=None,
        metadata={
            "name": "PaymentDetailAttachment",
            "type": "Element",
        },
    )
    payment_instruction_notes: PaymentInstructionNotes | None = field(
        default=None,
        metadata={
            "name": "PaymentInstructionNotes",
            "type": "Element",
        },
    )
    is_credit: IsCredit | None = field(
        default=None,
        metadata={
            "name": "IsCredit",
            "type": "Element",
        },
    )
    repetitive_code: RepetitiveCode | None = field(
        default=None,
        metadata={
            "name": "RepetitiveCode",
            "type": "Element",
        },
    )
    financial_charges_allocation: FinancialChargesAllocation | None = field(
        default=None,
        metadata={
            "name": "FinancialChargesAllocation",
            "type": "Element",
        },
    )
    list_of_payment_document_detail: ListOfPaymentDocumentDetail | None = (
        field(
            default=None,
            metadata={
                "name": "ListOfPaymentDocumentDetail",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class ListOfPaymentRequestDetail:
    payment_request_detail: list[PaymentRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRequest:
    payment_request_header: PaymentRequestHeader = field(
        metadata={
            "name": "PaymentRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_request_detail: ListOfPaymentRequestDetail = field(
        metadata={
            "name": "ListOfPaymentRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_summary: PaymentRequestSummary = field(
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
