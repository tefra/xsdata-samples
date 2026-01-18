from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    DocumentationBlock,
)
from .category_string import CategoryString
from .ip6_address_string import Ip6AddressString
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv6DhcpServerConfiguration:
    """
    Defines the configuration of a IPv6 DHCP server that runs on the
    network endpoint.

    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particlar
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Describable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar admin_data: This represents the administrative data for the
        describable object.
    :ivar address_range_lower_bound: Lower range of IP addresses to be
        issued to DHCP clients.  IPv6 Address. Notation: FFFF:...:FFFF.
    :ivar address_range_upper_bound: Upper range of IP addresses to be
        issued to DHCP clients. IPv6 Address. Notation: FFFF:...:FFFF.
    :ivar default_gateway: IP address of the default gateway. Notation
        255.255.255.255
    :ivar default_lease_time: Amount of time in seconds that a client
        may keep the IP address.
    :ivar dns_server_addresses:
    :ivar network_mask: Default network mask to be used by DHCP clients.
        Notation 255.255.255.255
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
        name = "IPV-6-DHCP-SERVER-CONFIGURATION"

    desc: None | MultiLanguageOverviewParagraph = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: None | DocumentationBlock = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: None | AdminData = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    address_range_lower_bound: None | Ip6AddressString = field(
        default=None,
        metadata={
            "name": "ADDRESS-RANGE-LOWER-BOUND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    address_range_upper_bound: None | Ip6AddressString = field(
        default=None,
        metadata={
            "name": "ADDRESS-RANGE-UPPER-BOUND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    default_gateway: None | Ip6AddressString = field(
        default=None,
        metadata={
            "name": "DEFAULT-GATEWAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    default_lease_time: None | TimeValue = field(
        default=None,
        metadata={
            "name": "DEFAULT-LEASE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dns_server_addresses: (
        None | Ipv6DhcpServerConfiguration.DnsServerAddresses
    ) = field(
        default=None,
        metadata={
            "name": "DNS-SERVER-ADDRESSES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_mask: None | Ip6AddressString = field(
        default=None,
        metadata={
            "name": "NETWORK-MASK",
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

    @dataclass
    class DnsServerAddresses:
        """
        :ivar dns_server_address: IP addresses of preconfigured DNS
            servers. Notation: FFFF:...:FFFF.
        """

        dns_server_address: list[Ip6AddressString] = field(
            default_factory=list,
            metadata={
                "name": "DNS-SERVER-ADDRESS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
