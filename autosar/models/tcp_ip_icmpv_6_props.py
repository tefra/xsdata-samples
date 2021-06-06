from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TcpIpIcmpv6Props:
    """
    This meta-class specifies the configuration options for ICMPv6 (Internet
    Control Message Protocol).

    :ivar tcp_ip_icmp_v_6_echo_reply_avoid_fragmentation: This attribute
        defines whether the echo reply is only transmitted in case that
        the incoming ICMPv6 Echo Request (Pings) fits the MTU of the
        respective interface, i.e. can be transmitted without IPv6
        fragmentation.
    :ivar tcp_ip_icmp_v_6_echo_reply_enabled: This attribute enables or
        disables transmission of ICMP echo reply message in case of a
        ICMP echo reception.
    :ivar tcp_ip_icmp_v_6_hop_limit: Default Hop-Limit value of outgoing
        ICMPv6 packets.
    :ivar tcp_ip_icmp_v_6_msg_destination_unreachable_enabled: This
        attribute Enables/Disables the transmission of Destination
        Unreachable Messages.
    :ivar tcp_ip_icmp_v_6_msg_parameter_problem_enabled: If enabled an
        ICMPv6 parameter problem message will be sent if a received
        packet has been dropped due to unknown options or headers that
        are found in the packet.
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
        name = "TCP-IP-ICMPV-6-PROPS"

    tcp_ip_icmp_v_6_echo_reply_avoid_fragmentation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-6-ECHO-REPLY-AVOID-FRAGMENTATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_icmp_v_6_echo_reply_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-6-ECHO-REPLY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_icmp_v_6_hop_limit: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-6-HOP-LIMIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_icmp_v_6_msg_destination_unreachable_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-6-MSG-DESTINATION-UNREACHABLE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    tcp_ip_icmp_v_6_msg_parameter_problem_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TCP-IP-ICMP-V-6-MSG-PARAMETER-PROBLEM-ENABLED",
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
