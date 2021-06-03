from dataclasses import dataclass, field
from typing import Optional
from autosar.models.boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UdpNmEcu:
    """
    Udp NM specific ECU attributes.

    :ivar nm_repeat_msg_indication_enabled: Enable/disable the
        notification that a RepeatMessageRequest bit has been received.
    :ivar nm_synchronization_point_enabled: Enable/disable the NM
        Coordination algorithm to being able to initiate the
        synchronization algorithm.
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
        name = "UDP-NM-ECU"

    nm_repeat_msg_indication_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MSG-INDICATION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_synchronization_point_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-SYNCHRONIZATION-POINT-ENABLED",
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
