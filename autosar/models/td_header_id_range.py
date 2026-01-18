from __future__ import annotations

from dataclasses import dataclass, field

from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TdHeaderIdRange:
    """
    Specifies a range of PDU header identifiers.

    This range is specified by a minimum and maximum header identifier; and
    the maximum header identifier shall be greater than or equal the
    minimum header identifier.

    :ivar max_header_id: Specifies the maximum PDU header identifier, in
        other words the upper bound of a range of PDU header
        identifiers.
    :ivar min_header_id: Specifies the minimum PDU header identifier, in
        other words the lower bound of a range of PDU header
        identifiers.
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
        name = "TD-HEADER-ID-RANGE"

    max_header_id: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-HEADER-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min_header_id: None | Integer = field(
        default=None,
        metadata={
            "name": "MIN-HEADER-ID",
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
