from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_quay_alignment import VehicleQuayAlignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleQuayAlignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleQuayAlignments_RelStructure"

    vehicle_quay_alignment: List[VehicleQuayAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleQuayAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
