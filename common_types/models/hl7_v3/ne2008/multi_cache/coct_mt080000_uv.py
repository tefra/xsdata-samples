from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    Ad,
    AnyType,
    Bl,
    Cd,
    Ce,
    Cs,
    EdExplicit,
    EnExplicit,
    Ii,
    Int,
    IvlTsExplicit,
    PqExplicit,
    St,
    SxcmTsExplicit,
    TelExplicit,
    TsExplicit,
)
from ..core.voc import (
    ActClass,
    ActClassObservation,
    ActClassProcedure,
    ActClassRoot,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPertainsValue,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    EntityClass,
    EntityClassContainer,
    EntityClassManufacturedMaterial,
    EntityClassMaterial,
    EntityClassNonPersonLivingSubject,
    EntityClassRoot,
    EntityDeterminer,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetSubject,
    ParticipationType,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    RoleClassSpecimen,
    XAccommodationRequestorRole,
    XActMoodIntentEvent,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XLabProcessClassCodes,
    XParticipationAuthorPerformer,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
    XSuccReplPrev,
)
from .coct_mt070000_uv01 import CoctMt070000Uv01LocatedEntity
from .coct_mt090000_uv01 import CoctMt090000Uv01AssignedEntity
from .coct_mt150000_uv02 import CoctMt150000Uv02Organization

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class CoctMt080000UvActRef:
    class Meta:
        name = "COCT_MT080000UV.ActRef"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassRoot = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvAdditiveMaterial:
    class Meta:
        name = "COCT_MT080000UV.AdditiveMaterial"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassMaterial = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class CoctMt080000UvAuthorOrPerformer:
    class Meta:
        name = "COCT_MT080000UV.AuthorOrPerformer"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    note_text: None | St = field(
        default=None,
        metadata={
            "name": "noteText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_entity: None | CoctMt090000Uv01AssignedEntity = field(
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: XParticipationAuthorPerformer = field(
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvAutomationSpecimenObservationEvent:
    class Meta:
        name = "COCT_MT080000UV.AutomationSpecimenObservationEvent"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: None | St = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: AnyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.SPCOBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvContent4:
    class Meta:
        name = "COCT_MT080000UV.Content4"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    position_number: list[Int] = field(
        default_factory=list,
        metadata={
            "name": "positionNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    container_holder: CoctMt080000UvHolder = field(
        metadata={
            "name": "containerHolder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPartitive.CONT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvCriterion:
    class Meta:
        name = "COCT_MT080000UV.Criterion"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Cd = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    text: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: None | AnyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    interpretation_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassObservation = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvIdentifiedContainer:
    class Meta:
        name = "COCT_MT080000UV.IdentifiedContainer"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPassive.IDENT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvIdentifiedHolder:
    class Meta:
        name = "COCT_MT080000UV.IdentifiedHolder"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        default=RoleClassPassive.IDENT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvManufacturedProduct:
    class Meta:
        name = "COCT_MT080000UV.ManufacturedProduct"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    manufacturer_organization: CoctMt150000Uv02Organization = field(
        metadata={
            "name": "manufacturerOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassManufacturedProduct = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CoctMt080000UvPerformer:
    class Meta:
        name = "COCT_MT080000UV.Performer"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    note_text: None | St = field(
        default=None,
        metadata={
            "name": "noteText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigned_entity: None | CoctMt090000Uv01AssignedEntity = field(
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationPhysicalPerformer = field(
        default=ParticipationPhysicalPerformer.PRF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSpecimenAlternateIdentifier:
    class Meta:
        name = "COCT_MT080000UV.SpecimenAlternateIdentifier"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    assigning_organization: None | CoctMt150000Uv02Organization = field(
        default=None,
        metadata={
            "name": "assigningOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPassive.IDENT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSpecimenObservationEvent:
    class Meta:
        name = "COCT_MT080000UV.SpecimenObservationEvent"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: None | St = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    value: AnyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassObservation = field(
        init=False,
        default=ActClassObservation.OBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSpecimenStub:
    class Meta:
        name = "COCT_MT080000UV.SpecimenStub"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassSpecimen = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CoctMt080000UvAdditive:
    class Meta:
        name = "COCT_MT080000UV.Additive"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    additive: CoctMt080000UvAdditiveMaterial = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPartitive.ADTV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvAdditive2:
    class Meta:
        name = "COCT_MT080000UV.Additive2"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    additive: CoctMt080000UvAdditiveMaterial = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPartitive.ADTV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvHolder:
    class Meta:
        name = "COCT_MT080000UV.Holder"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_identified_holder: list[CoctMt080000UvIdentifiedHolder] = field(
        default_factory=list,
        metadata={
            "name": "asIdentifiedHolder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent4 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_located_entity: None | CoctMt070000Uv01LocatedEntity = field(
        default=None,
        metadata={
            "name": "asLocatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.HOLD,
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


@dataclass(kw_only=True)
class CoctMt080000UvPrecondition:
    class Meta:
        name = "COCT_MT080000UV.Precondition"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    priority_number: None | Int = field(
        default=None,
        metadata={
            "name": "priorityNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    conjunction_code: None | Cs = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    criterion: None | CoctMt080000UvCriterion = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: (
        ActRelationshipConditional
        | ActRelationshipHasComponent
        | ActRelationshipOutcome
        | ActRelationshipCostTracking
        | ActRelationshipPosting
        | str
        | ActRelationshipHasSupport
        | ActRelationshipTemporallyPertains
        | ActRelationshipPertainsValue
        | ActRelationshipSequel
        | XActRelationshipDocument
        | XActRelationshipEntry
        | XActRelationshipEntryRelationship
        | XActRelationshipExternalReference
        | XActRelationshipPatientTransport
        | XActRelationshipPertinentInfo
        | XActRelationshipRelatedAuthorizations
        | XActReplaceOrRevise
        | XSuccReplPrev
    ) = field(
        init=False,
        default=ActRelationshipConditional.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSubject1:
    class Meta:
        name = "COCT_MT080000UV.Subject1"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    identified_container: None | CoctMt080000UvIdentifiedContainer = field(
        metadata={
            "name": "identifiedContainer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetSubject = field(
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSubject2:
    class Meta:
        name = "COCT_MT080000UV.Subject2"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    identified_holder: None | CoctMt080000UvIdentifiedHolder = field(
        metadata={
            "name": "identifiedHolder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetSubject = field(
        default=ParticipationTargetSubject.SBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        },
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSubject4:
    class Meta:
        name = "COCT_MT080000UV.Subject4"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    specimen_observation_event: (
        None | CoctMt080000UvSpecimenObservationEvent
    ) = field(
        default=None,
        metadata={
            "name": "specimenObservationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    automation_specimen_observation_event: (
        None | CoctMt080000UvAutomationSpecimenObservationEvent
    ) = field(
        default=None,
        metadata={
            "name": "automationSpecimenObservationEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetSubject = field(
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvContent3:
    class Meta:
        name = "COCT_MT080000UV.Content3"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    position_number: list[Int] = field(
        default_factory=list,
        metadata={
            "name": "positionNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    container_holder: CoctMt080000UvHolder = field(
        metadata={
            "name": "containerHolder",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPartitive.CONT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvProcess:
    class Meta:
        name = "COCT_MT080000UV.Process"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: None | St = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: list[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    approach_site_code: None | Cd = field(
        default=None,
        metadata={
            "name": "approachSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    target_site_code: None | Cd = field(
        default=None,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    performer: list[CoctMt080000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    precondition: list[CoctMt080000UvPrecondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClassProcedure = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: XActMoodIntentEvent = field(
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CoctMt080000UvProcessStep:
    class Meta:
        name = "COCT_MT080000UV.ProcessStep"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Cd = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    text: None | St = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    subject1: list[CoctMt080000UvSubject1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    subject2: list[CoctMt080000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    author_or_performer: list[CoctMt080000UvAuthorOrPerformer] = field(
        default_factory=list,
        metadata={
            "name": "authorOrPerformer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: XLabProcessClassCodes = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvContainer:
    class Meta:
        name = "COCT_MT080000UV.Container"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: None | Ii = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    risk_code: None | Ce = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    handling_code: None | Ce = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    capacity_quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "name": "capacityQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    height_quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "name": "heightQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    diameter_quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "name": "diameterQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    cap_type_code: None | Ce = field(
        default=None,
        metadata={
            "name": "capTypeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    separator_type_code: None | Ce = field(
        default=None,
        metadata={
            "name": "separatorTypeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    barrier_delta_quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "name": "barrierDeltaQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    bottom_delta_quantity: None | PqExplicit = field(
        default=None,
        metadata={
            "name": "bottomDeltaQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_identified_container: None | CoctMt080000UvIdentifiedContainer = field(
        default=None,
        metadata={
            "name": "asIdentifiedContainer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent3 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_located_entity: None | CoctMt070000Uv01LocatedEntity = field(
        default=None,
        metadata={
            "name": "asLocatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    additive: list[CoctMt080000UvAdditive2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassContainer = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class CoctMt080000UvProduct:
    class Meta:
        name = "COCT_MT080000UV.Product"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    process: None | CoctMt080000UvProcess = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    act_ref: None | CoctMt080000UvActRef = field(
        default=None,
        metadata={
            "name": "actRef",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvSubject3:
    class Meta:
        name = "COCT_MT080000UV.Subject3"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    sequence_number: None | Int = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    process_step: None | CoctMt080000UvProcessStep = field(
        metadata={
            "name": "processStep",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    type_code: ParticipationTargetSubject = field(
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvContent1:
    class Meta:
        name = "COCT_MT080000UV.Content1"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    container: CoctMt080000UvContainer = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: (
        RoleClassMutualRelationship
        | RoleClassPassive
        | str
        | RoleClassOntological
        | RoleClassPartitive
        | RoleClassRootValue
        | XAccommodationRequestorRole
        | XDocumentEntrySubject
        | XDocumentSubject
        | XInformationRecipientRole
        | XRoleClassAccommodationRequestor
        | XRoleClassCoverage
        | XRoleClassCoverageInvoice
        | XRoleClassCredentialedEntity
        | XRoleClassPayeePolicyRelationship
    ) = field(
        init=False,
        default=RoleClassPartitive.CONT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        },
    )


@dataclass(kw_only=True)
class CoctMt080000UvManufactured:
    class Meta:
        name = "COCT_MT080000UV.Manufactured"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    quantity: list[PqExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | St = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    risk_code: None | Ce = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    handling_code: None | Ce = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    lot_number_text: None | St = field(
        default=None,
        metadata={
            "name": "lotNumberText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    expiration_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "expirationTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_specimen_alternate_identifier: list[
        CoctMt080000UvSpecimenAlternateIdentifier
    ] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenAlternateIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_manufactured_product: None | CoctMt080000UvManufacturedProduct = field(
        metadata={
            "name": "asManufacturedProduct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    as_specimen_stub: list[CoctMt080000UvSpecimenStub] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenStub",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent1 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    additive: list[CoctMt080000UvAdditive] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassManufacturedMaterial = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class CoctMt080000UvNatural:
    class Meta:
        name = "COCT_MT080000UV.Natural"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    quantity: list[PqExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    risk_code: None | Ce = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    handling_code: None | Ce = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_specimen_alternate_identifier: list[
        CoctMt080000UvSpecimenAlternateIdentifier
    ] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenAlternateIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_specimen_stub: list[CoctMt080000UvSpecimenStub] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenStub",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent1 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    additive: list[CoctMt080000UvAdditive] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassRoot = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class CoctMt080000UvNonPersonLivingSubject:
    class Meta:
        name = "COCT_MT080000UV.NonPersonLivingSubject"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    quantity: list[PqExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    existence_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "existenceTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    risk_code: None | Ce = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    handling_code: None | Ce = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    administrative_gender_code: None | Ce = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    birth_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    deceased_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "deceasedInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    deceased_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "deceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    multiple_birth_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "multipleBirthInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    multiple_birth_order_number: None | Int = field(
        default=None,
        metadata={
            "name": "multipleBirthOrderNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    organ_donor_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "organDonorInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    strain_text: None | EdExplicit = field(
        default=None,
        metadata={
            "name": "strainText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    gender_status_code: None | Ce = field(
        default=None,
        metadata={
            "name": "genderStatusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_specimen_alternate_identifier: list[
        CoctMt080000UvSpecimenAlternateIdentifier
    ] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenAlternateIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_specimen_stub: list[CoctMt080000UvSpecimenStub] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenStub",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent1 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    additive: list[CoctMt080000UvAdditive] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassNonPersonLivingSubject = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
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


@dataclass(kw_only=True)
class CoctMt080000UvPerson:
    class Meta:
        name = "COCT_MT080000UV.Person"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    quantity: list[PqExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    name: list[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    desc: None | EdExplicit = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    status_code: None | Cs = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    existence_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "existenceTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    telecom: list[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    risk_code: None | Ce = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    handling_code: None | Ce = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    administrative_gender_code: None | Ce = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    birth_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    deceased_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "deceasedInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    deceased_time: None | TsExplicit = field(
        default=None,
        metadata={
            "name": "deceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    multiple_birth_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "multipleBirthInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    multiple_birth_order_number: None | Int = field(
        default=None,
        metadata={
            "name": "multipleBirthOrderNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    organ_donor_ind: None | Bl = field(
        default=None,
        metadata={
            "name": "organDonorInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    addr: list[Ad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    disability_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "disabilityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    race_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "raceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    ethnic_group_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "ethnicGroupCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    as_specimen_alternate_identifier: list[
        CoctMt080000UvSpecimenAlternateIdentifier
    ] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenAlternateIdentifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_specimen_stub: list[CoctMt080000UvSpecimenStub] = field(
        default_factory=list,
        metadata={
            "name": "asSpecimenStub",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    as_content: None | CoctMt080000UvContent1 = field(
        default=None,
        metadata={
            "name": "asContent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    additive: list[CoctMt080000UvAdditive] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
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


@dataclass(kw_only=True)
class CoctMt080000UvSpecimen:
    class Meta:
        name = "COCT_MT080000UV.Specimen"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Ii = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    code: Ce = field(
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    specimen_natural: None | CoctMt080000UvNatural = field(
        default=None,
        metadata={
            "name": "specimenNatural",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    specimen_manufactured: None | CoctMt080000UvManufactured = field(
        default=None,
        metadata={
            "name": "specimenManufactured",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    specimen_non_person_living_subject: (
        None | CoctMt080000UvNonPersonLivingSubject
    ) = field(
        default=None,
        metadata={
            "name": "specimenNonPersonLivingSubject",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    specimen_person: None | CoctMt080000UvPerson = field(
        default=None,
        metadata={
            "name": "specimenPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    source_natural: None | CoctMt080000UvNatural = field(
        default=None,
        metadata={
            "name": "sourceNatural",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    source_manufactured: None | CoctMt080000UvManufactured = field(
        default=None,
        metadata={
            "name": "sourceManufactured",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    source_non_person_living_subject: (
        None | CoctMt080000UvNonPersonLivingSubject
    ) = field(
        default=None,
        metadata={
            "name": "sourceNonPersonLivingSubject",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    source_person: None | CoctMt080000UvPerson = field(
        default=None,
        metadata={
            "name": "sourcePerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    subject_of1: list[CoctMt080000UvSubject4] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    subject_of2: list[CoctMt080000UvSubject3] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    product_of: None | CoctMt080000UvProduct = field(
        default=None,
        metadata={
            "name": "productOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: RoleClassSpecimen = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
