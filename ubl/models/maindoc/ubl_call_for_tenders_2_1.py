from __future__ import annotations

from dataclasses import dataclass, field

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    AdditionalDocumentReference,
    ContractingParty,
    LegalDocumentReference,
    OriginatorCustomerParty,
    ProcurementProject,
    ProcurementProjectLot,
    ReceiverParty,
    Signature,
    TechnicalDocumentReference,
    TenderingProcess,
    TenderingTerms,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    ApprovalDate,
    ContractFolderId,
    CopyIndicator,
    CustomizationId,
    Id,
    IssueDate,
    IssueTime,
    Note,
    PreviousVersionId,
    ProfileExecutionId,
    ProfileId,
    UblversionId,
    Uuid,
    VersionId,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2"


@dataclass(frozen=True, kw_only=True)
class CallForTendersType:
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
    contract_folder_id: ContractFolderId = field(
        metadata={
            "name": "ContractFolderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    approval_date: None | ApprovalDate = field(
        default=None,
        metadata={
            "name": "ApprovalDate",
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
    version_id: None | VersionId = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_version_id: None | PreviousVersionId = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    legal_document_reference: None | LegalDocumentReference = field(
        default=None,
        metadata={
            "name": "LegalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    technical_document_reference: None | TechnicalDocumentReference = field(
        default=None,
        metadata={
            "name": "TechnicalDocumentReference",
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
    contracting_party: ContractingParty = field(
        metadata={
            "name": "ContractingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    originator_customer_party: tuple[OriginatorCustomerParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receiver_party: None | ReceiverParty = field(
        default=None,
        metadata={
            "name": "ReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tendering_terms: None | TenderingTerms = field(
        default=None,
        metadata={
            "name": "TenderingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tendering_process: None | TenderingProcess = field(
        default=None,
        metadata={
            "name": "TenderingProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_project: ProcurementProject = field(
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    procurement_project_lot: tuple[ProcurementProjectLot, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True, kw_only=True)
class CallForTenders(CallForTendersType):
    class Meta:
        namespace = (
            "urn:oasis:names:specification:ubl:schema:xsd:CallForTenders-2"
        )
