from dataclasses import dataclass, field
from typing import Optional, Union

from ..core.datatypes_base import (
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IvlTsExplicit,
    St,
    TsExplicit,
)
from ..core.voc import (
    ActClass,
    ActClassControlAct,
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
from .mcci_mt000300_uv01 import (
    McciMt000300Uv01Acknowledgement,
    McciMt000300Uv01AttentionLine,
    McciMt000300Uv01Receiver,
    McciMt000300Uv01RespondTo,
    McciMt000300Uv01Sender,
)
from .mfmi_mt700711_uv01 import (
    MfmiMt700711Uv01Author2,
    MfmiMt700711Uv01AuthorOrPerformer,
    MfmiMt700711Uv01Custodian,
    MfmiMt700711Uv01DataEnterer,
    MfmiMt700711Uv01Definition,
    MfmiMt700711Uv01InformationRecipient,
    MfmiMt700711Uv01InFulfillmentOf,
    MfmiMt700711Uv01Overseer,
    MfmiMt700711Uv01QueryAck,
    MfmiMt700711Uv01Reason,
    MfmiMt700711Uv01ReplacementOf,
)
from .prpa_mt201306_uv02 import PrpaMt201306Uv02QueryByParameter
from .prpa_mt201310_uv02 import PrpaMt201310Uv02Patient

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class PrpaIn201306Uv02MfmiMt700711Uv01Subject2:
    class Meta:
        name = "PRPA_IN201306UV02.MFMI_MT700711UV01.Subject2"

    realm_code: list[Cs] = field(
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
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    patient: Optional[PrpaMt201310Uv02Patient] = field(
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
    type_code: Optional[ParticipationTargetSubject] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaIn201306Uv02MfmiMt700711Uv01RegistrationEvent:
    class Meta:
        name = "PRPA_IN201306UV02.MFMI_MT700711UV01.RegistrationEvent"

    realm_code: list[Cs] = field(
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
    subject1: Optional[PrpaIn201306Uv02MfmiMt700711Uv01Subject2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    author: Optional[MfmiMt700711Uv01Author2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    custodian: Optional[MfmiMt700711Uv01Custodian] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    in_fulfillment_of: list[MfmiMt700711Uv01InFulfillmentOf] = field(
        default_factory=list,
        metadata={
            "name": "inFulfillmentOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    definition: list[MfmiMt700711Uv01Definition] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    replacement_of: list[MfmiMt700711Uv01ReplacementOf] = field(
        default_factory=list,
        metadata={
            "name": "replacementOf",
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
    class_code: ActClass = field(
        init=False,
        default=ActClass.REG,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
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


@dataclass
class PrpaIn201306Uv02MfmiMt700711Uv01Subject1:
    class Meta:
        name = "PRPA_IN201306UV02.MFMI_MT700711UV01.Subject1"

    realm_code: list[Cs] = field(
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
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    registration_event: Optional[
        PrpaIn201306Uv02MfmiMt700711Uv01RegistrationEvent
    ] = field(
        default=None,
        metadata={
            "name": "registrationEvent",
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
    type_code: Union[
        ActRelationshipConditional,
        ActRelationshipHasComponent,
        ActRelationshipOutcome,
        ActRelationshipCostTracking,
        ActRelationshipPosting,
        str,
        ActRelationshipHasSupport,
        ActRelationshipTemporallyPertains,
        ActRelationshipPertainsValue,
        ActRelationshipSequel,
        XActRelationshipDocument,
        XActRelationshipEntry,
        XActRelationshipEntryRelationship,
        XActRelationshipExternalReference,
        XActRelationshipPatientTransport,
        XActRelationshipPertinentInfo,
        XActRelationshipRelatedAuthorizations,
        XActReplaceOrRevise,
        XSuccReplPrev,
    ] = field(
        init=False,
        default=ActRelationshipPertainsValue.SUBJ,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
            "pattern": r"[^\s]+",
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


@dataclass
class PrpaIn201306Uv02MfmiMt700711Uv01ControlActProcess:
    class Meta:
        name = "PRPA_IN201306UV02.MFMI_MT700711UV01.ControlActProcess"

    realm_code: list[Cs] = field(
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
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    text: Optional[EdExplicit] = field(
        default=None,
        metadata={
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
    priority_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "priorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    reason_code: list[Ce] = field(
        default_factory=list,
        metadata={
            "name": "reasonCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    language_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    overseer: list[MfmiMt700711Uv01Overseer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    author_or_performer: list[MfmiMt700711Uv01AuthorOrPerformer] = field(
        default_factory=list,
        metadata={
            "name": "authorOrPerformer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    data_enterer: list[MfmiMt700711Uv01DataEnterer] = field(
        default_factory=list,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    information_recipient: list[MfmiMt700711Uv01InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    subject: list[PrpaIn201306Uv02MfmiMt700711Uv01Subject1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    reason_of: list[MfmiMt700711Uv01Reason] = field(
        default_factory=list,
        metadata={
            "name": "reasonOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    query_ack: Optional[MfmiMt700711Uv01QueryAck] = field(
        default=None,
        metadata={
            "name": "queryAck",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    query_by_parameter: Optional[PrpaMt201306Uv02QueryByParameter] = field(
        default=None,
        metadata={
            "name": "queryByParameter",
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
    class_code: Optional[ActClassControlAct] = field(
        default=None,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: Optional[XActMoodIntentEvent] = field(
        default=None,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class PrpaIn201306Uv02McciMt000300Uv01Message:
    class Meta:
        name = "PRPA_IN201306UV02.MCCI_MT000300UV01.Message"

    realm_code: list[Cs] = field(
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
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: Optional[Ii] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    creation_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "creationTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    security_text: Optional[St] = field(
        default=None,
        metadata={
            "name": "securityText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    version_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "versionCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    interaction_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "interactionId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    profile_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "profileId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    processing_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "processingCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    processing_mode_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "processingModeCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    accept_ack_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "acceptAckCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    attachment_text: list[EdExplicit] = field(
        default_factory=list,
        metadata={
            "name": "attachmentText",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    receiver: list[McciMt000300Uv01Receiver] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        },
    )
    respond_to: list[McciMt000300Uv01RespondTo] = field(
        default_factory=list,
        metadata={
            "name": "respondTo",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    sender: Optional[McciMt000300Uv01Sender] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    attention_line: list[McciMt000300Uv01AttentionLine] = field(
        default_factory=list,
        metadata={
            "name": "attentionLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    acknowledgement: list[McciMt000300Uv01Acknowledgement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        },
    )
    control_act_process: Optional[
        PrpaIn201306Uv02MfmiMt700711Uv01ControlActProcess
    ] = field(
        default=None,
        metadata={
            "name": "controlActProcess",
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


@dataclass
class PrpaIn201306Uv02(PrpaIn201306Uv02McciMt000300Uv01Message):
    class Meta:
        name = "PRPA_IN201306UV02"
        namespace = "urn:hl7-org:v3"

    itsversion: str = field(
        init=False,
        default="XML_1.0",
        metadata={
            "name": "ITSVersion",
            "type": "Attribute",
            "required": True,
        },
    )
