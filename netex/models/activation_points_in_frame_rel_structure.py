from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .activation_point import ActivationPoint
from .beacon_point import BeaconPoint
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ActivationPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "activationPointsInFrame_RelStructure"

    activation_point: Iterable[Union[BeaconPoint, ActivationPoint]] = field(
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
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
