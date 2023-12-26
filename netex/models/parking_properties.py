from dataclasses import dataclass
from .parking_properties_versioned_child_structure import (
    ParkingPropertiesVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ParkingProperties(ParkingPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
