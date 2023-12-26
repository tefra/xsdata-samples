from dataclasses import dataclass, field
from typing import List, Optional, Union
from ..core.datatypes_base import (
    Ce,
    Cs,
    En,
    EnExplicit,
    Ii,
    Int,
    IvlTsExplicit,
    On,
    PnExplicit,
)
from ..core.voc import (
    EntityClass,
    EntityClassNonPersonLivingSubject,
    EntityClassOrganization,
    EntityDeterminer,
    NullFlavor,
    ParticipationTargetSubject,
    ParticipationType,
    RoleClassEmployee,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    XAccommodationRequestorRole,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
)
from .coct_mt150002_uv01 import CoctMt150002Uv01Organization
from .coct_mt150003_uv03 import CoctMt150003Uv03Organization
from .coct_mt150007_uv import CoctMt150007UvOrganization
from .coct_mt510000_uv06 import CoctMt510000Uv06CoverageRecord
from .coct_mt820000_uv import CoctMt820000UvCareProvision

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaMt201304Uv02CoveredParty:
    class Meta:
        name = "PRPA_MT201304UV02.CoveredParty"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    coverage_record: Optional[CoctMt510000Uv06CoverageRecord] = field(
        default=None,
        metadata={
            "name": "coverageRecord",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.COV,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Employee:
    class Meta:
        name = "PRPA_MT201304UV02.Employee"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    employer_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata={
            "name": "employerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[RoleClassEmployee] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Group:
    class Meta:
        name = "PRPA_MT201304UV02.Group"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: List[En] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[EntityClassOrganization] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Nation:
    class Meta:
        name = "PRPA_MT201304UV02.Nation"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    name: Optional[On] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.NAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02OtherIds:
    class Meta:
        name = "PRPA_MT201304UV02.OtherIDs"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    scoping_organization: Optional[CoctMt150002Uv01Organization] = field(
        default=None,
        metadata={
            "name": "scopingOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[
        Union[
            RoleClassMutualRelationship,
            RoleClassPassive,
            str,
            RoleClassOntological,
            RoleClassPartitive,
            RoleClassRootValue,
        ]
    ] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class PrpaMt201304Uv02Student:
    class Meta:
        name = "PRPA_MT201304UV02.Student"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    school_organization: Optional[CoctMt150007UvOrganization] = field(
        default=None,
        metadata={
            "name": "schoolOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Union[
        RoleClassMutualRelationship,
        RoleClassPassive,
        str,
        RoleClassOntological,
        RoleClassPartitive,
        RoleClassRootValue,
        XAccommodationRequestorRole,
        XDocumentEntrySubject,
        XDocumentSubject,
        XInformationRecipientRole,
        XRoleClassAccommodationRequestor,
        XRoleClassCoverage,
        XRoleClassCoverageInvoice,
        XRoleClassCredentialedEntity,
        XRoleClassPayeePolicyRelationship,
    ] = field(
        init=False,
        default=RoleClassMutualRelationship.STD,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class PrpaMt201304Uv02Subject:
    class Meta:
        name = "PRPA_MT201304UV02.Subject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    care_provision: Optional[CoctMt820000UvCareProvision] = field(
        default=None,
        metadata={
            "name": "careProvision",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Citizen:
    class Meta:
        name = "PRPA_MT201304UV02.Citizen"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    political_nation: Optional[PrpaMt201304Uv02Nation] = field(
        default=None,
        metadata={
            "name": "politicalNation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Union[
        RoleClassMutualRelationship,
        RoleClassPassive,
        str,
        RoleClassOntological,
        RoleClassPartitive,
        RoleClassRootValue,
        XAccommodationRequestorRole,
        XDocumentEntrySubject,
        XDocumentSubject,
        XInformationRecipientRole,
        XRoleClassAccommodationRequestor,
        XRoleClassCoverage,
        XRoleClassCoverageInvoice,
        XRoleClassCredentialedEntity,
        XRoleClassPayeePolicyRelationship,
    ] = field(
        init=False,
        default=RoleClassMutualRelationship.CIT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class PrpaMt201304Uv02Member:
    class Meta:
        name = "PRPA_MT201304UV02.Member"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    group: Optional[PrpaMt201304Uv02Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Union[
        RoleClassMutualRelationship,
        RoleClassPassive,
        str,
        RoleClassOntological,
        RoleClassPartitive,
        RoleClassRootValue,
        XAccommodationRequestorRole,
        XDocumentEntrySubject,
        XDocumentSubject,
        XInformationRecipientRole,
        XRoleClassAccommodationRequestor,
        XRoleClassCoverage,
        XRoleClassCoverageInvoice,
        XRoleClassCredentialedEntity,
        XRoleClassPayeePolicyRelationship,
    ] = field(
        init=False,
        default=RoleClassPartitive.MBR,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class PrpaMt201304Uv02PatientOfOtherProvider:
    class Meta:
        name = "PRPA_MT201304UV02.PatientOfOtherProvider"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    subject_of: Optional[PrpaMt201304Uv02Subject] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Union[
        RoleClassMutualRelationship,
        RoleClassPassive,
        str,
        RoleClassOntological,
        RoleClassPartitive,
        RoleClassRootValue,
        XAccommodationRequestorRole,
        XDocumentEntrySubject,
        XDocumentSubject,
        XInformationRecipientRole,
        XRoleClassAccommodationRequestor,
        XRoleClassCoverage,
        XRoleClassCoverageInvoice,
        XRoleClassCredentialedEntity,
        XRoleClassPayeePolicyRelationship,
    ] = field(
        init=False,
        default=RoleClassMutualRelationship.PAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass
class PrpaMt201304Uv02NonPersonLivingSubject:
    class Meta:
        name = "PRPA_MT201304UV02.NonPersonLivingSubject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: List[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_patient_of_other_provider: List[
        PrpaMt201304Uv02PatientOfOtherProvider
    ] = field(
        default_factory=list,
        metadata={
            "name": "asPatientOfOtherProvider",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_member: List[PrpaMt201304Uv02Member] = field(
        default_factory=list,
        metadata={
            "name": "asMember",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_other_ids: List[PrpaMt201304Uv02OtherIds] = field(
        default_factory=list,
        metadata={
            "name": "asOtherIDs",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Optional[EntityClassNonPersonLivingSubject] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Person:
    class Meta:
        name = "PRPA_MT201304UV02.Person"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: List[PnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    as_patient_of_other_provider: List[
        PrpaMt201304Uv02PatientOfOtherProvider
    ] = field(
        default_factory=list,
        metadata={
            "name": "asPatientOfOtherProvider",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_employee: List[PrpaMt201304Uv02Employee] = field(
        default_factory=list,
        metadata={
            "name": "asEmployee",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_citizen: List[PrpaMt201304Uv02Citizen] = field(
        default_factory=list,
        metadata={
            "name": "asCitizen",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_student: List[PrpaMt201304Uv02Student] = field(
        default_factory=list,
        metadata={
            "name": "asStudent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_member: List[PrpaMt201304Uv02Member] = field(
        default_factory=list,
        metadata={
            "name": "asMember",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_other_ids: List[PrpaMt201304Uv02OtherIds] = field(
        default_factory=list,
        metadata={
            "name": "asOtherIDs",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaMt201304Uv02Patient:
    class Meta:
        name = "PRPA_MT201304UV02.Patient"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    very_important_person_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "veryImportantPersonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    patient_person: Optional[PrpaMt201304Uv02Person] = field(
        default=None,
        metadata={
            "name": "patientPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    patient_non_person_living_subject: Optional[
        PrpaMt201304Uv02NonPersonLivingSubject
    ] = field(
        default=None,
        metadata={
            "name": "patientNonPersonLivingSubject",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    provider_organization: Optional[CoctMt150003Uv03Organization] = field(
        default=None,
        metadata={
            "name": "providerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    covered_party_of: List[PrpaMt201304Uv02CoveredParty] = field(
        default_factory=list,
        metadata={
            "name": "coveredPartyOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: Union[
        RoleClassMutualRelationship,
        RoleClassPassive,
        str,
        RoleClassOntological,
        RoleClassPartitive,
        RoleClassRootValue,
        XAccommodationRequestorRole,
        XDocumentEntrySubject,
        XDocumentSubject,
        XInformationRecipientRole,
        XRoleClassAccommodationRequestor,
        XRoleClassCoverage,
        XRoleClassCoverageInvoice,
        XRoleClassCredentialedEntity,
        XRoleClassPayeePolicyRelationship,
    ] = field(
        init=False,
        default=RoleClassMutualRelationship.PAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )
