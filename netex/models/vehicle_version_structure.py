from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .compound_train_ref import CompoundTrainRef
from .equipments_rel_structure import EquipmentsRelStructure
from .multilingual_string import MultilingualString
from .operator_ref import OperatorRef
from .private_code import PrivateCode
from .train_ref import TrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Vehicle_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref: List[CompoundTrainRef] = field(
        default_factory=list,
        metadata={
            "name": "CompoundTrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    train_ref: List[TrainRef] = field(
        default_factory=list,
        metadata={
            "name": "TrainRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    vehicle_type_ref: Optional[VehicleTypeRef] = field(
        default=None,
        metadata={
            "name": "VehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    actual_vehicle_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "actualVehicleEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )