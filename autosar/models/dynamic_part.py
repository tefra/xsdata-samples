from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .dynamic_part_alternative import DynamicPartAlternative
from .segment_position import SegmentPosition

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class DynamicPart:
    """
    Dynamic part of a multiplexed I-Pdu.

    Reserved space which is used to transport varying SignalIPdus at the
    same position, controlled by the corresponding selectorFieldCode.

    :ivar segment_positions: The StaticPart and the DynamicPart can be
        separated in multiple segments within the multiplexed PDU.
        Therefore the StaticPart and the DynamicPart can contain
        multiple SegmentPositions.
    :ivar dynamic_part_alternatives: Com IPdu alternatives that are
        transmitted  in the Dynamic Part of the MultiplexedIPdu.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "DYNAMIC-PART"

    segment_positions: None | DynamicPart.SegmentPositions = field(
        default=None,
        metadata={
            "name": "SEGMENT-POSITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dynamic_part_alternatives: None | DynamicPart.DynamicPartAlternatives = (
        field(
            default=None,
            metadata={
                "name": "DYNAMIC-PART-ALTERNATIVES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass(kw_only=True)
    class SegmentPositions:
        segment_position: list[SegmentPosition] = field(
            default_factory=list,
            metadata={
                "name": "SEGMENT-POSITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass(kw_only=True)
    class DynamicPartAlternatives:
        dynamic_part_alternative: list[DynamicPartAlternative] = field(
            default_factory=list,
            metadata={
                "name": "DYNAMIC-PART-ALTERNATIVE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
