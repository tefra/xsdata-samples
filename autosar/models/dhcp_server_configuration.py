from dataclasses import dataclass, field
from typing import Optional

from .ipv_4_dhcp_server_configuration import Ipv4DhcpServerConfiguration
from .ipv_6_dhcp_server_configuration import Ipv6DhcpServerConfiguration

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DhcpServerConfiguration:
    """Defines the configuration of DHCP servers that are running on the network
    endpoint.

    It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on
    the same Ecu.

    :ivar ipv_4_dhcp_server_configuration: Configuration of a IPv4 DHCP
        server that runs on the network endpoint.
    :ivar ipv_6_dhcp_server_configuration: Configuration of a IPv6 DHCP
        server that runs on the network endpoint.
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
        name = "DHCP-SERVER-CONFIGURATION"

    ipv_4_dhcp_server_configuration: Optional[Ipv4DhcpServerConfiguration] = (
        field(
            default=None,
            metadata={
                "name": "IPV-4-DHCP-SERVER-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    ipv_6_dhcp_server_configuration: Optional[Ipv6DhcpServerConfiguration] = (
        field(
            default=None,
            metadata={
                "name": "IPV-6-DHCP-SERVER-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
