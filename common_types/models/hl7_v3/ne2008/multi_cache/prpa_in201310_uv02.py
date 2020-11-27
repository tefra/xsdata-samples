from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from common_types.models.hl7_v3.ne2008.core.datatypes_base import (
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IvlTsExplicit,
    St,
    TsExplicit,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActClass,
    ActClassControlAct,
    ActMood,
    ActRelationshipConditional,
    ActRelationshipCostTracking,
    ActRelationshipHasComponent,
    ActRelationshipHasSupport,
    ActRelationshipOutcome,
    ActRelationshipPosting,
    ActRelationshipSequel,
    ActRelationshipTemporallyPertains,
    NullFlavor,
    ParticipationTargetSubject,
    XActMoodIntentEvent,
    XActRelationshipDocument,
    XActRelationshipEntry,
    XActRelationshipEntryRelationship,
    XActRelationshipExternalReference,
    XActRelationshipPatientTransport,
    XActRelationshipPertinentInfo,
    XActRelationshipRelatedAuthorizations,
    XActReplaceOrRevise,
    XSuccReplPrev,
)
from common_types.models.hl7_v3.ne2008.multi_cache.mcci_mt000300_uv01 import (
    McciMt000300Uv01Acknowledgement,
    McciMt000300Uv01AttentionLine,
    McciMt000300Uv01Receiver,
    McciMt000300Uv01RespondTo,
    McciMt000300Uv01Sender,
)
from common_types.models.hl7_v3.ne2008.multi_cache.mfmi_mt700711_uv01 import (
    MfmiMt700711Uv01Author2,
    MfmiMt700711Uv01AuthorOrPerformer,
    MfmiMt700711Uv01Custodian,
    MfmiMt700711Uv01DataEnterer,
    MfmiMt700711Uv01Definition,
    MfmiMt700711Uv01InFulfillmentOf,
    MfmiMt700711Uv01InformationRecipient,
    MfmiMt700711Uv01Overseer,
    MfmiMt700711Uv01QueryAck,
    MfmiMt700711Uv01Reason,
    MfmiMt700711Uv01ReplacementOf,
)
from common_types.models.hl7_v3.ne2008.multi_cache.prpa_mt201304_uv02 import PrpaMt201304Uv02Patient
from common_types.models.hl7_v3.ne2008.multi_cache.prpa_mt201307_uv02 import PrpaMt201307Uv02QueryByParameter

__NAMESPACE__ = "urn:hl7-org:v3"


class PrpaIn201310Uv02MfmiMt700711Uv01Subject1Value(Enum):
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
class PrpaIn201310Uv02MfmiMt700711Uv01Subject2:
    class Meta:
        name = "PRPA_IN201310UV02.MFMI_MT700711UV01.Subject2"

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
    patient: Optional[PrpaMt201304Uv02Patient] = field(
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
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrpaIn201310Uv02MfmiMt700711Uv01RegistrationEvent:
    class Meta:
        name = "PRPA_IN201310UV02.MFMI_MT700711UV01.RegistrationEvent"

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
    subject1: Optional[PrpaIn201310Uv02MfmiMt700711Uv01Subject2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    author: Optional[MfmiMt700711Uv01Author2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    custodian: Optional[MfmiMt700711Uv01Custodian] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
            "nillable": True,
        }
    )
    in_fulfillment_of: List[MfmiMt700711Uv01InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    definition: List[MfmiMt700711Uv01Definition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    replacement_of: List[MfmiMt700711Uv01ReplacementOf] = field(
        default_factory=list,
        metadata={
            "name": "replacementOf",
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
        default=ActClass.REG,
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
class PrpaIn201310Uv02MfmiMt700711Uv01Subject1:
    class Meta:
        name = "PRPA_IN201310UV02.MFMI_MT700711UV01.Subject1"

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
    registration_event: Optional[PrpaIn201310Uv02MfmiMt700711Uv01RegistrationEvent] = field(
        default=None,
        metadata={
            "name": "registrationEvent",
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
    type_code: Union[ActRelationshipConditional, ActRelationshipHasComponent, ActRelationshipOutcome, ActRelationshipCostTracking, ActRelationshipPosting, str, ActRelationshipHasSupport, ActRelationshipTemporallyPertains, PrpaIn201310Uv02MfmiMt700711Uv01Subject1Value, ActRelationshipSequel, XActRelationshipDocument, XActRelationshipEntry, XActRelationshipEntryRelationship, XActRelationshipExternalReference, XActRelationshipPatientTransport, XActRelationshipPertinentInfo, XActRelationshipRelatedAuthorizations, XActReplaceOrRevise, XSuccReplPrev] = field(
        init=False,
        default=PrpaIn201310Uv02MfmiMt700711Uv01Subject1Value.SUBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
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
class PrpaIn201310Uv02MfmiMt700711Uv01ControlActProcess:
    class Meta:
        name = "PRPA_IN201310UV02.MFMI_MT700711UV01.ControlActProcess"

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
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
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
    reason_code: List[Ce] = field(
        default_factory=list,
        metadata={
            "name": "reasonCode",
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
    overseer: List[MfmiMt700711Uv01Overseer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author_or_performer: List[MfmiMt700711Uv01AuthorOrPerformer] = field(
        default_factory=list,
        metadata={
            "name": "authorOrPerformer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: List[MfmiMt700711Uv01DataEnterer] = field(
        default_factory=list,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    information_recipient: List[MfmiMt700711Uv01InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    subject: List[PrpaIn201310Uv02MfmiMt700711Uv01Subject1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason_of: List[MfmiMt700711Uv01Reason] = field(
        default_factory=list,
        metadata={
            "name": "reasonOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    query_ack: Optional[MfmiMt700711Uv01QueryAck] = field(
        default=None,
        metadata={
            "name": "queryAck",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    query_by_parameter: Optional[PrpaMt201307Uv02QueryByParameter] = field(
        default=None,
        metadata={
            "name": "queryByParameter",
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
    class_code: Optional[ActClassControlAct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    mood_code: Optional[XActMoodIntentEvent] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PrpaIn201310Uv02McciMt000300Uv01Message:
    class Meta:
        name = "PRPA_IN201310UV02.MCCI_MT000300UV01.Message"

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
    creation_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    security_text: Optional[St] = field(
        default=None,
        metadata={
            "name": "securityText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    version_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "versionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    interaction_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "interactionId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    profile_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "profileId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    processing_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "processingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    processing_mode_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "processingModeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    accept_ack_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "acceptAckCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    attachment_text: List[EdExplicit] = field(
        default_factory=list,
        metadata={
            "name": "attachmentText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    receiver: List[McciMt000300Uv01Receiver] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    respond_to: List[McciMt000300Uv01RespondTo] = field(
        default_factory=list,
        metadata={
            "name": "respondTo",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    sender: Optional[McciMt000300Uv01Sender] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    attention_line: List[McciMt000300Uv01AttentionLine] = field(
        default_factory=list,
        metadata={
            "name": "attentionLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    acknowledgement: List[McciMt000300Uv01Acknowledgement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    control_act_process: Optional[PrpaIn201310Uv02MfmiMt700711Uv01ControlActProcess] = field(
        default=None,
        metadata={
            "name": "controlActProcess",
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


@dataclass
class PrpaIn201310Uv02(PrpaIn201310Uv02McciMt000300Uv01Message):
    class Meta:
        name = "PRPA_IN201310UV02"
        namespace = "urn:hl7-org:v3"

    itsversion: str = field(
        init=False,
        default="XML_1.0",
        metadata={
            "name": "ITSVersion",
            "type": "Attribute",
            "required": True,
        }
    )
