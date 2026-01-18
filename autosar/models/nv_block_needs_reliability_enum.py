from __future__ import annotations

from dataclasses import dataclass, field

from .nv_block_needs_reliability_enum_simple import (
    NvBlockNeedsReliabilityEnumSimple,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class NvBlockNeedsReliabilityEnum:
    """
    Reliability against data loss on the non-volatile medium.

    These requirements give only a relative indication, for example on the
    required degree of redundancy for storage. They do, however, not
    specify by which means (e.g. software or hardware) the reliability is
    actually achieved.

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
        name = "NV-BLOCK-NEEDS-RELIABILITY-ENUM"

    value: NvBlockNeedsReliabilityEnumSimple | None = field(
        default=None,
        metadata={
            "required": True,
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
