from dataclasses import dataclass, field
from typing import List, Optional, Union
from ..core.datatypes import IvlInt
from ..core.datatypes_base import (
    AdExplicit,
    Any,
    Cd,
    Ce,
    Cs,
    EdExplicit,
    EnExplicit,
    Ii,
    Int,
    IvlTs,
    IvlTsExplicit,
    OnExplicit,
    PnExplicit,
    Sc,
    St,
    TelExplicit,
    Tn,
    TsExplicit,
)
from ..core.voc import (
    ActClass,
    ActClassCareProvision,
    ActClassObservation,
    ActClassProcedure,
    ActClassRoot,
    ActMood,
    ActMoodCompletionTrack,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPertainsValue,
    ActRelationshipPosting,
    ActRelationshipReason,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    EntityClass,
    EntityClassDevice,
    EntityClassManufacturedMaterial,
    EntityClassNonPersonLivingSubject,
    EntityClassOrganization,
    EntityClassPlace,
    EntityDeterminer,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetLocation,
    ParticipationTargetSubject,
    ParticipationType,
    RoleClassAssignedEntity,
    RoleClassLocatedEntity,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    RoleClassSpecimen,
    RoleLinkType,
    XAccommodationRequestorRole,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XDeterminerInstanceKind,
    XDocumentEntrySubject,
    XDocumentSubject,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
    XSuccReplPrev,
)
from .coct_mt050000_uv01 import CoctMt050000Uv01Patient
from .coct_mt240003_uv02 import CoctMt240003Uv02ServiceDeliveryLocation
from .coct_mt960000_uv05 import CoctMt960000Uv05Position

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt290000Uv06AdministrativeDiagnosis:
    class Meta:
        name = "COCT_MT290000UV06.AdministrativeDiagnosis"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06AdministrativeDiagnosisReference:
    class Meta:
        name = "COCT_MT290000UV06.AdministrativeDiagnosisReference"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[Ii] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06BillableModifier:
    class Meta:
        name = "COCT_MT290000UV06.BillableModifier"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06Device:
    class Meta:
        name = "COCT_MT290000UV06.Device"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[Ii] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassAssignedEntity] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Device2:
    class Meta:
        name = "COCT_MT290000UV06.Device2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[St] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufacturer_model_name: Optional[Sc] = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    software_name: Optional[Sc] = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassDevice] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06InjuryPlace:
    class Meta:
        name = "COCT_MT290000UV06.InjuryPlace"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: List[EnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    desc: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    position_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "positionText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    injury_location: List["CoctMt290000Uv06InjuryLocation"] = field(
        default_factory=list,
        metadata={
            "name": "injuryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassPlace] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06Location:
    class Meta:
        name = "COCT_MT290000UV06.Location"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_delivery_location: Optional[CoctMt240003Uv02ServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationTargetLocation] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Location1:
    class Meta:
        name = "COCT_MT290000UV06.Location1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_delivery_location: Optional[CoctMt240003Uv02ServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "serviceDeliveryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationTargetLocation] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ManufacturedMaterial:
    class Meta:
        name = "COCT_MT290000UV06.ManufacturedMaterial"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassManufacturedMaterial] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: Optional[XDeterminerInstanceKind] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ManufacturedProductOrganization:
    class Meta:
        name = "COCT_MT290000UV06.ManufacturedProductOrganization"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[OnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassOrganization] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06NonPersonLivingSubject:
    class Meta:
        name = "COCT_MT290000UV06.NonPersonLivingSubject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[Tn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[EntityClassNonPersonLivingSubject] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06PresentingIndication:
    class Meta:
        name = "COCT_MT290000UV06.PresentingIndication"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06ProviderPerson:
    class Meta:
        name = "COCT_MT290000UV06.ProviderPerson"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: Optional[PnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    telecom: Optional[TelExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    administrative_gender_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "administrativeGenderCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    birth_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    addr: Optional[AdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.PSN,
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
        }
    )


@dataclass
class CoctMt290000Uv06Specimen:
    class Meta:
        name = "COCT_MT290000UV06.Specimen"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassSpecimen] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Subject3:
    class Meta:
        name = "COCT_MT290000UV06.Subject3"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    position: Optional[CoctMt960000Uv05Position] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Subject5:
    class Meta:
        name = "COCT_MT290000UV06.Subject5"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    patient: Optional[CoctMt050000Uv01Patient] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt290000Uv06Substitution:
    class Meta:
        name = "COCT_MT290000UV06.Substitution"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.SUBST,
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
        }
    )


@dataclass
class CoctMt290000Uv06HealthCareProvider:
    class Meta:
        name = "COCT_MT290000UV06.HealthCareProvider"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    health_care_provider_person: Optional[CoctMt290000Uv06ProviderPerson] = field(
        default=None,
        metadata={
            "name": "healthCareProviderPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, RoleClassRootValue, XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PROV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt290000Uv06InjuryLocation:
    class Meta:
        name = "COCT_MT290000UV06.InjuryLocation"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    name: List[Tn] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    addr: Optional[AdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    telecom: List[TelExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    located_injury_place: Optional[CoctMt290000Uv06InjuryPlace] = field(
        default=None,
        metadata={
            "name": "locatedInjuryPlace",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: List[CoctMt290000Uv06Subject3] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassLocatedEntity] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ManufacturedProduct:
    class Meta:
        name = "COCT_MT290000UV06.ManufacturedProduct"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: Optional[Ii] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_material: Optional[CoctMt290000Uv06ManufacturedMaterial] = field(
        default=None,
        metadata={
            "name": "manufacturedMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    manufacturer_manufactured_product_organization: Optional[CoctMt290000Uv06ManufacturedProductOrganization] = field(
        default=None,
        metadata={
            "name": "manufacturerManufacturedProductOrganization",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Product2:
    class Meta:
        name = "COCT_MT290000UV06.Product2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: Optional[CoctMt290000Uv06Specimen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Reason:
    class Meta:
        name = "COCT_MT290000UV06.Reason"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    administrative_diagnosis_reference: Optional[CoctMt290000Uv06AdministrativeDiagnosisReference] = field(
        default=None,
        metadata={
            "name": "administrativeDiagnosisReference",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Reason3:
    class Meta:
        name = "COCT_MT290000UV06.Reason3"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "priorityNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    administrative_diagnosis: Optional[CoctMt290000Uv06AdministrativeDiagnosis] = field(
        default=None,
        metadata={
            "name": "administrativeDiagnosis",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Reason5:
    class Meta:
        name = "COCT_MT290000UV06.Reason5"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "priorityNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    presenting_indication: Optional[CoctMt290000Uv06PresentingIndication] = field(
        default=None,
        metadata={
            "name": "presentingIndication",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ReusableDevice:
    class Meta:
        name = "COCT_MT290000UV06.ReusableDevice"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    device: Optional[CoctMt290000Uv06Device] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.RDV,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Subject:
    class Meta:
        name = "COCT_MT290000UV06.Subject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substitution: Optional[CoctMt290000Uv06Substitution] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipPertainsValue.SUBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt290000Uv06Subject2:
    class Meta:
        name = "COCT_MT290000UV06.Subject2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    billable_modifier: Optional[CoctMt290000Uv06BillableModifier] = field(
        default=None,
        metadata={
            "name": "billableModifier",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipPertainsValue.SUBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt290000Uv06IndirectAuthorithyOver:
    class Meta:
        name = "COCT_MT290000UV06.IndirectAuthorithyOver"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    health_care_provider: Optional[CoctMt290000Uv06HealthCareProvider] = field(
        default=None,
        metadata={
            "name": "healthCareProvider",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: RoleLinkType = field(
        init=False,
        default=RoleLinkType.INDAUTH,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Origin:
    class Meta:
        name = "COCT_MT290000UV06.Origin"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    injury_location: Optional[CoctMt290000Uv06InjuryLocation] = field(
        default=None,
        metadata={
            "name": "injuryLocation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.ORG,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06PatientEncounter:
    class Meta:
        name = "COCT_MT290000UV06.PatientEncounter"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    activity_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "activityTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    priority_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    admission_referral_source_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "admissionReferralSourceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    discharge_disposition_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "dischargeDispositionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reason: List[CoctMt290000Uv06Reason5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.ENC,
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
        }
    )


@dataclass
class CoctMt290000Uv06Product1:
    class Meta:
        name = "COCT_MT290000UV06.Product1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_product: Optional[CoctMt290000Uv06ManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "manufacturedProduct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.PRD,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06SpecimenCollectionEvent:
    class Meta:
        name = "COCT_MT290000UV06.SpecimenCollectionEvent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    product: Optional[CoctMt290000Uv06Product2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    location: Optional[CoctMt290000Uv06Location1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassProcedure] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06AssignedEntity:
    class Meta:
        name = "COCT_MT290000UV06.AssignedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_provider_person: Optional[CoctMt290000Uv06ProviderPerson] = field(
        default=None,
        metadata={
            "name": "assignedProviderPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    assigned_non_person_living_subject: Optional[CoctMt290000Uv06NonPersonLivingSubject] = field(
        default=None,
        metadata={
            "name": "assignedNonPersonLivingSubject",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    assigned_device: Optional[CoctMt290000Uv06Device2] = field(
        default=None,
        metadata={
            "name": "assignedDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    indirect_authority: List[CoctMt290000Uv06IndirectAuthorithyOver] = field(
        default_factory=list,
        metadata={
            "name": "indirectAuthority",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[RoleClassAssignedEntity] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Component1:
    class Meta:
        name = "COCT_MT290000UV06.Component1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    patient_encounter: Optional[CoctMt290000Uv06PatientEncounter] = field(
        default=None,
        metadata={
            "name": "patientEncounter",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Component2:
    class Meta:
        name = "COCT_MT290000UV06.Component2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen_collection_event: Optional[CoctMt290000Uv06SpecimenCollectionEvent] = field(
        default=None,
        metadata={
            "name": "specimenCollectionEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Injury:
    class Meta:
        name = "COCT_MT290000UV06.Injury"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    target_site_code: Optional[Cd] = field(
        default=None,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    origin: List[CoctMt290000Uv06Origin] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassObservation] = field(
        default=None,
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
        }
    )


@dataclass
class CoctMt290000Uv06Author:
    class Meta:
        name = "COCT_MT290000UV06.Author"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Author1:
    class Meta:
        name = "COCT_MT290000UV06.Author1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Author2:
    class Meta:
        name = "COCT_MT290000UV06.Author2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Consultant:
    class Meta:
        name = "COCT_MT290000UV06.Consultant"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.CON,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Performer:
    class Meta:
        name = "COCT_MT290000UV06.Performer"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    function_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "functionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ParticipationPhysicalPerformer] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Reason1:
    class Meta:
        name = "COCT_MT290000UV06.Reason1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sequence_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    injury: Optional[CoctMt290000Uv06Injury] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ResponsibleParty:
    class Meta:
        name = "COCT_MT290000UV06.ResponsibleParty"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.RESP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06SecondaryPerformer:
    class Meta:
        name = "COCT_MT290000UV06.SecondaryPerformer"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    function_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "functionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt290000Uv06AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.SPRF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06PatientCareProvisionRequest:
    class Meta:
        name = "COCT_MT290000UV06.PatientCareProvisionRequest"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: Optional[CoctMt290000Uv06Author2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason: List[CoctMt290000Uv06Reason] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassCareProvision] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.RQO,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06ServiceRequest:
    class Meta:
        name = "COCT_MT290000UV06.ServiceRequest"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: Optional[CoctMt290000Uv06Author1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.RQO,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06InFulfillmentOf:
    class Meta:
        name = "COCT_MT290000UV06.InFulfillmentOf"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_request: Optional[CoctMt290000Uv06ServiceRequest] = field(
        default=None,
        metadata={
            "name": "serviceRequest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipFulfills] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06Reason4:
    class Meta:
        name = "COCT_MT290000UV06.Reason4"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    sequence_number: Optional[Int] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    patient_care_provision_request: Optional[CoctMt290000Uv06PatientCareProvisionRequest] = field(
        default=None,
        metadata={
            "name": "patientCareProvisionRequest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt290000Uv06BillableClinicalService:
    class Meta:
        name = "COCT_MT290000UV06.BillableClinicalService"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    priority_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reason_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "reasonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt290000Uv06Subject5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reusable_device: Optional[CoctMt290000Uv06ReusableDevice] = field(
        default=None,
        metadata={
            "name": "reusableDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    product: List[CoctMt290000Uv06Product1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: Optional[CoctMt290000Uv06ResponsibleParty] = field(
        default=None,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    secondary_performer: List[CoctMt290000Uv06SecondaryPerformer] = field(
        default_factory=list,
        metadata={
            "name": "secondaryPerformer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: Optional[CoctMt290000Uv06Performer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: Optional[CoctMt290000Uv06Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    consultant: List[CoctMt290000Uv06Consultant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: Optional[CoctMt290000Uv06Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    in_fulfillment_of: List[CoctMt290000Uv06InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason1: List[CoctMt290000Uv06Reason1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason2: List[CoctMt290000Uv06Reason4] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason3: List[CoctMt290000Uv06Reason3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    component: Optional[CoctMt290000Uv06Component2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of1: List[CoctMt290000Uv06Subject2] = field(
        default_factory=list,
        metadata={
            "name": "subjectOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of2: Optional[CoctMt290000Uv06Subject] = field(
        default=None,
        metadata={
            "name": "subjectOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    component_of: List[CoctMt290000Uv06Component1] = field(
        default_factory=list,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[ActMoodCompletionTrack] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
