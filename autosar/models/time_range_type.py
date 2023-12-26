from dataclasses import dataclass, field
from typing import Optional
from .absolute_tolerance import AbsoluteTolerance
from .relative_tolerance import RelativeTolerance
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimeRangeType:
    """The timeRange can be specified with the value attribute.

    Optionally a tolerance can be defined.

    :ivar tolerance: Optional specification of a tolerance.
    :ivar value: Average value of a date (in seconds)
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
        name = "TIME-RANGE-TYPE"

    tolerance: Optional["TimeRangeType.Tolerance"] = field(
        default=None,
        metadata={
            "name": "TOLERANCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "VALUE",
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

    @dataclass
    class Tolerance:
        absolute_tolerance: Optional[AbsoluteTolerance] = field(
            default=None,
            metadata={
                "name": "ABSOLUTE-TOLERANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        relative_tolerance: Optional[RelativeTolerance] = field(
            default=None,
            metadata={
                "name": "RELATIVE-TOLERANCE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
