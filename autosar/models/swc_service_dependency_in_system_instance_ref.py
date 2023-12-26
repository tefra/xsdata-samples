from dataclasses import dataclass, field
from typing import List, Optional
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
from .system_subtypes_enum import SystemSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcServiceDependencyInSystemInstanceRef:
    """
    :ivar base_ref:
    :ivar context_root_sw_composition_ref:
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
        name = "SWC-SERVICE-DEPENDENCY-IN-SYSTEM-INSTANCE-REF"

    base_ref: Optional[
        "SwcServiceDependencyInSystemInstanceRef.BaseRef"
    ] = field(
        default=None,
        metadata={
            "name": "BASE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_root_sw_composition_ref: Optional[
        "SwcServiceDependencyInSystemInstanceRef.ContextRootSwCompositionRef"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-COMPOSITION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_sw_component_prototype_ref: List[
        "SwcServiceDependencyInSystemInstanceRef.ContextSwComponentPrototypeRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_swc_service_dependency_ref: Optional[
        "SwcServiceDependencyInSystemInstanceRef.TargetSwcServiceDependencyRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-SWC-SERVICE-DEPENDENCY-REF",
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
    class BaseRef(Ref):
        dest: Optional[SystemSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextRootSwCompositionRef(Ref):
        dest: Optional[RootSwCompositionPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ContextSwComponentPrototypeRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TargetSwcServiceDependencyRef(Ref):
        dest: Optional[SwcServiceDependencySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
