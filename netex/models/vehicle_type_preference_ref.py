from dataclasses import dataclass
from netex.models.vehicle_type_preference_ref_structure import VehicleTypePreferenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypePreferenceRef(VehicleTypePreferenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
