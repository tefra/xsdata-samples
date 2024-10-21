from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .compound_train_ref import CompoundTrainRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportTypeRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "transportTypeRefs_RelStructure"

    transport_type_ref_or_vehicle_type_ref: Iterable[
        Union[
            SimpleVehicleTypeRef,
            CompoundTrainRef,
            TrainRef,
            VehicleTypeRef,
            TransportTypeRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
