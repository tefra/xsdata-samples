from dataclasses import dataclass, field
from typing import List, Optional
from common_types.models.hl7_v3.ne2008.core.datatypes_base import (
    Any,
    Ce,
    Cs,
    EdExplicit,
    Ii,
    IntType,
    IvlTsExplicit,
    St,
)
from common_types.models.hl7_v3.ne2008.core.voc import (
    ActClass,
    ActClassPosition,
    ActMood,
    ActRelationshipHasComponent,
    ContextControl,
    NullFlavor,
    ParticipationTargetDevice,
    ParticipationType,
)
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090108_uv import CoctMt090108UvAssignedPerson
from common_types.models.hl7_v3.ne2008.multi_cache.coct_mt090303_uv01 import CoctMt090303Uv01AssignedDevice

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt960000Uv05Author:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_person:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Author"

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
    assigned_person: Optional[CoctMt090108UvAssignedPerson] = field(
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
        default=ParticipationType.AUT,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
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
class CoctMt960000Uv05Device1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_device:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Device1"

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
    assigned_device: Optional[CoctMt090303Uv01AssignedDevice] = field(
        default=None,
        metadata={
            "name": "assignedDevice",
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
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt960000Uv05Device2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar assigned_device:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Device2"

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
    assigned_device: Optional[CoctMt090303Uv01AssignedDevice] = field(
        default=None,
        metadata={
            "name": "assignedDevice",
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
    context_control_code: ContextControl = field(
        default=ContextControl.ON,
        metadata={
            "name": "contextControlCode",
            "type": "Attribute",
        }
    )


@dataclass
class CoctMt960000Uv05PositionAccuracy:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar value:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.PositionAccuracy"

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
    value: Optional[Ce] = field(
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
        default=ActClass.POSACC,
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
class CoctMt960000Uv05Component2:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar position_accuracy:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "COCT_MT960000UV05.Component2"

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
    position_accuracy: Optional[CoctMt960000Uv05PositionAccuracy] = field(
        default=None,
        metadata={
            "name": "positionAccuracy",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
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
    context_conduction_ind: str = field(
        default="true",
        metadata={
            "name": "contextConductionInd",
            "type": "Attribute",
            "pattern": r"true|false",
        }
    )


@dataclass
class CoctMt960000Uv05PositionCoordinate:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar code:
    :ivar text:
    :ivar value:
    :ivar method_code:
    :ivar device:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.PositionCoordinate"

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
    value: Optional[Any] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    method_code: Optional[Ce] = field(
        default=None,
        metadata={
            "name": "methodCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    device: List[CoctMt960000Uv05Device1] = field(
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
        default=ActClass.POSCOORD,
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
class CoctMt960000Uv05Component1:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar sequence_number:
    :ivar position_coordinate:
    :ivar null_flavor:
    :ivar type_code:
    :ivar context_control_code:
    :ivar context_conduction_ind:
    """
    class Meta:
        name = "COCT_MT960000UV05.Component1"

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
    position_coordinate: Optional[CoctMt960000Uv05PositionCoordinate] = field(
        default=None,
        metadata={
            "name": "positionCoordinate",
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
    type_code: Optional[ActRelationshipHasComponent] = field(
        default=None,
        metadata={
            "name": "typeCode",
            "type": "Attribute",
            "required": True,
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


@dataclass
class CoctMt960000Uv05Position:
    """
    :ivar realm_code:
    :ivar type_id:
    :ivar template_id:
    :ivar id:
    :ivar code:
    :ivar text:
    :ivar effective_time:
    :ivar activity_time:
    :ivar value:
    :ivar device:
    :ivar author:
    :ivar component1:
    :ivar component2:
    :ivar null_flavor:
    :ivar class_code:
    :ivar mood_code:
    """
    class Meta:
        name = "COCT_MT960000UV05.Position"

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
    activity_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "activityTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    value: Optional[St] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        }
    )
    device: List[CoctMt960000Uv05Device2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    author: Optional[CoctMt960000Uv05Author] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    component1: List[CoctMt960000Uv05Component1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "nillable": True,
        }
    )
    component2: Optional[CoctMt960000Uv05Component2] = field(
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
    class_code: Optional[ActClassPosition] = field(
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