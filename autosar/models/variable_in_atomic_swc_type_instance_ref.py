from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
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

    port_prototype_ref: (
        None | VariableInAtomicSwcTypeInstanceRef.PortPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_variable_data_prototype_ref: (
        None | VariableInAtomicSwcTypeInstanceRef.RootVariableDataPrototypeRef
    ) = field(
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
    target_data_prototype_ref: (
        None | VariableInAtomicSwcTypeInstanceRef.TargetDataPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-DATA-PROTOTYPE-REF",
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
    class PortPrototypeRef(Ref):
        dest: PortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class RootVariableDataPrototypeRef(Ref):
        dest: VariableDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextDataPrototypeRef(Ref):
        dest: ApplicationCompositeElementDataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetDataPrototypeRef(Ref):
        dest: DataPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
