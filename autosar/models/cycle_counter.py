from __future__ import annotations

from dataclasses import dataclass, field

from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CycleCounter:
    """
    The communication cycle where the frame is send is described by the
    attribute "cycleCounter".

    :ivar cycle_counter: The communication cycle where the frame
        described by this timing is sent. If a timing is given in this
        way the referencing FlexrayCluster shall specify the
        cycleCountMax as upper bound and point of total repetition. This
        value is incremented at the beginning of each new cycle, ranging
        from 0 to cycleCountMax, and is reset to 0 after a sequence of
        cycleCountMax+1 cycles.
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
        name = "CYCLE-COUNTER"

    cycle_counter: Integer | None = field(
        default=None,
        metadata={
            "name": "CYCLE-COUNTER",
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
