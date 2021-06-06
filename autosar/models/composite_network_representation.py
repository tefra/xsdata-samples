from dataclasses import dataclass, field
from typing import Optional
from .application_composite_element_in_port_interface_instance_ref import ApplicationCompositeElementInPortInterfaceInstanceRef
from .sw_pointer_target_props import SwDataDefProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CompositeNetworkRepresentation:
    """
    This meta-class is used to define the network representation of leaf
    elements of composite application data types.

    :ivar leaf_element_iref: This represents that leaf element of an
        application composite data type.
    :ivar network_representation: The SwDataDefProps owned by the
        CompositeNetworkRepresentation are used to define the network
        representation of the leaf element of an
        ApplicationCompositeDataType.
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
        name = "COMPOSITE-NETWORK-REPRESENTATION"

    leaf_element_iref: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef] = field(
        default=None,
        metadata={
            "name": "LEAF-ELEMENT-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    network_representation: Optional[SwDataDefProps] = field(
        default=None,
        metadata={
            "name": "NETWORK-REPRESENTATION",
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
