from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.ref import Ref
from autosar.models.root_sw_component_prototype_subtypes_enum import RootSwComponentPrototypeSubtypesEnum
from autosar.models.sw_component_prototype_subtypes_enum import SwComponentPrototypeSubtypesEnum
from autosar.models.swc_service_dependency_subtypes_enum import SwcServiceDependencySubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcServiceDependencyInExecutableInstanceRef:
    """
    :ivar context_root_component_ref:
    :ivar context_component_ref:
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
        name = "SWC-SERVICE-DEPENDENCY-IN-EXECUTABLE-INSTANCE-REF"

    context_root_component_ref: Optional["SwcServiceDependencyInExecutableInstanceRef.ContextRootComponentRef"] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    context_component_ref: List["SwcServiceDependencyInExecutableInstanceRef.ContextComponentRef"] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    target_swc_service_dependency_ref: Optional["SwcServiceDependencyInExecutableInstanceRef.TargetSwcServiceDependencyRef"] = field(
        default=None,
        metadata={
            "name": "TARGET-SWC-SERVICE-DEPENDENCY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class ContextRootComponentRef(Ref):
        dest: Optional[RootSwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ContextComponentRef(Ref):
        dest: Optional[SwComponentPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class TargetSwcServiceDependencyRef(Ref):
        dest: Optional[SwcServiceDependencySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
