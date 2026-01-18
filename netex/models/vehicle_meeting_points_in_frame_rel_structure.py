from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_meeting_point import VehicleMeetingPoint

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingPointsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleMeetingPointsInFrame_RelStructure"

    vehicle_meeting_point: Iterable[VehicleMeetingPoint] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMeetingPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
