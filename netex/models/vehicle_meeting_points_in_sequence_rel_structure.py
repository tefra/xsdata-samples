from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point_in_path import VehicleMeetingPointInPath

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointsInSequenceRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "vehicleMeetingPointsInSequence_RelStructure"

    vehicle_meeting_point_in_path: Iterable[VehicleMeetingPointInPath] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPointInPath",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
