from __future__ import annotations

from dataclasses import dataclass

from .vehicle_type_stop_assignment_version_structure import (
    VehicleTypeStopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeStopAssignment(VehicleTypeStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
