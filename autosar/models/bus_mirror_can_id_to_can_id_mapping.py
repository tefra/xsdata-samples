from dataclasses import dataclass, field
from typing import Optional
from autosar.models.can_frame_triggering_subtypes_enum import CanFrameTriggeringSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref

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

    remapped_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "REMAPPED-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    souce_can_id_ref: Optional["BusMirrorCanIdToCanIdMapping.SouceCanIdRef"] = field(
        default=None,
        metadata={
            "name": "SOUCE-CAN-ID-REF",
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
    class SouceCanIdRef(Ref):
        dest: Optional[CanFrameTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
