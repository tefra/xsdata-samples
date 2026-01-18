from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_type_stop_assignment import VehicleTypeStopAssignment
from .vehicle_type_stop_assignment_ref import VehicleTypeStopAssignmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleTypeStopAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypeStopAssignments_RelStructure"

    vehicle_type_stop_assignment_ref_or_vehicle_type_stop_assignment: Iterable[
        VehicleTypeStopAssignmentRef | VehicleTypeStopAssignment
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleTypeStopAssignmentRef",
                    "type": VehicleTypeStopAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeStopAssignment",
                    "type": VehicleTypeStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
