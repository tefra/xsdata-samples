from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .abstract_provided_port_prototype_subtypes_enum import (
    AbstractProvidedPortPrototypeSubtypesEnum,
)
from .ref import Ref
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PPortInCompositionInstanceRef:
    """
    :ivar context_component_ref:
    :ivar target_p_port_ref:
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
        name = "P-PORT-IN-COMPOSITION-INSTANCE-REF"

    context_component_ref: PPortInCompositionInstanceRef.ContextComponentRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_p_port_ref: PPortInCompositionInstanceRef.TargetPPortRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-P-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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
    class ContextComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetPPortRef(Ref):
        dest: AbstractProvidedPortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
