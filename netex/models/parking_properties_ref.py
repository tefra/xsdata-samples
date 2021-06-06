from dataclasses import dataclass
from .parking_properties_ref_structure import ParkingPropertiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingPropertiesRef(ParkingPropertiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
