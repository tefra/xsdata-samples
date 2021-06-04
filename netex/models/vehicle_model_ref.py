from dataclasses import dataclass
from netex.models.vehicle_model_ref_structure import VehicleModelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleModelRef(VehicleModelRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
