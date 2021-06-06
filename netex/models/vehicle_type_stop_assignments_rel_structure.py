from dataclasses import dataclass, field
from typing import List
from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_type_stop_assignment import VehicleTypeStopAssignment
from .vehicle_type_stop_assignment_ref import VehicleTypeStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypeStopAssignments_RelStructure"

    vehicle_type_stop_assignment_ref: List[VehicleTypeStopAssignmentRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeStopAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_type_stop_assignment: List[VehicleTypeStopAssignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypeStopAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
