from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.r_port_prototype_subtypes_enum import RPortPrototypeSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.root_sw_component_prototype_subtypes_enum import RootSwComponentPrototypeSubtypesEnum
from autosar.models.sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum
from autosar.models.variable_data_prototype_subtypes_enum import VariableDataPrototypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EventInExecutableInstanceRef:
    """
    :ivar context_root_sw_component_prototype_ref:
    :ivar context_sw_component_prototype_ref:
    :ivar context_r_port_prototype_ref:
    :ivar target_event_ref:
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "EVENT-IN-EXECUTABLE-INSTANCE-REF"

    context_root_sw_component_prototype_ref: Optional["EventInExecutableInstanceRef.ContextRootSwComponentPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_sw_component_prototype_ref: List["EventInExecutableInstanceRef.ContextSwComponentPrototypeRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_r_port_prototype_ref: Optional["EventInExecutableInstanceRef.ContextRPortPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-R-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_event_ref: Optional["EventInExecutableInstanceRef.TargetEventRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class ContextRootSwComponentPrototypeRef(Ref):
        dest: Optional[RootSwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextSwComponentPrototypeRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextRPortPrototypeRef(Ref):
        dest: Optional[RPortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetEventRef(Ref):
        dest: Optional[VariableDataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )