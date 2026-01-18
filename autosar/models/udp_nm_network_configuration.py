from __future__ import annotations

from dataclasses import dataclass, field

from .ip4_address_string import Ip4AddressString
from .ip6_address_string import Ip6AddressString
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UdpNmNetworkConfiguration:
    """
    This meta-class defines the attributes for the configuration of a UDP
    port and UDP multicast IP address of the Nm communication on a VLAN.

    :ivar ipv_4_multicast_ip_address: Multicast IPv4 Address to which
        the message will be transmitted.
    :ivar ipv_6_multicast_ip_address: Multicast IPv6 Address to which
        the message will be transmitted
    :ivar udp_port: This attribute allows to configure a udp port number
        that is used for reception and transmission of UdpNm messages.
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
        name = "UDP-NM-NETWORK-CONFIGURATION"

    ipv_4_multicast_ip_address: Ip4AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-4-MULTICAST-IP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_6_multicast_ip_address: Ip6AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-6-MULTICAST-IP-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    udp_port: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "UDP-PORT",
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
