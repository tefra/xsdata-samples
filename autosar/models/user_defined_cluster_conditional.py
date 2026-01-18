from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .can_physical_channel import CanPhysicalChannel
from .ethernet_physical_channel import EthernetPhysicalChannel
from .flexray_physical_channel import FlexrayPhysicalChannel
from .integer import Integer
from .lin_physical_channel import LinPhysicalChannel
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .string import String
from .ttcan_physical_channel import TtcanPhysicalChannel
from .user_defined_physical_channel import UserDefinedPhysicalChannel

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class UserDefinedClusterConditional:
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
        name = "USER-DEFINED-CLUSTER-CONDITIONAL"

    baudrate: None | PositiveUnlimitedInteger = field(
        default=None,
        metadata={
            "name": "BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channels: (
        None | UserDefinedClusterConditional.PhysicalChannels
    ) = field(
        default=None,
        metadata={
            "name": "PHYSICAL-CHANNELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_name: None | String = field(
        default=None,
        metadata={
            "name": "PROTOCOL-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: None | String = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    speed: None | Integer = field(
        default=None,
        metadata={
            "name": "SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class PhysicalChannels:
        can_physical_channel: list[CanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "CAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_physical_channel: list[EthernetPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_physical_channel: list[FlexrayPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_physical_channel: list[LinPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "LIN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_physical_channel: list[TtcanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_physical_channel: list[UserDefinedPhysicalChannel] = (
            field(
                default_factory=list,
                metadata={
                    "name": "USER-DEFINED-PHYSICAL-CHANNEL",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
