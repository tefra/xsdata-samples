from dataclasses import dataclass, field
from typing import Optional

from .positive_integer import PositiveInteger
from .tcp_tp import TcpTp
from .udp_tp import UdpTp

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RtpTp:
    """
    RTP over UDP or over TCP as transport protocol.

    :ivar ssrc: Synchronization source identifier uniquely identifies
        the source of a stream. The synchronization sources within the
        same RTP session will be unique.
    :ivar tcp_udp_config: Tcp or Udp Configuration.
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
        name = "RTP-TP"

    ssrc: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SSRC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_udp_config: Optional["RtpTp.TcpUdpConfig"] = field(
        default=None,
        metadata={
            "name": "TCP-UDP-CONFIG",
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
    class TcpUdpConfig:
        tcp_tp: Optional[TcpTp] = field(
            default=None,
            metadata={
                "name": "TCP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_tp: Optional[UdpTp] = field(
            default=None,
            metadata={
                "name": "UDP-TP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
