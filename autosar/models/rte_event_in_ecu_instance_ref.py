from __future__ import annotations

from dataclasses import dataclass, field

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

    context_root_composition_ref: (
        RteEventInEcuInstanceRef.ContextRootCompositionRef | None
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_atomic_component_ref: (
        RteEventInEcuInstanceRef.ContextAtomicComponentRef | None
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ATOMIC-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_rte_event_ref: RteEventInEcuInstanceRef.TargetRteEventRef | None = (
        field(
            default=None,
            metadata={
                "name": "TARGET-RTE-EVENT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ContextRootCompositionRef(Ref):
        dest: RootSwCompositionPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextAtomicComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetRteEventRef(Ref):
        dest: RteEventSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
