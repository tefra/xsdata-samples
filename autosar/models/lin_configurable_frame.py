from dataclasses import dataclass, field
from typing import Optional
from .lin_frame_subtypes_enum import LinFrameSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinConfigurableFrame:
    """Assignment of messageIds to Frames.

    This element shall be used for the LIN 2.0 Assign-Frame command.

    :ivar frame_ref: Reference to a Frame that is processed by the slave
        node.
    :ivar message_id: MessageId for the referenced frame
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
        name = "LIN-CONFIGURABLE-FRAME"

    frame_ref: Optional["LinConfigurableFrame.FrameRef"] = field(
        default=None,
        metadata={
            "name": "FRAME-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    message_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MESSAGE-ID",
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
    class FrameRef(Ref):
        dest: Optional[LinFrameSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
