from dataclasses import dataclass
from netex.models.vehicle_requirement_version_structure import VehicleRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRequirement(VehicleRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
