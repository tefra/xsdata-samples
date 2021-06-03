from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.coupling_port_ref_conditional import CouplingPortRefConditional
from autosar.models.coupling_port_subtypes_enum import CouplingPortSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CouplingPortConnection:
    """
    Connection between two CouplingPorts (firstPort and secondPort) or between
    a collection of Ports that are all referenced by the portCollection
    reference.

    :ivar first_port_ref: Reference to the first CouplingPort that is
        connected via the CouplingPortConnection.
    :ivar node_ports: This property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar plca_local_node_count: Defines the number of communication
        participants in case 10BASE-T1S and the nodePort reference is
        used.
    :ivar plca_transmit_opportunity_timer: Timer for the transmission in
        bit time to evaluate if a Transmission Opportunity is yield or
        not.
    :ivar second_port_ref: Reference to the second CouplingPort that is
        connected via the CouplingPortConnection.
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
        name = "COUPLING-PORT-CONNECTION"

    first_port_ref: Optional["CouplingPortConnection.FirstPortRef"] = field(
        default=None,
        metadata={
            "name": "FIRST-PORT-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    node_ports: Optional["CouplingPortConnection.NodePorts"] = field(
        default=None,
        metadata={
            "name": "NODE-PORTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    plca_local_node_count: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PLCA-LOCAL-NODE-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    plca_transmit_opportunity_timer: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PLCA-TRANSMIT-OPPORTUNITY-TIMER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    second_port_ref: Optional["CouplingPortConnection.SecondPortRef"] = field(
        default=None,
        metadata={
            "name": "SECOND-PORT-REF",
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
    class FirstPortRef(Ref):
        dest: Optional[CouplingPortSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class NodePorts:
        coupling_port_ref_conditional: List[CouplingPortRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class SecondPortRef(Ref):
        dest: Optional[CouplingPortSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
