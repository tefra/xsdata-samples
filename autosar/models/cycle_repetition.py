from dataclasses import dataclass, field
from typing import Optional
from .cycle_repetition_type import CycleRepetitionType
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CycleRepetition:
    """
    The communication cycle where the frame is send is described by the
    attributes baseCycle and cycleRepetition.

    :ivar base_cycle: The first communication cycle where the frame is
        sent. This value is incremented at the beginning of each new
        cycle, ranging from 0 to 63, and is reset to 0 after a sequence
        of 64 cycles.
    :ivar cycle_repetition: The number of communication cycles (after
        the first cycle) whenever the frame described by this timing is
        sent again.
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
        name = "CYCLE-REPETITION"

    base_cycle: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "BASE-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    cycle_repetition: Optional[CycleRepetitionType] = field(
        default=None,
        metadata={
            "name": "CYCLE-REPETITION",
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
