from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ModeInProcessInstanceRef:
    """
    :ivar context_mode_declaration_group_prototype_ref:
    :ivar target_mode_declaration_ref:
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
        name = "MODE-IN-PROCESS-INSTANCE-REF"

    context_mode_declaration_group_prototype_ref: ModeInProcessInstanceRef.ContextModeDeclarationGroupPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_mode_declaration_ref: ModeInProcessInstanceRef.TargetModeDeclarationRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-MODE-DECLARATION-REF",
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
    class ContextModeDeclarationGroupPrototypeRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetModeDeclarationRef(Ref):
        dest: ModeDeclarationSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
