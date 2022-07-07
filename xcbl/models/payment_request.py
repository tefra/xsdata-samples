from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Attachment,
    ContactNumber,
    CorrespondenceLanguage,
    Country,
    Currency,
    Language,
    ListOfIdentifier,
    ListOfReferenceCoded,
    NameAddress,
    OrderContact,
    OtherContacts,
    Party,
    PartyId,
    Purpose,
    ReceivingContact,
    Reference,
    ReferenceCoded,
    ShippingContact,
)
from xcbl.models.invoice import InvoiceItemDetail
from xcbl.models.order_request import (
    AccountDetail,
    BillToParty,
    BuyerParty,
    CardInfo,
    FinancialInstitution,
    ListOfPartyCoded,
    MonetaryValue,
    PaymentMeanReference,
)
from xcbl.models.payment_request_acknowledgment import (
    FinancialInstitutionDetail,
    ListOfRateOfExchangeDetail,
    OriginatingFinancialInstitution,
    PayeeParty,
    PayerParty,
    PaymentDocumentId,
    PaymentRequestSummary,
    ReceivingFinancialInstitution,
    SettlementAmount,
    SupplierParty,
)
from xcbl.models.payment_status_response import (
    PaymentDates,
    PaymentRequestId,
)


@dataclass
class ActualAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class AdjustmentAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChargeAccount:
    account_detail: Optional[AccountDetail] = field(
        default=None,
        metadata={
            "name": "AccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ChargeFinancialInstitution:
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Company:
    party_id: Optional[PartyId] = field(
        default=None,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    industry_sector_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndustrySectorCoded",
            "type": "Element",
        }
    )
    industry_sector_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndustrySectorCodedOther",
            "type": "Element",
        }
    )


@dataclass
class ExpectedAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FeeAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoicingDetailAmountDue:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoicingDetailAmountPaid:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoicingDetailReference:
    reference_coded: Optional[ReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class InvoicingItemDetail:
    invoice_item_detail: Optional[InvoiceItemDetail] = field(
        default=None,
        metadata={
            "name": "InvoiceItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LegalReportingInvoicedAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LegalReportingPayeeCountry:
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LegalReportingPaymentAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class LegalReportingSupplyingCountry:
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OriginatingFispecificId:
    class Meta:
        name = "OriginatingFISpecificID"

    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentDetailAttachment:
    attachment: Optional[Attachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentReference:
    list_of_reference_coded: Optional[ListOfReferenceCoded] = field(
        default=None,
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestAttachment:
    attachment: Optional[Attachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestParty:
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        }
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class PaymentRequestPurpose:
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReceivingFispecificId:
    class Meta:
        name = "ReceivingFISpecificID"

    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class RemittanceAdviceId:
    class Meta:
        name = "RemittanceAdviceID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SettlementCurrency:
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Adjustment:
    line_item_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemReference",
            "type": "Element",
        }
    )
    adjustment_reason_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustmentReasonCoded",
            "type": "Element",
            "required": True,
        }
    )
    adjustment_reason_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustmentReasonCodedOther",
            "type": "Element",
        }
    )
    adjustment_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustmentDate",
            "type": "Element",
        }
    )
    expected_amount: Optional[ExpectedAmount] = field(
        default=None,
        metadata={
            "name": "ExpectedAmount",
            "type": "Element",
        }
    )
    adjustment_amount: Optional[AdjustmentAmount] = field(
        default=None,
        metadata={
            "name": "AdjustmentAmount",
            "type": "Element",
        }
    )
    adjustment_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustmentPercent",
            "type": "Element",
        }
    )
    actual_amount: Optional[ActualAmount] = field(
        default=None,
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "required": True,
        }
    )
    adjustment_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdjustmentNote",
            "type": "Element",
        }
    )


@dataclass
class FinancialChargesAllocation:
    charge_regulation_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChargeRegulationCoded",
            "type": "Element",
            "required": True,
        }
    )
    charge_regulation_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChargeRegulationCodedOther",
            "type": "Element",
        }
    )
    fee_amount: Optional[FeeAmount] = field(
        default=None,
        metadata={
            "name": "FeeAmount",
            "type": "Element",
        }
    )
    charge_account: Optional[ChargeAccount] = field(
        default=None,
        metadata={
            "name": "ChargeAccount",
            "type": "Element",
        }
    )
    charge_financial_institution: Optional[ChargeFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "ChargeFinancialInstitution",
            "type": "Element",
        }
    )


@dataclass
class LegalReportingParty:
    company: Optional[Company] = field(
        default=None,
        metadata={
            "name": "Company",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestHeader:
    payment_request_purpose: Optional[PaymentRequestPurpose] = field(
        default=None,
        metadata={
            "name": "PaymentRequestPurpose",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_id: Optional[PaymentRequestId] = field(
        default=None,
        metadata={
            "name": "PaymentRequestID",
            "type": "Element",
            "required": True,
        }
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
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
    general_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNotes",
            "type": "Element",
        }
    )
    payment_request_attachment: Optional[PaymentRequestAttachment] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAttachment",
            "type": "Element",
        }
    )


@dataclass
class LegalReportingInformation:
    legal_reporting_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalReportingIndicator",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_supplemental_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalReportingSupplementalCode",
            "type": "Element",
        }
    )
    legal_reporting_party: Optional[LegalReportingParty] = field(
        default=None,
        metadata={
            "name": "LegalReportingParty",
            "type": "Element",
        }
    )
    legal_reporting_invoiced_amount: Optional[LegalReportingInvoicedAmount] = field(
        default=None,
        metadata={
            "name": "LegalReportingInvoicedAmount",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_payment_amount: Optional[LegalReportingPaymentAmount] = field(
        default=None,
        metadata={
            "name": "LegalReportingPaymentAmount",
            "type": "Element",
        }
    )
    legal_reporting_supplying_country: Optional[LegalReportingSupplyingCountry] = field(
        default=None,
        metadata={
            "name": "LegalReportingSupplyingCountry",
            "type": "Element",
        }
    )
    legal_reporting_payee_country: Optional[LegalReportingPayeeCountry] = field(
        default=None,
        metadata={
            "name": "LegalReportingPayeeCountry",
            "type": "Element",
        }
    )
    legal_reporting_import_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalReportingImportDate",
            "type": "Element",
        }
    )
    legal_reporting_payment_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalReportingPaymentDate",
            "type": "Element",
        }
    )
    legal_reporting_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "LegalReportingDescription",
            "type": "Element",
        }
    )


@dataclass
class ListOfAdjustments:
    adjustment: List[Adjustment] = field(
        default_factory=list,
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class InvoicingDetail:
    invoicing_detail_reference: Optional[InvoicingDetailReference] = field(
        default=None,
        metadata={
            "name": "InvoicingDetailReference",
            "type": "Element",
            "required": True,
        }
    )
    invoicing_detail_amount_due: Optional[InvoicingDetailAmountDue] = field(
        default=None,
        metadata={
            "name": "InvoicingDetailAmountDue",
            "type": "Element",
        }
    )
    invoicing_detail_amount_paid: Optional[InvoicingDetailAmountPaid] = field(
        default=None,
        metadata={
            "name": "InvoicingDetailAmountPaid",
            "type": "Element",
        }
    )
    invoicing_item_detail: Optional[InvoicingItemDetail] = field(
        default=None,
        metadata={
            "name": "InvoicingItemDetail",
            "type": "Element",
        }
    )
    list_of_adjustments: Optional[ListOfAdjustments] = field(
        default=None,
        metadata={
            "name": "ListOfAdjustments",
            "type": "Element",
        }
    )


@dataclass
class ListOfInvoicingDetail:
    invoicing_detail: List[InvoicingDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoicingDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Subsidiary:
    party_id: Optional[PartyId] = field(
        default=None,
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    list_of_invoicing_detail: Optional[ListOfInvoicingDetail] = field(
        default=None,
        metadata={
            "name": "ListOfInvoicingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfSubsidiary:
    subsidiary: List[Subsidiary] = field(
        default_factory=list,
        metadata={
            "name": "Subsidiary",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class RemittanceAdviceDetail:
    list_of_subsidiary: Optional[ListOfSubsidiary] = field(
        default=None,
        metadata={
            "name": "ListOfSubsidiary",
            "type": "Element",
            "required": True,
        }
    )
    list_of_invoicing_detail: Optional[ListOfInvoicingDetail] = field(
        default=None,
        metadata={
            "name": "ListOfInvoicingDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_adjustments: Optional[ListOfAdjustments] = field(
        default=None,
        metadata={
            "name": "ListOfAdjustments",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_id: Optional[RemittanceAdviceId] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceID",
            "type": "Element",
        }
    )
    contact_number: Optional[ContactNumber] = field(
        default=None,
        metadata={
            "name": "ContactNumber",
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
class PaymentDocumentDetail:
    remittance_advice_detail: Optional[RemittanceAdviceDetail] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentDocumentDetail:
    payment_document_detail: List[PaymentDocumentDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDocumentDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentRequestDetail:
    payment_document_id: Optional[PaymentDocumentId] = field(
        default=None,
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
        }
    )
    payment_dates: Optional[PaymentDates] = field(
        default=None,
        metadata={
            "name": "PaymentDates",
            "type": "Element",
        }
    )
    financial_institution_detail: Optional[FinancialInstitutionDetail] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionDetail",
            "type": "Element",
            "required": True,
        }
    )
    originating_financial_institution: Optional[OriginatingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    receiving_fispecific_id: List[ReceivingFispecificId] = field(
        default_factory=list,
        metadata={
            "name": "ReceivingFISpecificID",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
    originating_fispecific_id: Optional[OriginatingFispecificId] = field(
        default=None,
        metadata={
            "name": "OriginatingFISpecificID",
            "type": "Element",
            "required": True,
        }
    )
    receiving_financial_institution: Optional[ReceivingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "ReceivingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    card_info: Optional[CardInfo] = field(
        default=None,
        metadata={
            "name": "CardInfo",
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
    settlement_currency: Optional[SettlementCurrency] = field(
        default=None,
        metadata={
            "name": "SettlementCurrency",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_party: Optional[PaymentRequestParty] = field(
        default=None,
        metadata={
            "name": "PaymentRequestParty",
            "type": "Element",
            "required": True,
        }
    )
    legal_reporting_information: Optional[LegalReportingInformation] = field(
        default=None,
        metadata={
            "name": "LegalReportingInformation",
            "type": "Element",
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
    payment_urgency_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentUrgencyCoded",
            "type": "Element",
        }
    )
    payment_urgency_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentUrgencyCodedOther",
            "type": "Element",
        }
    )
    international_payment_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "InternationalPaymentIndicator",
            "type": "Element",
        }
    )
    intra_company_payment_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntraCompanyPaymentIndicator",
            "type": "Element",
        }
    )
    payment_mean_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        }
    )
    payment_mean_reference: Optional[PaymentMeanReference] = field(
        default=None,
        metadata={
            "name": "PaymentMeanReference",
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
    payment_reference: Optional[PaymentReference] = field(
        default=None,
        metadata={
            "name": "PaymentReference",
            "type": "Element",
        }
    )
    accept_fxmarket_rate: Optional[str] = field(
        default=None,
        metadata={
            "name": "AcceptFXMarketRate",
            "type": "Element",
        }
    )
    list_of_rate_of_exchange_detail: Optional[ListOfRateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        }
    )
    payment_detail_attachment: Optional[PaymentDetailAttachment] = field(
        default=None,
        metadata={
            "name": "PaymentDetailAttachment",
            "type": "Element",
        }
    )
    payment_instruction_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentInstructionNotes",
            "type": "Element",
        }
    )
    is_credit: Optional[str] = field(
        default=None,
        metadata={
            "name": "IsCredit",
            "type": "Element",
        }
    )
    repetitive_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "RepetitiveCode",
            "type": "Element",
        }
    )
    financial_charges_allocation: Optional[FinancialChargesAllocation] = field(
        default=None,
        metadata={
            "name": "FinancialChargesAllocation",
            "type": "Element",
        }
    )
    list_of_payment_document_detail: Optional[ListOfPaymentDocumentDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentDocumentDetail",
            "type": "Element",
        }
    )


@dataclass
class ListOfPaymentRequestDetail:
    payment_request_detail: List[PaymentRequestDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRequestDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentRequest:
    payment_request_header: Optional[PaymentRequestHeader] = field(
        default=None,
        metadata={
            "name": "PaymentRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_request_detail: Optional[ListOfPaymentRequestDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentRequestDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_summary: Optional[PaymentRequestSummary] = field(
        default=None,
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )
