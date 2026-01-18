from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv4ArpProps:
    """
    Specifies the configuration options for the ARP (Address Resolution
    Protocol).

    :ivar tcp_ip_arp_num_gratuitous_arp_on_startup: This attribute
        specifies the number of gratuitous ARP replies which shall be
        sent on assignment of a new IP address.
    :ivar tcp_ip_arp_packet_queue_enabled: This attribute enables (TRUE)
        or disables (FALSE) support of the ARP Packet Queue according to
        IETF RFC 1122, section 2.3.2.2.
    :ivar tcp_ip_arp_request_timeout: This attribute specifies a timeout
        in seconds for the validity of ARP requests. After the
        transmission of an ARP request the TcpIp shall skip the
        transmission of any further ARP requests to the same destination
        within a duration of tcpIpArpRequestTimeout seconds. (IETF RFC
        1122, section 2.3.2.1).
    :ivar tcp_ip_arp_table_entry_timeout: This attribute specifies the
        timeout in seconds after which an unused ARP entry is removed.
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
        name = "IPV-4-ARP-PROPS"

    tcp_ip_arp_num_gratuitous_arp_on_startup: PositiveInteger | None = (
        field(
            default=None,
            metadata={
                "name": "TCP-IP-ARP-NUM-GRATUITOUS-ARP-ON-STARTUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    tcp_ip_arp_packet_queue_enabled: Boolean | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-ARP-PACKET-QUEUE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_arp_request_timeout: TimeValue | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-ARP-REQUEST-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_arp_table_entry_timeout: TimeValue | None = field(
        default=None,
        metadata={
            "name": "TCP-IP-ARP-TABLE-ENTRY-TIMEOUT",
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
