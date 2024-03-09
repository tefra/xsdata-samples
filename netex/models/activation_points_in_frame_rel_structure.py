from dataclasses import dataclass, field
from typing import List, Union

from .activation_point_1 import ActivationPoint1
from .beacon_point import BeaconPoint
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationPointsInFrame_RelStructure"

    activation_point: List[Union[BeaconPoint, ActivationPoint1]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
