from __future__ import annotations

from dataclasses import dataclass, field

from .bsw_implementation_subtypes_enum import BswImplementationSubtypesEnum
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ModeInBswInstanceRef:
    """
    Instance reference to be capable of referencing a specific
    ModeDeclaration of a ModeDeclarationGroupPrototype utilized in a BSW
    module.

    :ivar context_bsw_implementation_ref: Specifies the BSW
        implementation that manifests the context.
    :ivar context_mode_declaration_group_prototype_ref: Specifies the
        mode declaration group prototype that manifests the context.
    :ivar target_mode_declaration_ref: Specifies the specific mode
        declaration in the given context.
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
        name = "MODE-IN-BSW-INSTANCE-REF"

    context_bsw_implementation_ref: (
        None | ModeInBswInstanceRef.ContextBswImplementationRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-BSW-IMPLEMENTATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_mode_declaration_group_prototype_ref: (
        None | ModeInBswInstanceRef.ContextModeDeclarationGroupPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_mode_declaration_ref: (
        None | ModeInBswInstanceRef.TargetModeDeclarationRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-MODE-DECLARATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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
    class ContextBswImplementationRef(Ref):
        dest: BswImplementationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextModeDeclarationGroupPrototypeRef(Ref):
        dest: ModeDeclarationGroupPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetModeDeclarationRef(Ref):
        dest: ModeDeclarationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
