from dataclasses import dataclass, field
from typing import Optional, Tuple

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    CatalogueLine,
    ContractorCustomerParty,
    DocumentReference,
    ProviderParty,
    ReceiverParty,
    ReferencedContract,
    SellerSupplierParty,
    Signature,
    SourceCatalogueReference,
    TradingTerms,
    ValidityPeriod,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    ActionCode,
    CustomizationId,
    Description,
    Id,
    IssueDate,
    IssueTime,
    LineCountNumeric,
    Name,
    Note,
    PreviousVersionId,
    ProfileExecutionId,
    ProfileId,
    RevisionDate,
    RevisionTime,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2"


@dataclass(frozen=True)
class CatalogueType:
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
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    action_code: Optional[ActionCode] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
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
    revision_date: Optional[RevisionDate] = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revision_time: Optional[RevisionTime] = field(
        default=None,
        metadata={
            "name": "RevisionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: Tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: Tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_version_id: Optional[PreviousVersionId] = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
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
    validity_period: Tuple[ValidityPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    referenced_contract: Tuple[ReferencedContract, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReferencedContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    source_catalogue_reference: Optional[SourceCatalogueReference] = field(
        default=None,
        metadata={
            "name": "SourceCatalogueReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: Tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    signature: Tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    provider_party: Optional[ProviderParty] = field(
        default=None,
        metadata={
            "name": "ProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    receiver_party: Optional[ReceiverParty] = field(
        default=None,
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
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
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    trading_terms: Tuple[TradingTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TradingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_line: Tuple[CatalogueLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CatalogueLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class Catalogue(CatalogueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:Catalogue-2"
