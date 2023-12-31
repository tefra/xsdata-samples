from dataclasses import dataclass
from .simple_vehicle_type_version_structure import (
    SimpleVehicleTypeVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SimpleVehicleType(SimpleVehicleTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
