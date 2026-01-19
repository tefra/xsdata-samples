from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_position_alignment import VehiclePositionAlignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePositionAlignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehiclePositionAlignments_RelStructure"

    vehicle_position_alignment: Sequence[VehiclePositionAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePositionAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
