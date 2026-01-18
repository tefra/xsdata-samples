from __future__ import annotations

from dataclasses import dataclass, field

from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)
from .trigger_subtypes_enum import TriggerSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
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

    context_composition_ref: (
        None | TriggerInSystemInstanceRef.ContextCompositionRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_component_ref: list[
        TriggerInSystemInstanceRef.ContextComponentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_port_ref: None | TriggerInSystemInstanceRef.ContextPortRef = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_trigger_ref: None | TriggerInSystemInstanceRef.TargetTriggerRef = (
        field(
            default=None,
            metadata={
                "name": "TARGET-TRIGGER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class ContextCompositionRef(Ref):
        dest: RootSwCompositionPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextPortRef(Ref):
        dest: PortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetTriggerRef(Ref):
        dest: TriggerSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
