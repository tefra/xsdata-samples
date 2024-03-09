from dataclasses import dataclass

from .vehicle_type_stop_assignment_ref_structure import (
    VehicleTypeStopAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeStopAssignmentRef(VehicleTypeStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
