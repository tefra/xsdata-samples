from dataclasses import dataclass, field
from typing import Optional

from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanNmRangeConfig:
    """
    Defines the CANID ranges that are used for Nm.

    This range definition is redundant to the attribute "rxIdentifierRange"
    of CanFrameTriggering. For backward compatibility reasons this
    redundancy shall be preserved and both shall be defined. In future this
    element will be removed from the model.

    :ivar lower_can_id: Lower CAN Identifier of a receive CAN L-PDU for
        identifier range definition.
    :ivar upper_can_id: Upper CAN Identifier of a receive CAN L-PDU for
        identifier range definition.
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
        name = "CAN-NM-RANGE-CONFIG"

    lower_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "LOWER-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "UPPER-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
