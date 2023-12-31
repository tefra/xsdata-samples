from dataclasses import dataclass
from .vehicle_profile_ref_structure import VehicleProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleProfileRef(VehicleProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
