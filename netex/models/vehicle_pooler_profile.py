from dataclasses import dataclass
from .vehicle_pooler_profile_version_structure import (
    VehiclePoolerProfileVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehiclePoolerProfile(VehiclePoolerProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
