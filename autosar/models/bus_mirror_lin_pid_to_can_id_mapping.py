from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .lin_frame_triggering_subtypes_enum import LinFrameTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BusMirrorLinPidToCanIdMapping:
    """
    This element defines a rule for remapping a single LIN Frame.

    :ivar remapped_can_id: This attribute defines the CanId on the
        targetChannel.
    :ivar source_lin_pid_ref: This reference points to the sourceFrame
        with sourceCanId on the sourceChannel.
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
        name = "BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING"

    remapped_can_id: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "REMAPPED-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    source_lin_pid_ref: BusMirrorLinPidToCanIdMapping.SourceLinPidRef | None = field(
        default=None,
        metadata={
            "name": "SOURCE-LIN-PID-REF",
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

    @dataclass
    class SourceLinPidRef(Ref):
        dest: LinFrameTriggeringSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
