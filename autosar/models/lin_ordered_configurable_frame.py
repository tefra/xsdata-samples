from dataclasses import dataclass, field
from typing import Optional
from .integer import Integer
from .lin_frame_subtypes_enum import LinFrameSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinOrderedConfigurableFrame:
    """With the assignment of the index to a frame a mapping of Pids to Frames is
    possible.

    This element shall be used for the LIN 2.1 Assign-Frame-PID-Range
    command.

    :ivar frame_ref: Reference to a Frame that is processed by the slave
        node.
    :ivar index: This attribute is used to order the elements and allows
        an assignment of Pids to ConfigurableFrames that are defined in
        the slave.
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
        name = "LIN-ORDERED-CONFIGURABLE-FRAME"

    frame_ref: Optional["LinOrderedConfigurableFrame.FrameRef"] = field(
        default=None,
        metadata={
            "name": "FRAME-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    index: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "INDEX",
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
    class FrameRef(Ref):
        dest: Optional[LinFrameSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
