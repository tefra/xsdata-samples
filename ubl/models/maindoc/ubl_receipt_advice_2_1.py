from dataclasses import dataclass, field
from typing import Optional

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AdditionalDocumentReference,
    BuyerCustomerParty,
    DeliveryCustomerParty,
    DespatchDocumentReference,
    DespatchSupplierParty,
    OrderReference,
    ReceiptLine,
    SellerSupplierParty,
    Shipment,
    Signature,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    CopyIndicator,
    CustomizationId,
    DocumentStatusCode,
    Id,
    IssueDate,
    IssueTime,
    LineCountNumeric,
    Note,
    ProfileExecutionId,
    ProfileId,
    ReceiptAdviceTypeCode,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:ReceiptAdvice-2"


@dataclass(frozen=True)
class ReceiptAdviceType:
    ublextensions: Optional[Ublextensions] = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    ublversion_id: Optional[UblversionId] = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customization_id: Optional[CustomizationId] = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_id: Optional[ProfileId] = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_execution_id: Optional[ProfileExecutionId] = field(
        default=None,
        metadata={
            "name": "ProfileExecutionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    copy_indicator: Optional[CopyIndicator] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_status_code: Optional[DocumentStatusCode] = field(
        default=None,
        metadata={
            "name": "DocumentStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    receipt_advice_type_code: Optional[ReceiptAdviceTypeCode] = field(
        default=None,
        metadata={
            "name": "ReceiptAdviceTypeCode",
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
    line_count_numeric: Optional[LineCountNumeric] = field(
        default=None,
        metadata={
            "name": "LineCountNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_reference: tuple[OrderReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderReference",
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
    delivery_customer_party: Optional[DeliveryCustomerParty] = field(
        default=None,
        metadata={
            "name": "DeliveryCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    despatch_supplier_party: Optional[DespatchSupplierParty] = field(
        default=None,
        metadata={
            "name": "DespatchSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_line: tuple[ReceiptLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceiptLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ReceiptAdvice(ReceiptAdviceType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:ReceiptAdvice-2"
        )
