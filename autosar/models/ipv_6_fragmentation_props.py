from dataclasses import dataclass, field
from typing import Optional
from autosar.models.positive_integer import PositiveInteger
from autosar.models.time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv6FragmentationProps:
    """
    This meta-class specifies the configuration options for IPv6 packet
    fragmentation/reassembly.

    :ivar tcp_ip_ip_reassembly_buffer_count: Number of buffers that can
        be used for fragment reassembly. In case of a reassembly error
        or if not all fragments are received in time this buffer will be
        blocked until the specified "Fragment Reassembly Timeout" has
        been exceeded.   A value of 0 disables fragment reassembly.
    :ivar tcp_ip_ip_reassembly_buffer_size: Size of each fragment tx
        buffer in bytes.
    :ivar tcp_ip_ip_reassembly_segment_count: Specifies the maximum
        number of consecutive data segments that can be managed in each
        reassembly buffer. If all fragments are received in order, only
        one segment will be needed.  To deal with fragments received out
        of order this value should be configured bigger than 1.
    :ivar tcp_ip_ip_reassembly_timeout: Specifies the timeout in seconds
        after which an incomplete datagram gets discarded.
    :ivar tcp_ip_ip_tx_fragment_buffer_count: These buffers will be used
        if the IpV6 receives packets from the upper layer that do not
        fit into the MTU and thus must be fragmented.  A value of 0
        disables tx fragmentation.
    :ivar tcp_ip_ip_tx_fragment_buffer_size: Size of each fragment tx
        buffer in bytes.
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
        name = "IPV-6-FRAGMENTATION-PROPS"

    tcp_ip_ip_reassembly_buffer_count: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-REASSEMBLY-BUFFER-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_ip_reassembly_buffer_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-REASSEMBLY-BUFFER-SIZE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_ip_reassembly_segment_count: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-REASSEMBLY-SEGMENT-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_ip_reassembly_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-REASSEMBLY-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_ip_tx_fragment_buffer_count: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-TX-FRAGMENT-BUFFER-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_ip_tx_fragment_buffer_size: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-IP-TX-FRAGMENT-BUFFER-SIZE",
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
