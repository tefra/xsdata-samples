from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanNmEcu:
    """
    CAN specific attributes.

    :ivar nm_repeat_msg_indication_enabled: Enable/disable the
        notification that a RepeatMessageRequest bit has been received.
        This attribute is deprecated and shall be not used. It will be
        removed in the future. The nmRepeatMsgIndEnabled attribute in
        NmEcu shall be used instead.
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
        name = "CAN-NM-ECU"

    nm_repeat_msg_indication_enabled: Boolean | None = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MSG-INDICATION-ENABLED",
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
