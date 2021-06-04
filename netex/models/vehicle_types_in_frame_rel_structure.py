from dataclasses import dataclass, field
from typing import List
from netex.models.compound_train import CompoundTrain
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.train import Train
from netex.models.vehicle_type import VehicleType

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypesInFrame_RelStructure"

    compound_train: List[CompoundTrain] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train: List[Train] = field(
        default_factory=list,
        metadata={
            "name": "Train",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type: List[VehicleType] = field(
        default_factory=list,
        metadata={
            "name": "VehicleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
