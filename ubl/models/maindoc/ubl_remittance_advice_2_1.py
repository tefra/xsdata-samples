from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    AdditionalDocumentReference,
    BillingReference,
    InvoicePeriod,
    PayeeParty,
    PaymentMeans,
    RemittanceAdviceLine,
    Signature,
    TaxTotal,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    CustomizationId,
    DocumentCurrencyCode,
    Id,
    InvoicingPartyReference,
    LineCountNumeric,
    Note,
    PayerReference,
    PaymentOrderReference,
    ProfileExecutionId,
    ProfileId,
    TotalCreditAmount,
    TotalDebitAmount,
    TotalPaymentAmount,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2"


@dataclass
class RemittanceAdviceType:
    ublextensions: Optional[Ublextensions] = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        }
    )
    ublversion_id: Optional[UblversionId] = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customization_id: Optional[CustomizationId] = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    profile_id: Optional[ProfileId] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    profile_execution_id: Optional[ProfileExecutionId] = field(
        default=None,
        metadata={
            "name": "ProfileExecutionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    copy_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_currency_code: Optional[DocumentCurrencyCode] = field(
        default=None,
        metadata={
            "name": "DocumentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_debit_amount: Optional[TotalDebitAmount] = field(
        default=None,
        metadata={
            "name": "TotalDebitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_credit_amount: Optional[TotalCreditAmount] = field(
        default=None,
        metadata={
            "name": "TotalCreditAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_payment_amount: Optional[TotalPaymentAmount] = field(
        default=None,
        metadata={
            "name": "TotalPaymentAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_order_reference: Optional[PaymentOrderReference] = field(
        default=None,
        metadata={
            "name": "PaymentOrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payer_reference: Optional[PayerReference] = field(
        default=None,
        metadata={
            "name": "PayerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoicing_party_reference: Optional[InvoicingPartyReference] = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_count_numeric: Optional[LineCountNumeric] = field(
        default=None,
        metadata={
            "name": "LineCountNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoice_period: List[InvoicePeriod] = field(
        default_factory=list,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: Optional[BillingReference] = field(
        default=None,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_document_reference: List[AdditionalDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_means: Optional[PaymentMeans] = field(
        default=None,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    remittance_advice_line: List[RemittanceAdviceLine] = field(
        default_factory=list,
        metadata={
            "name": "RemittanceAdviceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class RemittanceAdvice(RemittanceAdviceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:RemittanceAdvice-2"