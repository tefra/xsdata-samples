from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.physical_channel_ref_conditional import PhysicalChannelRefConditional
from autosar.models.positive_integer import PositiveInteger

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BusMirrorChannel:
    """
    This element assigns a busMirrorNetworkId to the referenced channel.

    :ivar bus_mirror_network_id: This attribute defines the networkId of
        the communication channel.
    :ivar channels: Reference to PhysicalChannel that is used in the bus
        mirroring as sourceChannel or targetChannel. This property was
        modified due to atpVariation (DirectedAssociationPattern).
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
        name = "BUS-MIRROR-CHANNEL"

    bus_mirror_network_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "BUS-MIRROR-NETWORK-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    channels: Optional["BusMirrorChannel.Channels"] = field(
        default=None,
        metadata={
            "name": "CHANNELS",
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
    class Channels:
        physical_channel_ref_conditional: List[PhysicalChannelRefConditional] = field(
            default_factory=list,
            metadata={
                "name": "PHYSICAL-CHANNEL-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
