from dataclasses import dataclass, field
from typing import Optional

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AccountingCustomerParty,
    AccountingSupplierParty,
    AdditionalDocumentReference,
    BuyerCustomerParty,
    OrderReference,
    OriginatorCustomerParty,
    SellerSupplierParty,
    Signature,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    AcceptedIndicator,
    AccountingCost,
    AccountingCostCode,
    CopyIndicator,
    CustomerReference,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    ProfileExecutionId,
    ProfileId,
    RejectionNote,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:OrderResponseSimple-2"
)


@dataclass(frozen=True)
class OrderResponseSimpleType:
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
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accepted_indicator: Optional[AcceptedIndicator] = field(
        default=None,
        metadata={
            "name": "AcceptedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    rejection_note: tuple[RejectionNote, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RejectionNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customer_reference: Optional[CustomerReference] = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_reference: Optional[OrderReference] = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
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
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
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
            "required": True,
        },
    )
    originator_customer_party: Optional[OriginatorCustomerParty] = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OrderResponseSimple(OrderResponseSimpleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:OrderResponseSimple-2"
