from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .p_port_prototype_subtypes_enum import PPortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_component_prototype_subtypes_enum import (
    RootSwComponentPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ProvidedMethodInExecutableInstanceRef:
    """
    :ivar context_root_sw_component_prototype_ref:
    :ivar context_component_prototype_ref:
    :ivar context_p_port_prototype_ref:
    :ivar target_method_ref:
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
        name = "PROVIDED-METHOD-IN-EXECUTABLE-INSTANCE-REF"

    context_root_sw_component_prototype_ref: ProvidedMethodInExecutableInstanceRef.ContextRootSwComponentPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_component_prototype_ref: list[
        ProvidedMethodInExecutableInstanceRef.ContextComponentPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_p_port_prototype_ref: ProvidedMethodInExecutableInstanceRef.ContextPPortPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-P-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_method_ref: ProvidedMethodInExecutableInstanceRef.TargetMethodRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-METHOD-REF",
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
    class ContextRootSwComponentPrototypeRef(Ref):
        dest: RootSwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextComponentPrototypeRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextPPortPrototypeRef(Ref):
        dest: PPortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetMethodRef(Ref):
        dest: ClientServerOperationSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
