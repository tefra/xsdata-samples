from dataclasses import dataclass

from .vehicle_requirement_ref_structure import VehicleRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRequirementRef(VehicleRequirementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
