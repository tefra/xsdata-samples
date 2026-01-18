from __future__ import annotations

from dataclasses import dataclass, field

from .r_port_prototype_subtypes_enum import RPortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_cluster_design_component_prototype_subtypes_enum import (
    RootSwClusterDesignComponentPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RPortPrototypeInSoftwareClusterDesignInstanceRef:
    """
    :ivar context_root_sw_cluster_design_component_prototype_ref:
    :ivar context_sw_component_prototype_ref:
    :ivar target_r_port_prototype_ref:
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
        name = "R-PORT-PROTOTYPE-IN-SOFTWARE-CLUSTER-DESIGN-INSTANCE-REF"

    context_root_sw_cluster_design_component_prototype_ref: (
        RPortPrototypeInSoftwareClusterDesignInstanceRef.ContextRootSwClusterDesignComponentPrototypeRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-CLUSTER-DESIGN-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_sw_component_prototype_ref: list[
        RPortPrototypeInSoftwareClusterDesignInstanceRef.ContextSwComponentPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_r_port_prototype_ref: (
        RPortPrototypeInSoftwareClusterDesignInstanceRef.TargetRPortPrototypeRef
        | None
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-R-PORT-PROTOTYPE-REF",
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
    class ContextRootSwClusterDesignComponentPrototypeRef(Ref):
        dest: RootSwClusterDesignComponentPrototypeSubtypesEnum | None = field(
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
    class TargetRPortPrototypeRef(Ref):
        dest: RPortPrototypeSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
