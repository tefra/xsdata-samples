from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.i_signal_i_pdu_subtypes_enum import ISignalIPduSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.segment_position import SegmentPosition

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class StaticPart:
    """Some parts/signals of the I-PDU may be the same regardless of the
    selector field.

    Such a part is called static part. The static part is optional.

    :ivar segment_positions: The StaticPart and the DynamicPart can be
        separated in multiple segments within the multiplexed PDU.
        Therefore the StaticPart and the DynamicPart can contain
        multiple SegmentPositions.
    :ivar i_pdu_ref: Reference to a Com IPdu which is routed to the
        IPduM module and is combined to a multiplexedPdu.
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
        name = "STATIC-PART"

    segment_positions: Optional["StaticPart.SegmentPositions"] = field(
        default=None,
        metadata={
            "name": "SEGMENT-POSITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    i_pdu_ref: Optional["StaticPart.IPduRef"] = field(
        default=None,
        metadata={
            "name": "I-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass
    class SegmentPositions:
        segment_position: List[SegmentPosition] = field(
            default_factory=list,
            metadata={
                "name": "SEGMENT-POSITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class IPduRef(Ref):
        dest: Optional[ISignalIPduSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
