from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.train_component import TrainComponent
from netex.models.train_component_ref import TrainComponentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainComponentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainComponents_RelStructure"

    train_component_ref: List[TrainComponentRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component: List[TrainComponent] = field(
        default_factory=list,
        metadata={
            "name": "TrainComponent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
