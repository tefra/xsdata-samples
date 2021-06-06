from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .open_transport_mode_ref import OpenTransportModeRef
from .transport_mode_structure import TransportModeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportModesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transportModes_RelStructure"

    open_transport_mode_ref: List[OpenTransportModeRef] = field(
        default_factory=list,
        metadata={
            "name": "OpenTransportModeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: List[TransportModeStructure] = field(
        default_factory=list,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
