from __future__ import annotations

from dataclasses import dataclass, field

from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BusMirrorCanIdRangeMapping:
    """
    This element defines a rule for remapping a set of CAN IDs.

    :ivar destination_base_id: Base ID merged with the masked parts of
        the original CAN ID to form the mapped CAN ID.
    :ivar source_can_id_code: Value to match masked original CAN IDs.
    :ivar source_can_id_mask: Mask applied to original CAN IDs before
        comparison.
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
        name = "BUS-MIRROR-CAN-ID-RANGE-MAPPING"

    destination_base_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "DESTINATION-BASE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_can_id_code: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SOURCE-CAN-ID-CODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_can_id_mask: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "SOURCE-CAN-ID-MASK",
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
