from dataclasses import dataclass, field
from typing import Optional
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayFifoRange:
    """
    FIFO Frame Id range acceptance criteria.

    :ivar range_max: Max Range.
    :ivar range_min: Min Range.
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
        name = "FLEXRAY-FIFO-RANGE"

    range_max: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "RANGE-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    range_min: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "RANGE-MIN",
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
