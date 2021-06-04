from dataclasses import dataclass, field
from typing import List
from netex.models.activation_point_1 import ActivationPoint1
from netex.models.activation_point_2 import ActivationPoint2
from netex.models.beacon_point import BeaconPoint
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure

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
            "min_occurs": 1,
        }
    )
    activation_point: List[ActivationPoint2] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_activation_point: List[ActivationPoint1] = field(
        default_factory=list,
        metadata={
            "name": "ActivationPoint_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
