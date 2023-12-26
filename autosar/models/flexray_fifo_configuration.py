from dataclasses import dataclass, field
from typing import List, Optional
from .boolean import Boolean
from .flexray_fifo_range import FlexrayFifoRange
from .flexray_physical_channel_subtypes_enum import (
    FlexrayPhysicalChannelSubtypesEnum,
)
from .integer import Integer
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayFifoConfiguration:
    """
    One First In First Out (FIFO) queued receive structure, defining the admittance
    criteria to the FIFO, and mandating the ability to admit messages into the FIFO
    based on Message Id filtering criteria.

    :ivar admit_without_message_id: Boolean configuration which
        determines whether or not frames received in the dynamic segment
        that don't contain a message ID will be admitted into the FIFO.
    :ivar base_cycle: FIFO cycle counter acceptance criteria.
    :ivar channel_ref: Fifo channel admittance criteria.
    :ivar cycle_repetition: FIFO cycle counter acceptance criteria.
    :ivar fifo_depth: FrFifoDepth configures the maximum number of rx-
        frames which can be contained in the FIFO.
    :ivar fifo_ranges: FIFO Frame Id range acceptance criteria.
    :ivar msg_id_mask: FIFO message identifier acceptance criteria (Mask
        filter).
    :ivar msg_id_match: FIFO message identifier acceptance criteria
        (Match filter).
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
        name = "FLEXRAY-FIFO-CONFIGURATION"

    admit_without_message_id: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ADMIT-WITHOUT-MESSAGE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    base_cycle: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "BASE-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    channel_ref: Optional["FlexrayFifoConfiguration.ChannelRef"] = field(
        default=None,
        metadata={
            "name": "CHANNEL-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cycle_repetition: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "CYCLE-REPETITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fifo_depth: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "FIFO-DEPTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fifo_ranges: Optional["FlexrayFifoConfiguration.FifoRanges"] = field(
        default=None,
        metadata={
            "name": "FIFO-RANGES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msg_id_mask: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MSG-ID-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    msg_id_match: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MSG-ID-MATCH",
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
    class ChannelRef(Ref):
        dest: Optional[FlexrayPhysicalChannelSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class FifoRanges:
        flexray_fifo_range: List[FlexrayFifoRange] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-FIFO-RANGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
