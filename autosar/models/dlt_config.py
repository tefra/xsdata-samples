from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .dlt_log_channel import DltLogChannel
from .string import String

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DltConfig:
    """
    This element defines a Dlt configuration for a specific Ecu.

    :ivar dlt_ecu_id: This attribute defines the name of the ECU for use
        within the Dlt protocol.
    :ivar dlt_log_channels: Describes the DltLogChannels that are
        configured for the log/trace message output
    :ivar session_id_support: This attribute defines whether the
        sessionId is used or not.
    :ivar timestamp_support: This attribute defines whether a timestamp
        shall be added to the Dlt messages or not.
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
        name = "DLT-CONFIG"

    dlt_ecu_id: Optional[String] = field(
        default=None,
        metadata={
            "name": "DLT-ECU-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dlt_log_channels: Optional["DltConfig.DltLogChannels"] = field(
        default=None,
        metadata={
            "name": "DLT-LOG-CHANNELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    session_id_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "SESSION-ID-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    timestamp_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TIMESTAMP-SUPPORT",
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
    class DltLogChannels:
        dlt_log_channel: list[DltLogChannel] = field(
            default_factory=list,
            metadata={
                "name": "DLT-LOG-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
