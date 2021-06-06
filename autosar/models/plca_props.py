from dataclasses import dataclass, field
from typing import Optional
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PlcaProps:
    """
    This meta-class allows to configure the PLCA (Physical Layer Collision
    Avoidance) in case 10-BASE-T1S Ethernet is used and PLCA is enabled on the
    CouplingPort (PHY).

    :ivar plca_local_node_id: This attribute defines the node ID when
        the PLCA mode for 10BASE-T1S is used.
    :ivar plca_max_burst_count: Defines maximum packets allowed to be
        transmitted within a TO. This configuration can be different
        from one ECU to another within the PLCA mixed segment.
    :ivar plca_max_burst_timer: Limits the burst frames in bit time.
        This configuration can be different from one ECU to another
        within the PLCA mixed segment. For PLCA burst mode to work
        properly this timer should be set greater than one IPG.
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
        name = "PLCA-PROPS"

    plca_local_node_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PLCA-LOCAL-NODE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    plca_max_burst_count: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PLCA-MAX-BURST-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    plca_max_burst_timer: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PLCA-MAX-BURST-TIMER",
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
