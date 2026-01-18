from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class Date:
    """
    A datatype representing a timestamp.

    The smallest granularity is 1 second. This datatype represents a
    timestamp in the format yyyy-mm-dd followed by an optional time. The
    lead-in character for the time is "T" and the format is hh:mm:ss. In
    addition, a time zone designator shall be specified. The time zone
    designator can either be "Z" (for UTC) or the time offset to UTC, i.e.
    (+|-)hh:mm. Examples: 2009-07-23 2009-07-23T14:38:00+01:00
    2009-07-23T13:38:00Z.

    :ivar value:
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
        name = "DATE"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
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
