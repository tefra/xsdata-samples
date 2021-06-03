from dataclasses import dataclass, field
from typing import Optional
from autosar.models.dhcpv_6_props import Dhcpv6Props
from autosar.models.ipv_6_fragmentation_props import Ipv6FragmentationProps
from autosar.models.ipv_6_ndp_props import Ipv6NdpProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv6Props:
    """
    This meta-class specifies the configuration options for IPv6.

    :ivar dhcp_props: Configuration properties for DHCPv6.
    :ivar fragmentation_props: Configuration properties for IPv6 packet
        fragmentation/reassembly.
    :ivar ndp_props: Configuration properties for the Neighbor Discovery
        Protocol for IPv6.
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
        name = "IPV-6-PROPS"

    dhcp_props: Optional[Dhcpv6Props] = field(
        default=None,
        metadata={
            "name": "DHCP-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    fragmentation_props: Optional[Ipv6FragmentationProps] = field(
        default=None,
        metadata={
            "name": "FRAGMENTATION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    ndp_props: Optional[Ipv6NdpProps] = field(
        default=None,
        metadata={
            "name": "NDP-PROPS",
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
