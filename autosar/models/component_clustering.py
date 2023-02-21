from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    DocumentationBlock,
    VariationPoint,
)
from .component_in_system_instance_ref import ComponentInSystemInstanceRef
from .mapping_scope_enum import MappingScopeEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ComponentClustering:
    """Constraint that forces the mapping of all referenced SW component instances
    to the same ECU, Core, Partition depending on the defined mappingScope
    attribute.

    If mappingScope is not specified then mappingScopeEcu shall be
    assumed.

    :ivar introduction: This represents introductory documentation about
        the mapping constraint.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar clustered_component_irefs: Reference to the components that
        have to be mapped together.
    :ivar mapping_scope: This attribute indicates whether the
        ComponentClustering mapping constraint applies to different
        ECUs, partitions or cores. If this attribute is not specified
        then mappingScopeEcu shall be assumed.
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
        name = "COMPONENT-CLUSTERING"

    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    clustered_component_irefs: Optional["ComponentClustering.ClusteredComponentIrefs"] = field(
        default=None,
        metadata={
            "name": "CLUSTERED-COMPONENT-IREFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mapping_scope: Optional[MappingScopeEnum] = field(
        default=None,
        metadata={
            "name": "MAPPING-SCOPE",
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
    class ClusteredComponentIrefs:
        clustered_component_iref: List[ComponentInSystemInstanceRef] = field(
            default_factory=list,
            metadata={
                "name": "CLUSTERED-COMPONENT-IREF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
