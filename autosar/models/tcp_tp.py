from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue
from .tp_port import TpPort

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TcpTp:
    """
    Content Model for TCP configuration.

    :ivar keep_alive_interval: Specifies the interval in seconds between
        subsequent keepalive probes.
    :ivar keep_alive_probes_max: Maximum number of times that TCP
        retransmits an individual data segment before aborting the
        connection.
    :ivar keep_alive_time: Specifies the time in seconds between the
        last data packet sent and the first keepalive probe.
    :ivar keep_alives: Indicates if Keep-Alive messages are send.
    :ivar nagles_algorithm: Indicates if Nagle's Algorithm is used.
    :ivar receive_window_min: Minimum size of the TCP receive window in
        byte.
    :ivar tcp_tp_port: TCP Port configuration.
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
        name = "TCP-TP"

    keep_alive_interval: TimeValue | None = field(
        default=None,
        metadata={
            "name": "KEEP-ALIVE-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    keep_alive_probes_max: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "KEEP-ALIVE-PROBES-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    keep_alive_time: TimeValue | None = field(
        default=None,
        metadata={
            "name": "KEEP-ALIVE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    keep_alives: Boolean | None = field(
        default=None,
        metadata={
            "name": "KEEP-ALIVES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nagles_algorithm: Boolean | None = field(
        default=None,
        metadata={
            "name": "NAGLES-ALGORITHM",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    receive_window_min: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "RECEIVE-WINDOW-MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_tp_port: TpPort | None = field(
        default=None,
        metadata={
            "name": "TCP-TP-PORT",
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
