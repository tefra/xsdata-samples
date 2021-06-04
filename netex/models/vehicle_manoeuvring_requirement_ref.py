from dataclasses import dataclass
from netex.models.vehicle_manoeuvring_requirement_ref_structure import VehicleManoeuvringRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleManoeuvringRequirementRef(VehicleManoeuvringRequirementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
