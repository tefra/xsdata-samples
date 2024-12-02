from dataclasses import dataclass, field
from typing import Optional

from .port_group_subtypes_enum import PortGroupSubtypesEnum
from .ref import Ref
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InnerPortGroupInCompositionInstanceRef:
    """
    :ivar context_ref:
    :ivar target_ref: Links a PortGroup in a composition to another
        PortGroup, that is defined in a component which is part of this
        CompositionSwComponentType. There shall be at most one
        innerGroup per contained SwComponentPrototype.
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
        name = "INNER-PORT-GROUP-IN-COMPOSITION-INSTANCE-REF"

    context_ref: list["InnerPortGroupInCompositionInstanceRef.ContextRef"] = (
        field(
            default_factory=list,
            metadata={
                "name": "CONTEXT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    target_ref: Optional[
        "InnerPortGroupInCompositionInstanceRef.TargetRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class ContextRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetRef(Ref):
        dest: Optional[PortGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
