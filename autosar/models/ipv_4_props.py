from dataclasses import dataclass, field
from typing import Optional
from .ipv_4_arp_props import Ipv4ArpProps
from .ipv_4_auto_ip_props import Ipv4AutoIpProps
from .ipv_4_fragmentation_props import Ipv4FragmentationProps

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Ipv4Props:
    """
    This meta-class specifies the configuration options for IPv4.

    :ivar arp_props: Configuration properties for the ARP (Address
        Resolution Protocol).
    :ivar auto_ip_props: Configuration options for Auto-IP (automatic
        private IP addressing).
    :ivar fragmentation_props: Configuration options for IPv4 packet
        fragmentation/reassembly.
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
        name = "IPV-4-PROPS"

    arp_props: Optional[Ipv4ArpProps] = field(
        default=None,
        metadata={
            "name": "ARP-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    auto_ip_props: Optional[Ipv4AutoIpProps] = field(
        default=None,
        metadata={
            "name": "AUTO-IP-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    fragmentation_props: Optional[Ipv4FragmentationProps] = field(
        default=None,
        metadata={
            "name": "FRAGMENTATION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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
