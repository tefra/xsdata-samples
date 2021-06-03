from dataclasses import dataclass, field
from typing import Optional
from autosar.models.annotation import VariationPoint
from autosar.models.component_in_system_instance_ref import ComponentInSystemInstanceRef

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwComponentPrototypeAssignment:
    """
    This meta-class is only required to allow for the variant modeling of an
    instanceRef.

    :ivar sw_component_iref: hierarchical tree(s) of Software Components
        belonging to this CP Software Cluster. This reference is used to
        describe the belonging SWCs if the CP Software Cluster is
        described in the context of a System,
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
        name = "SW-COMPONENT-PROTOTYPE-ASSIGNMENT"

    sw_component_iref: Optional[ComponentInSystemInstanceRef] = field(
        default=None,
        metadata={
            "name": "SW-COMPONENT-IREF",
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
