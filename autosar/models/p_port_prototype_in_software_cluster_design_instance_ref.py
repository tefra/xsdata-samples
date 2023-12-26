from dataclasses import dataclass, field
from typing import List, Optional
from .p_port_prototype_subtypes_enum import PPortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_cluster_design_component_prototype_subtypes_enum import (
    RootSwClusterDesignComponentPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PPortPrototypeInSoftwareClusterDesignInstanceRef:
    """
    :ivar context_root_sw_cluster_design_component_prototype_ref:
    :ivar context_sw_component_prototype_ref:
    :ivar target_p_port_prototype_ref:
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
        name = "P-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF"

    context_root_sw_cluster_design_component_prototype_ref: Optional[
        "PPortPrototypeInSoftwareClusterDesignInstanceRef.ContextRootSwClusterDesignComponentPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-CLUSTER-DESIGN-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_sw_component_prototype_ref: List[
        "PPortPrototypeInSoftwareClusterDesignInstanceRef.ContextSwComponentPrototypeRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_p_port_prototype_ref: Optional[
        "PPortPrototypeInSoftwareClusterDesignInstanceRef.TargetPPortPrototypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-P-PORT-PROTOTYPE-REF",
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
    class ContextRootSwClusterDesignComponentPrototypeRef(Ref):
        dest: Optional[
            RootSwClusterDesignComponentPrototypeSubtypesEnum
        ] = field(
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
    class TargetPPortPrototypeRef(Ref):
        dest: Optional[PPortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
