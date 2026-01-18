from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .composition_sw_component_type_subtypes_enum import (
    CompositionSwComponentTypeSubtypesEnum,
)
from .ref import Ref
from .root_sw_composition_prototype_subtypes_enum import (
    RootSwCompositionPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)
from .swc_service_dependency_subtypes_enum import (
    SwcServiceDependencySubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcServiceDependencyInCompositionInstanceRef:
    """
    :ivar base_ref:
    :ivar root_context_ref: This identifies the rootSoftwareComposition
        if the instanceRef is modelled in the System context.
    :ivar context_sw_component_prototype_ref:
    :ivar target_swc_service_dependency_ref:
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
        name = "SWC-SERVICE-DEPENDENCY-IN-COMPOSITION-INSTANCE-REF"

    base_ref: SwcServiceDependencyInCompositionInstanceRef.BaseRef | None = field(
        default=None,
        metadata={
            "name": "BASE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    root_context_ref: SwcServiceDependencyInCompositionInstanceRef.RootContextRef | None = field(
        default=None,
        metadata={
            "name": "ROOT-CONTEXT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_sw_component_prototype_ref: list[
        SwcServiceDependencyInCompositionInstanceRef.ContextSwComponentPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_swc_service_dependency_ref: SwcServiceDependencyInCompositionInstanceRef.TargetSwcServiceDependencyRef | None = field(
        default=None,
        metadata={
            "name": "TARGET-SWC-SERVICE-DEPENDENCY-REF",
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
        dest: CompositionSwComponentTypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class RootContextRef(Ref):
        dest: RootSwCompositionPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextSwComponentPrototypeRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetSwcServiceDependencyRef(Ref):
        dest: SwcServiceDependencySubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
