from __future__ import annotations

from dataclasses import dataclass, field

from .boolean import Boolean
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class TcpIpIcmpv4Props:
    """
    This meta-class specifies the configuration options for ICMPv4
    (Internet Control Message Protocol).

    :ivar tcp_ip_icmp_v_4_echo_reply_enabled: This attribute enables or
        disables transmission of ICMP echo reply message in case of a
        ICMP echo reception.
    :ivar tcp_ip_icmp_v_4_ttl: This attribute is only relevant in case
        that ICMP (Internet Control Message Protocol) is used. It
        specifies the default Time-to-live value of outgoing ICMP
        packets.
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
        name = "TCP-IP-ICMPV-4-PROPS"

    tcp_ip_icmp_v_4_echo_reply_enabled: None | Boolean = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-4-ECHO-REPLY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tcp_ip_icmp_v_4_ttl: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-4-TTL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
