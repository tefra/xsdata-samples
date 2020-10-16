from dataclasses import dataclass, field
from enum import Enum
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
    CeExplicit,
    Cs,
    EdExplicit,
    EnExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    OnExplicit,
    PnExplicit,
    Pq,
    PqExplicit,
    ScExplicit,
    StExplicit,
    SxcmTsExplicit,
    TelExplicit,
    Ts,
    TsExplicit,
)
from common_types.models.hl7_v3.ne2008.core.narrative_block import StrucDocText
from common_types.models.hl7_v3.ne2008.core.sdtc import (
    BirthTime,
    DeceasedInd,
    DeceasedTime,
    DischargeDispositionCode,
    Id,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActClass,
    ActClassClinicalDocument,
    ActClassDocument,
    ActClassObservation,
    ActClassRoot,
    ActClassSupply,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipFulfills,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    ContextControl,
    EntityClass,
    EntityClassDevice,
    EntityClassManufacturedMaterial,
    EntityClassOrganization,
    EntityClassPlace,
    EntityClassRoot,
    EntityDeterminer,
    EntityDeterminerDetermined,
    NullFlavor,
    ParticipationPhysicalPerformer,
    ParticipationTargetLocation,
    ParticipationTargetSubject,
    ParticipationType,
    RoleClassAssignedEntity,
    RoleClassManufacturedProduct,
    RoleClassMutualRelationship,
    RoleClassOntological,
    RoleClassPartitive,
    RoleClassPassive,
    RoleClassServiceDeliveryLocation,
    RoleClassSpecimen,
    XAccommodationRequestorRole,
    XActClassDocumentEntryAct,
    XActClassDocumentEntryOrganizer,
    XActMoodDocumentObservation,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XDocumentActMood,
    XDocumentEncounterMood,
    XDocumentEntrySubject,
    XDocumentProcedureMood,
    XDocumentSubject,
    XDocumentSubstanceMood,
    XEncounterParticipant,
    XInformationRecipient,
    XInformationRecipientRole,
    XRoleClassAccommodationRequestor,
    XRoleClassCoverage,
    XRoleClassCoverageInvoice,
    XRoleClassCredentialedEntity,
    XRoleClassPayeePolicyRelationship,
    XSuccReplPrev,
    XServiceEventPerformer,
)

__NAMESPACE__ = "urn:hl7-org:v3"


class PocdMt000040AuthorizationValue(Enum):
    """
    :cvar PERT:
    :cvar NAME:
    :cvar AUTH:
    :cvar COVBY:
    :cvar ELNK:
    :cvar EXPL:
    :cvar PREV:
    :cvar REFV:
    :cvar SUBJ:
    :cvar DRIV:
    :cvar CAUS:
    :cvar MFST:
    :cvar ITEMSLOC:
    :cvar LIMIT:
    :cvar EVID:
    :cvar REFR:
    :cvar SUMM:
    """
    PERT = "PERT"
    NAME = "NAME"
    AUTH = "AUTH"
    COVBY = "COVBY"
    ELNK = "ELNK"
    EXPL = "EXPL"
    PREV = "PREV"
    REFV = "REFV"
    SUBJ = "SUBJ"
    DRIV = "DRIV"
    CAUS = "CAUS"
    MFST = "MFST"
    ITEMSLOC = "ITEMSLOC"
    LIMIT = "LIMIT"
    EVID = "EVID"
    REFR = "REFR"
    SUMM = "SUMM"


@dataclass
class PocdMt000040InfrastructureRootTypeId:
    """
    :ivar root:
    :ivar extension:
    :ivar assigning_authority_name: A human readable name or mnemonic for the assigning
                         authority. This name may be provided solely for the
                         convenience of unaided humans interpreting an  value
                         and can have no computational meaning. Note: no
                         automated processing must depend on the assigning
                         authority name to be present in any form.
    :ivar displayable: Specifies if the identifier is intended for human
                         display and data entry (displayable = true) as
                         opposed to pure machine interoperation (displayable
                         = false).
    """
    class Meta:
        name = "POCD_MT000040.InfrastructureRoot.typeId"

    root: str = field(
        init=False,
        default="2.16.840.1.113883.1.3",
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-2](\.(0|[1-9][0-9]*))*",
        }
    )
    extension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
        }
    )
    assigning_authority_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "assigningAuthorityName",
            "type": "Attribute",
            "min_length": 1,
        }
    )
    displayable: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


class PocdMt000040ParticipantRoleValue(Enum):
    """
    :cvar ROL:
    """
    ROL = "ROL"


class PocdMt000040ReferenceRangeValue(Enum):
    """
    :cvar PERT:
    :cvar NAME:
    :cvar AUTH:
    :cvar COVBY:
    :cvar ELNK:
    :cvar EXPL:
    :cvar PREV:
    :cvar REFV:
    :cvar SUBJ:
    :cvar DRIV:
    :cvar CAUS:
    :cvar MFST:
    :cvar ITEMSLOC:
    :cvar LIMIT:
    :cvar EVID:
    :cvar REFR:
    :cvar SUMM:
    """
    PERT = "PERT"
    NAME = "NAME"
    AUTH = "AUTH"
    COVBY = "COVBY"
    ELNK = "ELNK"
    EXPL = "EXPL"
    PREV = "PREV"
    REFV = "REFV"
    SUBJ = "SUBJ"
    DRIV = "DRIV"
    CAUS = "CAUS"
    MFST = "MFST"
    ITEMSLOC = "ITEMSLOC"
    LIMIT = "LIMIT"
    EVID = "EVID"
    REFR = "REFR"
    SUMM = "SUMM"


@dataclass
class PocdMt000040Component5:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar section:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "POCD_MT000040.Component5"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    section: Optional["PocdMt000040Section"] = field(
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class PocdMt000040Consent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar status_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Consent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.CONS,
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
class PocdMt000040Criterion:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar value:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Criterion"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
        }
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassObservation = field(
        default=ActClassObservation.OBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040CustodianOrganization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar name:
    :ivar telecom:
    :ivar addr:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.CustodianOrganization"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
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
    class_code: EntityClassOrganization = field(
        init=False,
        default=EntityClassOrganization.ORG,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Device:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar manufacturer_model_name:
    :ivar software_name:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Device"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    manufacturer_model_name: Optional[ScExplicit] = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    software_name: Optional[ScExplicit] = field(
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
    class_code: EntityClassDevice = field(
        default=EntityClassDevice.DEV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Entity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar desc:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Entity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    desc: Optional[EdExplicit] = field(
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
    class_code: EntityClassRoot = field(
        default=EntityClassRoot.ENT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040ExternalAct:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ExternalAct"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassRoot = field(
        default=ActClassRoot.ACT,
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
class PocdMt000040ExternalDocument:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar set_id:
    :ivar version_number:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ExternalDocument"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    set_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "setId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    version_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "versionNumber",
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
    class_code: ActClassDocument = field(
        default=ActClassDocument.DOC,
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
class PocdMt000040ExternalObservation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ExternalObservation"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassObservation = field(
        default=ActClassObservation.OBS,
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
class PocdMt000040ExternalProcedure:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ExternalProcedure"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.PROC,
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
class PocdMt000040LabeledDrug:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar name:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.LabeledDrug"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: EntityClassManufacturedMaterial = field(
        init=False,
        default=EntityClassManufacturedMaterial.MMAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminerDetermined = field(
        init=False,
        default=EntityDeterminerDetermined.KIND,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040LanguageCommunication:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar language_code:
    :ivar mode_code:
    :ivar proficiency_level_code:
    :ivar preference_ind:
    :ivar null_flavor:
    """
    class Meta:
        name = "POCD_MT000040.LanguageCommunication"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
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
    proficiency_level_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "proficiencyLevelCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    preference_ind: Optional[Bl] = field(
        default=None,
        metadata={
            "name": "preferenceInd",
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


@dataclass
class PocdMt000040Material:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar name:
    :ivar lot_number_text:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Material"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    code: Optional[CeExplicit] = field(
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
    lot_number_text: Optional[StExplicit] = field(
        default=None,
        metadata={
            "name": "lotNumberText",
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
    class_code: EntityClassManufacturedMaterial = field(
        init=False,
        default=EntityClassManufacturedMaterial.MMAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminerDetermined = field(
        init=False,
        default=EntityDeterminerDetermined.KIND,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040NonXmlbody:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar text:
    :ivar confidentiality_code:
    :ivar language_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.NonXMLBody"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "required": True,
        }
    )
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
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
        default=ActClass.DOCBODY,
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
class PocdMt000040ObservationRange:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar value:
    :ivar interpretation_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ObservationRange"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
        }
    )
    interpretation_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "interpretationCode",
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
    class_code: ActClassObservation = field(
        default=ActClassObservation.OBS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.EVN_CRT,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Order:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar priority_code:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Order"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
        }
    )
    code: Optional[Ce] = field(
        default=None,
        metadata={
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
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        }
    )
    class_code: ActClassRoot = field(
        default=ActClassRoot.ACT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.RQO,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040OrganizationPartOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar status_code:
    :ivar effective_time:
    :ivar whole_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.OrganizationPartOf"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    whole_organization: Optional["PocdMt000040Organization"] = field(
        default=None,
        metadata={
            "name": "wholeOrganization",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "PocdMt000040OrganizationPartOf.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassPartitive.PART,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class PocdMt000040ParentDocument:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar set_id:
    :ivar version_number:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ParentDocument"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
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
    set_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "setId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    version_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "versionNumber",
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
    class_code: ActClassClinicalDocument = field(
        init=False,
        default=ActClassClinicalDocument.DOCCLIN,
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
class PocdMt000040Person:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar name:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Person"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Place:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar name:
    :ivar addr:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Place"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    name: Optional[EnExplicit] = field(
        default=None,
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
    class_code: EntityClassPlace = field(
        init=False,
        default=EntityClassPlace.PLC,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040PlayingEntity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar quantity:
    :ivar name:
    :ivar birth_time:
    :ivar desc:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.PlayingEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    code: Optional[CeExplicit] = field(
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
    name: List[PnExplicit] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    birth_time: Optional[BirthTime] = field(
        default=None,
        metadata={
            "name": "birthTime",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    desc: Optional[StExplicit] = field(
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
    class_code: EntityClassRoot = field(
        default=EntityClassRoot.ENT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040RegionOfInterestValue(IntType):
    """
    :ivar unsorted:
    """
    class Meta:
        name = "POCD_MT000040.RegionOfInterest.value"

    unsorted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040SubjectPerson:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar name:
    :ivar administrative_gender_code:
    :ivar birth_time:
    :ivar deceased_ind:
    :ivar deceased_time:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.SubjectPerson"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    id: List[Id] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    name: List[PnExplicit] = field(
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
    deceased_ind: Optional[DeceasedInd] = field(
        default=None,
        metadata={
            "name": "deceasedInd",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
        }
    )
    deceased_time: Optional[DeceasedTime] = field(
        default=None,
        metadata={
            "name": "deceasedTime",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
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
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040AssignedCustodian:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar represented_custodian_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.AssignedCustodian"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    represented_custodian_organization: Optional[PocdMt000040CustodianOrganization] = field(
        default=None,
        metadata={
            "name": "representedCustodianOrganization",
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
    class_code: RoleClassAssignedEntity = field(
        init=False,
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Authorization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar consent:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Authorization"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    consent: Optional[PocdMt000040Consent] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, PocdMt000040AuthorizationValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=PocdMt000040AuthorizationValue.AUTH,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class PocdMt000040Birthplace:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar place:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.Birthplace"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    place: Optional[PocdMt000040Place] = field(
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "PocdMt000040Birthplace.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassPassive.BIRTHPL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class PocdMt000040InFulfillmentOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar order:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.InFulfillmentOf"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    order: Optional[PocdMt000040Order] = field(
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
    type_code: ActRelationshipFulfills = field(
        init=False,
        default=ActRelationshipFulfills.FLFS,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040MaintainedEntity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar effective_time:
    :ivar maintaining_person:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.MaintainedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    maintaining_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "maintainingPerson",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "PocdMt000040MaintainedEntity.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassPassive.MNT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class PocdMt000040Organization:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar name:
    :ivar telecom:
    :ivar addr:
    :ivar standard_industry_class_code:
    :ivar as_organization_part_of:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Organization"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    standard_industry_class_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "standardIndustryClassCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_organization_part_of: Optional[PocdMt000040OrganizationPartOf] = field(
        default=None,
        metadata={
            "name": "asOrganizationPartOf",
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
    class_code: EntityClassOrganization = field(
        init=False,
        default=EntityClassOrganization.ORG,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040ParticipantRole:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar playing_device:
    :ivar playing_entity:
    :ivar scoping_entity:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.ParticipantRole"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    playing_device: Optional[PocdMt000040Device] = field(
        default=None,
        metadata={
            "name": "playingDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    playing_entity: Optional[PocdMt000040PlayingEntity] = field(
        default=None,
        metadata={
            "name": "playingEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    scoping_entity: Optional[PocdMt000040Entity] = field(
        default=None,
        metadata={
            "name": "scopingEntity",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, PocdMt000040ParticipantRoleValue] = field(
        default=PocdMt000040ParticipantRoleValue.ROL,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class PocdMt000040Precondition:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar criterion:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Precondition"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    criterion: Optional[PocdMt000040Criterion] = field(
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "PocdMt000040Precondition.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipConditional.PRCN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar PERT:
        :cvar NAME:
        :cvar AUTH:
        :cvar COVBY:
        :cvar ELNK:
        :cvar EXPL:
        :cvar PREV:
        :cvar REFV:
        :cvar SUBJ:
        :cvar DRIV:
        :cvar CAUS:
        :cvar MFST:
        :cvar ITEMSLOC:
        :cvar LIMIT:
        :cvar EVID:
        :cvar REFR:
        :cvar SUMM:
        """
        PERT = "PERT"
        NAME = "NAME"
        AUTH = "AUTH"
        COVBY = "COVBY"
        ELNK = "ELNK"
        EXPL = "EXPL"
        PREV = "PREV"
        REFV = "REFV"
        SUBJ = "SUBJ"
        DRIV = "DRIV"
        CAUS = "CAUS"
        MFST = "MFST"
        ITEMSLOC = "ITEMSLOC"
        LIMIT = "LIMIT"
        EVID = "EVID"
        REFR = "REFR"
        SUMM = "SUMM"


@dataclass
class PocdMt000040Reference:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar seperatable_ind:
    :ivar external_act:
    :ivar external_observation:
    :ivar external_procedure:
    :ivar external_document:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Reference"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    external_act: Optional[PocdMt000040ExternalAct] = field(
        default=None,
        metadata={
            "name": "externalAct",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_observation: Optional[PocdMt000040ExternalObservation] = field(
        default=None,
        metadata={
            "name": "externalObservation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_procedure: Optional[PocdMt000040ExternalProcedure] = field(
        default=None,
        metadata={
            "name": "externalProcedure",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    external_document: Optional[PocdMt000040ExternalDocument] = field(
        default=None,
        metadata={
            "name": "externalDocument",
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
    type_code: Optional[XActRelationshipExternalReference] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040ReferenceRange:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar observation_range:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.ReferenceRange"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    observation_range: Optional[PocdMt000040ObservationRange] = field(
        default=None,
        metadata={
            "name": "observationRange",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, PocdMt000040ReferenceRangeValue, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=PocdMt000040ReferenceRangeValue.REFV,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class PocdMt000040RelatedDocument:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar parent_document:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.RelatedDocument"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    parent_document: Optional[PocdMt000040ParentDocument] = field(
        default=None,
        metadata={
            "name": "parentDocument",
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
    type_code: Optional[XActRelationshipDocument] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040RelatedEntity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar effective_time:
    :ivar related_person:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.RelatedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "relatedPerson",
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
    class_code: Optional[RoleClassMutualRelationship] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040RelatedSubject:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar subject:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.RelatedSubject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    subject: Optional[PocdMt000040SubjectPerson] = field(
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
    class_code: XDocumentSubject = field(
        default=XDocumentSubject.PRS,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040SpecimenRole:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar specimen_playing_entity:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.SpecimenRole"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    specimen_playing_entity: Optional[PocdMt000040PlayingEntity] = field(
        default=None,
        metadata={
            "name": "specimenPlayingEntity",
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
    class_code: RoleClassSpecimen = field(
        init=False,
        default=RoleClassSpecimen.SPEC,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040AssignedEntity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar assigned_person:
    :ivar represented_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.AssignedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
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
    assigned_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    represented_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "representedOrganization",
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
    class_code: RoleClassAssignedEntity = field(
        init=False,
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040AssociatedEntity:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar associated_person:
    :ivar scoping_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.AssociatedEntity"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    associated_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "associatedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    scoping_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "scopingOrganization",
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
    class_code: Optional[Union[RoleClassMutualRelationship, RoleClassPassive, str]] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
        }
    )


@dataclass
class PocdMt000040AuthoringDevice:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar manufacturer_model_name:
    :ivar software_name:
    :ivar as_maintained_entity:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.AuthoringDevice"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    manufacturer_model_name: Optional[ScExplicit] = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    software_name: Optional[ScExplicit] = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    as_maintained_entity: List[PocdMt000040MaintainedEntity] = field(
        default_factory=list,
        metadata={
            "name": "asMaintainedEntity",
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
    class_code: EntityClassDevice = field(
        init=False,
        default=EntityClassDevice.DEV,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Custodian:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_custodian:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Custodian"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_custodian: Optional[PocdMt000040AssignedCustodian] = field(
        default=None,
        metadata={
            "name": "assignedCustodian",
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
        default=ParticipationType.CST,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Guardian:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar guardian_person:
    :ivar guardian_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.Guardian"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    guardian_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "guardianPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    guardian_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "guardianOrganization",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "PocdMt000040Guardian.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.GUARD,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class PocdMt000040HealthCareFacility:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar location:
    :ivar service_provider_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.HealthCareFacility"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    location: Optional[PocdMt000040Place] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    service_provider_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "serviceProviderOrganization",
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
    class_code: RoleClassServiceDeliveryLocation = field(
        default=RoleClassServiceDeliveryLocation.SDLOC,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040IntendedRecipient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar addr:
    :ivar telecom:
    :ivar information_recipient:
    :ivar received_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.IntendedRecipient"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    information_recipient: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    received_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "receivedOrganization",
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
    class_code: XInformationRecipientRole = field(
        default=XInformationRecipientRole.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040ManufacturedProduct:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar manufactured_labeled_drug:
    :ivar manufactured_material:
    :ivar manufacturer_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.ManufacturedProduct"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    manufactured_labeled_drug: Optional[PocdMt000040LabeledDrug] = field(
        default=None,
        metadata={
            "name": "manufacturedLabeledDrug",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufactured_material: Optional[PocdMt000040Material] = field(
        default=None,
        metadata={
            "name": "manufacturedMaterial",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    manufacturer_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "manufacturerOrganization",
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
    class_code: RoleClassManufacturedProduct = field(
        init=False,
        default=RoleClassManufacturedProduct.MANU,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Participant2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar awareness_code:
    :ivar participant_role:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.Participant2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    awareness_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "awarenessCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant_role: Optional[PocdMt000040ParticipantRole] = field(
        default=None,
        metadata={
            "name": "participantRole",
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
    type_code: Optional[ParticipationType] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Specimen:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar specimen_role:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Specimen"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    specimen_role: Optional[PocdMt000040SpecimenRole] = field(
        default=None,
        metadata={
            "name": "specimenRole",
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
        default=ParticipationType.SPC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Subject:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar awareness_code:
    :ivar related_subject:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.Subject"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    awareness_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "awarenessCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_subject: Optional[PocdMt000040RelatedSubject] = field(
        default=None,
        metadata={
            "name": "relatedSubject",
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
    type_code: ParticipationTargetSubject = field(
        init=False,
        default=ParticipationTargetSubject.SBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040AssignedAuthor:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar addr:
    :ivar telecom:
    :ivar assigned_person:
    :ivar assigned_authoring_device:
    :ivar represented_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.AssignedAuthor"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
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
    assigned_person: Optional[PocdMt000040Person] = field(
        default=None,
        metadata={
            "name": "assignedPerson",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_authoring_device: Optional[PocdMt000040AuthoringDevice] = field(
        default=None,
        metadata={
            "name": "assignedAuthoringDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    represented_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "representedOrganization",
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
    class_code: RoleClassAssignedEntity = field(
        init=False,
        default=RoleClassAssignedEntity.ASSIGNED,
        metadata={
            "name": "classCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Authenticator:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar signature_code:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Authenticator"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "required": True,
        }
    )
    signature_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "signatureCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
        default=ParticipationType.AUTHEN,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Consumable:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar manufactured_product:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Consumable"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    manufactured_product: Optional[PocdMt000040ManufacturedProduct] = field(
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
        default=ParticipationType.CSM,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040DataEnterer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.DataEnterer"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
        default=ParticipationType.ENT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040EncounterParticipant:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.EncounterParticipant"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
    type_code: Optional[XEncounterParticipant] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040Informant12:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_entity:
    :ivar related_entity:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.Informant12"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_entity: Optional[PocdMt000040RelatedEntity] = field(
        default=None,
        metadata={
            "name": "relatedEntity",
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
    type_code: ParticipationType = field(
        init=False,
        default=ParticipationType.INF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040InformationRecipient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar intended_recipient:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.InformationRecipient"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    intended_recipient: Optional[PocdMt000040IntendedRecipient] = field(
        default=None,
        metadata={
            "name": "intendedRecipient",
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
    type_code: XInformationRecipient = field(
        default=XInformationRecipient.PRCP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040LegalAuthenticator:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar signature_code:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.LegalAuthenticator"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "required": True,
        }
    )
    signature_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "signatureCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
        default=ParticipationType.LA,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Location:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar health_care_facility:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Location"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    health_care_facility: Optional[PocdMt000040HealthCareFacility] = field(
        default=None,
        metadata={
            "name": "healthCareFacility",
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
    type_code: ParticipationTargetLocation = field(
        init=False,
        default=ParticipationTargetLocation.LOC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Participant1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar function_code:
    :ivar time:
    :ivar associated_entity:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.Participant1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    associated_entity: Optional[PocdMt000040AssociatedEntity] = field(
        default=None,
        metadata={
            "name": "associatedEntity",
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
    type_code: Optional[ParticipationType] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Patient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar name:
    :ivar administrative_gender_code:
    :ivar birth_time:
    :ivar marital_status_code:
    :ivar religious_affiliation_code:
    :ivar race_code:
    :ivar ethnic_group_code:
    :ivar guardian:
    :ivar birthplace:
    :ivar language_communication:
    :ivar null_flavor:
    :ivar class_code:
    :ivar determiner_code:
    """
    class Meta:
        name = "POCD_MT000040.Patient"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    name: List[PnExplicit] = field(
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
    guardian: List[PocdMt000040Guardian] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    birthplace: Optional[PocdMt000040Birthplace] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_communication: List[PocdMt000040LanguageCommunication] = field(
        default_factory=list,
        metadata={
            "name": "languageCommunication",
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
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Performer1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar function_code:
    :ivar time:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Performer1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
    type_code: Optional[XServiceEventPerformer] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040Performer2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar mode_code:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Performer2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    mode_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "modeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
    type_code: ParticipationPhysicalPerformer = field(
        init=False,
        default=ParticipationPhysicalPerformer.PRF,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Product:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar manufactured_product:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Product"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    manufactured_product: Optional[PocdMt000040ManufacturedProduct] = field(
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
        }
    )


@dataclass
class PocdMt000040ResponsibleParty:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_entity:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.ResponsibleParty"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    assigned_entity: Optional[PocdMt000040AssignedEntity] = field(
        default=None,
        metadata={
            "name": "assignedEntity",
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
        default=ParticipationType.RESP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar function_code:
    :ivar time:
    :ivar assigned_author:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.Author"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    assigned_author: Optional[PocdMt000040AssignedAuthor] = field(
        default=None,
        metadata={
            "name": "assignedAuthor",
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
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040EncompassingEncounter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar effective_time:
    :ivar discharge_disposition_code:
    :ivar responsible_party:
    :ivar encounter_participant:
    :ivar location:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.EncompassingEncounter"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "required": True,
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
    responsible_party: Optional[PocdMt000040ResponsibleParty] = field(
        default=None,
        metadata={
            "name": "responsibleParty",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter_participant: List[PocdMt000040EncounterParticipant] = field(
        default_factory=list,
        metadata={
            "name": "encounterParticipant",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    location: Optional[PocdMt000040Location] = field(
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.ENC,
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
class PocdMt000040PatientRole:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar addr:
    :ivar telecom:
    :ivar patient:
    :ivar provider_organization:
    :ivar null_flavor:
    :ivar class_code:
    """
    class Meta:
        name = "POCD_MT000040.PatientRole"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
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
    patient: Optional[PocdMt000040Patient] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    provider_organization: Optional[PocdMt000040Organization] = field(
        default=None,
        metadata={
            "name": "providerOrganization",
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
    class_code: Union[RoleClassMutualRelationship, RoleClassPassive, str, RoleClassOntological, RoleClassPartitive, "PocdMt000040PatientRole.Value", XAccommodationRequestorRole, XDocumentEntrySubject, XDocumentSubject, XInformationRecipientRole, XRoleClassAccommodationRequestor, XRoleClassCoverage, XRoleClassCoverageInvoice, XRoleClassCredentialedEntity, XRoleClassPayeePolicyRelationship] = field(
        init=False,
        default=RoleClassMutualRelationship.PAT,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar ROL:
        """
        ROL = "ROL"


@dataclass
class PocdMt000040ServiceEvent:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar effective_time:
    :ivar performer:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ServiceEvent"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    performer: List[PocdMt000040Performer1] = field(
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
    class_code: ActClassRoot = field(
        default=ActClassRoot.ACT,
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
class PocdMt000040Component1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar encompassing_encounter:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.Component1"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    encompassing_encounter: Optional[PocdMt000040EncompassingEncounter] = field(
        default=None,
        metadata={
            "name": "encompassingEncounter",
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040DocumentationOf:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar service_event:
    :ivar null_flavor:
    :ivar type_code:
    """
    class Meta:
        name = "POCD_MT000040.DocumentationOf"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    service_event: Optional[PocdMt000040ServiceEvent] = field(
        default=None,
        metadata={
            "name": "serviceEvent",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, "PocdMt000040DocumentationOf.Value", ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=ActRelationshipSequel.DOC,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "pattern": r"[^\s]+",
        }
    )

    class Value(Enum):
        """
        :cvar PERT:
        :cvar NAME:
        :cvar AUTH:
        :cvar COVBY:
        :cvar ELNK:
        :cvar EXPL:
        :cvar PREV:
        :cvar REFV:
        :cvar SUBJ:
        :cvar DRIV:
        :cvar CAUS:
        :cvar MFST:
        :cvar ITEMSLOC:
        :cvar LIMIT:
        :cvar EVID:
        :cvar REFR:
        :cvar SUMM:
        """
        PERT = "PERT"
        NAME = "NAME"
        AUTH = "AUTH"
        COVBY = "COVBY"
        ELNK = "ELNK"
        EXPL = "EXPL"
        PREV = "PREV"
        REFV = "REFV"
        SUBJ = "SUBJ"
        DRIV = "DRIV"
        CAUS = "CAUS"
        MFST = "MFST"
        ITEMSLOC = "ITEMSLOC"
        LIMIT = "LIMIT"
        EVID = "EVID"
        REFR = "REFR"
        SUMM = "SUMM"


@dataclass
class PocdMt000040Encounter:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar discharge_disposition_code:
    :ivar priority_code:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Encounter"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    discharge_disposition_code: Optional[DischargeDispositionCode] = field(
        default=None,
        metadata={
            "name": "dischargeDispositionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:sdtc",
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
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
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
    class_code: Optional[ActClass] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentEncounterMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040Observation:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar derivation_expr:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar repeat_number:
    :ivar language_code:
    :ivar value:
    :ivar interpretation_code:
    :ivar method_code:
    :ivar target_site_code:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar reference_range:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "POCD_MT000040.Observation"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    derivation_expr: Optional[StExplicit] = field(
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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
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
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: List[Any] = field(
        default_factory=list,
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
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference_range: List[PocdMt000040ReferenceRange] = field(
        default_factory=list,
        metadata={
            "name": "referenceRange",
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
    mood_code: Optional[XActMoodDocumentObservation] = field(
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
class PocdMt000040ObservationMedia:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar language_code:
    :ivar value:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar id_attribute:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ObservationMedia"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[EdExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
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
    mood_code: Optional[ActMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040Procedure:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar language_code:
    :ivar method_code:
    :ivar approach_site_code:
    :ivar target_site_code:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "POCD_MT000040.Procedure"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    priority_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
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
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
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
    class_code: Optional[ActClass] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentProcedureMood] = field(
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
class PocdMt000040RecordTarget:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar patient_role:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "POCD_MT000040.RecordTarget"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    patient_role: Optional[PocdMt000040PatientRole] = field(
        default=None,
        metadata={
            "name": "patientRole",
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
        default=ParticipationType.RCT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_control_code: ContextControl = field(
        init=False,
        default=ContextControl.OP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class PocdMt000040RegionOfInterest:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar value:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar id_attribute:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.RegionOfInterest"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
            "min_occurs": 1,
        }
    )
    code: Optional[Cs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    value: List[PocdMt000040RegionOfInterestValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
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
        default=ActClass.ROIOVL,
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
class PocdMt000040SubstanceAdministration:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar repeat_number:
    :ivar route_code:
    :ivar approach_site_code:
    :ivar dose_quantity:
    :ivar rate_quantity:
    :ivar max_dose_quantity:
    :ivar administration_unit_code:
    :ivar subject:
    :ivar specimen:
    :ivar consumable:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "POCD_MT000040.SubstanceAdministration"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    effective_time: List[Ts] = field(
        default_factory=list,
        metadata={
            "name": "effectiveTime",
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
    repeat_number: Optional[IvlInt] = field(
        default=None,
        metadata={
            "name": "repeatNumber",
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
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    consumable: Optional[PocdMt000040Consumable] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.SBADM,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentSubstanceMood] = field(
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
class PocdMt000040Supply:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar repeat_number:
    :ivar independent_ind:
    :ivar quantity:
    :ivar expected_use_time:
    :ivar subject:
    :ivar specimen:
    :ivar product:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Supply"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    priority_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
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
    quantity: Optional[Pq] = field(
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
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    product: Optional[PocdMt000040Product] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List["PocdMt000040EntryRelationship"] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
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
    class_code: ActClassSupply = field(
        init=False,
        default=ActClassSupply.SPLY,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentSubstanceMood] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PocdMt000040Component4:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar seperatable_ind:
    :ivar act:
    :ivar encounter:
    :ivar observation:
    :ivar observation_media:
    :ivar organizer:
    :ivar procedure:
    :ivar region_of_interest:
    :ivar substance_administration:
    :ivar supply:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "POCD_MT000040.Component4"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    act: Optional["PocdMt000040Act"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter: Optional[PocdMt000040Encounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[PocdMt000040Observation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_media: Optional[PocdMt000040ObservationMedia] = field(
        default=None,
        metadata={
            "name": "observationMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    organizer: Optional["PocdMt000040Organizer"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    procedure: Optional[PocdMt000040Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    region_of_interest: Optional[PocdMt000040RegionOfInterest] = field(
        default=None,
        metadata={
            "name": "regionOfInterest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substance_administration: Optional[PocdMt000040SubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply: Optional[PocdMt000040Supply] = field(
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class PocdMt000040Organizer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar status_code:
    :ivar effective_time:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar reference:
    :ivar precondition:
    :ivar component:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Organizer"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    status_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "statusCode",
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
        }
    )
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[PocdMt000040Component4] = field(
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
    class_code: Optional[XActClassDocumentEntryOrganizer] = field(
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
class PocdMt000040EntryRelationship:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar seperatable_ind:
    :ivar act:
    :ivar encounter:
    :ivar observation:
    :ivar observation_media:
    :ivar organizer:
    :ivar procedure:
    :ivar region_of_interest:
    :ivar substance_administration:
    :ivar supply:
    :ivar null_flavor:
    :ivar type_code:
    :ivar inversion_ind:
    :ivar context_conduction_ind:
    :ivar negation_ind:
    """
    class Meta:
        name = "POCD_MT000040.EntryRelationship"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    act: Optional["PocdMt000040Act"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter: Optional[PocdMt000040Encounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[PocdMt000040Observation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_media: Optional[PocdMt000040ObservationMedia] = field(
        default=None,
        metadata={
            "name": "observationMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    organizer: Optional[PocdMt000040Organizer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    procedure: Optional[PocdMt000040Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    region_of_interest: Optional[PocdMt000040RegionOfInterest] = field(
        default=None,
        metadata={
            "name": "regionOfInterest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substance_administration: Optional[PocdMt000040SubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply: Optional[PocdMt000040Supply] = field(
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
    type_code: Optional[XActRelationshipEntryRelationship] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
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
class PocdMt000040Act:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar status_code:
    :ivar effective_time:
    :ivar priority_code:
    :ivar language_code:
    :ivar subject:
    :ivar specimen:
    :ivar performer:
    :ivar author:
    :ivar informant:
    :ivar participant:
    :ivar entry_relationship:
    :ivar reference:
    :ivar precondition:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    :ivar negation_ind:
    """
    class Meta:
        name = "POCD_MT000040.Act"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    priority_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    specimen: List[PocdMt000040Specimen] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    performer: List[PocdMt000040Performer2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry_relationship: List[PocdMt000040EntryRelationship] = field(
        default_factory=list,
        metadata={
            "name": "entryRelationship",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    reference: List[PocdMt000040Reference] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    precondition: List[PocdMt000040Precondition] = field(
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
    class_code: Optional[XActClassDocumentEntryAct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XDocumentActMood] = field(
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
class PocdMt000040Entry:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar act:
    :ivar encounter:
    :ivar observation:
    :ivar observation_media:
    :ivar organizer:
    :ivar procedure:
    :ivar region_of_interest:
    :ivar substance_administration:
    :ivar supply:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "POCD_MT000040.Entry"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    act: Optional[PocdMt000040Act] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    encounter: Optional[PocdMt000040Encounter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation: Optional[PocdMt000040Observation] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    observation_media: Optional[PocdMt000040ObservationMedia] = field(
        default=None,
        metadata={
            "name": "observationMedia",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    organizer: Optional[PocdMt000040Organizer] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    procedure: Optional[PocdMt000040Procedure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    region_of_interest: Optional[PocdMt000040RegionOfInterest] = field(
        default=None,
        metadata={
            "name": "regionOfInterest",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    substance_administration: Optional[PocdMt000040SubstanceAdministration] = field(
        default=None,
        metadata={
            "name": "substanceAdministration",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    supply: Optional[PocdMt000040Supply] = field(
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
    type_code: XActRelationshipEntry = field(
        default=XActRelationshipEntry.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class PocdMt000040Section:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar title:
    :ivar text:
    :ivar confidentiality_code:
    :ivar language_code:
    :ivar subject:
    :ivar author:
    :ivar informant:
    :ivar entry:
    :ivar component:
    :ivar id_attribute:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.Section"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    title: Optional[StExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    text: Optional[StrucDocText] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    subject: Optional[PocdMt000040Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    entry: List[PocdMt000040Entry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[PocdMt000040Component5] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    id_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
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
        default=ActClass.DOCSECT,
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
class PocdMt000040Component3:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar section:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "POCD_MT000040.Component3"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    section: Optional[PocdMt000040Section] = field(
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class PocdMt000040StructuredBody:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar confidentiality_code:
    :ivar language_code:
    :ivar component:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.StructuredBody"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: List[PocdMt000040Component3] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
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
        default=ActClass.DOCBODY,
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
class PocdMt000040Component2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar non_xmlbody:
    :ivar structured_body:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "POCD_MT000040.Component2"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
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
    non_xmlbody: Optional[PocdMt000040NonXmlbody] = field(
        default=None,
        metadata={
            "name": "nonXMLBody",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    structured_body: Optional[PocdMt000040StructuredBody] = field(
        default=None,
        metadata={
            "name": "structuredBody",
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
    type_code: ActRelationshipHasComponent = field(
        init=False,
        default=ActRelationshipHasComponent.COMP,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
        }
    )
    context_conduction_ind: str = field(
        init=False,
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class PocdMt000040ClinicalDocument:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar title:
    :ivar effective_time:
    :ivar confidentiality_code:
    :ivar language_code:
    :ivar set_id:
    :ivar version_number:
    :ivar copy_time:
    :ivar record_target:
    :ivar author:
    :ivar data_enterer:
    :ivar informant:
    :ivar custodian:
    :ivar information_recipient:
    :ivar legal_authenticator:
    :ivar authenticator:
    :ivar participant:
    :ivar in_fulfillment_of:
    :ivar documentation_of:
    :ivar related_document:
    :ivar authorization:
    :ivar component_of:
    :ivar component:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "POCD_MT000040.ClinicalDocument"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    type_id: Optional[PocdMt000040InfrastructureRootTypeId] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
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
            "required": True,
        }
    )
    title: Optional[StExplicit] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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
    confidentiality_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "confidentialityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    language_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    set_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "setId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    version_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "versionNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    copy_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "copyTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    record_target: List[PocdMt000040RecordTarget] = field(
        default_factory=list,
        metadata={
            "name": "recordTarget",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    author: List[PocdMt000040Author] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    data_enterer: Optional[PocdMt000040DataEnterer] = field(
        default=None,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    informant: List[PocdMt000040Informant12] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    custodian: Optional[PocdMt000040Custodian] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    information_recipient: List[PocdMt000040InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    legal_authenticator: Optional[PocdMt000040LegalAuthenticator] = field(
        default=None,
        metadata={
            "name": "legalAuthenticator",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    authenticator: List[PocdMt000040Authenticator] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    participant: List[PocdMt000040Participant1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    in_fulfillment_of: List[PocdMt000040InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    documentation_of: List[PocdMt000040DocumentationOf] = field(
        default_factory=list,
        metadata={
            "name": "documentationOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    related_document: List[PocdMt000040RelatedDocument] = field(
        default_factory=list,
        metadata={
            "name": "relatedDocument",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    authorization: List[PocdMt000040Authorization] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component_of: Optional[PocdMt000040Component1] = field(
        default=None,
        metadata={
            "name": "componentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    component: Optional[PocdMt000040Component2] = field(
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
    class_code: ActClassClinicalDocument = field(
        init=False,
        default=ActClassClinicalDocument.DOCCLIN,
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
