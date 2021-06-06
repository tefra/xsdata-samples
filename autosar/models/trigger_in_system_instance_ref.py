from dataclasses import dataclass, field
from typing import List, Optional
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import RootSwCompositionPrototypeSubtypesEnum
from .sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TriggerInSystemInstanceRef:
    """
    :ivar context_composition_ref: This represents tha reference to the
        RootSwCompositiontype representing a context of the InstanceRef.
    :ivar context_component_ref: This represents the set of context
        components. The association is ordered because it needs to
        respect the nesting order.
    :ivar context_port_ref: This represents the PortPrototype in which
        the target Trigger is located.
    :ivar target_trigger_ref: This represents the target Trigger.
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
        name = "TRIGGER-IN-SYSTEM-INSTANCE-REF"

    context_composition_ref: Optional["TriggerInSystemInstanceRef.ContextCompositionRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_component_ref: List["TriggerInSystemInstanceRef.ContextComponentRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_port_ref: Optional["TriggerInSystemInstanceRef.ContextPortRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_trigger_ref: Optional["TriggerInSystemInstanceRef.TargetTriggerRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-TRIGGER-REF",
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
    class ContextCompositionRef(Ref):
        dest: Optional[RootSwCompositionPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextComponentRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextPortRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetTriggerRef(Ref):
        dest: Optional[TriggerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
