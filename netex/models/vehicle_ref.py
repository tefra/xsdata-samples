from dataclasses import dataclass
from netex.models.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleRef(VehicleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
