from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv4FragmentationProps:
    """
    Specifies the configuration options for IPv4 packet
    fragmentation/reassembly.

    :ivar tcp_ip_ip_fragmentation_rx_enabled: Enables (TRUE) or disables
        (FALSE) support for reassembling of incoming datagrams that are
        fragmented according to IETF RFC 815 (IP Datagram Reassembly
        Algorithms).
    :ivar tcp_ip_ip_num_fragments: Specifies the maximum number of IP
        fragments per datagram.
    :ivar tcp_ip_ip_num_reass_dgrams: Specifies the maximum number of
        fragmented IP datagrams that can be reassembled in parallel.
    :ivar tcp_ip_ip_reass_timeout: Specifies the timeout in [s] after
        which an incomplete datagram gets discarded.
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
        name = "IPV-4-FRAGMENTATION-PROPS"

    tcp_ip_ip_fragmentation_rx_enabled: Boolean | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-FRAGMENTATION-RX-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ip_num_fragments: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-NUM-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ip_num_reass_dgrams: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-NUM-REASS-DGRAMS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_ip_reass_timeout: TimeValue | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-REASS-TIMEOUT",
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
