from __future__ import annotations

from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ieee1722Tp:
    """
    Content Model for IEEE 1722 configuration.

    :ivar relative_representation_time: Defines the time when content
        shall be presented (in seconds). The actual absolute time is
        creation time plus relative presentation time.
    :ivar stream_identifier: IEEE 1722 stream identifier
    :ivar sub_type: Protocol type.
    :ivar version: Revision of Ieee1722 standard
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
        name = "IEEE-1722-TP"

    relative_representation_time: TimeValue | None = field(
        default=None,
        metadata={
            "name": "RELATIVE-REPRESENTATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    stream_identifier: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "STREAM-IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sub_type: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SUB-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    version: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "VERSION",
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
