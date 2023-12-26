from dataclasses import dataclass, field
from typing import Optional
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .rte_event_subtypes_enum import RteEventSubtypesEnum
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RteEventInEcuInstanceRef:
    """
    :ivar context_root_composition_ref:
    :ivar context_atomic_component_ref:
    :ivar target_rte_event_ref:
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
        name = "RTE-EVENT-IN-ECU-INSTANCE-REF"

    context_root_composition_ref: Optional[
        "RteEventInEcuInstanceRef.ContextRootCompositionRef"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_atomic_component_ref: Optional[
        "RteEventInEcuInstanceRef.ContextAtomicComponentRef"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ATOMIC-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_rte_event_ref: Optional[
        "RteEventInEcuInstanceRef.TargetRteEventRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-RTE-EVENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ContextRootCompositionRef(Ref):
        dest: Optional[RootSwCompositionPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextAtomicComponentRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetRteEventRef(Ref):
        dest: Optional[RteEventSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
