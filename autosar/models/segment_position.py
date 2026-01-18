from __future__ import annotations

from dataclasses import dataclass, field

from .byte_order_enum import ByteOrderEnum
from .integer import Integer

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SegmentPosition:
    """
    The StaticPart and the DynamicPart can be separated in multiple
    segments within the multiplexed PDU.

    The ISignalIPdus are copied bit by bit into the MultiplexedIPdu. If the
    space of the first segment is 5 bits large than the first 5 bits of the
    ISignalIPdu are copied into this first segment and so on.

    :ivar segment_byte_order: This attribute defines the order of the
        bytes of the segment and the packing into the MultiplexedIPdu.
        Please consider that [constr_3247] and [constr_3224] are
        restricting the usage of this attribute.
    :ivar segment_length: Data Length of the segment in bits.
    :ivar segment_position: Segments bit position relatively to the
        beginning of a multiplexed IPdu. Note that the absolute position
        of the segment in the MultiplexedIPdu is determined by the
        definition of the segmentByteOrder attribute of the
        SegmentPosition. If Big Endian is specified, the start position
        indicates the bit position of the most significant bit in the
        IPdu. If Little Endian is specified, the start position
        indicates the bit position of the least significant bit in the
        IPdu. In AUTOSAR the bit counting is always set to "sawtooth"
        and the bit order is set to "Decreasing". The bit counting in
        byte 0 starts with bit 0 (least significant bit). The most
        significant bit in byte 0 is bit 7.
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
        name = "SEGMENT-POSITION"

    segment_byte_order: ByteOrderEnum | None = field(
        default=None,
        metadata={
            "name": "SEGMENT-BYTE-ORDER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    segment_length: Integer | None = field(
        default=None,
        metadata={
            "name": "SEGMENT-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    segment_position: Integer | None = field(
        default=None,
        metadata={
            "name": "SEGMENT-POSITION",
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
