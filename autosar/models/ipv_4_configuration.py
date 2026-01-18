from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .ip4_address_string import Ip4AddressString
from .ip_address_keep_enum import IpAddressKeepEnum
from .ipv_4_address_source_enum import Ipv4AddressSourceEnum
from .positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv4Configuration:
    """
    Internet Protocol version 4 (IPv4) configuration.

    :ivar assignment_priority: Priority of assignment (1 is highest). If
        a new address from an assignment method with a higher priority
        is available, it overwrites the IP address previously assigned
        by an assignment method with a lower priority.
    :ivar default_gateway: IP address of the default gateway.
    :ivar dns_server_addresses:
    :ivar ip_address_keep_behavior: Defines the lifetime of a
        dynamically fetched IP address.
    :ivar ipv_4_address: IPv4 Address. Notation: 255.255.255.255. The IP
        Address shall be declared in case the ipv4AddressSource is FIXED
        and thus no auto-configuration mechanism is used.
    :ivar ipv_4_address_source: Defines how the node obtains its IP
        address.
    :ivar network_mask: Network mask. Notation 255.255.255.255
    :ivar ttl: Lifespan of data (0..255). The purpose of the TimeToLive
        field is to avoid a situation in which an undeliverable datagram
        keeps circulating on a system.
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
        name = "IPV-4-CONFIGURATION"

    assignment_priority: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "ASSIGNMENT-PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    default_gateway: Ip4AddressString | None = field(
        default=None,
        metadata={
            "name": "DEFAULT-GATEWAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dns_server_addresses: Ipv4Configuration.DnsServerAddresses | None = (
        field(
            default=None,
            metadata={
                "name": "DNS-SERVER-ADDRESSES",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    ip_address_keep_behavior: IpAddressKeepEnum | None = field(
        default=None,
        metadata={
            "name": "IP-ADDRESS-KEEP-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_4_address: Ip4AddressString | None = field(
        default=None,
        metadata={
            "name": "IPV-4-ADDRESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ipv_4_address_source: Ipv4AddressSourceEnum | None = field(
        default=None,
        metadata={
            "name": "IPV-4-ADDRESS-SOURCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_mask: Ip4AddressString | None = field(
        default=None,
        metadata={
            "name": "NETWORK-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ttl: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "TTL",
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
        :ivar dns_server_address: IP addresses of preconfigured DNS
            servers.
        """

        dns_server_address: list[Ip4AddressString] = field(
            default_factory=list,
            metadata={
                "name": "DNS-SERVER-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
