from dataclasses import dataclass, field
from typing import Optional

from ubl.models.common.ubl_common_aggregate_components_2_1 import (
    ApplicablePeriod,
    ApplicableRegulation,
    BeneficiaryParty,
    GuaranteeDocumentReference,
    GuarantorParty,
    ImmobilizedSecurity,
    InterestedParty,
    Signature,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    ConstitutionCode,
    ContractFolderId,
    CopyIndicator,
    CustomizationId,
    GuaranteeTypeCode,
    Id,
    IssueDate,
    IssueTime,
    LiabilityAmount,
    Note,
    ProfileExecutionId,
    ProfileId,
    Purpose,
    UblversionId,
    Uuid,
)
from ubl.models.common.ubl_common_extension_components_2_1 import Ublextensions

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2"
)


@dataclass(frozen=True)
class GuaranteeCertificateType:
    ublextensions: Ublextensions | None = field(
        default=None,
        metadata={
            "name": "UBLExtensions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2",
        },
    )
    ublversion_id: UblversionId | None = field(
        default=None,
        metadata={
            "name": "UBLVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customization_id: CustomizationId | None = field(
        default=None,
        metadata={
            "name": "CustomizationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_id: ProfileId | None = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    profile_execution_id: ProfileExecutionId | None = field(
        default=None,
        metadata={
            "name": "ProfileExecutionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    copy_indicator: CopyIndicator | None = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_folder_id: ContractFolderId | None = field(
        default=None,
        metadata={
            "name": "ContractFolderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    guarantee_type_code: GuaranteeTypeCode | None = field(
        default=None,
        metadata={
            "name": "GuaranteeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    purpose: tuple[Purpose, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    liability_amount: LiabilityAmount | None = field(
        default=None,
        metadata={
            "name": "LiabilityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    constitution_code: ConstitutionCode | None = field(
        default=None,
        metadata={
            "name": "ConstitutionCode",
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
    applicable_period: ApplicablePeriod | None = field(
        default=None,
        metadata={
            "name": "ApplicablePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    applicable_regulation: tuple[ApplicableRegulation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ApplicableRegulation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    guarantee_document_reference: tuple[GuaranteeDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "GuaranteeDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    immobilized_security: tuple[ImmobilizedSecurity, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ImmobilizedSecurity",
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
            "min_occurs": 1,
        },
    )
    guarantor_party: GuarantorParty | None = field(
        default=None,
        metadata={
            "name": "GuarantorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    interested_party: InterestedParty | None = field(
        default=None,
        metadata={
            "name": "InterestedParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    beneficiary_party: BeneficiaryParty | None = field(
        default=None,
        metadata={
            "name": "BeneficiaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class GuaranteeCertificate(GuaranteeCertificateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:GuaranteeCertificate-2"
