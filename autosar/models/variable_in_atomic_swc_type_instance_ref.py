from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .application_composite_element_data_prototype_subtypes_enum import (
    ApplicationCompositeElementDataPrototypeSubtypesEnum,
)
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class VariableInAtomicSwcTypeInstanceRef:
    """
    :ivar port_prototype_ref: This is the port providing the paramter or
        the entry point to the parameter structure.
    :ivar root_variable_data_prototype_ref:
    :ivar context_data_prototype_ref: This ist the context in a
        compositeDataType.
    :ivar target_data_prototype_ref: This is the target of the instance
        ref. Note that it shall be one of
        ApplicationCompositeElementDataPrototype of
        VariableDataPrototype.
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
        name = "VARIABLE-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"

    port_prototype_ref: VariableInAtomicSwcTypeInstanceRef.PortPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_variable_data_prototype_ref: VariableInAtomicSwcTypeInstanceRef.RootVariableDataPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "ROOT-VARIABLE-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_data_prototype_ref: list[
        VariableInAtomicSwcTypeInstanceRef.ContextDataPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_ref: VariableInAtomicSwcTypeInstanceRef.TargetDataPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
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
    class PortPrototypeRef(Ref):
        dest: PortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RootVariableDataPrototypeRef(Ref):
        dest: VariableDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextDataPrototypeRef(Ref):
        dest: ApplicationCompositeElementDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetDataPrototypeRef(Ref):
        dest: DataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
