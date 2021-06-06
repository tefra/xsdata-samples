from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .control_centre import ControlCentre
from .control_centre_ref import ControlCentreRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ControlCentresRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "ControlCentres_RelStructure"

    control_centre_ref: List[ControlCentreRef] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentreRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre: List[ControlCentre] = field(
        default_factory=list,
        metadata={
            "name": "ControlCentre",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
