from dataclasses import dataclass, field
from typing import List
from netex.models.compound_train_ref import CompoundTrainRef
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.train_ref import TrainRef
from netex.models.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleTypeRefs_RelStructure"

    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    vehicle_type_ref: List[VehicleTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
