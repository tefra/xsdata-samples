from dataclasses import dataclass

from .vehicle_manoeuvring_requirement_version_structure import (
    VehicleManoeuvringRequirementVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleManoeuvringRequirement(
    VehicleManoeuvringRequirementVersionStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
