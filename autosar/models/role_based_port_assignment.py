from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .identifier import Identifier
from .port_prototype_subtypes_enum import PortPrototypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RoleBasedPortAssignment:
    """This class specifies an assignment of a role to a particular service port
    (RPortPrototype or PPortPrototype) of an AtomicSwComponentType.

    With this assignment, the role of the service port can be mapped to
    a specific ServiceNeeds element, so that a tool is able to create
    the correct connector.

    :ivar port_prototype_ref: Service PortPrototype used in the assigned
        role. This PortPrototype shall either belong to the same
        AtomicSwComponentType as the SwcInternalBehavior which owns the
        ServiceDependency or to the same NvBlockSwComponentType as the
        NvBlockDescriptor.
    :ivar role: This is the role of the assigned Port in the given
        context. The value shall be a shortName of the Blueprint of a
        PortInterface as standardized in the Software Specification of
        the related AUTOSAR Service.
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
        name = "ROLE-BASED-PORT-ASSIGNMENT"

    port_prototype_ref: Optional["RoleBasedPortAssignment.PortPrototypeRef"] = field(
        default=None,
        metadata={
            "name": "PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
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

    @dataclass
    class PortPrototypeRef(Ref):
        dest: Optional[PortPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
