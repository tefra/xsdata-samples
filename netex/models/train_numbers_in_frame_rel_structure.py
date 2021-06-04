from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.train_number import TrainNumber
from netex.models.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TrainNumbersInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "trainNumbersInFrame_RelStructure"

    train_number: List[TrainNumber] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: List[TrainNumberRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
