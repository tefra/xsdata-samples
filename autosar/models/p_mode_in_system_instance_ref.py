from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_provided_port_prototype_subtypes_enum import (
    AbstractProvidedPortPrototypeSubtypesEnum,
)
from .mode_declaration_group_prototype_subtypes_enum import (
    ModeDeclarationGroupPrototypeSubtypesEnum,
)
from .mode_declaration_subtypes_enum import ModeDeclarationSubtypesEnum
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PModeInSystemInstanceRef:
    """
    :ivar context_composition_ref:
    :ivar context_component_ref:
    :ivar context_p_port_ref:
    :ivar context_mode_declaration_group_ref:
    :ivar target_mode_ref:
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
        name = "P-MODE-IN-SYSTEM-INSTANCE-REF"

    context_composition_ref: (
        None | PModeInSystemInstanceRef.ContextCompositionRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_component_ref: list[
        PModeInSystemInstanceRef.ContextComponentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_p_port_ref: None | PModeInSystemInstanceRef.ContextPPortRef = (
        field(
            default=None,
            metadata={
                "name": "CONTEXT-P-PORT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    context_mode_declaration_group_ref: (
        None | PModeInSystemInstanceRef.ContextModeDeclarationGroupRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-MODE-DECLARATION-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_mode_ref: None | PModeInSystemInstanceRef.TargetModeRef = field(
        default=None,
        metadata={
            "name": "TARGET-MODE-REF",
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

    @dataclass
    class ContextCompositionRef(Ref):
        dest: None | RootSwCompositionPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextComponentRef(Ref):
        dest: None | SwComponentPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextPPortRef(Ref):
        dest: None | AbstractProvidedPortPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextModeDeclarationGroupRef(Ref):
        dest: None | ModeDeclarationGroupPrototypeSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetModeRef(Ref):
        dest: None | ModeDeclarationSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
