from dataclasses import dataclass, field
from typing import Optional
from autosar.models.boolean import Boolean
from autosar.models.positive_integer import PositiveInteger
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TcpProps:
    """
    This meta-class specifies the configuration options for TCP (Transmission
    Control Protocol).

    :ivar tcp_congestion_avoidance_enabled: Enables (TRUE) or disables
        (FALSE) support of TCP congestion avoidance algorithm according
        to IETF RFC 5681.
    :ivar tcp_delayed_ack_timeout: The maximal time an acknowledgment is
        delayed for transmission in seconds.
    :ivar tcp_fast_recovery_enabled: Enables (TRUE) or disables (FALSE)
        support of TCP Fast Recovery according to IETF RFC 5681.
    :ivar tcp_fast_retransmit_enabled: Enables (TRUE) or disables
        (FALSE) support of TCP Fast Retransmission according to IETF RFC
        5681.
    :ivar tcp_fin_wait_2_timeout: Timeout in [s] to receive a FIN from
        the remote node (after this node has initiated connection
        termination), i.e. maximum time waiting in FINWAIT-2 for a
        connection termination request from the remote TCP.
    :ivar tcp_keep_alive_enabled: Enables (TRUE) or disables (FALSE) TCP
        Keep Alive Probes according to IETF RFC 1122 chapter 4.2.3.6.
    :ivar tcp_keep_alive_interval: Specifies the interval in seconds
        between subsequent keepalive probes.
    :ivar tcp_keep_alive_probes_max: Maximum number of times that a TCP
        Keep Alive is retransmitted before the connection is closed.
    :ivar tcp_keep_alive_time: Specifies the time in [s] between the
        last data packet sent (simple ACKs are not considered data) and
        the first keepalive probe.
    :ivar tcp_max_rtx: Maximum number of times that a TCP segment is
        retransmitted before the TCP connection is closed. This
        parameter is only valid if tcpRetransmissionTimeout is
        configured.  Note: This parameter also applies for FIN
        retransmissions.
    :ivar tcp_msl: Maximum segment lifetime in [s].
    :ivar tcp_nagle_enabled: Enables (TRUE) or disables (FALSE) support
        of Nagle's algorithm according to IETF RFC 1122 (chapter 4.2.3.4
        When to Send Data). If enabled the Nagle's algorithm is
        activated per default for all TCP sockets, but can be
        deactivated per Socket (with the attribute
        TcpTp.nagleAlgorithm).
    :ivar tcp_receive_window_max: Default value of maximum receive
        window in bytes.
    :ivar tcp_retransmission_timeout: Timeout in [s] before an
        unacknowledged TCP segment is sent again. If the timeout is
        disabled, no TCP segments shall be retransmitted.
    :ivar tcp_slow_start_enabled: Enables (TRUE) or disables (FALSE)
        support of TCP slow start algorithm according to IETF RFC 5681.
    :ivar tcp_syn_max_rtx: Maximum number of times that a TCP SYN is
        retransmitted.
    :ivar tcp_syn_received_timeout: Timeout in [s] to complete a
        remotely initiated TCP connection establishment, i.e. maximum
        time waiting in SYN-RECEIVED for a confirming connection request
        acknowledgment after having both received and sent a connection
        request.
    :ivar tcp_ttl: Default Time-to-live value of outgoing TCP packets.
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
        name = "TCP-PROPS"

    tcp_congestion_avoidance_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-CONGESTION-AVOIDANCE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_delayed_ack_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-DELAYED-ACK-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_fast_recovery_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-FAST-RECOVERY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_fast_retransmit_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-FAST-RETRANSMIT-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_fin_wait_2_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-FIN-WAIT-2-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_keep_alive_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-KEEP-ALIVE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_keep_alive_interval: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-KEEP-ALIVE-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_keep_alive_probes_max: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-KEEP-ALIVE-PROBES-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_keep_alive_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-KEEP-ALIVE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_max_rtx: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-MAX-RTX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_msl: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-MSL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_nagle_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-NAGLE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_receive_window_max: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-RECEIVE-WINDOW-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_retransmission_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-RETRANSMISSION-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_slow_start_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-SLOW-START-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_syn_max_rtx: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-SYN-MAX-RTX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_syn_received_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-SYN-RECEIVED-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ttl: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-TTL",
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
