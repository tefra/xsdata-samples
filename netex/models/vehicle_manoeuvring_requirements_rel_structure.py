from dataclasses import dataclass, field
from typing import List
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.vehicle_manoeuvring_requirement import VehicleManoeuvringRequirement
from netex.models.vehicle_manoeuvring_requirement_ref import VehicleManoeuvringRequirementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleManoeuvringRequirementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleManoeuvringRequirements_RelStructure"

    vehicle_manoeuvring_requirement_ref: List[VehicleManoeuvringRequirementRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleManoeuvringRequirementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_manoeuvring_requirement: List[VehicleManoeuvringRequirement] = field(
        default_factory=list,
        metadata={
            "name": "VehicleManoeuvringRequirement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
