from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .ar_variable_in_implementation_data_instance_ref import (
    ArVariableInImplementationDataInstanceRef,
)
from .ref import Ref
from .variable_data_prototype_subtypes_enum import (
    VariableDataPrototypeSubtypesEnum,
)
from .variable_in_atomic_swc_type_instance_ref import (
    VariableInAtomicSwcTypeInstanceRef,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AutosarVariableRef:
    """
    This class represents a reference to a variable within AUTOSAR which
    can be one of the following use cases: localVariable: * localVariable
    which is used as whole (e.g.

    InterRunnableVariable, inputValue for curve) autosarVariable: * a
    variable provided via Port which is used as whole (e.g.
    dataAccesspoints) * an element inside of a composite local variable
    typed by ApplicationDatatype (e.g. inputValue for a curve) * an element
    inside of a composite variable provided via Port and typed by
    ApplicationDatatype (e.g. inputValue for a curve)
    autosarVariableInImplDatatype: * an element inside of a composite local
    variable typed by ImplementationDatatype (e.g. nvramData mapping) * an
    element inside of a composite variable provided via Port and typed by
    ImplementationDatatype (e.g. inputValue for a curve).

    :ivar autosar_variable_in_impl_datatype: This is used if the target
        variable is inside of variableDataPrototype typed by an
        ImplementationDataType.
    :ivar autosar_variable_iref: This references a variable which is
        provided by a port and/or which is part of a CompositeDataType.
    :ivar local_variable_ref: This reference is used if the variable is
        local to the current component. It would also be possible to use
        the instance refence here. Such an instance ref would not have a
        contextElement, since the current instance is the context. But
        the local instance is a special case which may provide further
        optimization. Therefore an expclicit reference is provided for
        this case.
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
        name = "AUTOSAR-VARIABLE-REF"

    autosar_variable_in_impl_datatype: ArVariableInImplementationDataInstanceRef | None = field(
        default=None,
        metadata={
            "name": "AUTOSAR-VARIABLE-IN-IMPL-DATATYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    autosar_variable_iref: VariableInAtomicSwcTypeInstanceRef | None = (
        field(
            default=None,
            metadata={
                "name": "AUTOSAR-VARIABLE-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    local_variable_ref: AutosarVariableRef.LocalVariableRef | None = (
        field(
            default=None,
            metadata={
                "name": "LOCAL-VARIABLE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class LocalVariableRef(Ref):
        dest: VariableDataPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
