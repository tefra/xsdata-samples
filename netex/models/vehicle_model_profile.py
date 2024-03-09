from dataclasses import dataclass

from .vehicle_model_profile_version_structure import (
    VehicleModelProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelProfile(VehicleModelProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
