from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_required_port_prototype_subtypes_enum import (
    AbstractRequiredPortPrototypeSubtypesEnum,
)
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class RVariableInAtomicSwcInstanceRef:
    """
    :ivar context_r_port_ref:
    :ivar target_data_element_ref:
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
        name = "R-VARIABLE-IN-ATOMIC-SWC-INSTANCE-REF"

    context_r_port_ref: (
        None | RVariableInAtomicSwcInstanceRef.ContextRPortRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-R-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_element_ref: (
        None | RVariableInAtomicSwcInstanceRef.TargetDataElementRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-ELEMENT-REF",
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
    class ContextRPortRef(Ref):
        dest: AbstractRequiredPortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetDataElementRef(Ref):
        dest: VariableDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
