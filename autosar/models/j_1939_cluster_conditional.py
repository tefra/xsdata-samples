from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .boolean import Boolean
from .can_cluster_bus_off_recovery import CanClusterBusOffRecovery
from .can_physical_channel import CanPhysicalChannel
from .ethernet_physical_channel import EthernetPhysicalChannel
from .flexray_physical_channel import FlexrayPhysicalChannel
from .integer import Integer
from .lin_physical_channel import LinPhysicalChannel
from .positive_integer import PositiveInteger
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .string import String
from .ttcan_physical_channel import TtcanPhysicalChannel
from .user_defined_physical_channel import UserDefinedPhysicalChannel

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class J1939ClusterConditional:
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
    :ivar bus_off_recovery: CAN bus off monitoring / recovery at system
        level.
    :ivar can_fd_baudrate: Specifies the data segment baud rate of the
        controller in bits/s.
    :ivar network_id: This represents the network ID for the J1939
        cluster.
    :ivar request_2_support: Enables support for the Request2 PGN
        (RQST2).
    :ivar uses_address_arbitration: Defines whether the nodes attached
        to this channel use an initial address claim, and whether they
        react to contending address claims of other nodes. True: The
        initial address claim is sent, and the node reacts to address
        claims of other nodes. False: The node only sends an address
        claim upon request, and does not care for contending address
        claims.
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
        name = "J-1939-CLUSTER-CONDITIONAL"

    baudrate: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channels: Optional[
        "J1939ClusterConditional.PhysicalChannels"
    ] = field(
        default=None,
        metadata={
            "name": "PHYSICAL-CHANNELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_name: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: Optional[String] = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    speed: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bus_off_recovery: Optional[CanClusterBusOffRecovery] = field(
        default=None,
        metadata={
            "name": "BUS-OFF-RECOVERY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_fd_baudrate: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "CAN-FD-BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NETWORK-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    request_2_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "REQUEST-2-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    uses_address_arbitration: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USES-ADDRESS-ARBITRATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass
    class PhysicalChannels:
        can_physical_channel: List[CanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "CAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_physical_channel: List[EthernetPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_physical_channel: List[FlexrayPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_physical_channel: List[LinPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "LIN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_physical_channel: List[TtcanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_physical_channel: List[
            UserDefinedPhysicalChannel
        ] = field(
            default_factory=list,
            metadata={
                "name": "USER-DEFINED-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
