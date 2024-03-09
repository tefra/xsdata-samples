from dataclasses import dataclass

from .vehicle_entrance_ref_structure import VehicleEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntranceRef(VehicleEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
