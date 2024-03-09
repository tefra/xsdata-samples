from dataclasses import dataclass

from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeRef(VehicleTypeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
