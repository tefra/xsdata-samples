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
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .string import String
from .time_value import TimeValue
from .ttcan_physical_channel import TtcanPhysicalChannel
from .user_defined_physical_channel import UserDefinedPhysicalChannel

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TtcanClusterConditional:
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
    :ivar basic_cycle_length: Length of a basic-cycle. Unit: NTUs
    :ivar ntu: Unit measuring all times and providing a constant of the
        whole network. For level 1, this is always the CAN bit time.
        Unit: seconds.
    :ivar operation_mode: Possible operation modes True: Time-Triggered
        False: Event-Synchronised-Time-Triggered
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
        name = "TTCAN-CLUSTER-CONDITIONAL"

    baudrate: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channels: Optional[
        "TtcanClusterConditional.PhysicalChannels"
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
    basic_cycle_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "BASIC-CYCLE-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ntu: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NTU",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    operation_mode: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "OPERATION-MODE",
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
