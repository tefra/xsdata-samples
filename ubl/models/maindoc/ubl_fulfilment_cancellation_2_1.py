from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AdditionalDocumentReference,
    BuyerCustomerParty,
    Contract,
    DeliveryCustomerParty,
    DespatchDocumentReference,
    DespatchSupplierParty,
    OrderReference,
    OriginatorCustomerParty,
    ReceiptDocumentReference,
    SellerSupplierParty,
    Signature,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    CancellationNote,
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:FulfilmentCancellation-2"
)


@dataclass(frozen=True, kw_only=True)
class FulfilmentCancellationType:
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
    id: Id = field(
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
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
    issue_time: None | IssueTime = field(
        default=None,
        metadata={
            "name": "IssueTime",
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
    cancellation_note: tuple[CancellationNote, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CancellationNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "min_occurs": 1,
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
    order_reference: tuple[OrderReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderReference",
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
    contract: tuple[Contract, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    signature: tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_customer_party: BuyerCustomerParty = field(
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    seller_supplier_party: SellerSupplierParty = field(
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    delivery_customer_party: None | DeliveryCustomerParty = field(
        default=None,
        metadata={
            "name": "DeliveryCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_supplier_party: None | DespatchSupplierParty = field(
        default=None,
        metadata={
            "name": "DespatchSupplierParty",
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


@dataclass(frozen=True, kw_only=True)
class FulfilmentCancellation(FulfilmentCancellationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:FulfilmentCancellation-2"
