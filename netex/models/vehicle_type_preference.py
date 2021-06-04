from dataclasses import dataclass
from netex.models.vehicle_type_preference_versioned_child_structure import VehicleTypePreferenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypePreference(VehicleTypePreferenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
