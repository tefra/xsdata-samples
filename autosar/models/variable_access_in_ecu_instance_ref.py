from dataclasses import dataclass, field
from typing import Optional
from autosar.models.ref import Ref
from autosar.models.root_sw_composition_prototype_subtypes_enum import RootSwCompositionPrototypeSubtypesEnum
from autosar.models.sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum
from autosar.models.variable_access_subtypes_enum import VariableAccessSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
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

    context_root_composition_ref: Optional["VariableAccessInEcuInstanceRef.ContextRootCompositionRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_atomic_component_ref: Optional["VariableAccessInEcuInstanceRef.ContextAtomicComponentRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ATOMIC-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_variable_access_ref: Optional["VariableAccessInEcuInstanceRef.TargetVariableAccessRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-VARIABLE-ACCESS-REF",
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
    class ContextRootCompositionRef(Ref):
        dest: Optional[RootSwCompositionPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextAtomicComponentRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetVariableAccessRef(Ref):
        dest: Optional[VariableAccessSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )