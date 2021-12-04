from dataclasses import dataclass, field
from typing import List
from .activation_point import ActivationPoint
from .beacon_point import BeaconPoint
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationPointsInFrame_RelStructure"

    beacon_point: List[BeaconPoint] = field(
        default_factory=list,
        metadata={
            "name": "BeaconPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    activation_point: List[ActivationPoint] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
