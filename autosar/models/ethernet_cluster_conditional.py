from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.can_physical_channel import CanPhysicalChannel
from autosar.models.coupling_port_connection import CouplingPortConnection
from autosar.models.ethernet_physical_channel import EthernetPhysicalChannel
from autosar.models.flexray_physical_channel import FlexrayPhysicalChannel
from autosar.models.integer import Integer
from autosar.models.lin_physical_channel import LinPhysicalChannel
from autosar.models.mac_multicast_group import MacMulticastGroup
from autosar.models.positive_unlimited_integer import PositiveUnlimitedInteger
from autosar.models.string import String
from autosar.models.time_value import TimeValue
from autosar.models.ttcan_physical_channel import TtcanPhysicalChannel
from autosar.models.user_defined_physical_channel import UserDefinedPhysicalChannel

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class EthernetClusterConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar baudrate: Channels speed in bits/s.
    :ivar physical_channels: This relationship defines which channel
        element belongs to which cluster. A channel shall be assigned to
        exactly one cluster, whereas a cluster may have one or more
        channels. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar protocol_name: The name of the protocol used.
    :ivar protocol_version: The version of the protocol used.
    :ivar speed: This attribute is deprecated and is replaced by the
        attribute "baudrate". Old description: Channels speed in kbps.
    :ivar coupling_port_connections: The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar coupling_port_startup_active_time: The attribute specifies the
        time in second a coupling port is switched on to enable the host
        ECU (ECU that maintains an Ethernet switch) to listen to the
        network for potential network management requests.
    :ivar coupling_port_switchoff_delay: Switch off delay for
        CouplingPorts in seconds. It denotes the delay of switching off
        couplingPorts after the request to switch off a couplingPort was
        issued. (e.g. switch off of Ethernet switch ports).
    :ivar mac_multicast_groups: MacMulticastGroup that is defined for
        the Subnet (EthernetCluster).
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "ETHERNET-CLUSTER-CONDITIONAL"

    baudrate: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    physical_channels: Optional["EthernetClusterConditional.PhysicalChannels"] = field(
        default=None,
        metadata={
            "name": "PHYSICAL-CHANNELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    protocol_name: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    protocol_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    speed: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_connections: Optional["EthernetClusterConditional.CouplingPortConnections"] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-CONNECTIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_startup_active_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-STARTUP-ACTIVE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    coupling_port_switchoff_delay: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "COUPLING-PORT-SWITCHOFF-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mac_multicast_groups: Optional["EthernetClusterConditional.MacMulticastGroups"] = field(
        default=None,
        metadata={
            "name": "MAC-MULTICAST-GROUPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass
    class PhysicalChannels:
        can_physical_channel: List[CanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "CAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        ethernet_physical_channel: List[EthernetPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        flexray_physical_channel: List[FlexrayPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        lin_physical_channel: List[LinPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "LIN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        ttcan_physical_channel: List[TtcanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
        user_defined_physical_channel: List[UserDefinedPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class CouplingPortConnections:
        coupling_port_connection: List[CouplingPortConnection] = field(
            default_factory=list,
            metadata={
                "name": "COUPLING-PORT-CONNECTION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class MacMulticastGroups:
        mac_multicast_group: List[MacMulticastGroup] = field(
            default_factory=list,
            metadata={
                "name": "MAC-MULTICAST-GROUP",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
