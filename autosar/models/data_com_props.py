from dataclasses import dataclass, field
from typing import Optional
from .send_indication_enum import SendIndicationEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataComProps:
    """
    Represents a single resource required or provided by a CP Software Cluster
    which relates to the port based communication on VFB level.

    :ivar send_indication: Send indication behavior for last-is-the best
        data communciation.
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
        name = "DATA-COM-PROPS"

    send_indication: Optional[SendIndicationEnum] = field(
        default=None,
        metadata={
            "name": "SEND-INDICATION",
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
