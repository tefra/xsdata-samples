from dataclasses import dataclass, field
from typing import List, Optional
from ..core.datatypes_base import (
    Cd,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    St,
    TsExplicit,
)
from ..core.voc import (
    ActClassControlAct,
    NullFlavor,
    XActMoodIntentEvent,
)
from .mcci_mt000100_uv01 import (
    McciMt000100Uv01AttentionLine,
    McciMt000100Uv01Receiver,
    McciMt000100Uv01RespondTo,
    McciMt000100Uv01Sender,
)
from .qupc_mt040300_uv01 import QupcMt040300Uv01ParameterList
from .quqi_mt020001_uv01 import (
    QuqiMt020001Uv01AuthorOrPerformer,
    QuqiMt020001Uv01DataEnterer,
    QuqiMt020001Uv01InformationRecipient,
    QuqiMt020001Uv01Overseer,
    QuqiMt020001Uv01Reason,
    QuqiMt020001Uv01SortControl,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class QupcIn043100Uv01QuqiMt020001Uv01QueryByParameter:
    class Meta:
        name = "QUPC_IN043100UV01.QUQI_MT020001UV01.QueryByParameter"

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
    query_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "queryId",
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
    modify_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "modifyCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    response_element_group_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "responseElementGroupId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    response_modality_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "responseModalityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    response_priority_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "responsePriorityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    initial_quantity: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "initialQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    initial_quantity_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "initialQuantityCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    execution_and_delivery_time: Optional[TsExplicit] = field(
        default=None,
        metadata={
            "name": "executionAndDeliveryTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    parameter_list: List[QupcMt040300Uv01ParameterList] = field(
        default_factory=list,
        metadata={
            "name": "parameterList",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    sort_control: List[QuqiMt020001Uv01SortControl] = field(
        default_factory=list,
        metadata={
            "name": "sortControl",
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


@dataclass
class QupcIn043100Uv01QuqiMt020001Uv01ControlActProcess:
    class Meta:
        name = "QUPC_IN043100UV01.QUQI_MT020001UV01.ControlActProcess"

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
    overseer: List[QuqiMt020001Uv01Overseer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author_or_performer: List[QuqiMt020001Uv01AuthorOrPerformer] = field(
        default_factory=list,
        metadata={
            "name": "authorOrPerformer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    data_enterer: List[QuqiMt020001Uv01DataEnterer] = field(
        default_factory=list,
        metadata={
            "name": "dataEnterer",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    information_recipient: List[QuqiMt020001Uv01InformationRecipient] = field(
        default_factory=list,
        metadata={
            "name": "informationRecipient",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    reason_of: List[QuqiMt020001Uv01Reason] = field(
        default_factory=list,
        metadata={
            "name": "reasonOf",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    query_by_parameter: Optional[QupcIn043100Uv01QuqiMt020001Uv01QueryByParameter] = field(
        default=None,
        metadata={
            "name": "queryByParameter",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
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
class QupcIn043100Uv01McciMt000100Uv01Message:
    class Meta:
        name = "QUPC_IN043100UV01.MCCI_MT000100UV01.Message"

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
    sequence_number: Optional[IntType] = field(
        default=None,
        metadata={
            "name": "sequenceNumber",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
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
    receiver: List[McciMt000100Uv01Receiver] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 1,
        }
    )
    respond_to: List[McciMt000100Uv01RespondTo] = field(
        default_factory=list,
        metadata={
            "name": "respondTo",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    sender: Optional[McciMt000100Uv01Sender] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    attention_line: List[McciMt000100Uv01AttentionLine] = field(
        default_factory=list,
        metadata={
            "name": "attentionLine",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    control_act_process: Optional[QupcIn043100Uv01QuqiMt020001Uv01ControlActProcess] = field(
        default=None,
        metadata={
            "name": "controlActProcess",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )


@dataclass
class QupcIn043100Uv01(QupcIn043100Uv01McciMt000100Uv01Message):
    class Meta:
        name = "QUPC_IN043100UV01"
        namespace = "urn:hl7-org:v3"

    itsversion: str = field(
        init=False,
        default="XML_1.0",
        metadata={
            "name": "ITSVersion",
            "type": "Attribute",
        }
    )
