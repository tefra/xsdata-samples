from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    AdditionalDocumentReference,
    AllowanceCharge,
    BillingReference,
    BuyerCustomerParty,
    ContractDocumentReference,
    Delivery,
    DeliveryTerms,
    DespatchDocumentReference,
    InvoiceLine,
    InvoicePeriod,
    LegalMonetaryTotal,
    OrderReference,
    OriginatorDocumentReference,
    PayeeParty,
    PaymentAlternativeExchangeRate,
    PaymentExchangeRate,
    PaymentMeans,
    PaymentTerms,
    PrepaidPayment,
    PricingExchangeRate,
    ReceiptDocumentReference,
    SellerSupplierParty,
    Signature,
    StatementDocumentReference,
    TaxExchangeRate,
    TaxRepresentativeParty,
    TaxTotal,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    AccountingCost,
    AccountingCostCode,
    CopyIndicator,
    CustomizationId,
    DocumentCurrencyCode,
    Id,
    InvoiceTypeCode,
    IssueDate,
    IssueTime,
    LineCountNumeric,
    Note,
    PaymentAlternativeCurrencyCode,
    PaymentCurrencyCode,
    PricingCurrencyCode,
    ProfileExecutionId,
    ProfileId,
    TaxCurrencyCode,
    TaxPointDate,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:SelfBilledInvoice-2"
)


@dataclass(frozen=True)
class SelfBilledInvoiceType:
    ublextensions: None | Ublextensions = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    ublversion_id: None | UblversionId = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customization_id: None | CustomizationId = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_id: None | ProfileId = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_execution_id: None | ProfileExecutionId = field(
        default=None,
        metadata={
            "name": "ProfileExecutionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    id: None | Id = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    copy_indicator: None | CopyIndicator = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: None | Uuid = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: None | IssueDate = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_time: None | IssueTime = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_point_date: None | TaxPointDate = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoice_type_code: None | InvoiceTypeCode = field(
        default=None,
        metadata={
            "name": "InvoiceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_currency_code: None | DocumentCurrencyCode = field(
        default=None,
        metadata={
            "name": "DocumentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_currency_code: None | TaxCurrencyCode = field(
        default=None,
        metadata={
            "name": "TaxCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pricing_currency_code: None | PricingCurrencyCode = field(
        default=None,
        metadata={
            "name": "PricingCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_currency_code: None | PaymentCurrencyCode = field(
        default=None,
        metadata={
            "name": "PaymentCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_alternative_currency_code: (
        None | PaymentAlternativeCurrencyCode
    ) = field(
        default=None,
        metadata={
            "name": "PaymentAlternativeCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: None | AccountingCostCode = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: None | AccountingCost = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_count_numeric: None | LineCountNumeric = field(
        default=None,
        metadata={
            "name": "LineCountNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoice_period: tuple[InvoicePeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_reference: None | OrderReference = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_document_reference: tuple[ContractDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_document_reference: tuple[DespatchDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DespatchDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_document_reference: tuple[ReceiptDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceiptDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    statement_document_reference: tuple[StatementDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "StatementDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    originator_document_reference: tuple[OriginatorDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "OriginatorDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    additional_document_reference: tuple[AdditionalDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AdditionalDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    signature: tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: None | AccountingCustomerParty = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    accounting_supplier_party: None | AccountingSupplierParty = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    buyer_customer_party: None | BuyerCustomerParty = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: None | SellerSupplierParty = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_party: None | PayeeParty = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_representative_party: None | TaxRepresentativeParty = field(
        default=None,
        metadata={
            "name": "TaxRepresentativeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: tuple[DeliveryTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_means: None | PaymentMeans = field(
        default=None,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    prepaid_payment: tuple[PrepaidPayment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PrepaidPayment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_exchange_rate: None | TaxExchangeRate = field(
        default=None,
        metadata={
            "name": "TaxExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_exchange_rate: None | PricingExchangeRate = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_exchange_rate: None | PaymentExchangeRate = field(
        default=None,
        metadata={
            "name": "PaymentExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_alternative_exchange_rate: (
        None | PaymentAlternativeExchangeRate
    ) = field(
        default=None,
        metadata={
            "name": "PaymentAlternativeExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    legal_monetary_total: None | LegalMonetaryTotal = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    invoice_line: tuple[InvoiceLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class SelfBilledInvoice(SelfBilledInvoiceType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:SelfBilledInvoice-2"
        )
