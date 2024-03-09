from dataclasses import dataclass, field
from typing import Optional

from .handle_out_of_range_enum import HandleOutOfRangeEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ISignalProps:
    """
    Additional ISignal properties that may be stored in different files.

    :ivar handle_out_of_range: This attribute defines the
        outOfRangeHandling for received and sent signals.
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
        name = "I-SIGNAL-PROPS"

    handle_out_of_range: Optional[HandleOutOfRangeEnum] = field(
        default=None,
        metadata={
            "name": "HANDLE-OUT-OF-RANGE",
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
