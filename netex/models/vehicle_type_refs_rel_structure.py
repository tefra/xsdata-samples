from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .compound_train_ref import CompoundTrainRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .train_ref import TrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleTypeRefs_RelStructure"

    vehicle_type_ref: Iterable[
        Union[CompoundTrainRef, TrainRef, VehicleTypeRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
