from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .component_in_system_instance_ref import ComponentInSystemInstanceRef
from .mapping_scope_enum import MappingScopeEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class ComponentSeparation:
    """
    Constraint that forces the two referenced SW components (called A and B
    in the following) not to be mapped to the same ECU, Core, Partition
    depending on the defined mappingScope attribute.

    If mappingScope is not specified then mappingScopeEcu shall be assumed.
    If a SW component (e.g. A) is a composition, none of the atomic SW
    components making up the A composition shall be mapped together with
    any of the atomic SW components making up the B composition.
    Furthermore, A and B shall be disjoint.

    :ivar introduction: This represents introductory documentation about
        the mapping constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar mapping_scope: This attribute indicates whether the
        ComponentSeparation mapping constraint applies to different
        ECUs, partitions or cores. If this attribute is not specified
        then mappingScopeEcu shall be assumed.
    :ivar separated_component_irefs: The two components that have to be
        mapped to different ECUs
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
        name = "COMPONENT-SEPARATION"

    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mapping_scope: None | MappingScopeEnum = field(
        default=None,
        metadata={
            "name": "MAPPING-SCOPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    separated_component_irefs: (
        None | ComponentSeparation.SeparatedComponentIrefs
    ) = field(
        default=None,
        metadata={
            "name": "SEPARATED-COMPONENT-IREFS",
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
    class SeparatedComponentIrefs:
        separated_component_iref: list[ComponentInSystemInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "SEPARATED-COMPONENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
                "max_occurs": 2,
            },
        )
