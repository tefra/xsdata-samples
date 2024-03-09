from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import VariationPoint
from .ref import Ref
from .runnable_entity_group_subtypes_enum import (
    RunnableEntityGroupSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class InnerRunnableEntityGroupInCompositionInstanceRef:
    """
    This meta-class represents the ability to define an InstanceRef to a nested
    RunnableEntityGroup.

    :ivar context_sw_component_prototype_ref: This represents the nested
        structure of SwComponentPrototypes.
    :ivar target_runnable_entity_group_ref: This represents the target
        association of the InstanceRef.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "INNER-RUNNABLE-ENTITY-GROUP-IN-COMPOSITION-INSTANCE-REF"

    context_sw_component_prototype_ref: List[
        "InnerRunnableEntityGroupInCompositionInstanceRef.ContextSwComponentPrototypeRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_runnable_entity_group_ref: Optional[
        "InnerRunnableEntityGroupInCompositionInstanceRef.TargetRunnableEntityGroupRef"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-RUNNABLE-ENTITY-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class TargetRunnableEntityGroupRef(Ref):
        dest: Optional[RunnableEntityGroupSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
