from dataclasses import dataclass, field
from typing import Optional
from .network_restriction_version_structure import NetworkRestrictionVersionStructure
from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeAtPointVersionStructure(NetworkRestrictionVersionStructure):
    class Meta:
        name = "VehicleTypeAtPoint_VersionStructure"

    for_vehicle_type_ref: Optional[VehicleTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "ForVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )