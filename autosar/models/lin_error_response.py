from __future__ import annotations

from dataclasses import dataclass, field

from .i_signal_triggering_subtypes_enum import ISignalTriggeringSubtypesEnum
from .integer import Integer
from .lin_frame_triggering_subtypes_enum import LinFrameTriggeringSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinErrorResponse:
    """
    Each slave node shall publish a one bit signal, named response_error,
    to the master node in one of its transmitted unconditional frames.

    The response_error signal shall be set whenever a frame (except for
    event triggered frame responses) that is transmitted or received by the
    slave node contains an error in the frame response. The response_error
    signal shall be cleared when the unconditional frame containing the
    response_error signal is successfully transmitted.

    :ivar frame_triggering_ref: Reference to an unconditional frame
        that transmits the response error. The referenced
        LinFrameTriggering shall contain a reference to an
        unconditionalFrame.
    :ivar response_error_position: Specifies the position of the
        ResponseError bit in the frame. Each slave node shall publish
        one response error in one of its transmitted unconditional
        frames.
    :ivar response_error_ref: This ISignal shall be taken to transport
        the responseError bit.
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
        name = "LIN-ERROR-RESPONSE"

    frame_triggering_ref: LinErrorResponse.FrameTriggeringRef | None = field(
        default=None,
        metadata={
            "name": "FRAME-TRIGGERING-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_error_position: Integer | None = field(
        default=None,
        metadata={
            "name": "RESPONSE-ERROR-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_error_ref: LinErrorResponse.ResponseErrorRef | None = field(
        default=None,
        metadata={
            "name": "RESPONSE-ERROR-REF",
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
    class FrameTriggeringRef(Ref):
        dest: LinFrameTriggeringSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ResponseErrorRef(Ref):
        dest: ISignalTriggeringSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
