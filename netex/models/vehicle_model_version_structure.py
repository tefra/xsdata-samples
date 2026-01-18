from __future__ import annotations

from dataclasses import dataclass, field

from .car_model_profile_ref import CarModelProfileRef
from .compound_train_ref import CompoundTrainRef
from .cycle_model_profile_ref import CycleModelProfileRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .vehicle_equipment_profile_refs_rel_structure import (
    VehicleEquipmentProfileRefsRelStructure,
)
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleModelVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleModel_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    manufacturer: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_type_ref_or_vehicle_type_ref: (
        None
        | SimpleVehicleTypeRef
        | CompoundTrainRef
        | TrainRef
        | VehicleTypeRef
        | TransportTypeRef
    ) = field(
        default=None,
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
    equipment_profiles: None | VehicleEquipmentProfileRefsRelStructure = field(
        default=None,
        metadata={
            "name": "equipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_model_profile_ref: (
        None | CycleModelProfileRef | CarModelProfileRef
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CycleModelProfileRef",
                    "type": CycleModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarModelProfileRef",
                    "type": CarModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
