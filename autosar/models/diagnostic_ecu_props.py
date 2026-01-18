from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticEcuProps:
    """
    This meta-class is defined to gather diagnostic-related properties that
    apply in the scope of an entire ECU.

    :ivar is_obd_relevant: This attribute indicates whether the ECU
        makes any contribution to the OBD.
    :ivar send_resp_pend_on_trans_to_boot: The purpose of this attribute
        is to define whether or not the ECU should send a NRC 0x78
        (response pending) before transitioning to the bootloader (in
        this case the attribute shall be set to "true") or if the
        transition shall be initiated without sending NRC 0x78 (in this
        case the attribute shall be set to "false").
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
        name = "DIAGNOSTIC-ECU-PROPS"

    is_obd_relevant: Boolean | None = field(
        default=None,
        metadata={
            "name": "IS-OBD-RELEVANT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    send_resp_pend_on_trans_to_boot: Boolean | None = field(
        default=None,
        metadata={
            "name": "SEND-RESP-PEND-ON-TRANS-TO-BOOT",
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
