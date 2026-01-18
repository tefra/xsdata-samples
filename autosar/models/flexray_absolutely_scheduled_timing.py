from __future__ import annotations

from dataclasses import dataclass, field

from .cycle_counter import CycleCounter
from .cycle_repetition import CycleRepetition
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayAbsolutelyScheduledTiming:
    """
    Each frame in FlexRay is identified by its slot id and communication
    cycle.

    A description is provided by the usage of AbsolutelyScheduledTiming. In
    the static segment a frame can be sent multiple times within one
    communication cycle. For describing this case multiple
    AbsolutelyScheduledTimings have to be used. The main use case would be
    that a frame is sent twice within one communication cycle.

    :ivar communication_cycle: The communication cycle where the frame
        is sent.
    :ivar slot_id: In the static part the SlotID defines the slot in
        which the frame is transmitted. The SlotID also determines, in
        combination with FlexrayCluster::numberOfStaticSlots, whether
        the frame is sent in static or dynamic segment. In the dynamic
        part, the slot id is equivalent to a priority. Lower dynamic
        slot ids are all sent until the end of the dynamic segment.
        Higher numbers, which were ignored that time, have to wait one
        cycle and then shall try again. minValue: 1 maxValue: 2047
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
        name = "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING"

    communication_cycle: (
        FlexrayAbsolutelyScheduledTiming.CommunicationCycle | None
    ) = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    slot_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SLOT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class CommunicationCycle:
        cycle_counter: CycleCounter | None = field(
            default=None,
            metadata={
                "name": "CYCLE-COUNTER",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        cycle_repetition: CycleRepetition | None = field(
            default=None,
            metadata={
                "name": "CYCLE-REPETITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
