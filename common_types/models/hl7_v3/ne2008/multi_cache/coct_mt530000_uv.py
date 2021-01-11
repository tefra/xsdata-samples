from dataclasses import dataclass, field
from typing import List, Optional, Union
from common_types.models.hl7_v3.ne2008.core.datatypes import (
    IvlInt,
    IvlPq,
    RtoPqPq,
)
from common_types.models.hl7_v3.ne2008.core.datatypes_base import (
    AdExplicit,
    Any,
    Bl,
    Cd,
    Ce,
    Cs,
    Cv,
    EdExplicit,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    OnExplicit,
    PnExplicit,
    PqExplicit,
    RtoQtyQty,
    St,
    SxcmTsExplicit,
    TelExplicit,
    TsExplicit,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActClass,
    ActClassContainer,
    ActClassControlAct,
    ActClassObservation,
    ActClassProcedure,
    ActClassRoot,
    ActClassSupply,
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
    EntityClassManufacturedMaterial,
    EntityClassMaterial,
    EntityClassOrganization,
    EntityClassPlace,
    EntityClassRoot,
    EntityDeterminer,
    EntityDeterminerDetermined,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetDevice,
    ParticipationTargetLocation,
    ParticipationTargetSubject,
    ParticipationType,
    ParticipationVerifier,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassRootValue,
    RoleClassServiceDeliveryLocation,
    XAccommodationRequestorRole,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XClinicalStatementActMood,
    XClinicalStatementEncounterMood,
    XClinicalStatementObservationMood,
    XClinicalStatementProcedureMood,
    XClinicalStatementSubstanceMood,
    XClinicalStatementSupplyMood,
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
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt050000_uv01 import CoctMt050000Uv01Patient
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt080000_uv import CoctMt080000UvSpecimen
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090000_uv01 import CoctMt090000Uv01AssignedEntity
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090102_uv02 import CoctMt090102Uv02AssignedPerson
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt230100_uv import CoctMt230100UvMedication

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt530000UvActDefinition:
    class Meta:
        name = "COCT_MT530000UV.ActDefinition"

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
    text: Optional[EdExplicit] = field(
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
        default=ActMood.DEF_VALUE,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvActReference:
    class Meta:
        name = "COCT_MT530000UV.ActReference"

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
    class_code: Optional[ActClassRoot] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[ActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvDataEnterer:
    class Meta:
        name = "COCT_MT530000UV.DataEnterer"

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
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "signatureCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "signatureText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=ParticipationType.ENT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvLabeledDrug:
    class Meta:
        name = "COCT_MT530000UV.LabeledDrug"

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
    name: Optional[EnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    expiration_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "expirationTime",
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
    determiner_code: Optional[EntityDeterminer] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvMaterial:
    class Meta:
        name = "COCT_MT530000UV.Material"

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
    name: Optional[EnExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    lot_number_text: Optional[St] = field(
        default=None,
        metadata={
            "name": "lotNumberText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    expiration_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "expirationTime",
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
    determiner_code: Optional[EntityDeterminer] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvMaterialKind2:
    class Meta:
        name = "COCT_MT530000UV.MaterialKind2"

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
    code: Optional[Cv] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    desc: Optional[St] = field(
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
    class_code: Optional[EntityClassMaterial] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: Optional[EntityDeterminerDetermined] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvOrganization:
    class Meta:
        name = "COCT_MT530000UV.Organization"

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
    name: List[OnExplicit] = field(
        default_factory=list,
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
    addr: List[AdExplicit] = field(
        default_factory=list,
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
class CoctMt530000UvPlace:
    class Meta:
        name = "COCT_MT530000UV.Place"

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
    name: List[EnExplicit] = field(
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
class CoctMt530000UvPrecondition2:
    class Meta:
        name = "COCT_MT530000UV.Precondition2"

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
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    criterion: Optional["CoctMt530000UvCriterion"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=ActRelationshipConditional.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvProduct2:
    class Meta:
        name = "COCT_MT530000UV.Product2"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: Optional[CoctMt080000UvSpecimen] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvRecordTarget:
    class Meta:
        name = "COCT_MT530000UV.RecordTarget"

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
            "required": True,
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
        default=ParticipationType.RCT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvResponsibleParty1:
    class Meta:
        name = "COCT_MT530000UV.ResponsibleParty1"

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
    assigned_person: Optional[CoctMt090102Uv02AssignedPerson] = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
class CoctMt530000UvResponsibleParty2:
    class Meta:
        name = "COCT_MT530000UV.ResponsibleParty2"

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
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvVerifier:
    class Meta:
        name = "COCT_MT530000UV.Verifier"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "noteText",
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
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "signatureCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "signatureText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    type_code: Optional[ParticipationVerifier] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvBirthplace:
    class Meta:
        name = "COCT_MT530000UV.Birthplace"

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
    birthplace: Optional[CoctMt530000UvPlace] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=RoleClassPassive.BIRTHPL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt530000UvCriterion:
    class Meta:
        name = "COCT_MT530000UV.Criterion"

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
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    interpretation_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    precondition: List[CoctMt530000UvPrecondition2] = field(
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
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: str = field(
        default="false",
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvDefinition:
    class Meta:
        name = "COCT_MT530000UV.Definition"

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
    act_definition: Optional[CoctMt530000UvActDefinition] = field(
        default=None,
        metadata={
            "name": "actDefinition",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=ActRelationshipSequel.INST,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvHealthCareFacility:
    class Meta:
        name = "COCT_MT530000UV.HealthCareFacility"

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
    location: Optional[CoctMt530000UvPlace] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    service_provider_organization: Optional[CoctMt530000UvOrganization] = field(
        default=None,
        metadata={
            "name": "serviceProviderOrganization",
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
    class_code: Optional[RoleClassServiceDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvManufacturedProduct:
    class Meta:
        name = "COCT_MT530000UV.ManufacturedProduct"

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
    manufactured_labeled_drug: Optional[CoctMt530000UvLabeledDrug] = field(
        default=None,
        metadata={
            "name": "manufacturedLabeledDrug",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    manufactured_material: Optional[CoctMt530000UvMaterial] = field(
        default=None,
        metadata={
            "name": "manufacturedMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    manufacturer_organization: Optional[CoctMt530000UvOrganization] = field(
        default=None,
        metadata={
            "name": "manufacturerOrganization",
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
class CoctMt530000UvMaterialPart:
    class Meta:
        name = "COCT_MT530000UV.MaterialPart"

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
    part_material_kind: Optional[CoctMt530000UvMaterialKind2] = field(
        default=None,
        metadata={
            "name": "partMaterialKind",
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
    class_code: Optional[RoleClassPartitive] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvRole:
    class Meta:
        name = "COCT_MT530000UV.Role"

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
    code: Optional[Ce] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    scoping_organization: Optional[CoctMt530000UvOrganization] = field(
        default=None,
        metadata={
            "name": "scopingOrganization",
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
    class_code: Optional[Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, RoleClassRootValue]] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt530000UvSourceOf1:
    class Meta:
        name = "COCT_MT530000UV.SourceOf1"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    pause_quantity: Optional[PqExplicit] = field(
        default=None,
        metadata={
            "name": "pauseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    act_reference: Optional[CoctMt530000UvActReference] = field(
        default=None,
        metadata={
            "name": "actReference",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    type_code: Optional[Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    inversion_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "inversionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvAnimal:
    class Meta:
        name = "COCT_MT530000UV.Animal"

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
    quantity: Optional[PqExplicit] = field(
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
    strain_text: Optional[St] = field(
        default=None,
        metadata={
            "name": "strainText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    gender_status_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "genderStatusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_role: List[CoctMt530000UvRole] = field(
        default_factory=list,
        metadata={
            "name": "asRole",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    birthplace: Optional[CoctMt530000UvBirthplace] = field(
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
    class_code: EntityClass = field(
        init=False,
        default=EntityClass.ANM,
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
class CoctMt530000UvConditions:
    class Meta:
        name = "COCT_MT530000UV.Conditions"

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
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    criterion: Optional[CoctMt530000UvCriterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    type_code: Optional[ActRelationshipConditional] = field(
        default=None,
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
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvDevice:
    class Meta:
        name = "COCT_MT530000UV.Device"

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
    manufactured_product: Optional[CoctMt530000UvManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "manufacturedProduct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    type_code: Optional[ParticipationTargetDevice] = field(
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
class CoctMt530000UvEntity:
    class Meta:
        name = "COCT_MT530000UV.Entity"

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
    quantity: List[PqExplicit] = field(
        default_factory=list,
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    risk_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "riskCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    handling_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "handlingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_role: List[CoctMt530000UvRole] = field(
        default_factory=list,
        metadata={
            "name": "asRole",
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
    class_code: Optional[EntityClassRoot] = field(
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
class CoctMt530000UvLocation:
    class Meta:
        name = "COCT_MT530000UV.Location"

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
    health_care_facility: Optional[CoctMt530000UvHealthCareFacility] = field(
        default=None,
        metadata={
            "name": "healthCareFacility",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvMaterialKind:
    class Meta:
        name = "COCT_MT530000UV.MaterialKind"

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
    desc: Optional[St] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    material_part: List[CoctMt530000UvMaterialPart] = field(
        default_factory=list,
        metadata={
            "name": "materialPart",
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
    class_code: Optional[EntityClassMaterial] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: Optional[EntityDeterminerDetermined] = field(
        default=None,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvPerson:
    class Meta:
        name = "COCT_MT530000UV.Person"

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
    name: List[PnExplicit] = field(
        default_factory=list,
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
    multiple_birth_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "multipleBirthInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    multiple_birth_order_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "multipleBirthOrderNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    marital_status_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "maritalStatusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    religious_affiliation_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "religiousAffiliationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    race_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "raceCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    ethnic_group_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "ethnicGroupCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_role: List[CoctMt530000UvRole] = field(
        default_factory=list,
        metadata={
            "name": "asRole",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    birthplace: Optional[CoctMt530000UvBirthplace] = field(
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
class CoctMt530000UvPrecondition1:
    class Meta:
        name = "COCT_MT530000UV.Precondition1"

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
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    criterion: Optional[CoctMt530000UvCriterion] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=ActRelationshipConditional.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvProduct1:
    class Meta:
        name = "COCT_MT530000UV.Product1"

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
    manufactured_product: Optional[CoctMt530000UvManufacturedProduct] = field(
        default=None,
        metadata={
            "name": "manufacturedProduct",
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
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvAdministerableMaterial:
    class Meta:
        name = "COCT_MT530000UV.AdministerableMaterial"

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
    administerable_material_kind: Optional[CoctMt530000UvMaterialKind] = field(
        default=None,
        metadata={
            "name": "administerableMaterialKind",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, RoleClassRootValue, XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassPassive.ADMM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class CoctMt530000UvObservationRange:
    class Meta:
        name = "COCT_MT530000UV.ObservationRange"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    interpretation_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    precondition: List[CoctMt530000UvPrecondition1] = field(
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
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: str = field(
        default="false",
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvRelatedEntity:
    class Meta:
        name = "COCT_MT530000UV.RelatedEntity"

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
    addr: List[AdExplicit] = field(
        default_factory=list,
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
    related_person: Optional[CoctMt530000UvPerson] = field(
        default=None,
        metadata={
            "name": "relatedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    related_animal: Optional[CoctMt530000UvAnimal] = field(
        default=None,
        metadata={
            "name": "relatedAnimal",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    related_entity: Optional[CoctMt530000UvEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    scoping_person: Optional[CoctMt530000UvPerson] = field(
        default=None,
        metadata={
            "name": "scopingPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    scoping_animal: Optional[CoctMt530000UvAnimal] = field(
        default=None,
        metadata={
            "name": "scopingAnimal",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    scoping_entity: Optional[CoctMt530000UvEntity] = field(
        default=None,
        metadata={
            "name": "scopingEntity",
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
    class_code: Optional[RoleClassMutualRelationship] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvAuthor:
    class Meta:
        name = "COCT_MT530000UV.Author"

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
    note_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "noteText",
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
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "signatureCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    signature_text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "name": "signatureText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_entity: Optional[CoctMt530000UvRelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
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
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
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
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvConsumable:
    class Meta:
        name = "COCT_MT530000UV.Consumable"

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
    administerable_material: Optional[CoctMt530000UvAdministerableMaterial] = field(
        default=None,
        metadata={
            "name": "administerableMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    medication: Optional[CoctMt230100UvMedication] = field(
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
        default=ParticipationType.CSM,
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
class CoctMt530000UvInformant:
    class Meta:
        name = "COCT_MT530000UV.Informant"

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
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_entity: Optional[CoctMt530000UvRelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
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
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
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
        default=ParticipationType.INF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvPerformer:
    class Meta:
        name = "COCT_MT530000UV.Performer"

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
    time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_entity: Optional[CoctMt530000UvRelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
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
    assigned_entity: Optional[CoctMt090000Uv01AssignedEntity] = field(
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
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvReferenceRange:
    class Meta:
        name = "COCT_MT530000UV.ReferenceRange"

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
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_range: Optional[CoctMt530000UvObservationRange] = field(
        default=None,
        metadata={
            "name": "observationRange",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
        default=ActRelationshipPertainsValue.REFV,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvSubject2:
    class Meta:
        name = "COCT_MT530000UV.Subject2"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    awareness_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "awarenessCode",
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
    related_entity: Optional[CoctMt530000UvRelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    specimen: Optional[CoctMt080000UvSpecimen] = field(
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
    context_control_code: ContextControl = field(
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvControlActEvent:
    class Meta:
        name = "COCT_MT530000UV.ControlActEvent"

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
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    effective_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    reason_code: Optional[Cv] = field(
        default=None,
        metadata={
            "name": "reasonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    responsible_party: Optional[CoctMt530000UvResponsibleParty1] = field(
        default=None,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
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
    class_code: ActClassControlAct = field(
        init=False,
        default=ActClassControlAct.CACT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt530000UvSubject1:
    class Meta:
        name = "COCT_MT530000UV.Subject1"

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
    control_act_event: Optional[CoctMt530000UvControlActEvent] = field(
        default=None,
        metadata={
            "name": "controlActEvent",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="false",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvEncounter:
    class Meta:
        name = "COCT_MT530000UV.Encounter"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
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
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "confidentialityCode",
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
    length_of_stay_quantity: Optional[PqExplicit] = field(
        default=None,
        metadata={
            "name": "lengthOfStayQuantity",
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
    pre_admit_test_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "preAdmitTestInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    special_courtesies_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "specialCourtesiesCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    special_arrangement_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "specialArrangementCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List["CoctMt530000UvSourceOf2"] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    mood_code: Optional[XClinicalStatementEncounterMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvProcedure:
    class Meta:
        name = "COCT_MT530000UV.Procedure"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
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
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    interruptible_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "interruptibleInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "uncertaintyCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "methodCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata={
            "name": "approachSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    device: List[CoctMt530000UvDevice] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    product: List[CoctMt530000UvProduct2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List["CoctMt530000UvSourceOf2"] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    class_code: Optional[ActClassProcedure] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XClinicalStatementProcedureMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvSubstanceAdministration:
    class Meta:
        name = "COCT_MT530000UV.SubstanceAdministration"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
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
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    route_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "routeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    approach_site_code: List[Cd] = field(
        default_factory=list,
        metadata={
            "name": "approachSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    dose_quantity: Optional[IvlPq] = field(
        default=None,
        metadata={
            "name": "doseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    rate_quantity: Optional[IvlPq] = field(
        default=None,
        metadata={
            "name": "rateQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    dose_check_quantity: List[RtoQtyQty] = field(
        default_factory=list,
        metadata={
            "name": "doseCheckQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    max_dose_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata={
            "name": "maxDoseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    administration_unit_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "administrationUnitCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    consumable: Optional[CoctMt530000UvConsumable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List["CoctMt530000UvSourceOf2"] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
        default=ActClass.SBADM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XClinicalStatementSubstanceMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvSupply:
    class Meta:
        name = "COCT_MT530000UV.Supply"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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
    independent_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "independentInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    quantity: Optional[PqExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    expected_use_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "expectedUseTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    product: List[CoctMt530000UvProduct1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List["CoctMt530000UvSourceOf2"] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    class_code: Optional[ActClassSupply] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XClinicalStatementSupplyMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CoctMt530000UvComponent:
    class Meta:
        name = "COCT_MT530000UV.Component"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional["CoctMt530000UvObservation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    substance_administration: Optional[CoctMt530000UvSubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    supply: Optional[CoctMt530000UvSupply] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    procedure: Optional[CoctMt530000UvProcedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    encounter: Optional[CoctMt530000UvEncounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    act: Optional["CoctMt530000UvAct"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    organizer: Optional["CoctMt530000UvOrganizer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    act_reference: Optional[CoctMt530000UvActReference] = field(
        default=None,
        metadata={
            "name": "actReference",
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
    context_control_code: Optional[ContextControl] = field(
        default=None,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvOrganizer:
    class Meta:
        name = "COCT_MT530000UV.Organizer"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    component: List[CoctMt530000UvComponent] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List["CoctMt530000UvSourceOf2"] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    class_code: Optional[ActClassContainer] = field(
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
class CoctMt530000UvSourceOf2:
    class Meta:
        name = "COCT_MT530000UV.SourceOf2"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    pause_quantity: Optional[PqExplicit] = field(
        default=None,
        metadata={
            "name": "pauseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional["CoctMt530000UvObservation"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    substance_administration: Optional[CoctMt530000UvSubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    supply: Optional[CoctMt530000UvSupply] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    procedure: Optional[CoctMt530000UvProcedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    encounter: Optional[CoctMt530000UvEncounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    act: Optional["CoctMt530000UvAct"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    organizer: Optional[CoctMt530000UvOrganizer] = field(
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
    type_code: Optional[Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvObservation:
    class Meta:
        name = "COCT_MT530000UV.Observation"

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
    derivation_expr: Optional[St] = field(
        default=None,
        metadata={
            "name": "derivationExpr",
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    effective_time: List[SxcmTsExplicit] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
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
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "uncertaintyCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
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
    interpretation_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "interpretationCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    method_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "methodCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    target_site_code: List[Cd] = field(
        default_factory=list,
        metadata={
            "name": "targetSiteCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reference_range: List[CoctMt530000UvReferenceRange] = field(
        default_factory=list,
        metadata={
            "name": "referenceRange",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List["CoctMt530000UvSourceOf3"] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List[CoctMt530000UvSourceOf2] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    mood_code: Optional[XClinicalStatementObservationMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvSourceOf3:
    class Meta:
        name = "COCT_MT530000UV.SourceOf3"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    pause_quantity: Optional[PqExplicit] = field(
        default=None,
        metadata={
            "name": "pauseQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    conjunction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "conjunctionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    seperatable_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "seperatableInd",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[CoctMt530000UvObservation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    substance_administration: Optional[CoctMt530000UvSubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    supply: Optional[CoctMt530000UvSupply] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    procedure: Optional[CoctMt530000UvProcedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    encounter: Optional[CoctMt530000UvEncounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    act: Optional["CoctMt530000UvAct"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    organizer: Optional[CoctMt530000UvOrganizer] = field(
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
    type_code: Optional[Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, ActRelationshipPertainsValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev]] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AN,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt530000UvAct:
    class Meta:
        name = "COCT_MT530000UV.Act"

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
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
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
    availability_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "availabilityTime",
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
    confidentiality_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    uncertainty_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "uncertaintyCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: List[CoctMt530000UvSubject2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    record_target: Optional[CoctMt530000UvRecordTarget] = field(
        default=None,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    responsible_party: List[CoctMt530000UvResponsibleParty2] = field(
        default_factory=list,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    performer: List[CoctMt530000UvPerformer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: List[CoctMt530000UvAuthor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: Optional[CoctMt530000UvDataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    informant: List[CoctMt530000UvInformant] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    verifier: List[CoctMt530000UvVerifier] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    location: List[CoctMt530000UvLocation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: Optional[CoctMt530000UvDefinition] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    conditions: List[CoctMt530000UvConditions] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of1: List[CoctMt530000UvSourceOf1] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf1",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    source_of2: List[CoctMt530000UvSourceOf3] = field(
        default_factory=list,
        metadata={
            "name": "sourceOf2",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject_of: Optional[CoctMt530000UvSubject1] = field(
        default=None,
        metadata={
            "name": "subjectOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    target_of: List[CoctMt530000UvSourceOf2] = field(
        default_factory=list,
        metadata={
            "name": "targetOf",
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
    mood_code: Optional[XClinicalStatementActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )
    negation_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "negationInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )
