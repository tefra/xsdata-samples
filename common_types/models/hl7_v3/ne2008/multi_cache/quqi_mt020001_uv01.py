from dataclasses import dataclass, field
from typing import List, Optional
from common_types.models.hl7_v3.ne2008.core.datatypes_base import (
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTs,
    IvlTsExplicit,
    Sc,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActRelationshipReason,
    ContextControl,
    NullFlavor,
    ParticipationInformationRecipient,
    ParticipationType,
    XParticipationAuthorPerformer,
    XParticipationVrfRespSprfWit,
)
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090100_uv01 import CoctMt090100Uv01AssignedPerson
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090300_uv01 import CoctMt090300Uv01AssignedDevice
from common_types.models.hl7_v3.ne2008.multi_cache.mcai_mt900001_uv01 import McaiMt900001Uv01DetectedIssueEvent

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class QuqiMt020001Uv01AuthorOrPerformer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_device:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "QUQI_MT020001UV01.AuthorOrPerformer"

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
    assigned_device: Optional[CoctMt090300Uv01AssignedDevice] = field(
        default=None,
        metadata={
            "name": "assignedDevice",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
        default=None,
        metadata={
            "name": "assignedPerson",
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
    type_code: Optional[XParticipationAuthorPerformer] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class QuqiMt020001Uv01DataEnterer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "QUQI_MT020001UV01.DataEnterer"

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
    time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
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
        default=ParticipationType.ENT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class QuqiMt020001Uv01InformationRecipient:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar time:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "QUQI_MT020001UV01.InformationRecipient"

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
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
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
    type_code: Optional[ParticipationInformationRecipient] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class QuqiMt020001Uv01Overseer:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar note_text:
    :ivar time:
    :ivar mode_code:
    :ivar signature_code:
    :ivar signature_text:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "QUQI_MT020001UV01.Overseer"

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
    assigned_person: Optional[CoctMt090100Uv01AssignedPerson] = field(
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
    type_code: Optional[XParticipationVrfRespSprfWit] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_control_code: ContextControl = field(
        default=ContextControl.AP,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class QuqiMt020001Uv01Reason:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar detected_issue_event:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "QUQI_MT020001UV01.Reason"

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
    detected_issue_event: Optional[McaiMt900001Uv01DetectedIssueEvent] = field(
        default=None,
        metadata={
            "name": "detectedIssueEvent",
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
    type_code: Optional[ActRelationshipReason] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
        }
    )
    context_conduction_ind: Optional[str] = field(
        default=None,
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class QuqiMt020001Uv01SortControl:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar element_name:
    :ivar direction_code:
    :ivar null_flavor:
    """
    class Meta:
        name = "QUQI_MT020001UV01.SortControl"

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
    element_name: Optional[Sc] = field(
        default=None,
        metadata={
            "name": "elementName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    direction_code: Optional[Cs] = field(
        default=None,
        metadata={
            "name": "directionCode",
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
