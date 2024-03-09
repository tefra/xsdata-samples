from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlCentresInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "controlCentresInFrame_RelStructure"

    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
