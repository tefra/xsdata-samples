from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .abstract_provided_port_prototype_subtypes_enum import (
    AbstractProvidedPortPrototypeSubtypesEnum,
)
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PModeGroupInAtomicSwcInstanceRef:
    """
    :ivar context_p_port_ref:
    :ivar target_mode_group_ref:
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
        name = "P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF"

    context_p_port_ref: PModeGroupInAtomicSwcInstanceRef.ContextPPortRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-P-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_mode_group_ref: PModeGroupInAtomicSwcInstanceRef.TargetModeGroupRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-MODE-GROUP-REF",
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
    class ContextPPortRef(Ref):
        dest: AbstractProvidedPortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetModeGroupRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
