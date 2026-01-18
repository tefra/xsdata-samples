from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .application_composite_element_data_prototype_subtypes_enum import (
    ApplicationCompositeElementDataPrototypeSubtypesEnum,
)
from .argument_data_prototype_subtypes_enum import (
    ArgumentDataPrototypeSubtypesEnum,
)
from .client_server_operation_subtypes_enum import (
    ClientServerOperationSubtypesEnum,
)
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)
from .sw_component_type_subtypes_enum import SwComponentTypeSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class OperationArgumentInComponentInstanceRef:
    """
    :ivar base_ref:
    :ivar context_component_ref:
    :ivar context_port_prototype_ref:
    :ivar context_operation_ref:
    :ivar root_argument_data_prototype_ref:
    :ivar context_data_prototype_ref:
    :ivar target_data_prototype_ref:
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
        name = "OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF"

    base_ref: OperationArgumentInComponentInstanceRef.BaseRef | None = (
        field(
            default=None,
            metadata={
                "name": "BASE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    context_component_ref: list[
        OperationArgumentInComponentInstanceRef.ContextComponentRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_port_prototype_ref: OperationArgumentInComponentInstanceRef.ContextPortPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_operation_ref: OperationArgumentInComponentInstanceRef.ContextOperationRef | None = field(
        default=None,
        metadata={
            "name": "CONTEXT-OPERATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_argument_data_prototype_ref: OperationArgumentInComponentInstanceRef.RootArgumentDataPrototypeRef | None = field(
        default=None,
        metadata={
            "name": "ROOT-ARGUMENT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_data_prototype_ref: list[
        OperationArgumentInComponentInstanceRef.ContextDataPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-DATA-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_data_prototype_ref: OperationArgumentInComponentInstanceRef.TargetDataPrototypeRef | None = field(
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
    class BaseRef(Ref):
        dest: SwComponentTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextComponentRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextPortPrototypeRef(Ref):
        dest: PortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextOperationRef(Ref):
        dest: ClientServerOperationSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RootArgumentDataPrototypeRef(Ref):
        dest: ArgumentDataPrototypeSubtypesEnum | None = field(
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
