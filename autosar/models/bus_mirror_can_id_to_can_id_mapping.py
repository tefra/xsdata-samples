from __future__ import annotations

from dataclasses import dataclass, field

from .can_frame_triggering_subtypes_enum import CanFrameTriggeringSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BusMirrorCanIdToCanIdMapping:
    """
    This element defines a rule for remapping a single CAN ID.

    :ivar remapped_can_id: This attribute defines the CanId on the
        targetChannel.
    :ivar souce_can_id_ref: This reference points to the sourceFrame
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
        name = "BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING"

    remapped_can_id: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "REMAPPED-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    souce_can_id_ref: None | BusMirrorCanIdToCanIdMapping.SouceCanIdRef = (
        field(
            default=None,
            metadata={
                "name": "SOUCE-CAN-ID-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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

    @dataclass
    class SouceCanIdRef(Ref):
        dest: None | CanFrameTriggeringSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
