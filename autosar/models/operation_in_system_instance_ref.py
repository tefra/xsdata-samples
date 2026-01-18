from __future__ import annotations

from dataclasses import dataclass, field

from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class OperationInSystemInstanceRef:
    """
    :ivar context_composition_ref:
    :ivar context_component_ref:
    :ivar context_port_ref:
    :ivar target_operation_ref:
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
        name = "OPERATION-IN-SYSTEM-INSTANCE-REF"

    context_composition_ref: (
        None | OperationInSystemInstanceRef.ContextCompositionRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_component_ref: list[
        OperationInSystemInstanceRef.ContextComponentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_port_ref: None | OperationInSystemInstanceRef.ContextPortRef = (
        field(
            default=None,
            metadata={
                "name": "CONTEXT-PORT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    target_operation_ref: (
        None | OperationInSystemInstanceRef.TargetOperationRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-OPERATION-REF",
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
    class ContextCompositionRef(Ref):
        dest: RootSwCompositionPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextPortRef(Ref):
        dest: PortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetOperationRef(Ref):
        dest: ClientServerOperationSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
