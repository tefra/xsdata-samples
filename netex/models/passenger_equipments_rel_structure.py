from dataclasses import dataclass, field
from typing import List
from netex.models.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from netex.models.actual_vehicle_equipment import ActualVehicleEquipment
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.help_point_equipment import HelpPointEquipment
from netex.models.help_point_equipment_ref import HelpPointEquipmentRef
from netex.models.passenger_equipment import PassengerEquipment
from netex.models.passenger_equipment_ref import PassengerEquipmentRef
from netex.models.passenger_information_equipment import PassengerInformationEquipment
from netex.models.passenger_safety_equipment import PassengerSafetyEquipment
from netex.models.passenger_safety_equipment_ref import PassengerSafetyEquipmentRef
from netex.models.rubbish_disposal_equipment import RubbishDisposalEquipment
from netex.models.rubbish_disposal_equipment_ref import RubbishDisposalEquipmentRef
from netex.models.sanitary_equipment import SanitaryEquipment
from netex.models.sanitary_equipment_ref import SanitaryEquipmentRef
from netex.models.vehicle_equipment_ref import VehicleEquipmentRef
from netex.models.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PassengerEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "passengerEquipments_RelStructure"

    rubbish_disposal_equipment_ref: List[RubbishDisposalEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    help_point_equipment_ref: List[HelpPointEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_safety_equipment_ref: List[PassengerSafetyEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_equipment_ref: List[SanitaryEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_vehicle_ref: List[WheelchairVehicleRef] = field(
        default_factory=list,
        metadata={
            "name": "WheelchairVehicleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_vehicle_equipment_ref: List[AccessVehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessVehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_equipment_ref: List[VehicleEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_equipment_ref: List[PassengerEquipmentRef] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_information_equipment: List[PassengerInformationEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInformationEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rubbish_disposal_equipment: List[RubbishDisposalEquipment] = field(
        default_factory=list,
        metadata={
            "name": "RubbishDisposalEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    help_point_equipment: List[HelpPointEquipment] = field(
        default_factory=list,
        metadata={
            "name": "HelpPointEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_safety_equipment: List[PassengerSafetyEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerSafetyEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_equipment: List[SanitaryEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    actual_vehicle_equipment: List[ActualVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActualVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_equipment: List[PassengerEquipment] = field(
        default_factory=list,
        metadata={
            "name": "PassengerEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
