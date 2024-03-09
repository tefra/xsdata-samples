from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .system_signal_subtypes_enum import SystemSignalSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EmptySignalMapping:
    """If no actual data is configured for a client server communication the
    element EmptySignalMapping shall be used.

    An EmptySignalMapping shall only reference a SystemSignal that is
    referenced by an ISignal with length equal to zero. In this case
    there shall be an "update-bit" configured. The EmptySignal can be
    mapped to the response group or to request group.

    :ivar system_signal_ref: Reference to a SystemSignal with
        "signalLength" = 0 and an UpdateBit.
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
        name = "EMPTY-SIGNAL-MAPPING"

    system_signal_ref: Optional["EmptySignalMapping.SystemSignalRef"] = field(
        default=None,
        metadata={
            "name": "SYSTEM-SIGNAL-REF",
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
    class SystemSignalRef(Ref):
        dest: Optional[SystemSignalSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
