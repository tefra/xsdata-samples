from __future__ import annotations

from dataclasses import dataclass, field

from .cycle_counter import CycleCounter
from .cycle_repetition import CycleRepetition
from .integer import Integer
from .ttcan_trigger_type import TtcanTriggerType

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TtcanAbsolutelyScheduledTiming:
    """
    Each frame in TTCAN is identified by its slot id and communication
    cycle.

    A description is provided by the usage of AbsolutelyScheduledTiming. A
    frame can be sent multiple times within one communication cycle. For
    describing this case multiple AbsolutelyScheduledTimings have to be
    used. The main use case would be that a frame is sent twice within one
    communication cycle.

    :ivar communication_cycle: The communication cycle where the frame
        is sent.
    :ivar time_mark: Where FlexRay counts the slots in the static
        segment, TTCAN requires explicit Tx and Rx time marks.
    :ivar trigger: Trigger type for this time window.
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
        name = "TTCAN-ABSOLUTELY-SCHEDULED-TIMING"

    communication_cycle: (
        None | TtcanAbsolutelyScheduledTiming.CommunicationCycle
    ) = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    time_mark: None | Integer = field(
        default=None,
        metadata={
            "name": "TIME-MARK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    trigger: None | TtcanTriggerType = field(
        default=None,
        metadata={
            "name": "TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CommunicationCycle:
        cycle_counter: None | CycleCounter = field(
            default=None,
            metadata={
                "name": "CYCLE-COUNTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        cycle_repetition: None | CycleRepetition = field(
            default=None,
            metadata={
                "name": "CYCLE-REPETITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
