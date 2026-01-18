from __future__ import annotations

from dataclasses import dataclass, field

from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)
from .variable_access_subtypes_enum import VariableAccessSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class VariableAccessInEcuInstanceRef:
    """
    :ivar context_root_composition_ref:
    :ivar context_atomic_component_ref:
    :ivar target_variable_access_ref:
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
        name = "VARIABLE-ACCESS-IN-ECU-INSTANCE-REF"

    context_root_composition_ref: (
        None | VariableAccessInEcuInstanceRef.ContextRootCompositionRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_atomic_component_ref: (
        None | VariableAccessInEcuInstanceRef.ContextAtomicComponentRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ATOMIC-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_variable_access_ref: (
        None | VariableAccessInEcuInstanceRef.TargetVariableAccessRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-VARIABLE-ACCESS-REF",
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
    class ContextRootCompositionRef(Ref):
        dest: RootSwCompositionPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextAtomicComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetVariableAccessRef(Ref):
        dest: VariableAccessSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
