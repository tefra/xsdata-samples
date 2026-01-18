from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .ip6_address_string import Ip6AddressString
from .ip_address_keep_enum import IpAddressKeepEnum
from .ipv_6_address_source_enum import Ipv6AddressSourceEnum
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv6Configuration:
    """
    Internet Protocol version 6 (IPv6) configuration.

    :ivar assignment_priority: Priority of assignment (1 is highest). If
        a new address from an assignment method with a higher priority
        is available, it overwrites the IP address previously assigned
        by an assignment method with a lower priority.
    :ivar default_router: IP address of the default router.
    :ivar dns_server_addresses:
    :ivar enable_anycast: This attribute is used to enable anycast
        addressing (i.e. to one of multiple receivers).
    :ivar hop_count: The distance between two hosts. The hop count n
        means that n gateways separate the source host from the
        destination host (Range 0..255)
    :ivar ip_address_keep_behavior: Defines the lifetime of a
        dynamically fetched IP address.
    :ivar ip_address_prefix_length: IPv6 prefix length defines the part
        of the IPv6 address that is the network prefix.
    :ivar ipv_6_address: IPv6 Address. Notation: FFFF:...:FFFF. The IP
        Address shall be declared in case the ipv6AddressSource is FIXED
        and thus no auto-configuration mechanism is used.
    :ivar ipv_6_address_source: Defines how the node obtains its IP
        address.
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
        name = "IPV-6-CONFIGURATION"

    assignment_priority: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "ASSIGNMENT-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    default_router: Ip6AddressString | None = field(
        default=None,
        metadata={
            "name": "DEFAULT-ROUTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dns_server_addresses: Ipv6Configuration.DnsServerAddresses | None = (
        field(
            default=None,
            metadata={
                "name": "DNS-SERVER-ADDRESSES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    enable_anycast: Boolean | None = field(
        default=None,
        metadata={
            "name": "ENABLE-ANYCAST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    hop_count: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "HOP-COUNT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ip_address_keep_behavior: IpAddressKeepEnum | None = field(
        default=None,
        metadata={
            "name": "IP-ADDRESS-KEEP-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ip_address_prefix_length: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "IP-ADDRESS-PREFIX-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_6_address: Ip6AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-6-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_6_address_source: Ipv6AddressSourceEnum | None = field(
        default=None,
        metadata={
            "name": "IPV-6-ADDRESS-SOURCE",
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

    @dataclass
    class DnsServerAddresses:
        """
        :ivar dns_server_address: IP addresses of pre configured DNS
            servers.
        """

        dns_server_address: list[Ip6AddressString] = field(
            default_factory=list,
            metadata={
                "name": "DNS-SERVER-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
