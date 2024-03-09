from dataclasses import dataclass

from .vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompoundTrainRefStructure(VehicleTypeRefStructure):
    pass
