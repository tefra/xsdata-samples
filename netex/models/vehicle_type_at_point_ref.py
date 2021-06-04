from dataclasses import dataclass
from netex.models.vehicle_type_at_point_ref_structure import VehicleTypeAtPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeAtPointRef(VehicleTypeAtPointRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
