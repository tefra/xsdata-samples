from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AdditionalDocumentReference,
    BuyerCustomerParty,
    CatalogueDocumentReference,
    Contract,
    Delivery,
    DeliveryTerms,
    DestinationCountry,
    OriginatorCustomerParty,
    RequestedValidityPeriod,
    RequestForQuotationLine,
    SellerSupplierParty,
    Signature,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    LineCountNumeric,
    Note,
    PricingCurrencyCode,
    ProfileExecutionId,
    ProfileId,
    SubmissionDueDate,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:RequestForQuotation-2"
)


@dataclass(frozen=True, kw_only=True)
class RequestForQuotationType:
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
    issue_date: IssueDate = field(
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_time: IssueTime = field(
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    submission_due_date: None | SubmissionDueDate = field(
        default=None,
        metadata={
            "name": "SubmissionDueDate",
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
    pricing_currency_code: None | PricingCurrencyCode = field(
        default=None,
        metadata={
            "name": "PricingCurrencyCode",
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
    requested_validity_period: None | RequestedValidityPeriod = field(
        default=None,
        metadata={
            "name": "RequestedValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_document_reference: None | CatalogueDocumentReference = field(
        default=None,
        metadata={
            "name": "CatalogueDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
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
    originator_customer_party: None | OriginatorCustomerParty = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty = field(
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    buyer_customer_party: None | BuyerCustomerParty = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
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
    destination_country: None | DestinationCountry = field(
        default=None,
        metadata={
            "name": "DestinationCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract: tuple[Contract, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    request_for_quotation_line: tuple[RequestForQuotationLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RequestForQuotationLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True, kw_only=True)
class RequestForQuotation(RequestForQuotationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:RequestForQuotation-2"
