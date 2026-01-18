from dataclasses import dataclass, field

from .cyclic_timing import CyclicTiming
from .event_controlled_timing import EventControlledTiming

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TransmissionModeTiming:
    """
    If the COM Transmission Mode is false the timing is aggregated by the
    TransmissionModeTiming element in the role of
    transmissionModeFalseTiming.

    If the COM Transmission Mode is true the timing is aggregated by the
    TransmissionModeTiming element in the role of
    transmissionModeTrueTiming. COM supports the following Transmission
    Modes: * Periodic (Cyclic Timing) * Direct /n-times
    (EventControlledTiming) * Mixed (Cyclic and EventControlledTiming are
    assigned) * None (no timing is assigned).

    :ivar cyclic_timing: Periodic Transmission Mode.
    :ivar event_controlled_timing: Direct Transmission Mode.
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
        name = "TRANSMISSION-MODE-TIMING"

    cyclic_timing: CyclicTiming | None = field(
        default=None,
        metadata={
            "name": "CYCLIC-TIMING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_controlled_timing: EventControlledTiming | None = field(
        default=None,
        metadata={
            "name": "EVENT-CONTROLLED-TIMING",
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
