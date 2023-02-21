from dataclasses import dataclass, field
from typing import Optional
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RxIdentifierRange:
    """Optional definition of a CanId range to reduce the effort of specifying
    every possible FrameTriggering within the defined Id range during reception.

    All frames received within a range are mapped to the same Pdu that
    is passed to a upper layer module (e.g. Nm, CDD, PduR).

    :ivar lower_can_id: This attribute can be used together with the
        upperCanId attribute to define a range of CanIds.
    :ivar upper_can_id: This attribute can be used together with the
        lowerCanId attribute to define a range of CanIds.
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
        name = "RX-IDENTIFIER-RANGE"

    lower_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOWER-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    upper_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UPPER-CAN-ID",
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
